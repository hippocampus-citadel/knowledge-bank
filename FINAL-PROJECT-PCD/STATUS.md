# STATUS PROJECT

> Terakhir diperbarui: 2026-10-31

**`[USER (2026-11-07 01:45)]`**

## Saat ini

- Perlu membuat task assignment untuk Project Report selanjutnya
- Judul sudah diterima, detailnya lihat di `proposal_feedback.md`
- Terhambat sejak sebelumnya (belum berubah): akses GPU, keahlian tiga anggota, akses dokter gigi.

## Langkah berikutnya
1. Membuat task assignment dan penentuan weekly progressnya

## Pertanyaan terbuka

- Arti kelas 0 dan 1?
- Apakah gambar tanpa label benar-benar negatif?
- Target populasi final (data menunjuk remaja/dewasa muda)?
- Apakah pipeline adaptif lebih baik daripada pipeline tetap? (hipotesis, belum terbukti; hasil nol tetap sah) [dari update sebelumnya]
- Apakah ada studi yang memvalidasi skor OHI-S/DMF-T dari foto? (belum dicari) [dari update sebelumnya]

## Riwayat 

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
