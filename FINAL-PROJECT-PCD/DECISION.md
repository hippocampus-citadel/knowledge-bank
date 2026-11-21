# DECISION PROJECT

> Terakhir diperbarui: 2026-11-21

## DECISION UPDATE untuk [CLAUDE @w30 (2026-11-21 11:27)]
- Keputusan baru (+ alasan 1 kalimat):
  - TENGGAT FINAL = 7 DESEMBER 2026 (dari dosen); perbarui INDEX bagian Batasan (11 November hanya Weekly Progress). Alasan: ketentuan terbaru.
  - Daftar tahapan pipeline di ketentuan dosen OPSIONAL tetapi harus sesuai solusi yang diambil (dikonfirmasi user). Alasan: menentukan isi pipeline aplikasi.
  - Cakupan klaim dan gate: HANYA foto permukaan kunyah (Mandibular dan Maxillary); aplikasi meminta pengguna memotret permukaan kunyah; sudut lain "belum divalidasi" tanpa gate; perluasan masuk "pengembangan selanjutnya". Alasan: 96,7% lesi di dua view itu, ambang hanya dikalibrasi di sana, dan view lain hanya 3-15 lesi (dikonfirmasi user).
  - Gate ketajaman v2 = Tenengrad, tolak bila <1134,018, hanya oklusal. Alasan: satu-satunya metrik lolos aturan terkunci di val dan terkonfirmasi di test (TPR 0,874; FPR 0,128).
  - Test sudah dipakai SATU kali untuk gate ketajaman; tidak boleh diulang untuk komponen itu. Alasan: menjaga independensi.
  - Protokol gate v2 (val untuk menyetel, test sekali, ambang berbasis bahaya bukan persentil) diterapkan. Alasan: v1 berbasis persentil gagal.
  - [Usulan Claude, diikuti user, belum dikonfirmasi tertulis] Tidak ada varian preprocessing baru yang DILATIH (CLAHE gagal, specular tidak dilatih, normalisasi warna dan denoise tanpa dasar data); hasil negatif dilaporkan. Tahap klasik tetap ditampilkan dan dianalisis di aplikasi/laporan (gate, peringatan pantulan, koreksi gelap hanya bila E-B lolos). Alasan: kegagalan CLAHE, FP berada di gigi, dan dalam-view tidak ada efek kualitas foto; rubrik menilai tahapan dan analisisnya, bukan hanya kenaikan skor.
  - [Usulan Claude, belum diputuskan] Model aplikasi = baseline raw seed 0 (val 0,9178; test 0,9021; md5 aa7628bbc7ecdc19f000a5ba0f18e6ac; hasil CPU terreproduksi). Alasan: dilatih pada foto asli seperti input pengguna dan artefaknya terverifikasi.
  - U-Net/ROI, E2 training, E3, dan retrain model tetap DIBEKUKAN. Alasan: FP bukan di gusi/bibir, tenggat dekat, dan efek diperkirakan kecil.
  - Label dataset TIDAK diubah; skor/presisi dilaporkan terhadap label dataset dengan catatan kemungkinan label lesi dini tidak lengkap (sampel satu dokter, kecil). Alasan: perbandingan antar-eksperimen harus tetap valid.

## DECISION UPDATE untuk [CLAUDE @w30 (2026-11-19 08:10)]
- Keputusan baru (+ alasan 1 kalimat):
  - E1 dinyatakan gagal menurut aturan yang tidak diubah; parameter tidak disetel ulang (menjaga val independen).
  - Pembanding resmi E1 sampai E3 adalah rata-rata E0b 0,9141 (bukan baseline raw), karena template identik dan sanity check lolos 3/3.
  - E2 tidak dilatih sekarang (user setuju "kurang worth it": efek diperkirakan di bawah margin 0,01 dan memakan sekitar 7 jam GPU); kode dan parameter disimpan, boleh dilatih (3 seed) bila nanti ada sisa GPU dan waktu. E3 (E1+E2) ditahan, tidak relevan karena E1 gagal.
  - Batas keamanan E2 ditetapkan sebelum melihat angka dan tidak dilonggarkan: batal bila >20% kotak tersentuh atau >5% luas kotak terhapus; E2 layak GPU bila >=10% gambar terdampak; maksimal 2 putaran perbaikan detektor.
  - Uji ketahanan memakai best.pt E0b tanpa retrain, dengan tingkat degradasi dan ambang 0,02 ditetapkan sebelum melihat hasil; urutan evaluasi selalu degradasi lalu preprocessing.
  - USULAN Claude, belum dikonfirmasi tim: CLAHE keluar dari pipeline dan kasus gelap ditangani gate kecerahan, bukan perbaikan citra.
  - USULAN protokol gate v2, belum disetujui: ambang dipilih berdasarkan bahaya (tolak bila penurunan mAP kondisi itu > 0,02), val dipakai sebagai set pengembangan gate dengan satu konfirmasi di test (penyimpangan yang harus dicatat), dan metrik ketajaman diganti yang sensitif arah.

