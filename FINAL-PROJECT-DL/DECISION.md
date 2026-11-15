# DECISION PROJECT

> Terakhir diperbarui: 2026-11-15

## DECISION UPDATE untuk [CLAUDE @em (2026-11-15 18:09)]
- Keputusan baru (+ alasan 1 kalimat):
  - Pembanding literatur ada 3. Anguita untuk ANN 561 fitur (head-to-head). TCN-GRU untuk model sekuens (head-to-head hanya baseline GRU; 97,25% dianggap batas atas optimistis). Xia hanya untuk rentang (split 22/8 berbeda, bukan head-to-head). Alasan: hanya sumber ini yang protokolnya jelas dan dibaca penuh.
  - MSTCN tidak dihitung terpisah dari TCN-GRU. Alasan: grup penulis dan protokolnya sama, jadi bukan konfirmasi independen.
  - Kim, Springer, Ankita, Vazan (sementara), dan Mekruksavanich dicantumkan sebagai "tidak sebanding" beserta alasan. Alasan: menunjukkan evaluasi kritis sumber.
  - Angka >97% tidak dijadikan target, dan selisih lintas paper di bawah ±1–2 poin tidak ditafsirkan. Alasan: variasi antar-split sebesar itu.
  - Konfigurasi model dipilih lewat validasi per peserta, bukan test. Alasan: paper pembanding kemungkinan memilih konfigurasi lewat test sehingga optimistis.
  - Laporkan akurasi dan macro-F1. Alasan: paper pembanding melaporkan akurasi dan F1.

## DECISION UPDATE
- Validation dipisah per peserta, bukan diacak per window, dan dikunci pada peserta [1, 25, 27] (1.132 window, 15,4% dari train resmi) untuk semua eksperimen. Alasan: window overlap 50%, sehingga pemisahan acak menimbulkan kebocoran data (arahan dosen). Perubahan ukuran atau komposisi validation hanya boleh berdasarkan keterwakilan keenam kelas, bukan proporsi angka.
- Split train/test resmi UCI dipertahankan (21 dan 9 peserta, tidak beririsan). Pembagian sebenarnya dari total 10.299 window adalah 60,4% / 11,0% / 28,6%; angka 70/15/15 di proposal tidak dipakai lagi.
- Inertial Signals (128 × 9) menjadi input utama model sekuens, sedangkan 561 fitur hasil ekstraksi menjadi pembanding (ANN pada 561 fitur). Alasan: dosen membedakan keduanya.
- Model yang direncanakan: ANN (baseline), LSTM, GRU, BiLSTM, CNN 1D, dan CNN-LSTM.
- Pengaturan training dikunci lewat `common.py` dan sama untuk semua model: Adam (lr 1e-3), batch 64, maksimal 100 epoch, early stopping patience 10 pada validation loss, 5 seed. Normalisasi z-score per channel memakai statistik train saja. Alasan: perbandingan model harus adil. Early stopping patience 10 akan diuji dampaknya atas permintaan dosen, tetapi belum diubah.
- Hasil dilaporkan sebagai rata-rata ± SD dari 5 seed, bukan seed terbaik. Selisih skor di bawah ±0,01 tidak dianggap bermakna.
- Test set tidak dipakai untuk tuning; FINAL=True dijalankan sekali per model setelah konfigurasi final dipilih. Alasan: mencegah kebocoran evaluasi.
- Jangan menyimpulkan LSTM lebih baik daripada ANN. Alasan: skor validation lebih tinggi, tetapi SD antar-seed sekitar tiga kali lebih besar dan 85% selisihnya berasal dari satu peserta.
- Error peserta 25 diperlakukan sebagai temuan diagnostik; peserta atau window tersebut tidak dibuang.
- Waktu training wajib dicatat untuk setiap eksperimen sebagai perbandingan efisiensi (permintaan dosen).
- GroupKFold disarankan dosen, tetapi jumlah fold dan ukuran validation belum diputuskan; lihat Pertanyaan terbuka di STATUS.md.
