# FINAL PROJECT PCD - Sistem Skrining Awal Kesehatan Gigi Berbasis Kamera Smartphone

> LLM: baca dulu `SOP.md` dan `PREFERENCES.md`:
> - SOP: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/SOP.md
> - PREFERENCES: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/PREFERENCES.md
>
> Jika tidak bisa membuka link, minta user menempelkan isinya.

Terakhir diperbarui: 2026-11-11

## Ringkasan
- Tujuan: Mengembangkan prototipe sistem skrining awal yang menganalisis foto rongga mulut dari kamera smartphone untuk menampilkan indikasi beberapa kondisi gigi dan gusi.
- Tipe: Tugas Kuliah untuk Proyek Akhir Mata Kuliah Pemrosesan Citra Digital (PCD)
- Stack: [WAJIB] -> Python, OpenCV. [PERKIRAAN SEMENTARA]: PyTorch/Ultralytics YOLO, FastAPI, serta Flutter atau web responsif (Pilihan frontend dan deployment belum final)
- Batas Klaim: Alat ditujukan untuk skrining/edukasi awal, bukan diagnosis medis dan bukan pengganti pemeriksaan dokter gigi.

## Status saat ini
Status proyek per 11 November 2026 melaporkan bahwa baseline raw (YOLOv8s, split v2) untuk seed 0, 1, dan 2 telah rampung dengan stabil (test single_cls mAP50 di kisaran 0,8978–0,9021; SD ≈ 0,0024), uji 164 epoch menunjukkan overfitting ringan tanpa kenaikan metrik signifikan, dan makna kelas YOLO 0/1 berhasil diverifikasi 100% sebagai karies gigi permanen (D) dan gigi susu (d) berdasarkan perbandingan berkas LabelMe. Hambatan operasional meliputi kendala Weekly Progress yang jatuh tempo, inkonsistensi folder di Google Drive akibat akun non-pemilik, serta paket Anggota B yang belum dibekukan, sehingga langkah prioritas berikutnya mencakup pembekuan paket Anggota B, penetapan metrik keputusan dan margin secara tertulis, pembersihan data sensitif, serta pengunduhan bobot best.pt ke laptop.

(Detail lengkap: STATUS.md)

## Langkah berikutnya
  1. Bekukan paket untuk B: notebook, config.json, baseline_raw_results.csv (18 baris), catatan versi, daftar gambar yang dikecualikan otomatis.
  2. Tetapkan tertulis sebelum Tahap 1: metrik utama, kriteria "tahap berkontribusi tinggi", margin. USULAN sesi ini (belum diputuskan): metrik keputusan = val single_cls mAP50 (test hanya laporan akhir); ambang = kelipatan SD antar-seed; tambah kontrol "identity" (raw lewat jalur baca-tulis yang sama); multi-kelas deskriptif.
  3. Perbaiki jobdesc-week-1 dan dokumen lain: split v2; makna kelas D/d dan pemetaan 0/1; jumlah benchmark 6.266; catatan M/m sebagai keterbatasan; hapus entri split v1 seed 42 beserta larangannya di STATUS.md lama (sudah usang).
  4. Unduh best.pt seed 1 (50 epoch) dan e164 ke laptop, catat md5. Pastikan best.pt/last.pt seed 0 yang sah (md5 aa7628bb...) ada di folder Drive pemilik. Catat sambung lintas akun e164 di LOG.md pemilik.
  5. Uji 50 vs 164 untuk kondisi terbaik menunggu Tahap 1; bagian raw sudah ada. Pilihan lebih murah sekitar 100 epoch = usulan, belum diputuskan.
  6. SOP bagian 6: pastikan tidak ada email di notebook atau LOG.md yang masuk repo (versi lama baseline_raw_seed2.ipynb memuatnya).
  7. Opsional (usulan): satu pasang run raw vs kondisi terbaik di split benchmark paper sebagai pembanding sekunder untuk arahan dosen.

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
