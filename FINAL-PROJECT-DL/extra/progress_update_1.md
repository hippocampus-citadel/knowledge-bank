# **LAPORAN PROGRESS PROYEK AKHIR DEEP LEARNING Klasifikasi Aktivitas Manusia Menggunakan Data Sensor Smartphone** 

**Dataset:** UCI Human Activity Recognition Using Smartphones (UCI HAR) **Periode progress:** 7–12 November 2026 

**Status terakhir:** eksperimen ANN baseline dan LSTM v1 pada Inertial Signals 

**Catatan:** versi revisi dari laporan 12 November 2026. Istilah teknis dijelaskan singkat di Lampiran C. 

## **1. Ringkasan** 

Proyek sudah masuk tahap eksperimen model. Data validation sekarang dipisah berdasarkan peserta (participant), bukan diacak per window, sesuai arahan dosen supaya tidak terjadi kebocoran data (data leakage). Peserta 1, 25, dan 27 dipakai sebagai validation set: 1.132 window, atau 15,4% dari 7.352 window train resmi. 

ANN dipakai sebagai baseline pada 9 channel Inertial Signals (128 langkah waktu × 9 channel). Rata-rata dari 5 seed, ANN mendapat akurasi validation 0,9394 ± 0,0042 dan macro-F1 0,9389 ± 0,0046. LSTM v1 (64 unit) mendapat akurasi 0,9661 ± 0,0132 dan macro-F1 0,9669 ± 0,0129. Skor rata-rata LSTM lebih tinggi, tetapi hasilnya jauh lebih berubah-ubah antar seed. Karena itu belum bisa disimpulkan bahwa LSTM lebih baik. Perlu eksperimen lanjutan dan evaluasi pada test set. 

## **2. Temuan Utama** 

- **Data siap dipakai.** Inertial Signals disusun menjadi tensor (N, 128, 9), diperiksa, dinormalisasi per channel memakai statistik train saja, lalu disimpan dalam satu file .npz yang sama untuk semua eksperimen. 

- **Validation dipisah per peserta.** Peserta validation: [1, 25, 27]. Jumlahnya 1.132 dari 7.352 window (15,4%). Angka ini dekat dengan target 15% di proposal dan sedikit di atas rentang kasar 10–15% dari dosen. 

- **Tidak ada kebocoran antara train dan test.** Pada split resmi UCI, train berisi 21 peserta dan test 9 peserta, tidak ada yang sama. Validation diambil hanya dari train, jadi test tidak tersentuh selama tuning. 

- **ANN baseline berhasil dijalankan.** Arsitektur: Flatten (128×9) → Dense(256) → Dropout(0,3) → Dense(128) → Dropout(0,3) → Dense(6). Total 328.838 parameter. 

- **Kesalahan terbesar ANN: STANDING dikira SITTING.** Jumlahnya tepat 37 window di kelima seed. Angka yang sama persis berulang menunjukkan ini bukan kebetulan dari inisialisasi acak. 

- **Semua 37 window itu berasal dari peserta 25** , dari dua rangkaian window berdiri yang berurutan (kemungkinan dua sesi rekaman). Rata-rata sumbu z pada window yang salah sekitar 0,32, sedangkan pada window yang benar sekitar 0,05. Karena window saling overlap 50%, 37 window ini setara sekitar 19 window yang benar-benar independen. 

- **LSTM v1 lebih tinggi, tetapi belum stabil.** Sekitar 85% dari selisih jumlah error antara ANN dan LSTM berasal dari perbaikan error peserta 25. 

- **LSTM tidak konsisten pada kasus sulit yang sama.** STANDING→SITTING pada peserta 25 berjumlah 17, 0, 20, 37, 37 untuk seed 1–5. Seed 2 memperbaiki semuanya, seed 4 dan 5 sama sekali tidak. 

- **Test set belum dipakai** untuk memilih model. Semua eksperimen masih memakai FINAL=False. 

