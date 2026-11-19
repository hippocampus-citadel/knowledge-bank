# FINAL PROJECT PCD - Sistem Skrining Awal Kesehatan Gigi Berbasis Kamera Smartphone

> LLM: baca dulu `SOP.md` dan `PREFERENCES.md`:
> - SOP: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/SOP.md?v=20261116
> - PREFERENCES: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/PREFERENCES.md?v=20261031
>
> Jika tidak bisa membuka link, minta user menempelkan isinya.

Terakhir diperbarui: 2026-11-19

## Ringkasan
- Tujuan: Mengembangkan prototipe sistem skrining awal yang menganalisis foto rongga mulut dari kamera smartphone untuk menampilkan indikasi beberapa kondisi gigi dan gusi.
- Tipe: Tugas Kuliah untuk Proyek Akhir Mata Kuliah Pemrosesan Citra Digital (PCD)
- Stack: [WAJIB] -> Python, OpenCV. [PERKIRAAN SEMENTARA]: PyTorch/Ultralytics YOLO, FastAPI, serta Flutter atau web responsif (Pilihan frontend dan deployment belum final)
- Batas Klaim: Alat ditujukan untuk skrining/edukasi awal, bukan diagnosis medis dan bukan pengganti pemeriksaan dokter gigi.

## Status saat ini
E0b (pre_identity) selesai 3 seed dengan rata-rata val mAP50 0,9141 (SD 0,0051) dan sanity check lolos, namun nilai test seed 0 dan 1 belum terverifikasi. E1 (CLAHE) pada 2 seed gagal aturan keputusan dengan penurunan val ~0,021 dan tidak bisa diselamatkan, sedangkan E2 (specular) hanya kalibrasi dengan parameter usulan lolos batas keamanan namun kode belum diverifikasi. Uji ketahanan E0b mengungkap kerapuhan pada blur dan gerak (turun >0,02 level 2), dan quality gate v1 gagal kalibrasi karena ambang persentil alami tidak konsisten. Keputusan desain: gate untuk ketajaman, robustness training terpisah, template beku untuk E1, U-Net prioritas rendah; runtime Colab hilang, CSV aman di Drive, sandbox tidak untuk training.

## Langkah berikutnya
1. Catat di DECISION.md: E1 gagal (+ angka), kalibrasi E2 dua detektor lengkap termasuk yang gagal, hasil uji ketahanan dan tingkat degradasi, aturan 0,02, E0b + CLAHE inferensi-saja gagal.
2. Putuskan arah Tahap 1 berikutnya karena CLAHE gagal dan E2 diperkirakan netral: (a) setujui atau tolak protokol gate v2; (b) analisis kesalahan per strata pada best.pt E0b (blur, kecerahan, retraktor) yang belum dikerjakan; (c) maksimal 1 sampai 2 varian preprocessing baru yang ditetapkan sebelum dijalankan (kandidat: normalisasi warna/white balance, denoise ringan), 3 seed, pembanding E0b.
3. Tanyakan ke dosen: daftar pipeline wajib atau contoh, dan tenggat final.

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
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/STATUS.md?v=20261119 | perlu detail progres |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/REQUIREMENTS.md?v=20261031 | perlu mengetahui detail spesifik ketentuan dari dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/DECISION.md?v=20261119 | akan mengusulkan perubahan arah |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/literature-review.md?v=20261031 | butuh melihat hasil literature review yang telah dikumpulkan |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/proposal_feedback.md?v=20261105 | butuh melihat hasil evaluasi proposal oleh dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/log_history?v=20261111 | perlu meninjau apa saja yang telah dilakukan di sesi sesi sebelumnya |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/jobdesc-week-1.md?v=20261107 | butuh melihat job description tim untuk weekly progress 1 |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/exp-report-1.md?v=20261109 | butuh melihat hasil eksperimen reproduksi paper rujukan dan hasil penetapan baseline ablasi yang dijelaskan secara naratif |
