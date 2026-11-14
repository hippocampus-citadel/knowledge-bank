"""Terapkan snapshot akhir sesi ke folder project. Tanpa LLM: murni aturan (deterministik)."""
import os, re, sys, json, subprocess, pathlib, datetime, textwrap, urllib.parse, urllib.request

# ---- Konfigurasi ----------------------------------------------------------
V_FMT = "%Y%m%d"      # format tag ?v=. Pakai "%Y%m%d%H%M" jika bisa update >1x/hari (hindari cache)
INDEX_MAX_STEPS = 3   # jumlah "Langkah berikutnya" yang disalin ke INDEX.md
RESULT_FILE = "/tmp/snapshot_result.txt"
LLM_URL = os.environ.get("LLM_URL", "https://openrouter.ai/api/v1/chat/completions")
WIB = datetime.timezone(datetime.timedelta(hours=7))
NOW = datetime.datetime.now(WIB)
TODAY = NOW.strftime("%Y-%m-%d")

# label snapshot (awal teks, huruf kecil) -> kunci
LABELS = {
    "selesai": "riwayat",
    "sedang berjalan": "saat_ini",
    "langkah berikutnya": "langkah",
    "keputusan baru": "keputusan",
    "pertanyaan terbuka": "pertanyaan",
    "ringkasan": "ringkasan",
}

def fail(msg):
    pathlib.Path(RESULT_FILE).write_text("Gagal: " + msg, encoding="utf-8")
    print(msg, file=sys.stderr)
    sys.exit(1)

# ---- Parse isi Issue ------------------------------------------------------
body = os.environ.get("ISSUE_BODY", "")
m = re.search(r"(?ms)^###\s+Snapshot\s*\n+(.*)", body)
snap = (m.group(1) if m else body).strip()

m = re.search(r"(?mi)^\s*Project\s*:\s*(\S+)", snap)
if not m:
    fail("Baris 'Project: <nama-folder>' tidak ditemukan di snapshot.")
slug = m.group(1).strip("`*")
if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", slug):
    fail(f"Nama project tidak valid: {slug}")

m = re.search(r"(?mi)^\s*(?:Tag Akun|Penulis)\s*:\s*(.+?)\s*$", snap)
who = re.sub(r"[\[\]`*]", "", m.group(1))[:80] if m else "LLM"

cands = [d for d in pathlib.Path(".").iterdir()
         if d.is_dir() and not d.name.startswith(".")
         and d.name.lower() == slug.lower() and (d / "INDEX.md").exists()]
if len(cands) != 1:
    fail(f"Folder project '{slug}' tidak ditemukan (harus punya INDEX.md).")
root = cands[0]

blocks, cur = {}, None
for line in snap.splitlines():
    if line.strip().startswith("```"):
        continue
    mm = re.match(r"^[-*]\s+(.*)$", line)  # bullet level atas (kolom 0)
    if mm:
        low = mm.group(1).lower()
        key = next((v for k, v in LABELS.items() if low.startswith(k)), None)
        if key:
            cur = key
            blocks[key] = [line]
            continue
    if cur:
        blocks[cur].append(line)
if not blocks:
    fail("Tidak ada bagian snapshot yang dikenali (Selesai / Sedang berjalan / Langkah berikutnya / "
         "Keputusan baru / Pertanyaan terbuka / Ringkasan).")
for k in blocks:
    while blocks[k] and not blocks[k][-1].strip():
        blocks[k].pop()
btxt = lambda k: "\n".join(blocks[k])

# ---- Helper edit teks -----------------------------------------------------
def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""

def stamp_date(text):
    pat = r"(?m)^(>?[ \t]*Terakhir diperbarui:).*$"
    if re.search(pat, text):
        return re.sub(pat, lambda m: f"{m.group(1)} {TODAY}", text, count=1)
    first, _, rest = text.partition("\n")
    return f"{first}\n\n> Terakhir diperbarui: {TODAY}\n{rest}"

def set_section(text, heading, body_txt, mode="replace"):
    pat = re.compile(rf"(?ims)^(##[ \t]+{re.escape(heading)}[^\n]*\n)(.*?)(?=^##[ \t]|\Z)")
    m = pat.search(text)
    if not m:
        return text.rstrip() + f"\n\n## {heading}\n{body_txt}\n"
    old = m.group(2).strip("\n")
    new = body_txt if mode == "replace" else body_txt + ("\n\n" + old if old else "")
    return text[:m.start(2)] + new + "\n\n" + text[m.end(2):]

def set_signature(text, name):
    sig = f"**`[{name} ({TODAY})]`**"
    pat = r"(?m)^\*\*`\[.*\]`\*\*[ \t]*$"
    if re.search(pat, text):
        return re.sub(pat, lambda m: sig, text, count=1)
    return re.sub(r"(?m)^(>?[ \t]*Terakhir diperbarui:.*)$", lambda m: m.group(1) + "\n\n" + sig, text, count=1)

def add_decision(text, entry):
    m = re.search(r"(?m)^## DECISION UPDATE", text)  # terbaru di atas
    if m:
        return text[:m.start()] + entry + "\n\n" + text[m.start():]
    return text.rstrip() + "\n\n" + entry + "\n"

def top_steps(lines, n):
    body = textwrap.dedent("\n".join(lines[1:]))
    items, cur_item = [], None
    for l in body.splitlines():
        if re.match(r"^\s*\d+[.)]\s", l):
            cur_item = [l]
            items.append(cur_item)
        elif cur_item is not None and l.strip():
            cur_item.append(l)
    return "\n".join("\n".join(it) for it in items[:n])