Halaman 1 

## **3. Status Pekerjaan** 

|**Komponen**|**Status**|**Hasil / keputusan**|**Catatan**|
|---|---|---|---|
|Dataset UCI HAR|Selesai|Train 7.352, test 2.947|Split resmi dipertahankan|
|Muat Inertial Signals|Selesai|(N, 128, 9), 9 channel|Percepatan tubuh, giroskop,<br>percepatan total|
|Pemeriksaan kualitas<br>data|Selesai|Tidak ada NaN; bentuk data<br>konsisten|Train 21 peserta, test 9 peserta|
|Split validation|Selesai|Peserta [1, 25, 27]; 1.132 window<br>(15,4%)|Dikunci untuk semua<br>eksperimen|
|Normalisasi|Selesai|Z-score per channel dari train saja|Mencegah kebocoran statistik|
|Dataset v2|Selesai|X, y, g (ID peserta), idx, plus sinyal<br>dan 561 fitur|Sudah dipakai di semua hasil;<br>tinggal menyamakan lokasi file<br>untuk tim|
|EDA v2|Perlu<br>dijalankan<br>ulang|EDA lama memakai split 4 peserta|Jalankan dengan dataset v2|
|ANN baseline|Selesai|5 seed; akurasi 0,9394 ± 0,0042;<br>F1 0,9389 ± 0,0046|Hanya validation|
|Analisis error ANN|Selesai (awal)|37 STANDING→SITTING, semua<br>di peserta 25|Sudah dianalisis per rangkaian<br>window|
|LSTM v1|Selesai (awal)|5 seed; akurasi 0,9661 ± 0,0132;<br>F1 0,9669 ± 0,0129|Belum final|
|LSTM v2 dan model lain|Belum|Belum dijalankan|Target berikutnya|
|Perbandingan 561 fitur|Belum|Belum dibandingkan|Dikerjakan setelah model sinyal<br>selesai|
|Evaluasi test final|Belum|FINAL=False|Menunggu konfigurasi dipilih|
|Rumusan masalah dan<br>referensi proposal|Belum|Diminta dosen|Perlu dilengkapi|



## **4. Perubahan dari Proposal** 

Dosen meminta validation dipisah berdasarkan peserta untuk mencegah kebocoran data, dengan ukuran sekitar 10–15% dari train. Implementasi akhir memakai peserta [1, 25, 27], yaitu 1.132 window atau 15,4% dari 7.352 window train. Peserta dipilih berdasarkan jumlah window per peserta dan sebaran kelas. 

### **Koreksi pembagian data** 

Dosen menemukan bahwa angka 70/15/15 pada diagram proposal tidak sesuai. Pembagian yang sebenarnya, dihitung dari total 10.299 window, adalah sebagai berikut. 

|**Bagian**|**Jumlah window**|**Persen dari total**|**Peserta**|
|---|---|---|---|
|Train|6.220|60,4%|18|
|Validation|1.132|11,0%|3 (1, 25, 27)|
|Test|2.947|28,6%|9|
|Total|10.299|100%|30|



Halaman 2 

Train dan test mengikuti split resmi UCI (berdasarkan peserta), sehingga proporsinya memang bukan 70/15/15. Validation adalah 15,4% dari train resmi (7.352), bukan 15% dari total. 

### **Input dan daftar model** 

Dosen membedakan 561 fitur hasil ekstraksi dari Inertial Signals. Inertial Signals dipakai sebagai input utama model sekuens. Sedangkan 561 fitur direncanakan sebagai pembanding. Daftar model yang direncanakan: ANN baseline, LSTM, GRU, CNN 1D, CNN-LSTM, dan BiLSTM. Sampai saat ini baru ANN dan LSTM v1 yang sudah punya hasil. 

Dosen juga meminta proposal dilengkapi dengan rumusan masalah dan referensi. Bagian ini belum dikerjakan. 

