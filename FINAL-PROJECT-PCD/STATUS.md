# STATUS PROJECT

> Terakhir diperbarui: 2026-10-31

## `[CLAUDE w*********30 (2026-10-31 09:45)]`

**Update STATUS — 2026-10-31**
- Selesai sesi ini:
  - Membaca INDEX, SOP, PREFERENCES, dan REQUIREMENTS (STATUS dan DECISIONS tidak dibuka).
  - Literature review terarah (±25 artikel; yang dibaca abstrak dan potongan isi, bukan teks penuh; status Scopus BELUM diverifikasi, cek per ISSN). Gap mayoritas:
    (1) performa foto ponsel tertinggal (F1 ponsel 42,8–80% vs kamera profesional 68,3–95,4%, Moharrami dkk. 2024) dan recall rendah;
    (2) banyak studi memakai gigi cabut atau kamera intraoral, bukan foto pengguna awam;
    (3) uji lintas perangkat jarang (dataset Zenodo hanya satu perangkat);
    (4) preprocessing dan kualitas foto jarang menjadi variabel utama (Ding 2021 dan Park 2022 hanya sampingan);
    (5) pelaporan lemah (XAI hanya 3 dari 23 studi, aplikasi terdeploy hanya 4 studi);
    (6) uji pengguna awam terbatas (AICaries, OralCam).
  - Bukti VLM 2026: Gemini zero-shot sensitivitas tinggi tetapi presisi rendah (over-detection); YOLO lebih akurat untuk lokalisasi.
  - Penilaian feasibility terhadap rubrik dosen (tahap klasik pengolahan citra harus terlihat dan dianalisis per tahap).
- Sedang berjalan / terhambat:
  - Judul belum ada; scope masalah gigi belum final (karies pasti).
  - Terhambat informasi: akses GPU, keahlian tiga anggota, akses dokter gigi untuk validasi.
- Langkah berikutnya (urut prioritas):
  1. Konfirmasi dataset Zenodo: record yang dipakai (ada record berkas terbatas), lisensi, jumlah subset tanpa retraktor, ID pasien, definisi kelas.
  2. Susun proposal: problem statement, latar belakang, tabel literatur (template di REQUIREMENTS), proposed solution, deskripsi dataset.
  3. Rekomendasi judul berdasarkan gap di atas.
  4. Setelah proposal: baseline YOLO, lalu pipeline preprocessing.
- Keputusan baru (+ alasan 1 kalimat):
  - [KEPUTUSAN USER] Hanya memakai dataset Zenodo (Ahmed dkk., Sci Data 2025), tanpa menggabung dataset lain: menghindari masalah label, lisensi, dan provenans.
  - [KEPUTUSAN USER] Kontribusi utama = preprocessing pipeline-heavy: sejalan dengan rubrik (kelengkapan pipeline dan analisis per tahap).
  - [KEPUTUSAN USER] Pipeline preprocessing dibuat adaptif (tidak kaku): diinginkan user.
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Satu masalah utama (karies); gingivitis hanya jika dataset terverifikasi dan dievaluasi terpisah; gigi bungsu tidak layak dari foto; plak dan kalkulus feasibility rendah.
  - [REKOMENDASI AI, BELUM DIPUTUSKAN TIM] Adaptif berbasis aturan di OpenCV (ukur kualitas, lalu pilih tindakan), bukan model terlatih; eksperimen empat kondisi (tanpa preprocessing, tetap, adaptif, adaptif + quality gate) dengan metrik mAP50 dan recall; degradasi buatan pada test set; VLM hanya sebagai pembanding; Streamlit/Flask, bukan Flutter.
- Pertanyaan terbuka:
  - Target populasi (anak sekolah, dewasa, lansia)?
  - Apakah adaptif benar-benar lebih baik daripada pipeline tetap? (hipotesis, belum terbukti; hasil nol tetap sah)
  - Apakah ada studi yang memvalidasi skor OHI-S/DMF-T turunan foto? (belum dicari)

## `[USER (2026-10-31 ~07:00)]`

Saat ini masih ditahap literature review mandiri bersama tim. Judul belum diajukan, tanggal 4 November 2026 sudah harus jadi proposal yang memuat mengambil topik apa (merujuk pada REQUIREMENT.md), problem statement, latar belakang, hasil studi literatur (yang menjelaskan hubungannya apa, apa yang didapatkan dri rujukan, dan apa gapnya), proposed solution (usulan) dan dataset description (datanya dari mana). Untuk saat ini baru topik dan masalah yang baru ditemukan, literature review masih raw karena tim hanya mengumpulkan sumber tanpa mengarah ke kesimpulan gap dan metode yang ingin digunakan (detailnya lihat di literature-review.md).