def llm_summary(context):
    """Opsional. Hanya untuk 'Status saat ini' di INDEX. Gagal = None (tidak menggagalkan apa pun)."""
    key, model = os.environ.get("OPENROUTER_API_KEY"), os.environ.get("MODEL")
    if not key or not model:
        return None
    system = ("Tulis ringkasan status project 2-4 kalimat dalam bahasa Indonesia, ringkas dan faktual, "
              "hanya dari teks yang diberikan. Jangan mengarang dan jangan menambah angka. "
              "Keluarkan hanya satu paragraf, tanpa pembuka dan tanpa daftar.")
    req = urllib.request.Request(
        LLM_URL,
        data=json.dumps({"model": model, "temperature": 0.1,
                         "messages": [{"role": "system", "content": system},
                                      {"role": "user", "content": context}]}).encode(),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            out = json.load(r)["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Ringkasan LLM gagal:", e, file=sys.stderr)
        return None
    out = re.sub(r"\s*\n\s*", " ", out)
    return out if 40 <= len(out) <= 900 else None

def git_date(path):
    r = subprocess.run(["git", "log", "-1", "--format=%ct", "--", path], capture_output=True, text=True)
    return datetime.datetime.fromtimestamp(int(r.stdout.strip()), WIB) if r.stdout.strip() else None

# ---- STATUS.md ------------------------------------------------------------
changed, applied = set(), []
s0 = read(root / "STATUS.md")
s = s0 or "# STATUS PROJECT\n"
for key, heading, mode in [("saat_ini", "Saat ini", "replace"), ("langkah", "Langkah berikutnya", "replace"),
                           ("pertanyaan", "Pertanyaan terbuka", "replace"), ("riwayat", "Riwayat", "prepend")]:
    if key in blocks:
        s = set_section(s, heading, btxt(key), mode)
        applied.append(f"STATUS/{heading}")
if s != (s0 or "# STATUS PROJECT\n"):
    s = set_signature(stamp_date(s), who)
    (root / "STATUS.md").write_text(s.rstrip() + "\n", encoding="utf-8")
    changed.add(f"{root.name}/STATUS.md")

# ---- DECISION.md ----------------------------------------------------------
if "keputusan" in blocks:
    d0 = read(root / "DECISION.md") or "# DECISION PROJECT\n"
    entry = f"## DECISION UPDATE untuk [{who} ({NOW.strftime('%Y-%m-%d %H:%M')})]\n{btxt('keputusan')}"
    d = stamp_date(add_decision(d0, entry))
    (root / "DECISION.md").write_text(d.rstrip() + "\n", encoding="utf-8")
    changed.add(f"{root.name}/DECISION.md")
    applied.append("DECISION")

# ---- INDEX.md (+ tag ?v= di semua link raw ke file repo) ------------------
i = read(root / "INDEX.md")
notes, txt, src = [], "", ""
if "ringkasan" in blocks:
    first, rest = blocks["ringkasan"][0], blocks["ringkasan"][1:]
    after = first.split(":", 1)[1].strip() if ":" in first else ""
    txt = (after + "\n" + textwrap.dedent("\n".join(rest))).strip()
    src = "dari snapshot"
elif any(k in blocks for k in ("saat_ini", "langkah", "riwayat", "keputusan")):
    ctx = "\n\n".join(btxt(k) for k in ("riwayat", "saat_ini", "langkah", "keputusan", "pertanyaan") if k in blocks)
    txt = llm_summary(ctx[:6000]) or ""
    src = "dibuat LLM"
if txt:
    i = set_section(i, "Status saat ini", txt)
    applied.append(f"INDEX/Status saat ini ({src})")
else:
    notes.append("Status saat ini di INDEX tidak diubah (tidak ada ringkasan)")
if "langkah" in blocks:
    steps = top_steps(blocks["langkah"], INDEX_MAX_STEPS)
    if steps:
        i = set_section(i, "Langkah berikutnya", steps)
        applied.append("INDEX/Langkah berikutnya")
i = stamp_date(i)
changed.add(f"{root.name}/INDEX.md")

URL = re.compile(r"(https://raw\.githubusercontent\.com/[^/\s]+/[^/\s]+/[^/\s]+/)([^\s)|`>\]?]+)(\?v=[0-9]+)?")
def tag(m):
    path = urllib.parse.unquote(m.group(2))
    if not pathlib.Path(path).is_file():
        return m.group(0)
    d = NOW if path in changed else (git_date(path) or NOW)
    return f"{m.group(1)}{m.group(2)}?v={d.strftime(V_FMT)}"
i = URL.sub(tag, i)
(root / "INDEX.md").write_text(i.rstrip() + "\n", encoding="utf-8")

# ---- Selesai --------------------------------------------------------------
if os.environ.get("GITHUB_ENV"):
    with open(os.environ["GITHUB_ENV"], "a") as f:
        f.write(f"PROJECT_DIR={root.name}\n")
msg = (f"Berhasil untuk {root.name}. Diterapkan: {', '.join(applied) or '-'}. Tag ?v= link diperbarui di INDEX.md."
       + (" Catatan: " + "; ".join(notes) + "." if notes else ""))
pathlib.Path(RESULT_FILE).write_text(msg, encoding="utf-8")
print(msg)
