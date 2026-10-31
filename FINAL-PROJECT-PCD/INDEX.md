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
Status proyek per 31 Oktober 2026 menunjukkan bahwa tim telah merampungkan *literature review* terarah dan menetapkan fokus pada deteksi karies gigi menggunakan dataset tunggal Zenodo dengan kontribusi utama berupa *pipeline* preprocessing adaptif berbasis aturan dengan beberapa function OpenCV (tanpa menggabung dataset lain). Hambatan saat ini meliputi ketiadaan judul definitif, keterbatasan informasi akses GPU, dan keahlian tim, dengan langkah selanjutnya yang memprioritaskan konfirmasi detail dataset Zenodo, penyusunan proposal, serta perumusan rekomendasi judul.

(Detail lengkap: STATUS.md)

## Langkah berikutnya
1. Konfirmasi dataset Zenodo: record yang dipakai (ada record berkas terbatas), lisensi, jumlah subset tanpa retraktor, ID pasien, definisi kelas.
2. Susun proposal: problem statement, latar belakang, proposed solution, deskripsi dataset.
3. Rekomendasi judul berdasarkan gap yang ditemukan di sesi sebelumnya (Detail lihat STATUS.md)
4. Setelah proposal: baseline YOLO, lalu pipeline preprocessing.
     
## Keputusan penting (final)
- Tema project yang diambil adalah skrining kesehatan gigi via kamera smartphone. Alasan: Keputusan tim yang sudah final
- Sistem final akan terdiri dari layer pemrosesan citra + deteksi dan layer aplikasi web. Alasan: Ketentuan dari dosen untuk layer deteksi dibungkus aplikasi dan bukan notebook python biasa
- Preprocessing dan kualitas foto sebelum deteksi menjadi fokus kontribusi yang akan diuji. Alasan: lihat rubrik penilaian di REQUIREMENTS.md

(Daftar lengkap: DECISIONS.md)

## Batasan / requirement khusus
- Deadline: 4 November 2026 untuk Proposal Sementara (BUKAN DEADLINE FINAL)
- Aturan dosen: lihat REQUIREMENTS.md
- Hal yang tidak boleh diubah: Tema Skrining Gigi via Kamera Smartphone (Boleh diubah jika judul ditolak dosen setelah 4 November 2026)

## Konteks tambahan (baca HANYA jika kondisinya terpenuhi)
| File | Baca jika... |
|---|---|
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/STATUS.md | perlu detail progres |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/REQUIREMENTS.md | perlu mengetahui detail spesifik ketentuan dari dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/DECISIONS.md | akan mengusulkan perubahan arah |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/intenal_teams_files/literature-review.md | butuh melihat hasil literature review yang telah dikumpulkan |
