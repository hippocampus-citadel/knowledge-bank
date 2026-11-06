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
Update status per 7 November 2026, ide dan judul proyek sudah diterima oleh dosen sehingga project secara resmi sudah bisa dimulai (feedback dari dosen bisa dilihat di `proposal_feedback.md`). Judul resmi project ini adalah **Implementasi Teknik Pengolahan Citra Digital untuk Meningkatkan Deteksi Lesi Karies pada Foto Intraoral Remaja dan Dewasa Muda Berbasis Aplikasi Web**. Saat ini, user harus membuat planning weekly progress dan deadline yang harus disetor hingga deadline final serta task assignment untuk masing masing anggota

(Detail lengkap: STATUS.md)

## Langkah berikutnya
### Dari User
1. Membuat task assignment dan penentuan weekly progressnya
### Dari Sesi AI Sebelumnya
1. Konfirmasi makna kelas 0/1 dari teks penuh makalah (Nature/PMC dibuka manual; akses otomatis diblokir) atau penulis. Sementara pakai evaluasi satu kelas (`single_cls`) sebagai metrik utama.
2. Cek visual beberapa dari 23 kotak bermasalah.
3. Setelah proposal: kurva belajar (25/50/100% data latih), baseline YOLO di `dataset_split`, lalu pipeline preprocessing. Karena daya uji rendah (±383 grup latih, 83 grup uji), pertimbangkan 5-fold per grup + bootstrap per grup + beberapa seed.
     
## Keputusan penting (final)
- Judul resmi project ini adalah Implementasi Teknik Pengolahan Citra Digital untuk Meningkatkan Deteksi Lesi Karies pada Foto Intraoral Remaja dan Dewasa Muda Berbasis Aplikasi Web
- Tema project yang diambil adalah skrining kesehatan gigi via kamera smartphone. Alasan: Keputusan tim yang sudah final
- Sistem final akan terdiri dari layer pemrosesan citra + deteksi dan layer aplikasi web. Alasan: Ketentuan dari dosen untuk layer deteksi dibungkus aplikasi dan bukan notebook python biasa
- Preprocessing dan kualitas foto sebelum deteksi menjadi fokus kontribusi yang akan diuji. Alasan: lihat rubrik penilaian di REQUIREMENTS.md

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
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/DECISIONS.md | akan mengusulkan perubahan arah |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/intenal_teams_files/literature-review.md | butuh melihat hasil literature review yang telah dikumpulkan |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/proposal_feedback.md | butuh melihat hasil evaluasi proposal oleh dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/log_history.md | perlu meninjau apa saja yang telah dilakukan di sesi sesi sebelumnya |
