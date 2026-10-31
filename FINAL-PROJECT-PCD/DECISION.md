# DECISION PROJECT

> Terakhir diperbarui: 2026-10-31

## DECISION UPDATE untuk [CLAUDE w*********30 (2026-10-31 09:45)]
Keputusan baru (+ alasan 1 kalimat):
[KEPUTUSAN USER] Hanya memakai dataset Zenodo (Ahmed dkk., Sci Data 2025), tanpa menggabung dataset lain: menghindari masalah label, lisensi, dan provenans.
[KEPUTUSAN USER] Kontribusi utama = preprocessing pipeline-heavy: sejalan dengan rubrik (kelengkapan pipeline dan analisis per tahap).
[KEPUTUSAN USER] Pipeline preprocessing dibuat adaptif (tidak kaku): diinginkan user.
[REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Satu masalah utama (karies); gingivitis hanya jika dataset terverifikasi dan dievaluasi terpisah; gigi bungsu tidak layak dari foto; plak dan kalkulus feasibility rendah.
[REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Adaptif berbasis aturan di OpenCV (ukur kualitas, lalu pilih tindakan), bukan model terlatih; eksperimen empat kondisi (tanpa preprocessing, tetap, adaptif, adaptif + quality gate) dengan metrik mAP50 dan recall; degradasi buatan pada test set; VLM hanya sebagai pembanding; Streamlit/Flask, bukan Flutter.

(Daftar lengkap: DECISIONS.md)
