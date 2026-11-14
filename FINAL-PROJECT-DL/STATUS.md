# STATUS PROJECT

> Terakhir diperbarui: 2026-11-14

**`[CLAUDE @em (2026-11-14)]`**

## Saat ini
- Proyek berada di tahap eksperimen model. Weekly Progress Report #1 (periode 7–12 November 2026) sudah dikumpulkan dan dibahas dengan dosen. Baru ANN baseline dan LSTM v1 yang punya hasil, hanya pada validation. Test set belum dipakai (FINAL=False).
- Hasil sementara (rata-rata ± SD, 5 seed, validation): ANN akurasi 0,9394 ± 0,0042 dan macro-F1 0,9389 ± 0,0046 (328.838 parameter); LSTM v1 akurasi 0,9661 ± 0,0132 dan macro-F1 0,9669 ± 0,0129 (±19.334 parameter). LSTM belum bisa disimpulkan lebih baik karena SD antar-seed sekitar tiga kali lebih besar.
- Kesalahan dominan: STANDING→SITTING pada peserta 25 (37 window di setiap seed ANN; LSTM 17, 0, 20, 37, 37). Karena window overlap 50%, jumlah ini setara ±19 window independen. Penyebab fisiknya belum bisa dipastikan dari data.
- Belum dijalankan: GRU, BiLSTM, CNN 1D, CNN-LSTM, LSTM v2, ANN pada 561 fitur, dan EDA v2. Rumusan masalah dan referensi proposal (diminta dosen) belum dilengkapi.
- Dataset v2 (`har_clean_v2.npz`, meta, g, idx) sudah dipakai di semua hasil, tetapi lokasi filenya belum diseragamkan agar bisa dimuat `common.py` oleh semua anggota tim.
- Catatan teknis: pengaturan training dikunci lewat `common.py` (Adam lr 1e-3, batch 64, maksimal 100 epoch, early stopping patience 10 pada validation loss, 5 seed). Semua seed berhenti di epoch 12–13.

## Langkah berikutnya
1. Cari paper rujukan sebagai pembanding, lalu lengkapi proposal dengan rumusan masalah dan referensi (permintaan dosen).
2. Seragamkan lokasi dataset v2 untuk seluruh anggota tim.
3. Jalankan EDA v2 dengan split validation peserta [1, 25, 27]; EDA lama (4 peserta) tidak boleh dipakai di laporan final.
4. Putuskan skema validasi dengan GroupKFold (jumlah fold dan ukuran validation), dengan syarat keenam kelas terwakili di setiap fold validasi.
5. Konfirmasi apakah ke-30 peserta menjalankan keenam aktivitas.
6. Jalankan ANN pada 561 fitur, lalu GRU, BiLSTM, CNN 1D, dan CNN-LSTM; catat waktu training untuk setiap eksperimen.
7. Uji dampak tanpa early stopping patience 10 terhadap overfitting.
8. Jalankan LSTM v2 (mis. 128 unit) dengan pengaturan training yang sama.
9. Analisis error lintas model memakai prediksi per window dan ID peserta.
10. Pilih konfigurasi final tiap model, lalu jalankan FINAL=True sekali per model.

## Pertanyaan terbuka
- Berapa fold GroupKFold yang dipakai? Tim sempat bertanya apakah hasilnya 7 fold (21 peserta train resmi ÷ 3 peserta per fold; hitungan ini perlu dikonfirmasi). Dosen menyatakan perubahan proporsi split (mis. validation 5 peserta) harus berdasarkan keterwakilan kelas, bukan proporsi angka.
- Apakah ke-30 peserta lengkap melakukan keenam aktivitas? Perlu diverifikasi dari data.
- Mengapa semua seed berhenti di epoch 12–13, dan seberapa parah overfitting tanpa patience 10? Belum dicoba.
- Apa penyebab fisik error STANDING→SITTING pada peserta 25 (mis. posisi ponsel)?
- Apakah variasi antar-seed LSTM mengecil pada konfigurasi lain (LSTM v2) atau model pembanding?
- Paper rujukan apa yang relevan? Perlu dicari dan diverifikasi, jangan dikarang.

## Riwayat 
- Selesai sesi ini (periode 7–12 November 2026):
  - Validation dipisah per peserta [1, 25, 27]: 1.132 window (15,4% dari 7.352 window train resmi). Train menjadi 6.220 window (18 peserta); test resmi 2.947 window (9 peserta). Pembagian dari total 10.299 window adalah 60,4% / 11,0% / 28,6%, bukan 70/15/15 seperti di diagram proposal (koreksi dari dosen).
  - Inertial Signals dimuat sebagai tensor (N, 128, 9), tanpa NaN, dinormalisasi z-score per channel dengan statistik train saja, dan disimpan dalam satu file .npz yang sama untuk semua eksperimen.
  - ANN baseline (5 seed): akurasi 0,9394 ± 0,0042, macro-F1 0,9389 ± 0,0046. Kesalahan terbesar STANDING→SITTING sebanyak 37 window di semua seed, seluruhnya dari peserta 25 (dua dari empat rangkaian window berdiri; z total_acc rata-rata ≈ 0,32 pada yang salah, ≈ 0,05 pada yang benar).
  - LSTM v1 (5 seed): akurasi 0,9661 ± 0,0132, macro-F1 0,9669 ± 0,0129. Sekitar 85% selisih jumlah error terhadap ANN berasal dari perbaikan error peserta 25, tetapi hasilnya tidak konsisten antar-seed.
  - Feedback dosen: cari paper rujukan; gunakan GroupKFold; tiga peserta validasi harus mewakili keenam kelas; ubah proporsi split hanya berdasarkan keterwakilan kelas; coba skenario ANN 561 fitur; catat waktu training tiap eksperimen; uji dampak early stopping patience 10 terhadap overfitting.
  - Risiko metodologis tercatat: validation hanya tiga peserta (peserta 25 menyumbang sekitar 3 poin akurasi); lima seed hanya mengukur variasi inisialisasi, bukan pemilihan peserta validation; selisih skor di bawah ±0,01 tidak dianggap bermakna.
