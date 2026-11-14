# STATUS PROJECT

> Terakhir diperbarui: 2026-11-15

**`[@w30 (2026-11-15)]`**

## Saat ini
- Sedang berjalan / terhambat:
  - Status Weekly Progress 11 Nov dan paket Anggota B belum diketahui.
  - Template ref-v2 belum diuji di Colab. Struktur zip (folder images/ di level atas) dan format gambar (JPEG/PNG) belum diverifikasi.
  - Folder/berkas ganda di Drive (seed 0 dan 2, akun non-pemilik) belum terselesaikan.

## Langkah berikutnya
- Langkah berikutnya (urut prioritas):
  1. CRITICAL REVIEW metode preprocessing B (diminta user). Periksa: risiko inpainting specular menghapus lesi white spot; HE/CLAHE di kanal luminans; MSRCR banyak parameter; kontras HE/MSRCR/CLAHE = alternatif satu tahap, bukan ditumpuk; dukungan literatur (rujukan Thanh/Ding/Duong/Park belum diverifikasi); jumlah kandidat vs anggaran GPU; bahaya penyetelan parameter dari hasil val; status resize, augmentasi, ROI.
  2. Uji asap ref-v2 di Colab: PRE=[("identity",{})], cond pre_identity, epochs 2, seed 99; hapus baris seed 99 dari CSV.
  3. Tetapkan tertulis sebelum Tahap 1: metrik keputusan, kriteria "tahap berkontribusi", margin. [USULAN] val single_cls mAP50 (SD val 0,0049, n=3); test hanya laporan akhir; kontrol identity (E0b); kombinasi satu per kategori dengan urutan tetap.
  4. Putuskan kontrak SEL 1P untuk resize. [USULAN] longgarkan hanya untuk resize seluruh gambar.
  5. Perbarui jobdesc-week-1 dan STATUS.md lama: tiga split, kelas D/d, 6.266 gambar.
  6. Ganti nama/arsipkan `dataset_split` lama di Drive; pastikan run_meta.json seed 0/1/2 mencatat path split v2.
  7. Dari status sebelumnya: unduh best.pt seed 1 dan e164, catat md5; pastikan tidak ada email di notebook/LOG.md.

## Pertanyaan terbuka
- Pertanyaan terbuka:
  - Apakah tahap yang diuji harus mengikuti daftar B seluruhnya (sekitar 7 kondisi x 3 seed, sekitar 29 jam GPU, perkiraan kasar) atau disaring dulu?
  - Apakah ROI dipakai sebagai mask, crop, atau dikeluarkan dari Tahap 1?
  - Apakah augmentasi menjadi eksperimen terpisah (baseline harus diulang dengan setelan sama)?
  - Apakah dataset punya mask gigi untuk U-Net?

## Riwayat 
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