## **5. Alur Data yang Digunakan** 

- Mengunduh dan mengekstrak dataset UCI HAR. 

- Memuat 9 channel Inertial Signals: body_acc x/y/z, body_gyro x/y/z, total_acc x/y/z. 

- Menyusun tiap window menjadi tensor (128 langkah waktu, 9 channel). 

- Memeriksa bentuk data, jumlah NaN, ID peserta, dan pemisahan resmi train/test. 

- Mengambil peserta [1, 25, 27] dari train sebagai validation. 

- Menyimpan ID peserta (g) agar hasil bisa dievaluasi per peserta. 

- Menghitung rata-rata dan standar deviasi hanya dari train, lalu menormalisasi train, validation, dan test dengan angka itu. 

- Menyimpan semuanya dalam satu file terstruktur supaya semua eksperimen memakai split yang identik. 

Catatan: dataset UCI HAR sudah diproses oleh pembuatnya. Karena itu tahap ini lebih tepat disebut pemeriksaan dan standardisasi, bukan pembersihan data. Tidak ada outlier yang dibuang dan tidak ada label yang dikoreksi. 

## **6. EDA dan Temuan Data** 

Pada versi awal, train berjumlah 7.352 window dan test 2.947 window, tanpa NaN, dengan sebaran kelas yang relatif seimbang. Setelah validation menjadi tiga peserta, validation berjumlah 1.132 window dan keenam kelas tetap ada. 

Tabel di bawah membandingkan sebaran kelas train dan validation yang baru (dihitung dari jumlah window per kelas). 

|**Kelas**|**Train (6.220)**|**Validation (1.132)**|**Selisih (poin %)**|
|---|---|---|---|
|WALKING|16,1%|20,0%|+3,9|
|UPSTAIRS|14,5%|14,9%|+0,4|
|DOWNSTAIRS|13,4%|13,3%|−0,1|
|SITTING|17,7%|16,1%|−1,7|
|STANDING|18,8%|18,3%|−0,5|
|LAYING|19,5%|17,4%|−2,1|



EDA lama memakai empat peserta untuk validation, jadi ringkasan angkanya tidak boleh dipakai di laporan final. EDA v2 perlu dijalankan dengan dataset v2. Kesimpulan kualitatif tetap berlaku: skala antar-channel berbeda, dan total_acc masih mengandung komponen gravitasi. 

Halaman 3 

## **7. Eksperimen ANN Baseline** 

ANN dipakai sebagai baseline yang tidak memperhatikan urutan waktu. Input (128, 9) diratakan menjadi 1.152 angka, sehingga struktur waktunya hilang. Arsitektur: Flatten → Dense(256, ReLU) → Dropout(0,3) → Dense(128, ReLU) → Dropout(0,3) → Dense(6, Softmax), total 328.838 parameter. 

|**Metrik**|**Rata-rata ± SD (5 seed)**|**Arti**|
|---|---|---|
|Akurasi|0,9394 ± 0,0042|Variasi antar seed kecil|
|Precision macro|0,9438 ± 0,0046|Sedikit di atas akurasi|
|Recall macro|0,9406 ± 0,0048|Sejalan dengan akurasi|
|F1 macro|0,9389 ± 0,0046|Angka utama untuk pembanding|



Kesalahan terpenting adalah STANDING→SITTING sebanyak 37 window di semua seed. Karena jumlahnya persis sama, kesalahan ini dianggap sistematis, bukan noise dari inisialisasi. 

## **8. Analisis Error pada Peserta 25** 

Ada 74 window STANDING milik peserta 25. Berdasarkan putusnya overlap antar-window, window itu terbagi menjadi empat rangkaian berurutan dengan panjang 20, 17, 18, dan 19 window. Dua rangkaian pertama (37 window) selalu salah pada ANN. Dua rangkaian terakhir (37 window) selalu benar. 