## DECISION UPDATE untuk [CLAUDE @w30 (2026-11-16 18:07)]
- Keputusan baru (+ alasan 1 kalimat):
  - E0b wajib dijalankan untuk 3 seed (0, 1, 2); disetujui Wafi. Alasan: gambar berformat .jpg dan SEL 1P mengompres ulang, jadi kontrol berpasangan per seed diperlukan untuk memisahkan efek template/kompresi dari efek tahap.
  - Template ref-v2 tetap dibekukan walau ada bug callback waktu; jangan edit template maupun epoch_times.csv, dan saat analisis buang baris dengan epoch > EPOCHS. Alasan: semua kondisi memakai template yang sama, sehingga perbandingan tetap adil.
  - Augmentasi albumentations bawaan tidak dimatikan. Alasan: EXP hanya boleh berisi epochs dan cond, dan baseline berjalan dengan kondisi yang sama. Di laporan tulis "tanpa augmentasi tambahan di luar bawaan Ultralytics".
  - USULAN (Claude); Wafi tidak menyanggah, tetapi belum disetujui eksplisit oleh tim: Tahap 1 = E0b identity, E1 CLAHE, E2 specular kecil (<0,5% luas gambar), E3 = E1+E2; 3 seed; keputusan lewat val single_cls mAP50 vs E0b, lolos jika rata-rata naik >= 0,01 dan tidak ada seed yang lebih buruk dari identity; test disentuh sekali di akhir untuk pemenang; hasil negatif tetap dilaporkan. Dikeluarkan dari training: Gaussian, HE, MSRCR, resize offline, augmentasi sebagai hyperparameter, ROI crop, ROI U-Net. Pelengkap di luar training: uji ketahanan degradasi sintetis (blur, gerak, cahaya rendah, JPEG; val saja), quality gate di aplikasi, analisis visual Gaussian/HE/MSRCR tanpa training.

## DECISION UPDATE untuk [@w30 (2026-11-15 12:08)]
- Keputusan baru (+ alasan 1 kalimat):
  - [Wafi] Audit manual dilewati dan metrik otomatis dipercaya, karena foto tampak normal baginya.
  - [Wafi] Klaim dibatasi pada dataset yang dipakai (satu perangkat, pencahayaan tertentu), dengan quality gate sebagai mitigasi, karena kondisi HP lapangan tidak terwakili.
  - [Claude, dinyatakan pasti] Kontrol identity (E0b) wajib, karena tanpa kontrol efek tiap tahap tidak terukur.
  - [USULAN Claude, BELUM disetujui] Kandidat: CLAHE di kanal luminans; specular hanya komponen kecil (<0,5% luas gambar, ambang belum dikalibrasi). Metrik val single_cls mAP50, margin +0,01 (~2 SD 0,0049; angka usulan, bukan baku), 3 seed, test sekali untuk finalis. Uji ketahanan: degradasi sintetis (blur, kurang cahaya) 3 tingkat, hanya val, evaluasi best.pt baseline tanpa retrain; waspadai sirkularitas CLAHE vs kontras rendah linear.
  - [USULAN Claude, BELUM disetujui] Ditolak: Gaussian (derau rendah); HE dan MSRCR (cukup satu tahap kontras); resize offline (YOLO sudah menyeragamkan); augmentasi (hiperparameter training, eksperimen terpisah, baseline diulang); ROI crop dan U-Net (mask gigi belum tentu ada); specular gumpalan besar (piksel jenuh tidak menyimpan informasi).

## DECISION UPDATE untuk [@w30 (2026-11-15 02:00)]
- Keputusan baru (+ alasan 1 kalimat):
  - `preprocessing_REF_v2.ipynb` dipakai sebagai template eksperimen preprocessing, `baseline_raw_REF_v1.ipynb` tetap untuk baseline; alasan: preprocessing dan pencatatan waktu (permintaan dosen) belum didukung REF_v1.

