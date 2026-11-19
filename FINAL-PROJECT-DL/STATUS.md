# STATUS PROJECT

> Terakhir diperbarui: 2026-11-19

**`[CLAUDE @em (2026-11-19)]`**

## Saat ini
- Sedang berjalan / terhambat:
  - Tidak ada run yang berjalan.
  - Protokol evaluasi test (FINAL) belum didefinisikan: latih ulang di 21 peserta atau pakai model fold. Menunggu keputusan.
  - Normalisasi masih dari 18 peserta train lama, jadi statistik validation fold ikut terhitung (kebocoran kecil, besarnya belum diukur). Ditulis sebagai keterbatasan untuk sementara. Normalisasi per fold lewat mu/sd NPZ belum diverifikasi (bentuk array dan rumus pembalikan).
  - Diagnostik peserta 14/16/25 untuk ANN 561 fitur belum dijalankan.
  - INDEX.md masih usang. EDA v2 menunggu skema fold terkunci. Tabel literatur dan proposal (rumusan masalah + referensi) belum ditulis. Verifikasi kode Vazan dan paper Mutegeki & Han masih tertunda.
  - Anggota tim lain harus memakai common.py 2.0 dan template baru. Template lama (assert "1.1") tidak boleh dipakai bersama common 2.0.

## Langkah berikutnya
- Langkah berikutnya (urut prioritas):
  1. Jalankan GRU pada sinyal (CV), dengan NAME pola <model>_<input>_cv_v<N>.
  2. Jalankan diagnostik peserta 14, 16, 25 pada ANN 561 fitur (apakah SITTING<->STANDING di peserta 16 membaik dan WALKING->UPSTAIRS di peserta 14 tetap).
  3. Ulang LSTM v1 di CV (hasil lama [1,25,27] tidak sebanding), lalu BiLSTM, CNN 1D, CNN-LSTM, dan LSTM v2.
  4. Bandingkan model berpasangan per fold (selisih per fold dan jumlah fold yang dimenangkan). Selisih di bawah sekitar 0,01 tidak dianggap bermakna. Lalu analisis kelas yang tertukar lintas model, sesuai permintaan dosen.
  5. Uji dampak early stopping tanpa patience 10 (permintaan dosen). Kurva loss per fold sudah tersimpan di history JSON. Fold 2 mencapai val loss terbaik di epoch 1 pada smoke test, tetapi best_ep bervariasi 1 sampai 34.
  6. Tulis tabel literatur (kolom: split, input, konfigurasi dipilih dengan apa, metrik, status) dan lengkapi proposal. Hasil CV tidak boleh dibandingkan langsung dengan angka literatur karena protokolnya berbeda.
  7. Putuskan protokol FINAL (tanyakan dosen), implementasikan di common v2.x, lalu perbaiki INDEX.md dan jalankan EDA v2.

## Pertanyaan terbuka
- Pertanyaan terbuka:
  - FINAL: latih ulang di 21 peserta atau pakai model fold? Perlu ditanyakan ke dosen.
  - Perlu normalisasi per fold (v2.1) atau cukup ditulis sebagai keterbatasan?
  - Mengapa fitur 561 lebih stabil antar peserta (dugaan: ringkasan postur dari fitur ekstraksi)? Belum diuji, Low confidence.
  - Tanggal Weekly Progress Report berikutnya dan deadline final belum diketahui.
  - Ketidakkonsistenan dokumen: INDEX.md menyebut DECISIONS.md padahal file bernama DECISION.md, tanggal "2026-14-7" di STATUS.md tidak valid, SOP menyebut PREFERENCES.md di folder _global padahal tautan INDEX menunjuk ke root.

## Riwayat 
- Selesai sesi ini:
  - Membaca extra/ (proposal_feedback, progress1_feedback, progress_update_1). Dosen meminta GroupKFold, keterwakilan 6 kelas di validation, ANN 561 fitur, pencatatan waktu training, dan uji early stopping tanpa patience 10.
  - Verifikasi data mentah UCI HAR (hasil dari kode yang dijalankan user): semua 30 peserta punya 6 kelas (minimum 36 window per peserta-kelas). Train 7.352 window / 21 peserta, test 2.947 / 9 peserta, tidak ada irisan. NPZ v2 konsisten dengan data mentah (crosstab peserta x kelas sama, peserta fold = peserta train+val NPZ, test NPZ = test resmi). X di NPZ sudah z-score per channel. NPZ menyimpan mu, sd, fmu, fsd.
  - folds.json dibuat dari data mentah: GroupKFold(7) di 21 peserta train. Fold 0 [15,22,25], 1 [3,8,21], 2 [14,26,29], 3 [1,6,30], 4 [7,19,28], 5 [5,16,27], 6 [11,17,23]. Ukuran validation per fold 1058/1030/1059/1055/1050/1044/1056 (total 7.352). Test tidak disentuh.
  - StratifiedGroupKFold (1 seed) dicoba: tidak lebih seimbang dari GroupKFold, jadi tidak dipakai.
  - common.py v2.0 dibuat dan lolos smoke test: 7 fold x seed, output ke results_cv/, menyimpan n_val, parameter only_folds, resume otomatis, final=True sengaja diblokir (NotImplementedError). Template v2: usulan 5 perubahan (EXPECTED_COMMON="2.0", FOLDS_PATH masuk adaptor path, cek integritas diganti loop fold, rujukan D diganti D0, hapus FINAL dan perbarui teks markdown). Status penerapan ke template tim tidak dikonfirmasi.
  - ANN sinyal (128x9), CV 7 fold x 5 seed: acc 0,9188 ± 0,0562, macro-F1 0,9206 ± 0,0531 (SD antar fold). 328.838 parameter, 671 detik total. Akurasi per fold: 0,9331 / 0,9676 / 0,8678 / 0,9689 / 0,9204 / 0,8190 / 0,9549.
  - ANN 561 fitur, arsitektur sama, CV 7 fold x 5 seed: acc 0,9333 ± 0,0388, macro-F1 0,9339 ± 0,0374. 480 detik total (kecepatan Colab bervariasi, jangan dilaporkan sebagai efisiensi tanpa catatan). Parameter 177.542 (hitungan manual, belum dikonfirmasi dari summary()). Akurasi per fold: 0,9457 / 0,9608 / 0,8795 / 0,9591 / 0,8968 / 0,9075 / 0,9837.
  - Selisih fitur - sinyal per fold: +0,013 / -0,007 / +0,012 / -0,010 / -0,024 / +0,089 / +0,029. Seluruh kenaikan rata-rata berasal dari fold 5. Tanpa fold 5 selisihnya sekitar +0,002. Kesimpulan: tidak bisa dibedakan dari nol di 7 fold. Yang jelas: SD antar fold turun (0,056 menjadi 0,039) dan fold terendah naik (0,819 menjadi 0,880).
  - Diagnostik ANN sinyal: SD antar seed di dalam fold hanya 0,003 sampai 0,018, jadi variasi berasal dari peserta, bukan seed. Peserta 16 (akurasi 0,631): SITTING dan STANDING hampir tidak terpisah. Peserta 14 (0,652): WALKING hampir seluruhnya diprediksi UPSTAIRS. Peserta 25: 0,863. Secara keseluruhan SITTING<->STANDING menyumbang sekitar 63% kesalahan (hampir simetris), kelompok jalan sekitar 30%, LAYING hampir sempurna. Penyebab fisik belum bisa dipastikan dari data.

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
