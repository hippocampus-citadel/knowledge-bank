# FINAL PROJECT PCD - Sistem Skrining Awal Kesehatan Gigi Berbasis Kamera Smartphone

> LLM: baca dulu `SOP.md` dan `PREFERENCES.md`:
> - SOP: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/SOP.md?v=20261116
> - PREFERENCES: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/PREFERENCES.md?v=20261031
>
> Jika tidak bisa membuka link, minta user menempelkan isinya.

Terakhir diperbarui: 2026-11-16

## Ringkasan
- Tujuan: Mengembangkan prototipe sistem skrining awal yang menganalisis foto rongga mulut dari kamera smartphone untuk menampilkan indikasi beberapa kondisi gigi dan gusi.
- Tipe: Tugas Kuliah untuk Proyek Akhir Mata Kuliah Pemrosesan Citra Digital (PCD)
- Stack: [WAJIB] -> Python, OpenCV. [PERKIRAAN SEMENTARA]: PyTorch/Ultralytics YOLO, FastAPI, serta Flutter atau web responsif (Pilihan frontend dan deployment belum final)
- Batas Klaim: Alat ditujukan untuk skrining/edukasi awal, bukan diagnosis medis dan bukan pengganti pemeriksaan dokter gigi.

## Status saat ini
Sesi ini menyelesaikan smoke test dan eksperimen E0b (pre_identity) untuk seed 0 dan 1, menunjukkan selisih val mAP50 <0,002 terhadap baseline raw (jauh di bawah SD 0,0049 dan margin 0,01) sehingga sanity check lolos untuk 2 dari 3 seed. Template ref-v2 dibekukan meski ada bug baris epoch ekstra (+17 detik) dan augmentasi bawaan Ultralytics tetap aktif demi keadilan perbandingan. E0b seed 2 tertunda akibat kuota GPU akun-1, sedangkan E1–E3 belum dimulai menunggu pembersihan data seed 99, penguncian parameter specular, dan delegasi tugas tim. Keputusan fase 1 (E0b, E1 CLAHE, E2 specular kecil, E3 gabungan) dengan aturan keputusan val mAP50 sudah disepakati Wafi, namun pertanyaan terbuka soal format val/test, versi albumentations, anggaran GPU, mask gigi, dan persetujuan dosen masih terbuka.

## Langkah berikutnya
1. Pastikan baris seed 99 sudah terhapus dari kedua CSV. Kalau belum, hapus sekarang, karena ikut menggeser statistik E0b.
2. Jalankan E0b seed 2 (SEED=2, EXP={"cond":"pre_identity"}, PRE=[("identity",{})]); urutan sel: SEL 0, SEL 1, SEL 1P, sel bobot awal, SEL 2, SEL 3.
3. Hitung rata-rata dan SD E0b dari 3 seed (val single_cls mAP50). Angka ini menjadi pembanding resmi E1/E2/E3. Jangan memakai baseline raw sebagai pembanding utama.

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
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/STATUS.md?v=20261116 | perlu detail progres |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/REQUIREMENTS.md?v=20261031 | perlu mengetahui detail spesifik ketentuan dari dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/DECISION.md?v=20261116 | akan mengusulkan perubahan arah |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/literature-review.md?v=20261031 | butuh melihat hasil literature review yang telah dikumpulkan |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/proposal_feedback.md?v=20261105 | butuh melihat hasil evaluasi proposal oleh dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/log_history?v=20261111 | perlu meninjau apa saja yang telah dilakukan di sesi sesi sebelumnya |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/jobdesc-week-1.md?v=20261107 | butuh melihat job description tim untuk weekly progress 1 |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/internal_teams_files/exp-report-1.md?v=20261109 | butuh melihat hasil eksperimen reproduksi paper rujukan dan hasil penetapan baseline ablasi yang dijelaskan secara naratif |
