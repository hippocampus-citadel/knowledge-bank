# FINAL PROJECT PCD - Sistem Skrining Awal Kesehatan Gigi Berbasis Kamera Smartphone

> LLM: baca dulu `SOP.md` dan `PREFERENCES.md`:
> - SOP: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/SOP.md?v=20261114
> - PREFERENCES: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/PREFERENCES.md?v=20261031
>
> Jika tidak bisa membuka link, minta user menempelkan isinya.

Terakhir diperbarui: 2026-11-15

## Ringkasan
- Tujuan: Mengembangkan prototipe sistem skrining awal yang menganalisis foto rongga mulut dari kamera smartphone untuk menampilkan indikasi beberapa kondisi gigi dan gusi.
- Tipe: Tugas Kuliah untuk Proyek Akhir Mata Kuliah Pemrosesan Citra Digital (PCD)
- Stack: [WAJIB] -> Python, OpenCV. [PERKIRAAN SEMENTARA]: PyTorch/Ultralytics YOLO, FastAPI, serta Flutter atau web responsif (Pilihan frontend dan deployment belum final)
- Batas Klaim: Alat ditujukan untuk skrining/edukasi awal, bukan diagnosis medis dan bukan pengganti pemeriksaan dokter gigi.

## Status saat ini
Proyek telah menyelesaikan penulisan laporan eksperimen lanjutan dan PPT serta klarifikasi tiga split data, di mana `dataset_split_v2` ditetapkan untuk baseline dan ablasi. Template `preprocessing_REF_v2.ipynb` dengan kontrak SEL 1P dan pencatatan waktu per epoch telah dibuat dan diuji lokal, namun belum diverifikasi di Colab termasuk struktur zip dan format gambar. Analisis awal daftar preprocessing Anggota B mengidentifikasi kategori kecocokan, risiko inpainting specular, serta kebutuhan keputusan mengenai resize, augmentasi, dan ROI sebelum Tahap 1. Langkah prioritas saat ini meliputi *critical review* metode B, pengujian segera ref-v2 di Colab, penetapan metrik keputusan tertulis, serta pembersihan folder ganda dan pencatatan `run_meta.json` di Drive.

## Langkah berikutnya
1. Wafi menyetujui atau mengubah usulan di bawah.
2. Uji asap ref-v2 di Colab: PRE=[("identity",{})], cond pre_identity, epochs 2, seed 99; hapus baris seed 99 dari CSV.
3. Tetapkan TERTULIS sebelum Tahap 1: metrik, margin, aturan keputusan, parameter dikunci.

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
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/STATUS.md?v=20261115 | perlu detail progres |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/REQUIREMENTS.md?v=20261031 | perlu mengetahui detail spesifik ketentuan dari dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/DECISION.md?v=20261115 | akan mengusulkan perubahan arah |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/literature-review.md?v=20261031 | butuh melihat hasil literature review yang telah dikumpulkan |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/proposal_feedback.md?v=20261105 | butuh melihat hasil evaluasi proposal oleh dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/log_history?v=20261111 | perlu meninjau apa saja yang telah dilakukan di sesi sesi sebelumnya |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/jobdesc-week-1.md?v=20261107 | butuh melihat job description tim untuk weekly progress 1 |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/exp-report-1.md?v=20261109 | butuh melihat hasil eksperimen reproduksi paper rujukan dan hasil penetapan baseline ablasi yang dijelaskan secara naratif |