|**Kelompok**|**Jumlah window**|**Rata-rata z (total_acc)**|**Hasil ANN**|
|---|---|---|---|
|Rangkaian 1–2|37|≈ 0,32|Dikira SITTING (semua<br>seed)|
|Rangkaian 3–4|37|≈ 0,05|Dikenali sebagai<br>STANDING|



Nilai z window yang salah (0,32) lebih tinggi dari hampir semua window STANDING di train (di atas persentil 95, yaitu 0,14), tetapi masih ada di dalam rentang nilai SITTING di train. Jadi kesalahan ANN masuk akal dari sisi sinyal. Penyebab fisiknya, misalnya posisi ponsel bergeser, belum bisa dipastikan dari data yang ada. 

**Dua catatan.** Pertama, karena window overlap 50%, 37 window ini setara sekitar 19 window independen. Bukti sebenarnya adalah dua rangkaian berdiri yang sulit, bukan 37 contoh terpisah. Kedua, istilah "sesi" berasal dari putusnya overlap antar-window, bukan dari catatan waktu rekaman. Urutan window dianggap mengikuti waktu rekaman; hal ini didukung 70 dari 73 pasangan window berurutan yang memang saling overlap. 

## **9. Eksperimen LSTM v1** 

Arsitektur: Input → LSTM(64) → Dropout(0,3) → Dense(6, Softmax). Pengaturan latihan dikunci lewat common.py: Adam, learning rate 1e-3, batch 64, maksimal 100 epoch, early stopping (sabar 10 epoch) pada validation loss, dan lima seed. 

|**Metrik**|**Rata-rata ± SD (5 seed)**|**Catatan**|
|---|---|---|
|Akurasi|0,9661 ± 0,0132|Lebih tinggi dari ANN, tetapi SD sekitar tiga kali lebih<br>besar|
|Precision macro|0,9702 ± 0,0109|Belum jadi dasar memilih model|
|Recall macro|0,9671 ± 0,0131|Variasi antar seed cukup besar|
|F1 macro|0,9669 ± 0,0129|Belum final; perlu konfigurasi dan model lain|



Halaman 4 

Jumlah window STANDING yang salah menjadi SITTING pada peserta 25, per rangkaian window dan per seed: 

|**Seed**|**Rangk. 1 (20)**|**Rangk. 2 (17)**|**Rangk. 3 (18)**|**Rangk. 4 (19)**|**Total**|
|---|---|---|---|---|---|
|1|0|17|0|0|17|
|2|0|0|0|0|0|
|3|3|17|0|0|20|
|4|20|17|0|0|37|
|5|20|17|0|0|37|



LSTM bisa memperbaiki rangkaian sulit itu pada sebagian seed, tetapi tidak konsisten. Hasilnya hampir "semua atau tidak sama sekali" per rangkaian. Rangkaian 3 dan 4 tidak pernah salah. Rangkaian 2 salah di empat dari lima seed. Rangkaian 1 salah penuh di seed 4 dan 5, salah sebagian di seed 3, dan benar di seed 1 dan 2. 

## **10. Perbandingan Sementara ANN vs LSTM** 

|**Aspek**|**ANN**|**LSTM v1**|**Kesimpulan sementara**|
|---|---|---|---|
|Akurasi|0,9394 ± 0,0042|0,9661 ± 0,0132|LSTM lebih tinggi di<br>validation|
|Macro-F1|0,9389 ± 0,0046|0,9669 ± 0,0129|LSTM lebih tinggi, tapi<br>kurang stabil|
|Parameter|328.838|≈ 19.334|LSTM jauh lebih kecil|
|Rata-rata window salah (dari 1.132)|68,6|38,4|Selisih sekitar 30 window|
|Di peserta 25|60,4|34,8|Sekitar 85% dari selisih|
|Di peserta 1 dan 27|8,2|3,6|Selisih kecil|
|STANDING→SITTING di peserta 25|37 di tiap seed|17 / 0 / 20 / 37 / 37|LSTM memperbaiki<br>sebagian seed|
|Status|Baseline|Eksperimen awal|Belum ada model final|



