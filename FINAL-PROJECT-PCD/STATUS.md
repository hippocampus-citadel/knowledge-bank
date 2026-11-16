# STATUS PROJECT

> Terakhir diperbarui: 2026-11-16

**`[CLAUDE @w30 (2026-11-16)]`**

## Saat ini
- Sedang berjalan / terhambat:
  - E0b seed 2 belum jalan: T4 akun-1 sedang kena batas pemakaian. Opsi: tunggu limit pulih, atau jalankan di akun lain (notebook salinan baru + runtime baru; satu akun per seed; ACCOUNT berupa label, bukan email).
  - E1, E2, E3 belum dijalankan. Di BLOK DIISI SEL 1P baru ada fungsi identity dan clahe; fungsi specular belum ditulis.
  - Belum dikonfirmasi: (a) baris seed 99 sudah dihapus dari pre_identity_results.csv (6 baris) dan pre_identity_timing.csv (1 baris); (b) md5 best.pt seed 0 dan 1 sudah dicatat dan best.pt sudah diunduh ke laptop.

## Langkah berikutnya
- Langkah berikutnya (urut prioritas):
  1. Pastikan baris seed 99 sudah terhapus dari kedua CSV. Kalau belum, hapus sekarang, karena ikut menggeser statistik E0b.
  2. Jalankan E0b seed 2 (SEED=2, EXP={"cond":"pre_identity"}, PRE=[("identity",{})]); urutan sel: SEL 0, SEL 1, SEL 1P, sel bobot awal, SEL 2, SEL 3.
  3. Hitung rata-rata dan SD E0b dari 3 seed (val single_cls mAP50). Angka ini menjadi pembanding resmi E1/E2/E3. Jangan memakai baseline raw sebagai pembanding utama.
  4. Jalankan `import albumentations; print(albumentations.__version__)` di tiap akun penjalan, lalu bandingkan baris log albumentations antara run baseline dan E0b.
  5. Delegasikan E1 (CLAHE) ke anggota tim: kanal L di LAB, clip 2,0, tile 8x8, 3 seed. Parameter sudah dikunci, jangan disetel dari hasil val.
  6. Sebelum training E2 (inpainting specular kecil), selesaikan cek keamanan: hitung tumpang tindih komponen specular dengan kotak label karies di train, lalu periksa 30 sampel secara visual. Batalkan E2 jika tumpang tindih besar. Jalankan E3 (E1+E2) hanya setelah cek E2 selesai.
  7. Tulis tertulis sebelum Tahap 1: metrik, margin, aturan keputusan, parameter terkunci.

## Pertanyaan terbuka
- Pertanyaan terbuka:
  - Apakah pemilik template mau memperbaiki bug baris epoch ekstra, dan apa penyebab pastinya (belum dibuktikan dari kode)?
  - Format gambar val/test: apakah semuanya .jpg?
  - Versi albumentations di tiap akun (tidak dikunci di config.json); apakah sama?
  - Anggaran GPU: dengan sekitar 2 jam per run, 12 run (4 kondisi x 3 seed) kira-kira 24 jam, bukan 17 jam (ekstrapolasi dari seed 0 dan 1). Cukup atau perlu dikurangi?
  - Apakah dataset punya mask gigi? Cek nilai label dan shape_type di berkas JSON LabelMe. Status ROI klasik (varian mask) belum diputuskan.
  - Parameter specular (ambang HSV, batas 0,5%) belum dikalibrasi; siapa yang mengunci?
  - Pembagian E1 dan E2 ke anggota tim, dan siapa yang menyetujui hasil cek keamanan E2?
  - REQUIREMENTS.md tidak mencantumkan bobot persentase per kriteria. Apakah dosen bisa dikonfirmasi bahwa daftar pipeline hanya contoh?

