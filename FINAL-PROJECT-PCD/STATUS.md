# STATUS PROJECT

> Terakhir diperbarui: 2026-10-31

## `[CLAUDE em***********nt (2026-10-31 15:45)]`
**Update STATUS — 2026-10-31 (sesi review dataset)**
Legenda: [VERIFIED] = dihitung dari berkas lokal user; [INFERENSI] = kesimpulan AI dari pola data; [KEPUTUSAN USER]; [REKOMENDASI AI, BELUM DIPUTUSKAN TIM].

- Selesai sesi ini:
  - Langkah 1 STATUS sebelumnya (konfirmasi dataset) selesai sebagian, memakai skrip `analisis_dataset.py` pada Dataset.zip dan Benchmarking Dataset.zip.
  - Record: DOI 10.5281/zenodo.14827784, berkas terbuka, lisensi CC BY 4.0 (wajib atribusi) [VERIFIED]. Record berkas terbatas (v2) jangan dipakai; ID persisnya perlu verifikasi (hasil pencarian menunjukkan dua angka berbeda).
  - Isi: Dataset.zip = 6.265 gambar (no_retractors 2.752, retractors 2.753, pilot 760). Benchmark = 6.266 gambar (train 5.011 / valid 627 / test 628), gambarnya sama dengan Dataset.zip. Angka resmi 6.313 TIDAK cocok dengan berkas (selisih ±47) [VERIFIED]. Pakai angka hasil verifikasi di proposal.
  - Struktur: 5 view per set (Frontal, Left_Lateral, Mandibular, Maxillary_Occlusal, Right_Lateral). Nama: `anonymous_<A>-<site>-<N>-<F>_<T>_<View>_View.jpg` (F: 00=no_retractors, 01=retractors; N=nomor set berurutan; T=Unix ms). Folder pilot berpenamaan berbeda dan sebagian tidak terparse, jadi dikecualikan.
  - Set: no_retractors 559 set (542 lengkap lima view), retractors 563. 93% set retractors berpasangan dengan no_retractors N+1 (median 9 menit) → dugaan satu pasien menghasilkan satu set per subset, sekitar 560 pasien [INFERENSI, Medium]. ID pasien resmi tidak ada.
  - Label YOLO (Darknet_YOLO): format `kelas x_tengah y_tengah lebar tinggi` (normalisasi 0–1). Hanya kelas 0 dan 1; kelas 1 sekitar 9% kotak. Makna kelas TIDAK diketahui (tidak ada yaml/names di Dataset maupun Benchmark).
  - Positif (no_retractors): 957 gambar punya kotak; 90% di Mandibular (494) dan Maxillary_Occlusal (367); Frontal 13, Left_Lateral 40, Right_Lateral 43. 1.779 gambar tanpa berkas label = "kandidat negatif" (belum terbukti negatif; hanya 16 label kosong). 92% grup punya positif oklusal → ini dataset kasus karies, bukan populasi skrining.
  - Split resmi Benchmark BOCOR: 65,6% set asli (736/1.122) gambarnya tersebar di >1 split; 88,3% pasangan retractors/no_retractors terpisah antar split → split acak per gambar. Jangan dipakai untuk evaluasi. mAP di makalah kemungkinan optimistis (besarnya belum terukur) [VERIFIED untuk kebocoran].
  - Kualitas label: 23 kotak no_retractors (semuanya Frontal/Lateral) keluar gambar atau berukuran nol; oklusal 0. Penyebab belum diketahui (dugaan orientasi EXIF hampir pasti salah: 88% gambar tanpa EXIF).
  - Perangkat/resolusi: EXIF ada di 760/6.265 gambar (sama dengan jumlah pilot; kemungkinan hanya pilot, Low), minimal 3 model Samsung (SM-A235F, SM-N985F, SM-A045F). Resolusi sangat beragam (±727×408 sampai 4080×3060; rasio 16:9 dan 4:3). KOREKSI: klaim gap 3 di update 09:45 ("dataset Zenodo hanya satu perangkat") TIDAK terverifikasi, jangan dipakai di proposal.
  - Split buatan sendiri `buat_split.py`: subset no_retractors, semua 5 view, per grup (set + N berurutan dengan selisih ≤30 menit), stratifikasi, seed 42, 70/15/15 → 548 grup: train 383 / val 82 / test 83 (1.927 / 410 / 415 gambar). Val/test: 0 kotak bermasalah. Positif di test: Mandibular 73, Maxillary 59, Frontal 2, Left 4, Right 5 (frontal+lateral hanya deskriptif). Negatif oklusal di test sekitar 10 (Mandibular) dan 24 (Maxillary). Berkas `dataset_split/split.csv` dan `data.yaml` = bukti split; JANGAN diubah atau diulang dengan seed lain.

- Sedang berjalan / terhambat:
  - Proposal sementara jatuh tempo 4 November 2026; belum ditulis.
  - Belum diketahui: arti kelas 0/1, penyebab 23 kotak bermasalah, apakah "tanpa label" = tanpa karies, ID record terbatas yang tepat.
  - Terhambat sejak sebelumnya (belum berubah): akses GPU, keahlian tiga anggota, akses dokter gigi.