Kesimpulan yang aman saat ini bukan "LSTM pasti lebih baik dari ANN". Yang bisa dikatakan: pada split peserta yang sama, LSTM v1 punya skor validation rata-rata lebih tinggi dan bisa memperbaiki kesalahan STANDING→SITTING pada peserta 25 di sebagian seed. Namun variasi antar seed LSTM lebih besar, sehingga konfigurasinya belum bisa difinalkan. 

## **11. Hal yang Belum Selesai** 

- Menjalankan EDA v2 dan memakai angkanya sebagai dasar laporan final. 

- Mencoba LSTM v2 (misalnya 128 unit) dengan pengaturan latihan yang sama. 

- Menjalankan GRU, CNN 1D, CNN-LSTM, dan BiLSTM sesuai ruang lingkup proyek dan saran dosen. 

- Membandingkan 561 fitur dengan Inertial Signals. 

- Menyusun analisis sampel dan kelas yang sering tertukar di semua model. 

- Menetapkan konfigurasi final tiap model sebelum FINAL=True. 

Halaman 5 

- Menjalankan evaluasi test resmi hanya setelah konfigurasi final dipilih. 

- Melengkapi proposal dengan rumusan masalah dan referensi. 

- Menyusun tabel perbandingan akhir dan pembahasan keterbatasan. 

## **12. Risiko dan Catatan Metodologis** 

- Validation hanya terdiri dari tiga peserta, sehingga skornya sangat dipengaruhi karakter orang tertentu. Peserta 25 saja menyumbang sekitar 3 poin akurasi (37 dari 1.132 window). 

- Lima seed hanya mengukur variasi inisialisasi model, bukan ketidakpastian akibat pemilihan peserta validation. 

- Sebaran kelas validation sedikit berbeda dari train (WALKING +3,9 poin, LAYING −2,1, SITTING −1,7). 

- Window saling overlap 50%, jadi jumlah sampel efektif lebih sedikit dari jumlah window. Split per peserta harus dipertahankan. 

- Selisih skor di bawah sekitar 0,01 antar model atau konfigurasi jangan dianggap bermakna. 

- Test set berisi peserta yang berbeda dan tidak boleh dipakai untuk tuning. FINAL=True dijalankan sekali per model. 

- Perbandingan model harus memakai split, preprocessing, optimizer, batch size, early stopping, dan seed yang sama. 

- Jangan memilih seed terbaik sebagai hasil utama. Pakai rata-rata ± standar deviasi. 

- Error peserta 25 adalah temuan diagnostik, bukan alasan untuk membuang peserta atau window tersebut. 

## **13. Rencana Kerja Berikutnya** 

|**Tahap**|**Pekerjaan**|**Tujuan**|
|---|---|---|
|1|Samakan lokasi file dataset v2|Pastikan har_clean_v2.npz, meta, g, dan idx ada di path yang sama<br>dan bisa dimuat common.py oleh semua anggota tim.|
|2|Jalankan EDA v2|Pakai split [1, 25, 27]; simpan tabel sebaran kelas dan statistik<br>channel final.|
|3|LSTM v2|Uji konfigurasi kedua dengan pengaturan latihan yang tidak diubah.|
|4|Model sekuens lain|GRU, CNN 1D, CNN-LSTM, BiLSTM.|
|5|Analisis error lintas model|Pakai prediksi per window dan ID peserta untuk menemukan kelas<br>atau sampel yang konsisten salah.|
|6|Perbandingan 561 fitur|Dijalankan setelah model sinyal stabil, sebagai pembanding.|
|7|Lengkapi proposal|Tambahkan rumusan masalah dan referensi sesuai feedback dosen.|
|8|Test final|Pilih konfigurasi final dulu, lalu jalankan FINAL=True secara terkontrol.|