## Riwayat 
- Selesai sesi ini:
  - Notebook preprocessing_REF_v2.ipynb dan manual (Claude Doc "Manual Eksperimen Folder Bersama") sudah dibaca. Seed baseline = 0, 1, 2.
  - Smoke test ref-v2 di Colab lolos (akun-1, T4, SEED 99, 2 epoch, cond pre_identity): bootstrap, SEL 1P (5.505 gambar, 117 dtk), training, backup Drive, dan SEL 3 berjalan tanpa error.
  - Format gambar: train semuanya .jpg (3.859 berkas; val/test belum dicek). SEL 1P menulis ulang JPEG kualitas 100, sehingga piksel tidak identik dengan aslinya.
  - E0b (cond pre_identity, PRE=[("identity",{})]) selesai untuk seed 0 dan seed 1. Pembanding baseline raw, single_cls=True, subset=all:
    seed 0: val mAP50 0,9191 vs 0,9178; val mAP50-95 0,7229 vs 0,7214; test mAP50 0,9036 vs 0,9021.
    seed 1: val mAP50 0,9142 vs 0,9125; val mAP50-95 0,7199 vs 0,7183; test mAP50 0,8978 vs 0,9019.
    Selisih val < 0,002, jauh di bawah SD val baseline (0,0049) dan margin keputusan (0,01). Sanity check template v2 lolos untuk 2 dari 3 seed.
  - Waktu (GPU Tesla T4): train_seconds seed 0 = 6670,2 dtk (130,79 dtk/epoch); seed 1 = 6976,0 dtk (136,78 dtk/epoch). Smoke test: 144 dtk/epoch. Satu run kira-kira 2 jam termasuk preprocessing dan evaluasi.
  - Temuan bug kecil di template: epoch_times.csv selalu memuat 1 baris ekstra (epoch N+1, sekitar 17 dtk, diduga dari validasi final Ultralytics; dugaan dari pola waktu, belum dibuktikan dari kode). Akibatnya muncul peringatan "epoch tercatat 51 != EPOCHS 50" dan train_seconds lebih besar sekitar 17 dtk. Ini perilaku normal: epochs_logged = EPOCHS + 1.
  - Log "albumentations: Blur, MedianBlur, ToGray, CLAHE (p=0,01)" muncul otomatis di run training. Ini augmentasi bawaan Ultralytics, hanya pada train, dan tidak dimatikan.

- Selesai sesi ini:
  - Critical review daftar preprocessing Anggota B. Rujukan yang SUDAH diverifikasi: Thanh 2022 (teks penuh: 600x600, Gaussian tanpa parameter kernel, flip+rotasi tanpa warna; specular hanya dilaporkan sebagai false positive refleksi cahaya, inpainting BUKAN dari makalah) dan Ding 2021 (MSRCR dipakai, tetapi kenaikan mAP terkonfound jumlah data 3.990 -> 7.980 pada kelompok gabungan; test hanya 70 pasien). Duong dan Park BELUM terverifikasi (hanya abstrak Duong terbaca).
  - Notebook audit_degradasi.ipynb (diuji data palsu, lalu dijalankan Wafi di Colab pada dataset_split_v2 subset train saja, 1.500 gambar). Keluaran di Drive: final_project_pcd/audit_degradasi/ (metrics_train.csv, ekstrem_list.csv, sheets/). Hasil: derau rendah (noise_sigma median ~0,5 dari skala 0-255); kontras global cukup (frac_dark median <1%, dyn_range ~190); frac_spec median 2,2% (retractors) vs 0,9% (no_retractors); resolusi 490x870 s.d. 2.000x2.700. 947 dari 1.500 gambar tanpa berkas label = negatif sah (zip berisi 1.957 label dari 5.505 gambar, proporsi cocok).
  - Specular (aturan HSV V>=240 dan S<=40, ambang awal belum dikalibrasi): komponen besar (>0,5% luas gambar) mendominasi (median frac_big 0 pada no_retractors, 0,31 pada retractors; 300 gambar). Pengamatan visual Wafi: titik kecil = pantulan sungguhan; gumpalan besar menutup hampir satu mahkota, berhenti dekat gusi/batas gigi, hanya pada tampak lateral. EXIF dataset kosong, sehingga hipotesis flash tidak bisa diuji.

