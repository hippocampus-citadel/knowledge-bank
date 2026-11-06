# TEAM-ROLES — Final Project PCD (Skrining Karies, Foto Intraoral)

> Terakhir diperbarui: 7 November 2026

## 1. Keputusan yang TIDAK boleh diubah
- Judul: Implementasi Teknik Pengolahan Citra Digital untuk Meningkatkan Deteksi Lesi Karies pada Foto Intraoral Remaja dan Dewasa Muda Berbasis Aplikasi Web.
- Dataset: hanya Ahmed dkk. (Sci Data 2025), Zenodo DOI 10.5281/zenodo.14827784 (Benchmarking Dataset). Dilarang menggabung dataset lain.
- Split: folder `train`/`valid`/`test` bawaan benchmark (5.050/631/631). Semua eksperimen memakai split yang sama.
- Model deteksi: YOLOv8s, parameter dan augmentasi bawaan, sebagai acuan [8]. Variabel yang diubah hanya preprocessing.
- Preprocessing diterapkan offline, identik pada train, valid, dan test.
- Anotasi berupa kotak pada gigi berkaries (label `d`/`D`), bukan kontur lesi. Evaluasi sementara `single_cls`.
- Klaim: skrining/edukasi awal, bukan diagnosis medis.
- Stack wajib: Python + OpenCV untuk algoritma pengolahan citra.
- Dilarang mengarang sumber, angka, atau kutipan. Bila tidak pasti, tulis "perlu verifikasi".

## 2. Alur kerja dan tahap
- Tahap 1 (sekarang): ablasi per tahap: (1) raw, (2) tiap tahap preprocessing terpisah, (3) kombinasi.
- Tahap 2 (nanti, jangan dikerjakan sebelum Tahap 1 selesai): empat kondisi (tanpa preprocessing, tetap, adaptif, adaptif + quality gate) memakai tahap terpilih dari Tahap 1.
- Tenggat weekly progress: 11 November 2026. Tanggal final belum ada.

## 3. Anggota A — Data, baseline, evaluasi
- Tugas: unduh dan verifikasi dataset (lisensi, jumlah gambar, split), replikasi baseline YOLOv8s (target wajar mendekati mAP50 0,841, tidak harus sama persis), tulis skrip training dan evaluasi, bantu menjalankan run Tahap 1.
- Serahan (target 8 November): paket baseline beku berisi skrip, config (ukuran gambar, epoch, seed), lokasi data, bobot `weights/baseline_yolov8s.pt`, dan skema hasil.
- Skema hasil (CSV): `condition, seed, precision, recall, map50, map50_95, notes`.
- Memutuskan: ukuran gambar, epoch, daftar seed (minimal 3), kriteria "tahap berkontribusi tinggi" (ditulis sebelum eksperimen).

## 4. Anggota B — Preprocessing dan eksperimen Tahap 1
- Tugas: bangun fungsi preprocessing (OpenCV), uji visual, lalu retrain per tahap dan kombinasi memakai paket baseline A tanpa mengubah pengaturan lain.
- Kandidat tahap (usulan, belum final; B dan A menetapkan bersama): CLAHE, koreksi warna/white balance, denoising, koreksi gamma, sharpening.
- Kontrak fungsi: `preprocess(img_bgr, stages) -> {"final": ndarray, "stages": {nama_tahap: ndarray}}`. Satu fungsi per tahap, deterministik, tanpa efek samping.
- Serahan: modul `preprocess/`, tabel hasil per kondisi, gambar sebelum/sesudah dan histogram per tahap, catatan analisis (termasuk hasil nol/negatif).
- Usulan tenggat: fungsi siap 9 November, hasil awal sebelum 11 November.
- Dilarang: mengubah hiperparameter atau split agar hasil "terlihat bagus"; menerapkan preprocessing hanya pada test.

## 5. Anggota C — Aplikasi web
- Tugas: aplikasi web (framework bebas selama berbasis Python dan memenuhi rubrik; Streamlit/Flask disarankan). Arsitektur diputuskan C.
- Fitur wajib: unggah atau ambil gambar; tampilkan keluaran tiap tahap pipeline; tampilkan hasil deteksi (kotak + skor keyakinan); teks penafian "bukan diagnosis medis"; berjalan lancar tanpa error.
- Antarmuka yang dipakai: fungsi `preprocess` dari B dan bobot dari A. Gunakan stub/dummy dulu agar tidak menunggu.
- Aturan data: tidak menyimpan gambar unggahan secara permanen (usulan).
- Usulan tenggat: kerangka aplikasi dengan stub pada 10 November.
- Dilarang: mengklaim diagnosis; menambah fitur di luar rubrik sebelum fitur wajib stabil.

## 6. Aturan bersama
- Setiap anggota harus mampu menjelaskan seluruh pipeline dan eksperimen (penilaian individu mencakup tanya jawab).
- Hasil dicatat di repo dengan nama berkas dan skema tetap; angka tidak boleh disalin dari ingatan.
