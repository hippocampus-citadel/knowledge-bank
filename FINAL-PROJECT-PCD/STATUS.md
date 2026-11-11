# STATUS PROJECT

> Terakhir diperbarui: 2026-11-11

**`[CLAUDE @em (2026-11-11)]`**

## Saat ini
- Sedang berjalan / terhambat:
  - Weekly Progress jatuh tempo 11 Nov 2026. Status paket B tidak diketahui.
  - Hipotesis (n=1 per kondisi, belum terbukti): folder/berkas ganda di Drive muncul saat menulis lewat jalur pintasan akun non-pemilik shared folder (seed 0 dan 2 non-pemilik: s2 sempat ~28 folder, s0 61 last.pt dan 24 best.pt; seed 1 akun pemilik bersih). Patch (copy2 tanpa mkdir/os.replace) belum terbukti: isi folder weights run e164 belum dilaporkan.
  - config.json di Drive masih ckpt_every=2, belum diedit ke 5.
        
## Langkah berikutnya
- Langkah berikutnya (urut prioritas):
  1. Bekukan paket untuk B: notebook, config.json, baseline_raw_results.csv (18 baris), catatan versi, daftar gambar yang dikecualikan otomatis.
  2. Tetapkan tertulis sebelum Tahap 1: metrik utama, kriteria "tahap berkontribusi tinggi", margin. USULAN sesi ini (belum diputuskan): metrik keputusan = val single_cls mAP50 (test hanya laporan akhir); ambang = kelipatan SD antar-seed; tambah kontrol "identity" (raw lewat jalur baca-tulis yang sama); multi-kelas deskriptif.
  3. Perbaiki jobdesc-week-1 dan dokumen lain: split v2; makna kelas D/d dan pemetaan 0/1; jumlah benchmark 6.266; catatan M/m sebagai keterbatasan; hapus entri split v1 seed 42 beserta larangannya di STATUS.md lama (sudah usang).
  4. Unduh best.pt seed 1 (50 epoch) dan e164 ke laptop, catat md5. Pastikan best.pt/last.pt seed 0 yang sah (md5 aa7628bb...) ada di folder Drive pemilik. Catat sambung lintas akun e164 di LOG.md pemilik.
  5. Uji 50 vs 164 untuk kondisi terbaik menunggu Tahap 1; bagian raw sudah ada. Pilihan lebih murah sekitar 100 epoch = usulan, belum diputuskan.
  6. SOP bagian 6: pastikan tidak ada email di notebook atau LOG.md yang masuk repo (versi lama baseline_raw_seed2.ipynb memuatnya).
  7. Opsional (usulan): satu pasang run raw vs kondisi terbaik di split benchmark paper sebagai pembanding sekunder untuk arahan dosen.

## Pertanyaan terbuka
  - Arti label M/m: tanya penulis via Zenodo atau inspeksi visual?
  - Judul resmi menyebut "lesi karies", sedangkan anotasi paper mengelilingi gigi berkaries: judul dipertahankan atau diberi catatan?
  - Pemicu folder ganda belum diketahui (hipotesis pintasan non-pemilik).
  - Apakah uji kecukupan epoch pada kondisi terbaik tetap dijalankan, dan dengan margin berapa?
  - Apakah Weekly Progress 11 Nov dan paket B sudah dikirim atau dibekukan?
    
## Riwayat 

- Selesai (sejak 2026-11-09):
  - Baseline raw, split v2, YOLOv8s, 50 epoch, Ultralytics 8.4.207, Adam, batch 32, imgsz 640, workers 1, seed 0/1/2 selesai. Test single_cls mAP50: 0,9021 | 0,9019 | 0,8978 (SD ≈ 0,0024, n=3). Test single_cls mAP50-95: 0,7208 | 0,7145 | 0,713. Val single_cls mAP50: 0,9178 | 0,9125 | 0,9081.
  - Multi-kelas tidak stabil antar-seed (mis. precision val seed 0 vs 1: 0,7818 vs 0,6557).
  - retractors < no_retractors (test single_cls mAP50) di ketiga seed, selisih ±0,02, belum ada CI: s0 0,8925 vs 0,9155 | s1 0,8916 vs 0,9125 | s2 0,889 vs 0,9105.
  - Uji 164 epoch (raw, seed 1, cond baseline_raw_e164, split v2; disambung 2x lintas 3 akun dari epoch selesai 74 dan 148; results.csv lengkap 164 baris tanpa celah). Dibanding seed 1 50 epoch: test single_cls mAP50 0,8959 (0,9019), mAP50-95 0,7136 (0,7145); val single_cls mAP50 0,9108 (0,9125); multi-kelas naik: test mAP50 0,7232 (0,6957), val 0,7073 (0,6673). Epoch terbaik 103 (val multi mAP50 0,7086), plateau sekitar epoch 100; train loss terus turun, val box loss datar (overfitting ringan, Medium). Tafsir: tidak ada bukti 164 epoch menaikkan metrik utama (1 pasangan run; margin tidak ditetapkan sebelum run, jadi deskriptif).
  - Makna kelas terverifikasi (2.245 berkas LabelMe vs YOLO, cocok 100%): kelas_0 = D (karies gigi permanen, 6228 instance), kelas_1 = d (karies gigi susu, 554). Menurut paper, kotak dibuat mengelilingi GIGI berkaries.
  - Label M (44) dan m (1) ada di JSON, tidak ada di YOLO, arti tidak didefinisikan paper. 25 gambar hanya berlabel M/m; 15 masuk v2 sebagai negatif (train 12, test 3, val 0). Dampak diperkirakan di bawah SD antar-seed (Low-Medium).
  - md5: best.pt seed 0 aa7628bbc7ecdc19f000a5ba0f18e6ac (evaluasi ulang CPU mereproduksi 0,8144/0,8468/0,9021/0,7208); best.pt seed 2 51e95495410782698253245b97cb5b1b; best.pt e164 f35c8f6b3325aa006f7b222975004f9d; yolov8s.pt (seed 1 dst) 0a1d5d0619d5a24848a267ec1e3a3118 (md5 yolov8s.pt seed 0 tidak tercatat).
  - Notebook acuan baseline_raw_REF_v1.ipynb: parameter per salinan = SEED, ACCOUNT, EXP; mencatat LOG.md dan run_meta.json; sambung checkpoint terbukti jalan.
