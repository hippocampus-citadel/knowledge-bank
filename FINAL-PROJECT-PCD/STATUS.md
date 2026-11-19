# STATUS PROJECT

> Terakhir diperbarui: 2026-11-19

**`[CLAUDE @w30 (2026-11-19)]`**

## Saat ini
- Sedang berjalan / terhambat:
  - Runtime Colab sudah hilang; CSV hasil sudah aman di Drive. Notebook "Salinan preprocessing_REF_v2" adalah SANDBOX yang sudah diubah (pemeriksaan GPU diberi komentar, sel tambahan). Jangan dipakai untuk training; salin ulang template asli untuk training. Di sandbox jalankan SEL 0 saja (mengekstrak dataset ke /content/v2_raw = ROOT; ZIP berupa Path). SEL 1P menimpa gambar di tempat, jangan jalankan di sandbox kalibrasi.
  - Kalibrasi gate v2 menunggu persetujuan protokol (lihat Keputusan baru dan Pertanyaan terbuka).
  - E1 seed 2: belum dijalankan (hasil tidak mengubah keputusan, hanya melengkapi SD di laporan).
  - Pertanyaan "daftar pipeline wajib atau contoh" sengaja DITAHAN oleh user.

## Langkah berikutnya
- Langkah berikutnya (urut prioritas):
  1. Catat di DECISION.md: E1 gagal (+ angka), kalibrasi E2 dua detektor lengkap termasuk yang gagal, hasil uji ketahanan dan tingkat degradasi, aturan 0,02, E0b + CLAHE inferensi-saja gagal.
  2. Putuskan arah Tahap 1 berikutnya karena CLAHE gagal dan E2 diperkirakan netral: (a) setujui atau tolak protokol gate v2; (b) analisis kesalahan per strata pada best.pt E0b (blur, kecerahan, retraktor) yang belum dikerjakan; (c) maksimal 1 sampai 2 varian preprocessing baru yang ditetapkan sebelum dijalankan (kandidat: normalisasi warna/white balance, denoise ringan), 3 seed, pembanding E0b.
  3. Tanyakan ke dosen: daftar pipeline wajib atau contoh, dan tenggat final.
  4. Verifikasi kode _specular terhadap specular_mask pada 3 gambar bila E2 pernah dilatih; verifikasi nilai test E0b seed 0 dan 1 ke CSV.
  5. Layer aplikasi web dan implementasi quality gate di aplikasi: tidak dibahas sesi ini.

## Pertanyaan terbuka
- Pertanyaan terbuka:
  - Setujukah tim pada protokol gate v2 (val dipakai untuk menyetel gate)? Apakah nilai test E0b seed 0 dan 1 di CSV cocok dengan yang dikutip?
  - Apakah desain Tahap 1 di DECISION.md (sebelumnya berstatus usulan) sudah disetujui eksplisit oleh tim?
  - Apakah dosen mewajibkan semua tahap pada daftar pipeline atau hanya yang relevan (ditahan user)? Tenggat final? (11 November hanya progress update pertama.)
  - Anggaran GPU tersisa dan apakah dataset punya mask gigi (belum dijawab).
  - Dua gambar val dengan label di luar batas (lihat di atas): perlu diperiksa sumbernya; val efektif 824 gambar.

