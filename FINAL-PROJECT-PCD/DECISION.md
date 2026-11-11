# DECISION PROJECT

> Terakhir diperbarui: 2026-11-11

## DECISION UPDATE untuk [CLAUDE em***********nt (2026-11-11 18:30)]
- Keputusan baru (+ alasan 1 kalimat):
  - Semua eksperimen berikutnya membuat salinan dari baseline_raw_REF_v1.ipynb yang dibekukan; alasan: prosedur identik antar eksperimen.
  - Kondisi ablasi mulai dari yolov8s.pt (COCO) dengan konfigurasi baseline, tanpa transfer bobot hasil baseline; alasan: menghindari konfon antara efek tahap dan epoch tambahan.
  - Uji panjang training memakai cond terpisah (baseline_raw_e164), tidak mengubah config.json baseline; alasan: mencegah menimpa hasil baseline.

## DECISION UPDATE untuk [CLAUDE w*********30 (2026-11-09 13:45)]
- Keputusan baru (+ alasan 1 kalimat):
  - [KEPUTUSAN USER] Model hasil replikasi TIDAK dikunci sebagai baseline ablasi; replikasi hanya uji kewajaran; alasan: dilatih di split bocor dan melalui resume dengan pengaturan berubah.
  - [KEPUTUSAN USER] Baseline ablasi = YOLOv8s tanpa preprocessing yang dilatih di `dataset_split_v2` dengan konfigurasi mengikuti [8] disertai deviasi; alasan: split benchmark bocor (65,6% set tersebar lintas split) sehingga selisih antar-kondisi bisa terdistorsi.
  - [KEPUTUSAN USER] `dataset_split_v2` menggantikan `dataset_split` untuk eksperimen utama; pilot dikecualikan; alasan: komposisi retractors + no_retractors seperti benchmark tanpa kebocoran antar-grup yang terdeteksi.
  - [KEPUTUSAN USER] Semua kondisi ablasi memakai 50 epoch, batch 32, imgsz 640, Adam, workers 1, bobot awal COCO; alasan: hemat GPU; user akan menguji bahwa 164 epoch dapat dipangkas.
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Dasar ablasi = kontrol internal (baseline sendiri, split dan konfigurasi identik untuk semua kondisi), bukan angka [8]; jangan klaim lebih baik dari [8]; perbandingan absolut hanya jika split, konfigurasi, dan metrik identik.
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Metrik utama single_cls pada test; test dipakai sekali per run; tidak ada penyetelan lebih banyak untuk kondisi usulan; hasil negatif dilaporkan; 3 seed dan bootstrap per grup.
    
## DECISION UPDATE untuk [USER (2026-11-07 01:55)]
- Judul resmi: Implementasi Teknik Pengolahan Citra Digital untuk Meningkatkan Deteksi Lesi Karies pada Foto Intraoral Remaja dan Dewasa Muda Berbasis Aplikasi Web

## DECISION UPDATE untuk [CLAUDE em***********nt (2026-10-31 15:45)]
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
