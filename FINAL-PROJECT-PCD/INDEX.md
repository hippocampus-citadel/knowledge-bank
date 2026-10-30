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
Saat ini masih ditahap literature review mandiri bersama tim. Judul belum diajukan, tanggal 4 November 2026 sudah harus jadi proposal yang memuat mengambil topik apa (merujuk pada REQUIREMENT.md), problem statement, latar belakang, hasil studi literatur (yang menjelaskan hubungannya apa, apa yang didapatkan dri rujukan, dan apa gapnya), proposed solution (usulan) dan dataset description (datanya dari mana). Untuk saat ini baru topik dan masalah yang baru ditemukan, literature review masih raw karena tim hanya mengumpulkan sumber tanpa mengarah ke kesimpulan gap dan metode yang ingin digunakan (detailnya lihat di literature-review.md).

(Daftar lengkap: STATUS.md)

## Langkah berikutnya
1. Lakukan literature review ulang yang mengarah ke penemuan gap dari penelitian sebelumnya
2. Berikan rekomendasi judul berdasarkan hasil literature review terarah sebelumnya

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