## **14. Kesimpulan Progress** 

Per 12 November 2026, proyek punya dasar eksperimen yang jauh lebih terkontrol dibanding saat proposal: input Inertial Signals sudah distandardisasi, validation sudah dipisah per peserta, alur eksperimen sudah dikunci, dan ANN baseline serta LSTM v1 sudah diuji dengan lima seed. Temuan yang paling bernilai bukan hanya skor model, tetapi pola error yang bisa ditelusuri sampai ke peserta dan rangkaian window tertentu. 

Halaman 6 

Langkah berikutnya sebaiknya fokus pada konsistensi eksperimen, bukan mengejar skor validation tertinggi. LSTM v1 layak dilanjutkan karena rata-ratanya lebih tinggi, tetapi variasinya perlu dipahami lewat konfigurasi lain dan model pembanding. Test set belum boleh dipakai untuk memilih model sampai eksperimen selesai. 

## **Lampiran A – Angka Kunci** 

|**Item**|**Nilai**|
|---|---|
|Train resmi|7.352 window / 21 peserta|
|Test resmi|2.947 window / 9 peserta|
|Validation|1.132 window / peserta [1, 25, 27] / 15,4% dari train|
|Train setelah validation dipisah|6.220 window / 18 peserta|
|Pembagian dari total 10.299 window|Train 60,4% · Validation 11,0% · Test 28,6%|
|Input|128 langkah waktu × 9 channel Inertial Signals|
|Parameter ANN|328.838|
|Akurasi ANN|0,9394 ± 0,0042|
|Macro-F1 ANN|0,9389 ± 0,0046|
|Akurasi LSTM v1|0,9661 ± 0,0132|
|Macro-F1 LSTM v1|0,9669 ± 0,0129|
|ANN: STANDING→SITTING di peserta 25|37 di setiap seed|
|LSTM v1: STANDING→SITTING di peserta 25|17, 0, 20, 37, 37 untuk seed 1–5|



## **Lampiran B – Sumber Progress** 

Laporan ini disusun dari catatan kerja proyek yang diekspor pada 12 November 2026: keputusan preprocessing, feedback dosen, hasil EDA, konfigurasi common.py, hasil ANN 5 seed, analisis error peserta 25, dan hasil LSTM v1 yang tercatat sampai 22:23 WIB. 

Halaman 7 

## **Lampiran C – Istilah Singkat** 

|**Istilah**|**Arti**|
|---|---|
|Window|Potongan sinyal sensor sepanjang 128 langkah (sekitar 2,56 detik) yang menjadi<br>satu sampel data.|
|Peserta (participant)|Orang yang direkam. ID-nya tercatat di data, sehingga data bisa dipisah per orang.|
|Validation set|Data untuk memantau dan memilih model selama latihan.|
|Test set|Data untuk penilaian akhir. Tidak dipakai untuk memilih model.|
|Data leakage|Informasi dari data evaluasi ikut masuk ke latihan, sehingga skor tampak lebih<br>bagus dari kenyataan.|
|Seed|Angka awal pengacak. Lima seed berarti model dilatih lima kali dengan inisialisasi<br>berbeda.|
|± (SD)|Standar deviasi antar seed; makin besar berarti hasil antar seed makin berbeda.|
|Early stopping|Latihan dihentikan kalau validation loss tidak membaik selama 10 epoch.|
|Macro-F1|Rata-rata skor F1 semua kelas, dengan bobot sama untuk tiap kelas.|
|STANDING→SITTING|Window berdiri yang diprediksi model sebagai duduk.|
|total_acc (sumbu z)|Percepatan total dari sensor, termasuk gravitasi. Dipakai untuk membedakan postur<br>seperti duduk dan berdiri.|



Halaman 8 