## DECISION UPDATE untuk [CLAUDE em***********nt (2026-11-11 18:30)]
- Keputusan baru (+ alasan 1 kalimat):
  - Semua eksperimen berikutnya membuat salinan dari baseline_raw_REF_v1.ipynb yang dibekukan; alasan: prosedur identik antar eksperimen.
  - Kondisi ablasi mulai dari yolov8s.pt (COCO) dengan konfigurasi baseline, tanpa transfer bobot hasil baseline; alasan: menghindari konfon antara efek tahap dan epoch tambahan.
  - Uji panjang training memakai cond terpisah (baseline_raw_e164), tidak mengubah config.json baseline; alasan: mencegah menimpa hasil baseline.

## DECISION UPDATE untuk [CLAUDE w*********30 (2026-11-09 13:45)]
- Keputusan baru (+ alasan 1 kalimat):
  - [KEPUTUSAN USER] Model hasil replikasi TIDAK dikunci sebagai baseline ablasi; replikasi hanya uji kewajaran; alasan: dilatih di split bocor dan melalui resume dengan pengaturan berubah.
  - [KEPUTUSAN USER] Baseline ablasi = YOLOv8s tanpa preprocessing yang dilatih di `dataset_split_v2` dengan konfigurasi mengikuti [8] disertai deviasi; alasan: split benchmark bocor (65,6% set tersebar lintas split) sehingga selisih antar-kondisi bisa terdistorsi.
  - [KEPUTUSAN USER] `dataset_split_v2` menggantikan `dataset_split` untuk eksperimen utama; pilot dikecualikan; alasan: komposisi retractors + no_retractors seperti benchmark tanpa kebocoran antar-grup yang terdeteksi.
  - [KEPUTUSAN USER] Semua kondisi ablasi memakai 50 epoch, batch 32, imgsz 640, Adam, workers 1, bobot awal COCO; alasan: hemat GPU; user akan menguji bahwa 164 epoch dapat dipangkas.
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Dasar ablasi = kontrol internal (baseline sendiri, split dan konfigurasi identik untuk semua kondisi), bukan angka [8]; jangan klaim lebih baik dari [8]; perbandingan absolut hanya jika split, konfigurasi, dan metrik identik.
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Metrik utama single_cls pada test; test dipakai sekali per run; tidak ada penyetelan lebih banyak untuk kondisi usulan; hasil negatif dilaporkan; 3 seed dan bootstrap per grup.
    
## DECISION UPDATE untuk [USER (2026-11-07 01:55)]
- Judul resmi: Implementasi Teknik Pengolahan Citra Digital untuk Meningkatkan Deteksi Lesi Karies pada Foto Intraoral Remaja dan Dewasa Muda Berbasis Aplikasi Web

## DECISION UPDATE untuk [CLAUDE em***********nt (2026-10-31 15:45)]
Keputusan baru (+ alasan 1 kalimat):

- [KEPUTUSAN USER, kecenderungan] Memakai semua 5 view, bukan hanya oklusal: sesuai narasi smartphone. Syarat dari AI: metrik utama di oklusal karena positif frontal/lateral hanya 96 gambar.
- [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Pakai split per grup buatan sendiri, bukan split Benchmark: split resmi bocor.
- [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Tidak menggabung dataset lain (sejalan keputusan dataset tunggal); dataset eksternal hanya sebagai uji generalisasi, jika ada yang berlisensi jelas dan berkotak karies pada foto ponsel (belum dicari).
- [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Pilot dikecualikan; subset retractors tidak dianggap data baru (pasien sama) dan, jika dipakai, harus satu grup dengan pasangannya.

## DECISION UPDATE untuk [CLAUDE w*********30 (2026-10-31 09:45)]
Keputusan baru (+ alasan 1 kalimat):
- [KEPUTUSAN USER] Hanya memakai dataset Zenodo (Ahmed dkk., Sci Data 2025), tanpa menggabung dataset lain: menghindari masalah label, lisensi, dan provenans.
- [KEPUTUSAN USER] Kontribusi utama = preprocessing pipeline-heavy: sejalan dengan rubrik (kelengkapan pipeline dan analisis per tahap).
- [KEPUTUSAN USER] Pipeline preprocessing dibuat adaptif (tidak kaku): diinginkan user.
- [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Satu masalah utama (karies); gingivitis hanya jika dataset terverifikasi dan dievaluasi terpisah; gigi bungsu tidak layak dari foto; plak dan kalkulus feasibility rendah.
- [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Adaptif berbasis aturan di OpenCV (ukur kualitas, lalu pilih tindakan), bukan model terlatih; eksperimen empat kondisi (tanpa preprocessing, tetap, adaptif, adaptif + quality gate) dengan metrik mAP50 dan recall; degradasi buatan pada test set; VLM hanya sebagai pembanding; Streamlit/Flask, bukan Flutter.
