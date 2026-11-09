# FINAL PROJECT PCD - Sistem Skrining Awal Kesehatan Gigi Berbasis Kamera Smartphone

> LLM: baca dulu `SOP.md` dan `PREFERENCES.md`:
> - SOP: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/SOP.md
> - PREFERENCES: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/PREFERENCES.md
>
> Jika tidak bisa membuka link, minta user menempelkan isinya.

Terakhir diperbarui: 2026-10-31

## Ringkasan
- Tujuan: Mengembangkan prototipe sistem skrining awal yang menganalisis foto rongga mulut dari kamera smartphone untuk menampilkan indikasi beberapa kondisi gigi dan gusi.
- Tipe: Tugas Kuliah untuk Proyek Akhir Mata Kuliah Pemrosesan Citra Digital (PCD)
- Stack: [WAJIB] -> Python, OpenCV. [PERKIRAAN SEMENTARA]: PyTorch/Ultralytics YOLO, FastAPI, serta Flutter atau web responsif (Pilihan frontend dan deployment belum final)
- Batas Klaim: Alat ditujukan untuk skrining/edukasi awal, bukan diagnosis medis dan bukan pengganti pemeriksaan dokter gigi.

## Status saat ini
Status proyek per 9 November 2026 menunjukkan bahwa replikasi parsial pada *split benchmark* bawaan telah selesai sebagai uji kewajaran (*baseline* YOLOv8s dengan mAP50 *single_cls* 0,911), sementara eksperimen ablasi dengan *split* baru (`dataset_split_v2`, *seed* 0) mencatatkan mAP50 *single_cls* 0,902. Hambatan operasional saat ini berpusat pada keterbatasan kuota GPU Colab gratis, sinkronisasi Google Drive, dan inkonsistensi versi Ultralytics, sehingga langkah prioritas berikutnya meliputi penguncian konfigurasi via `config.json`, pembakuan protokol sambung *training*, eksekusi *seed* 1 dan 2.

(Detail lengkap: STATUS.md)

## Langkah berikutnya
1. Buat `config.json` di Drive (versi Ultralytics terkunci, nama zip split, md5 `split.csv` v2, epoch, batch, imgsz, workers, optimizer). Hitung dan isi md5 split sekali, lalu jangan diubah.
2. Setiap sesi mulai dengan Sel 0 (bootstrap): mount Drive, assert folder proyek terlihat, pasang `ultralytics==<versi config>` dan assert versinya, uji tulis Drive, ekstrak split dan assert md5, tulis `data.yaml`. Jika ada assert gagal, JANGAN lanjut.
3. Jalankan seed 1 dan 2 dengan prosedur di bagian "Protokol sambung training". Satu seed per sesi bila kuota terbatas.
4. Bekukan paket untuk B: notebook (Sel 0 + loop), config.json, `baseline_raw_results.csv`, catatan versi, daftar gambar yang dikecualikan otomatis.
5. Perbaiki jobdesc-week-1.md: split = `dataset_split_v2` (bukan benchmark bawaan), lisensi dataset CC BY 4.0, jumlah gambar benchmark 6.266, makna kelas 0/1 tidak diketahui.
6. Tetapkan tertulis metrik utama dan kriteria "tahap berkontribusi tinggi" sebelum Tahap 1.
7. Uji kecukupan 50 epoch: raw dan satu kondisi terbaik pada 50 vs 164 epoch, 2–3 seed, margin ditetapkan di awal; periksa apakah arah efek preprocessing tetap sama.

## Keputusan penting (final)
- Judul resmi project ini adalah Implementasi Teknik Pengolahan Citra Digital untuk Meningkatkan Deteksi Lesi Karies pada Foto Intraoral Remaja dan Dewasa Muda Berbasis Aplikasi Web
- Tema project yang diambil adalah skrining kesehatan gigi via kamera smartphone. Alasan: Keputusan tim yang sudah final
- Sistem final akan terdiri dari layer pemrosesan citra + deteksi dan layer aplikasi web. Alasan: Ketentuan dari dosen untuk layer deteksi dibungkus aplikasi dan bukan notebook python biasa
- Preprocessing dan kualitas foto sebelum deteksi menjadi fokus kontribusi yang akan diuji. Alasan: lihat rubrik penilaian di REQUIREMENTS.md
- Model hasil replikasi TIDAK dikunci sebagai baseline ablasi; replikasi hanya uji kewajaran; alasan: dilatih di split bocor dan melalui resume dengan pengaturan berubah.
  
(Daftar lengkap: DECISIONS.md)

## Batasan / requirement khusus
- Deadline: 11 November 2026 untuk Weekly Progress (BUKAN DEADLINE FINAL)
- Aturan dosen: lihat REQUIREMENTS.md
- Hal yang tidak boleh diubah: Tema Skrining Gigi via Kamera Smartphone 

## Konteks tambahan (baca HANYA jika kondisinya terpenuhi)
| File | Baca jika... |
|---|---|
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/STATUS.md | perlu detail progres |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/REQUIREMENTS.md | perlu mengetahui detail spesifik ketentuan dari dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/DECISION.md | akan mengusulkan perubahan arah |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/literature-review.md | butuh melihat hasil literature review yang telah dikumpulkan |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/proposal_feedback.md | butuh melihat hasil evaluasi proposal oleh dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/log_history | perlu meninjau apa saja yang telah dilakukan di sesi sesi sebelumnya |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/jobdesc-week-1.md | butuh melihat job description tim untuk weekly progress 1 |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/exp-report-1.md | butuh melihat hasil eksperimen reproduksi paper rujukan dan hasil penetapan baseline ablasi yang dijelaskan secara naratif |
