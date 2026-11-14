import os, re, sys, json, datetime, pathlib, urllib.request

ALLOWED = ["INDEX.md", "STATUS.md", "DECISION.md"]

body = os.environ["ISSUE_BODY"]
m = re.search(r"###\s*Project\s*\n+(.+?)\n+###\s*Snapshot\s*\n+(.+)", body, re.S)
if not m:
    sys.exit("Format issue tidak dikenali.")
slug, snap = m.group(1).strip(), m.group(2).strip()
if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", slug):
    sys.exit(f"Nama project tidak valid: {slug}")

# Cocokkan nama folder tanpa peduli huruf besar/kecil; folder harus punya INDEX.md
cands = [d for d in pathlib.Path(".").iterdir()
         if d.is_dir() and not d.name.startswith(".")
         and d.name.lower() == slug.lower() and (d / "INDEX.md").exists()]
if len(cands) != 1:
    sys.exit(f"Folder project '{slug}' tidak ditemukan (harus punya INDEX.md).")
root = cands[0]

current = ""
for f in ALLOWED:
    p = root / f
    text = p.read_text(encoding="utf-8") if p.exists() else "(belum ada)"
    current += f"\n##### {f}\n{text}\n"

today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

SYSTEM = """Kamu memperbarui file konteks project dari snapshot akhir sesi.
Aturan:
- Snapshot berisi perubahan (delta), bukan isi baru. GABUNGKAN ke file yang ada, jangan ditempel utuh.
- "Selesai sesi ini": ringkas 1 baris ke "Riwayat singkat" di STATUS.md (simpan maks 5, buang yang terlama).
- "Sedang berjalan / terhambat": GANTI bagian "Saat ini" di STATUS.md.
- "Langkah berikutnya": GANTI di STATUS.md, samakan di INDEX.md.
- "Keputusan baru": tambahkan ke DECISION.md, bukan STATUS.md.
- "Pertanyaan terbuka": taruh di STATUS.md, hapus yang sudah terjawab.
- Perbarui baris "Terakhir diperbarui" ke tanggal hari ini di INDEX.md dan STATUS.md.
- Jangan mengarang. Jangan mengubah bagian lain. Pertahankan bahasa dan format file.
- Keluarkan HANYA file yang berubah, dengan isi LENGKAP, dalam format persis:
=====FILE: <nama file>=====
<isi lengkap>
=====END=====
Tanpa teks lain."""

user = f"Tanggal hari ini: {today}\n\nISI SAAT INI:\n{current}\n\nSNAPSHOT:\n{snap}"

req = urllib.request.Request(
    "https://openrouter.ai/api/v1/chat/completions",
    data=json.dumps({
        "model": os.environ["MODEL"],
        "temperature": 0.1,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
    }).encode(),
    headers={
        "Authorization": "Bearer " + os.environ["OPENROUTER_API_KEY"],
        "Content-Type": "application/json",
    },
)
with urllib.request.urlopen(req, timeout=180) as r:
    out = json.load(r)["choices"][0]["message"]["content"]

blocks = re.findall(r"=====FILE: (\S+?)=====\n(.*?)\n=====END=====", out, re.S)
if not blocks:
    sys.exit("Output model tidak sesuai format. Tidak ada file yang diubah.")

for name, content in blocks:
    if name not in ALLOWED:
        sys.exit(f"File tidak diizinkan: {name}")
    if not content.strip() or len(content) > 30000:
        sys.exit(f"Isi {name} tidak valid.")
for name, content in blocks:
    (root / name).write_text(content.rstrip() + "\n", encoding="utf-8")

with open(os.environ["GITHUB_ENV"], "a") as f:
    f.write(f"PROJECT_DIR={root.name}\n")
print("Updated:", ", ".join(n for n, _ in blocks))