## Riwayat 
- Selesai sesi ini:
  (Metrik acuan semua eksperimen: val mAP50 single_cls=True. Test hanya untuk dokumentasi.)
  1. E0b (pre_identity) seed 2 selesai: val 0,9089; test 0,8999. Dengan itu E0b 3 seed: val 0,9191 / 0,9142 / 0,9089, rata-rata 0,9141, SD sampel 0,0051. Sanity check template ref-v2 lolos 3 dari 3 seed (selisih val terhadap baseline raw +0,0013, +0,0017, +0,0008; seed 0 tercatat 0,9190 di uji ketahanan, hanya beda pembulatan). Nilai test E0b seed 0 dan 1 yang dikutip di sesi ini tidak terverifikasi, mohon cek ke CSV sebelum dipakai di laporan.
  2. Pembersihan data: baris baseline_raw seed 2 dipulihkan dari CSV yang rusak akibat spreadsheet berlokal Indonesia (0,6743 terbaca 6,743 dan seterusnya). Sumber acuan sebaiknya CSV mentah di Drive. Baris seed 99 sudah dihapus dari kedua CSV (dikonfirmasi user). albumentations 2.0.8 di akun-1 dan akun-2, ultralytics 8.4.207, semua gambar .jpg.
  3. E1 (CLAHE: LAB kanal L, clip 2,0, tile 8x8, 3 seed direncanakan) didelegasikan ke teman B (seed 0) dan C (seed 1) di akun berbeda. Seed 2 belum dijalankan. Val: 0,8985 (seed 0) dan 0,8931 (seed 1) lawan E0b 0,9191 dan 0,9142 (selisih sekitar -0,021). Test: 0,8905 dan 0,8877. Aturan keputusan (rata-rata >= 0,9241 dan tiap seed >= E0b seed yang sama) GAGAL, dan secara matematis tidak bisa diselamatkan seed 2. Fungsi _clahe di SEL 1P sudah direview (parameter dibaca dari p["clip"], p["tile"]; BGR-LAB-BGR; hanya kanal L). User memastikan FP dan preview aman. Parameter TIDAK boleh disetel ulang dari hasil val.
  4. E2 (specular kecil) hanya kalibrasi dan cek keamanan, TIDAK dilatih. Detektor (urutan penting): kandidat = min(B,G,R) >= min_ch; filter ukuran komponen terhubung (min_area <= luas <= max_area_frac x luas gambar); lalu syarat kontras lokal (V - medianBlur(V, med_k) >= local_d); dilate; cv2.inpaint TELEA. Hasil pada train (3.859 gambar, 4.144 kotak label): detektor lama (V>=250 dan S<=30): 99,9% gambar dan 93,9% kotak tersentuh, gagal. Detektor baru min_ch 250, local_d 30: 75,9% gambar, 21,5% kotak tersentuh (gagal tipis terhadap batas 20%), luas kotak terhapus rata-rata 0,024%. Detektor baru min_ch 250, local_d 60: 59,7% gambar, 11,2% kotak, luas kotak terhapus rata-rata 0,008% (p95 0,046%), rasio specular di dalam kotak vs acak 0,55; lolos semua batas yang ditetapkan sebelum melihat angka. Parameter usulan: min_ch 250, local_d 60, med_k 51, max_area_frac 0,005, min_area 3, dilate 1, radius 3. Pemeriksaan visual pratinjau user: untuk 250/30 hampir tidak ada garis merah dibanding detektor lama; pratinjau 250/60 belum dilaporkan. Kode _specular untuk SEL 1P sudah ditulis tetapi belum diverifikasi identik dengan specular_mask pada 3 gambar.
  5. Uji ketahanan (robustness) memakai best.pt YANG SUDAH ADA tanpa retrain, pada val (826 gambar, 824 efektif karena 2 label di luar batas diabaikan Ultralytics: Right_Lateral_View anonymous_003-008-1115-01 dan Left_Lateral_View anonymous_003-008-1116-00). Urutan: gambar asli, degradasi, tahap preprocessing, simpan JPEG q100. Degradasi (skala 640): blur Gaussian sigma 1/2/4; blur gerak horizontal panjang 5/11/21; cahaya rendah kali 0,6/0,4/0,25; JPEG q 50/25/10. Cek kewajaran: nilai clean cocok dengan evaluasi E0b sebelumnya. Rata-rata val mAP50 E0b (3 seed): clean 0,9141; blur 0,9143 / 0,8764 / 0,8033; gerak 0,9072 / 0,8583 / 0,7180; gelap 0,9125 / 0,9035 / 0,8444; JPEG 0,9144 / 0,9106 / 0,8695. Ambang bahaya (turun > 0,02) terlewati antara L1 dan L2 untuk blur dan gerak, antara L2 dan L3 untuk gelap dan JPEG. Model rapuh terhadap ketajaman, relatif tahan terhadap cahaya dan kompresi.
  6. E1 pada val terdegradasi (seed 0 dan 1): kalah dari E0b di hampir semua kondisi (clean 0,8958); hanya dark_L3 unggul (0,8963 vs 0,8444) dan itu bias karena degradasi gelap kita linear, kebalikan CLAHE. E0b + CLAHE saat inferensi saja (3 seed): clean turun ke 0,8632 (-0,051); aturan (dark L2 dan L3 harus > +0,02 di ketiga seed) GAGAL (dark L2 negatif, dark L3 hanya +0,018 / +0,060 / +0,010). CSV tersimpan di Drive: robustness_identity.csv, robustness_clahe.csv, robustness_e0b_clahe_infer.csv.
  7. Kalibrasi quality gate v1 (gate_calibration.py; ambang = persentil ke-5 train bersih n=400; ketajaman = varians Laplacian pada lebar 640 >= 29,6; kecerahan = rata-rata abu-abu >= 126,5): GAGAL terhadap kriteria. Blur L1 (tidak berbahaya) lolos hanya 4,5%, gerak L1 50,5%, gelap L1 0%, clean lolos kedua gate 89%. Penyebab: persentil variasi alami bukan ukuran bahaya; varians Laplacian tidak konsisten antar jenis blur (blur L1 bermedian 14,3 vs gerak L2 16,4 padahal gerak L2 jauh lebih merusak).
  8. Diskusi desain: quality gate vs model robust. Pandangan Claude: gate sebagai lapisan utama untuk ketajaman, kebocoran gate diukur lewat kurva ketahanan; robustness training (augmentasi) adalah eksperimen terpisah dan baseline harus diulang. U-Net intraoral berprioritas rendah (model publik berdomain foto intraoral belum diverifikasi ada; ROI crop melanggar kontrak tahap); cara murah mengujinya adalah analisis kesalahan pada best.pt E0b (apakah false positive banyak di gusi, lidah, retraktor).
  9. Dibaca: template DL milik project sebelah (adaptor path Drive via pintasan folder). Keputusan: tidak mengubah template beku untuk E1 (risiko CSV bersama tertimpa antar-akun, kontaminasi seed 99 sudah menunjukkan rapuhnya).
  10. Skrip yang dibuat (ada di Colab/Drive user, tidak ada di repo): e2_specular_calibration.py (calibrate(n), preview, overlap), robustness_eval.py (main(pre_label, pre_fn, weights)), gate_calibration.py. Pustaka bantu perlu dimuat berurutan di runtime yang sama.

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
