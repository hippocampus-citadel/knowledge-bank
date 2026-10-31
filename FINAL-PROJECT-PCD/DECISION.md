# DECISION PROJECT

> Terakhir diperbarui: 2026-10-31

## DECISION UPDATE untuk [em***********nt (2026-10-31 15:45)]
Keputusan baru (+ alasan 1 kalimat):

- [KEPUTUSAN USER, kecenderungan] Memakai semua 5 view, bukan hanya oklusal: sesuai narasi smartphone. Syarat dari AI: metrik utama di oklusal karena positif frontal/lateral hanya 96 gambar.
- [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Pakai split per grup buatan sendiri, bukan split Benchmark: split resmi bocor.
- [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Tidak menggabung dataset lain (sejalan keputusan dataset tunggal); dataset eksternal hanya sebagai uji generalisasi, jika ada yang berlisensi jelas dan berkotak karies pada foto ponsel (belum dicari).
- [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Pilot dikecualikan; subset retractors tidak dianggap data baru (pasien sama) dan, jika dipakai, harus satu grup dengan pasangannya.

## DECISION UPDATE untuk [CLAUDE w*********30 (2026-10-31 09:45)]
Keputusan baru (+ alasan 1 kalimat):
- [KEPUTUSAN USER] Hanya memakai dataset Zenodo (Ahmed dkk., Sci Data 2025), tanpa menggabung dataset lain: menghindari masalah label, lisensi, dan provenans.
- [KEPUTUSAN USER] Kontribusi utama = preprocessing pipeline-heavy: sejalan dengan rubrik (kelengkapan pipeline dan analisis per tahap).
- [KEPUTUSAN USER] Pipeline preprocessing dibuat adaptif (tidak kaku): diinginkan user.
- [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Satu masalah utama (karies); gingivitis hanya jika dataset terverifikasi dan dievaluasi terpisah; gigi bungsu tidak layak dari foto; plak dan kalkulus feasibility rendah.
- [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Adaptif berbasis aturan di OpenCV (ukur kualitas, lalu pilih tindakan), bukan model terlatih; eksperimen empat kondisi (tanpa preprocessing, tetap, adaptif, adaptif + quality gate) dengan metrik mAP50 dan recall; degradasi buatan pada test set; VLM hanya sebagai pembanding; Streamlit/Flask, bukan Flutter.

(Daftar lengkap: DECISIONS.md)
