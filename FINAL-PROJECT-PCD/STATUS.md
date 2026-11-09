# STATUS PROJECT

> Terakhir diperbarui: 2026-11-09

**`[CLAUDE @w30 (2026-11-09)]`**

## Saat ini
  - Replikasi parsial [8] pada split benchmark bawaan (YOLOv8s, Adam, jadwal 164 epoch, batch 64 lalu 32 setelah 2x resume di epoch 86 dan 134; imgsz 640, seed 0, bobot awal COCO, GPU T4). Hasil test, bobot best.pt: multi-kelas P 0,751 / R 0,761 / mAP50 0,771; single_cls P 0,790 / R 0,876 / mAP50 0,911. Makalah: P 0,828 / R 0,807 / mAP50 0,841 (definisi evaluasi tidak disebut). Kesimpulan: pipeline berfungsi (uji kewajaran); BUKAN klaim reproduksi berhasil. Draf laporan replikasi sudah ditulis (belum ada di repo).
  - Baseline ablasi seed 0 di `dataset_split_v2` selesai (50 epoch, batch 32, imgsz 640, Adam, workers 1). Test single_cls: P 0,814 / R 0,847 / mAP50 0,902 / mAP50-95 0,721; multi-kelas mAP50 0,708. Subset: no_retractors 0,916, retractors 0,893 (satu seed, belum bermakna). Seed 0 sempat hilang (bobot gagal tersimpan di Drive) lalu diulang; val mAP50 multi-kelas ulang 0,694 vs 0,695 sebelumnya.
- Sedang berjalan / terhambat:
  - Baseline seed 1 dan 2 di `dataset_split_v2` BELUM dijalankan. Paket baseline beku untuk Anggota B BELUM diserahkan. Tahap 1 belum dimulai.
  - Kendala utama: batas GPU Colab gratis dan pindah akun/sesi. Masalah berulang: Drive tidak ter-mount di runtime baru; folder bersama tidak terlihat tanpa pintasan di My Drive; hasil training yang ditulis langsung ke Drive hilang diam-diam; versi Ultralytics bergeser (8.4.204, 8.4.207, 8.4.208); RAM sistem jebol pada batch 64 + workers 2.
    
## Langkah berikutnya
  1. Buat `config.json` di Drive (versi Ultralytics terkunci, nama zip split, md5 `split.csv` v2, epoch, batch, imgsz, workers, optimizer). Hitung dan isi md5 split sekali, lalu jangan diubah.
  2. Setiap sesi mulai dengan Sel 0 (bootstrap): mount Drive, assert folder proyek terlihat, pasang `ultralytics==<versi config>` dan assert versinya, uji tulis Drive, ekstrak split dan assert md5, tulis `data.yaml`. Jika ada assert gagal, JANGAN lanjut.
  3. Jalankan seed 1 dan 2 dengan prosedur di bagian "Protokol sambung training". Satu seed per sesi bila kuota terbatas.
  4. Bekukan paket untuk B: notebook (Sel 0 + loop), config.json, `baseline_raw_results.csv`, catatan versi, daftar gambar yang dikecualikan otomatis.
  5. Perbaiki TEAM-ROLES.md: split = `dataset_split_v2` (bukan benchmark bawaan), lisensi dataset CC BY 4.0, jumlah gambar benchmark 6.266, makna kelas 0/1 tidak diketahui.
  6. Tetapkan tertulis metrik utama dan kriteria "tahap berkontribusi tinggi" sebelum Tahap 1.
  7. Uji kecukupan 50 epoch: raw dan satu kondisi terbaik pada 50 vs 164 epoch, 2–3 seed, margin ditetapkan di awal; periksa apakah arah efek preprocessing tetap sama.

- Protokol sambung training (WAJIB, agar tidak salah versi, konfigurasi, atau path):
  - Jalur kanonik hasil: `/content/drive/MyDrive/final_project_pcd/runs_v2/<kondisi>_s<seed>/`. Hanya SATU akun yang menjalankan training; akun lain hanya berbagi folder dan WAJIB menambah pintasan di My Drive (klik kanan folder di "Shared with me" → Organize → Add shortcut), lalu `drive.mount(..., force_remount=True)`.
  - Training ditulis ke disk lokal Colab (`/content/runs_local`), BUKAN langsung ke Drive. Setelah selesai: salin ke Drive, `os.sync()`, assert ukuran `best.pt` dan `last.pt` sama, baru tulis penanda selesai. Verifikasi juga lewat browser dan unduh `best.pt` ke laptop.
  - Gunakan `plots=False` (galat `results.csv` pada langkah plot pernah membatalkan evaluasi).
  - Resume: salin `last.pt` dari Drive ke lokal, ubah `train_args` (batch, workers, project, name, save_dir) lewat `torch.load`/`torch.save`, cek `save_dir` tercetak berawal `/content/runs_local/` (atau `/content/repro_local/`), lalu `train(resume=True)`. Callback mencadangkan `last.pt` tiap 5 epoch; best.pt TIDAK ikut dicadangkan (perbaiki: cadangkan juga).
  - Catat setiap sesi di `LOG.md`: tanggal, akun, run, md5 split, versi Ultralytics, epoch terakhir, jalur hasil.
  - Jangan menjalankan sel ad hoc di luar notebook; jangan mencampur sel reproduksi dengan notebook baseline (variabel `DATA` tertimpa).
  - Preprocessing (B) tidak boleh mengubah geometri (resize, crop, rotasi, flip) maupun nama berkas.


## Pertanyaan terbuka
 - Selisih jumlah gambar val benchmark (625 terbaca vs 627 dari analisis berkas): penyebab belum diketahui; apakah pilot ikut terbaca di reproduksi belum diperiksa.
  - Versi Ultralytics yang dipakai untuk seed 0 v2 setelah diulang belum tercatat; config akan mengunci 8.4.207, tetapi seed 0 perlu dicek apakah sama.
  - Asal best.pt replikasi tidak pasti (kurva epoch 87–134 hilang; diduga ditulis pada 29 epoch terakhir). last.pt replikasi belum dievaluasi.
  - Apakah 50 epoch cukup (mAP50 val replikasi naik 0,765 → 0,799 pada fase akhir jadwal); belum terbukti.
  - Jumlah gambar/grup test v2, tingkat pasangan retractors–no_retractors, dan jumlah positif per subset/view v2 perlu dicatat dari keluaran pembuatan split.
  - Makna kelas 0/1; konfirmasi ke dosen soal tafsir "split yang sama"; tanggal final; format weekly progress 11 November.
    
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
