# STATUS PROJECT

> Terakhir diperbarui: 2026-11-15

**`[CLAUDE @em (2026-11-15)]`**

## Saat ini
- Sedang berjalan / terhambat:
  - Belum ada eksperimen baru (GroupKFold, ANN 561 fitur, GRU, dst.).
  - INDEX.md masih usang: status, langkah berikutnya, tanggal "2026-14-7" tidak valid, DECISIONS.md vs DECISION.md.
  - Tabel literatur belum ditulis.
  - Belum diperiksa: kode Vazan; paper asli Mutegeki & Han (92%, hanya abstrak).

## Langkah berikutnya
- Langkah berikutnya (urut prioritas):
  1. Tulis tabel literatur (kolom: split, input, konfigurasi dipilih dengan apa, metrik, status) dan lengkapi proposal (rumusan masalah + referensi).
  2. Perbaiki INDEX.md.
  3. Seragamkan lokasi dataset v2, lalu jalankan EDA v2.
  4. Putuskan skema GroupKFold (jumlah fold, keterwakilan kelas) dan verifikasi bahwa 30 peserta melakukan 6 aktivitas.
  5. Jalankan ANN 561 fitur (bandingkan Anguita) dan GRU (bandingkan baseline GRU 96,40). Lanjut ke model lain dan catat waktu training.
  6. Uji dampak early stopping patience 10.
  7. FINAL=True sekali per model; bandingkan ke literatur hanya pada test resmi.

## Pertanyaan terbuka
- Pertanyaan terbuka:
  - Jumlah fold GroupKFold dan ukuran validation (7 fold = 21 ÷ 3 baru hitungan, perlu konfirmasi).
  - Apakah dosen menerima 3 pembanding dan label "tidak sebanding"?
  - DOI nomor 4 user (`cicn67655…`) belum ditemukan; file yang diunggah adalah paper ICSESS.
  - Vazan: apakah LDA di-fit hanya pada train, dan apakah ModelCheckpoint dipantau pada test? (perlu cek kode GitHub-nya)
  - Mutegeki & Han: protokol asli belum dibaca.

## Riwayat 
- Selesai sesi ini:
  - STATUS.md dan DECISION.md lama ternyata berisi proyek BirdSet, bukan HAR. Draf pengganti sudah disusun di chat.
  - Riset pembanding literatur. Dibaca penuh:
    - Anguita 2013: 96%, SVM + 561 fitur, test resmi 2.947.
    - TCN-GRU (PLoS ONE 2024): 97,25%, baseline GRU 96,40%, test resmi 21/9, sinyal mentah.
    - MSTCN (F1000 2022): 97,42%, grup penulis sama dengan TCN-GRU.
    - Xia (IEEE Access 2020): akurasi 95,80%, F1 95,78%, split per peserta 22/8.
    - MDPI 2026: ≈95%, 30× split per peserta, 561 fitur.
  - Dinilai tidak sebanding:
    - Kim et al.: SMOTE dijalankan sebelum split acak.
    - Springer IJCIS 2026: confusion matrix berjumlah 736, sedangkan test resmi 2.947.
    - Ankita 2021: diagonal confusion matrix 2.708/2.947 ≈ 91,9%, bukan 97,89%.
    - Vazan (preprint): dicurigai bocor, kode belum diperiksa.
    - Mekruksavanich ICSESS: memakai MotionSense.

- Selesai sesi ini (periode 7–12 November 2026):
  - Validation dipisah per peserta [1, 25, 27]: 1.132 window (15,4% dari 7.352 window train resmi). Train menjadi 6.220 window (18 peserta); test resmi 2.947 window (9 peserta). Pembagian dari total 10.299 window adalah 60,4% / 11,0% / 28,6%, bukan 70/15/15 seperti di diagram proposal (koreksi dari dosen).
  - Inertial Signals dimuat sebagai tensor (N, 128, 9), tanpa NaN, dinormalisasi z-score per channel dengan statistik train saja, dan disimpan dalam satu file .npz yang sama untuk semua eksperimen.
  - ANN baseline (5 seed): akurasi 0,9394 ± 0,0042, macro-F1 0,9389 ± 0,0046. Kesalahan terbesar STANDING→SITTING sebanyak 37 window di semua seed, seluruhnya dari peserta 25 (dua dari empat rangkaian window berdiri; z total_acc rata-rata ≈ 0,32 pada yang salah, ≈ 0,05 pada yang benar).
  - LSTM v1 (5 seed): akurasi 0,9661 ± 0,0132, macro-F1 0,9669 ± 0,0129. Sekitar 85% selisih jumlah error terhadap ANN berasal dari perbaikan error peserta 25, tetapi hasilnya tidak konsisten antar-seed.
  - Feedback dosen: cari paper rujukan; gunakan GroupKFold; tiga peserta validasi harus mewakili keenam kelas; ubah proporsi split hanya berdasarkan keterwakilan kelas; coba skenario ANN 561 fitur; catat waktu training tiap eksperimen; uji dampak early stopping patience 10 terhadap overfitting.
  - Risiko metodologis tercatat: validation hanya tiga peserta (peserta 25 menyumbang sekitar 3 poin akurasi); lima seed hanya mengukur variasi inisialisasi, bukan pemilihan peserta validation; selisih skor di bawah ±0,01 tidak dianggap bermakna.