- Langkah berikutnya (urut prioritas):
  1. Tulis proposal; angka di atas dipakai untuk deskripsi dataset dan keterbatasan.
  2. Tulis klaim sesuai data: deteksi lesi karies pada foto intraoral, metrik utama di view oklusal, frontal/lateral deskriptif; BUKAN skrining populasi umum dan bukan klaim foto pengguna awam; populasi terbatas remaja/dewasa muda (abstrak: usia 10–24, Medium).
  3. Konfirmasi makna kelas 0/1 dari teks penuh makalah (Nature/PMC dibuka manual; akses otomatis diblokir) atau penulis. Sementara pakai evaluasi satu kelas (`single_cls`) sebagai metrik utama.
  4. Cek visual beberapa dari 23 kotak bermasalah.
  5. Setelah proposal: kurva belajar (25/50/100% data latih), baseline YOLO di `dataset_split`, lalu pipeline preprocessing. Karena daya uji rendah (±383 grup latih, 83 grup uji), pertimbangkan 5-fold per grup + bootstrap per grup + beberapa seed.

- Keputusan baru (+ alasan 1 kalimat):
  - [KEPUTUSAN USER, kecenderungan] Memakai semua 5 view, bukan hanya oklusal: sesuai narasi smartphone. Syarat dari AI: metrik utama di oklusal karena positif frontal/lateral hanya 96 gambar.
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Pakai split per grup buatan sendiri, bukan split Benchmark: split resmi bocor.
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Tidak menggabung dataset lain (sejalan keputusan dataset tunggal); dataset eksternal hanya sebagai uji generalisasi, jika ada yang berlisensi jelas dan berkotak karies pada foto ponsel (belum dicari).
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Pilot dikecualikan; subset retractors tidak dianggap data baru (pasien sama) dan, jika dipakai, harus satu grup dengan pasangannya.

- Pertanyaan terbuka:
  - Arti kelas 0 dan 1?
  - Apakah gambar tanpa label benar-benar negatif?
  - Target populasi final (data menunjuk remaja/dewasa muda)?
  - Apakah pipeline adaptif lebih baik daripada pipeline tetap? (hipotesis, belum terbukti; hasil nol tetap sah) [dari update sebelumnya]
  - Apakah ada studi yang memvalidasi skor OHI-S/DMF-T dari foto? (belum dicari) [dari update sebelumnya]

## `[CLAUDE w*********30 (2026-10-31 09:45)]`

**Update STATUS — 2026-10-31**
- Selesai sesi ini:
  - Membaca INDEX, SOP, PREFERENCES, dan REQUIREMENTS (STATUS dan DECISIONS tidak dibuka).
  - Literature review terarah (±25 artikel; yang dibaca abstrak dan potongan isi, bukan teks penuh; status Scopus BELUM diverifikasi, cek per ISSN). Gap mayoritas:
    (1) performa foto ponsel tertinggal (F1 ponsel 42,8–80% vs kamera profesional 68,3–95,4%, Moharrami dkk. 2024) dan recall rendah;
    (2) banyak studi memakai gigi cabut atau kamera intraoral, bukan foto pengguna awam;
    (3) uji lintas perangkat jarang (dataset Zenodo hanya satu perangkat);
    (4) preprocessing dan kualitas foto jarang menjadi variabel utama (Ding 2021 dan Park 2022 hanya sampingan);
    (5) pelaporan lemah (XAI hanya 3 dari 23 studi, aplikasi terdeploy hanya 4 studi);
    (6) uji pengguna awam terbatas (AICaries, OralCam).
  - Bukti VLM 2026: Gemini zero-shot sensitivitas tinggi tetapi presisi rendah (over-detection); YOLO lebih akurat untuk lokalisasi.
  - Penilaian feasibility terhadap rubrik dosen (tahap klasik pengolahan citra harus terlihat dan dianalisis per tahap).
- Sedang berjalan / terhambat:
  - Judul belum ada; scope masalah gigi belum final (karies pasti).
  - Terhambat informasi: akses GPU, keahlian tiga anggota, akses dokter gigi untuk validasi.
- Langkah berikutnya (urut prioritas):
  1. Konfirmasi dataset Zenodo: record yang dipakai (ada record berkas terbatas), lisensi, jumlah subset tanpa retraktor, ID pasien, definisi kelas.
  2. Susun proposal: problem statement, latar belakang, tabel literatur (template di REQUIREMENTS), proposed solution, deskripsi dataset.
  3. Rekomendasi judul berdasarkan gap di atas.
  4. Setelah proposal: baseline YOLO, lalu pipeline preprocessing.
- Keputusan baru (+ alasan 1 kalimat):
  - [KEPUTUSAN USER] Hanya memakai dataset Zenodo (Ahmed dkk., Sci Data 2025), tanpa menggabung dataset lain: menghindari masalah label, lisensi, dan provenans.
  - [KEPUTUSAN USER] Kontribusi utama = preprocessing pipeline-heavy: sejalan dengan rubrik (kelengkapan pipeline dan analisis per tahap).
  - [KEPUTUSAN USER] Pipeline preprocessing dibuat adaptif (tidak kaku): diinginkan user.
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Satu masalah utama (karies); gingivitis hanya jika dataset terverifikasi dan dievaluasi terpisah; gigi bungsu tidak layak dari foto; plak dan kalkulus feasibility rendah.
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Adaptif berbasis aturan di OpenCV (ukur kualitas, lalu pilih tindakan), bukan model terlatih; eksperimen empat kondisi (tanpa preprocessing, tetap, adaptif, adaptif + quality gate) dengan metrik mAP50 dan recall; degradasi buatan pada test set; VLM hanya sebagai pembanding; Streamlit/Flask, bukan Flutter.
- Pertanyaan terbuka:
  - Target populasi (anak sekolah, dewasa, lansia)?
  - Apakah adaptif benar-benar lebih baik daripada pipeline tetap? (hipotesis, belum terbukti; hasil nol tetap sah)
  - Apakah ada studi yang memvalidasi skor OHI-S/DMF-T turunan foto? (belum dicari)