- Selesai sesi ini:
  - Laporan eksperimen lanjutan (bagian 9-16 setelah exp-report-1) dan PPT ringkasan ditulis di chat. Belum masuk repo.
  - Klarifikasi tiga split (bukan keputusan baru): (1) split benchmark [8], bocor, hanya replikasi; (2) `dataset_split` = draf lokal awal, hanya no_retractors, untuk foto awam, tidak dipakai ablasi, diunggah ke Drive dengan nama sama; (3) `dataset_split_v2` = retraktor + no_retractors, bebas kebocoran, dipakai baseline dan ablasi.
  - Dibuat template `preprocessing_REF_v2.ipynb`: turunan `baseline_raw_REF_v1.ipynb` + SEL 1P (fungsi tahap dengan KONTRAK TAHAP: uint8 BGR, shape sama, deterministik, fotometrik) + pencatatan waktu per epoch (`epoch_times.csv`, `<cond>_timing.csv`; permintaan dosen). Diuji lokal dengan data palsu; BELUM diuji di Colab.
  - Manual folder bersama v2 (Claude Doc "Manual Eksperimen Folder Bersama - Final Project PCD") mencakup template baru.
  - Daftar preprocessing Anggota B diterima (rujukan belum diverifikasi): resize; Gaussian; inpainting specular highlight (HSV + cv2.inpaint); HE/MSRCR/CLAHE; segmentasi ROI gigi (klasik atau U-Net); augmentasi flip/rotasi tanpa perubahan warna.
  - Analisis awal daftar B: (A) cocok template: Gaussian, specular, HE, MSRCR, CLAHE, ROI varian mask; (B) geometris tapi label aman: resize (redundan dengan imgsz 640); (C) tidak cocok: augmentasi (hiperparameter training, hanya train), ROI crop (label ikut berubah), ROI U-Net (butuh mask gigi, belum tentu ada).

- Selesai (sejak 2026-11-09):
  - Baseline raw, split v2, YOLOv8s, 50 epoch, Ultralytics 8.4.207, Adam, batch 32, imgsz 640, workers 1, seed 0/1/2 selesai. Test single_cls mAP50: 0,9021 | 0,9019 | 0,8978 (SD ≈ 0,0024, n=3). Test single_cls mAP50-95: 0,7208 | 0,7145 | 0,713. Val single_cls mAP50: 0,9178 | 0,9125 | 0,9081.
  - Multi-kelas tidak stabil antar-seed (mis. precision val seed 0 vs 1: 0,7818 vs 0,6557).
  - retractors < no_retractors (test single_cls mAP50) di ketiga seed, selisih ±0,02, belum ada CI: s0 0,8925 vs 0,9155 | s1 0,8916 vs 0,9125 | s2 0,889 vs 0,9105.
  - Uji 164 epoch (raw, seed 1, cond baseline_raw_e164, split v2; disambung 2x lintas 3 akun dari epoch selesai 74 dan 148; results.csv lengkap 164 baris tanpa celah). Dibanding seed 1 50 epoch: test single_cls mAP50 0,8959 (0,9019), mAP50-95 0,7136 (0,7145); val single_cls mAP50 0,9108 (0,9125); multi-kelas naik: test mAP50 0,7232 (0,6957), val 0,7073 (0,6673). Epoch terbaik 103 (val multi mAP50 0,7086), plateau sekitar epoch 100; train loss terus turun, val box loss datar (overfitting ringan, Medium). Tafsir: tidak ada bukti 164 epoch menaikkan metrik utama (1 pasangan run; margin tidak ditetapkan sebelum run, jadi deskriptif).
  - Makna kelas terverifikasi (2.245 berkas LabelMe vs YOLO, cocok 100%): kelas_0 = D (karies gigi permanen, 6228 instance), kelas_1 = d (karies gigi susu, 554). Menurut paper, kotak dibuat mengelilingi GIGI berkaries.
  - Label M (44) dan m (1) ada di JSON, tidak ada di YOLO, arti tidak didefinisikan paper. 25 gambar hanya berlabel M/m; 15 masuk v2 sebagai negatif (train 12, test 3, val 0). Dampak diperkirakan di bawah SD antar-seed (Low-Medium).
  - md5: best.pt seed 0 aa7628bbc7ecdc19f000a5ba0f18e6ac (evaluasi ulang CPU mereproduksi 0,8144/0,8468/0,9021/0,7208); best.pt seed 2 51e95495410782698253245b97cb5b1b; best.pt e164 f35c8f6b3325aa006f7b222975004f9d; yolov8s.pt (seed 1 dst) 0a1d5d0619d5a24848a267ec1e3a3118 (md5 yolov8s.pt seed 0 tidak tercatat).
  - Notebook acuan baseline_raw_REF_v1.ipynb: parameter per salinan = SEED, ACCOUNT, EXP; mencatat LOG.md dan run_meta.json; sambung checkpoint terbukti jalan.
