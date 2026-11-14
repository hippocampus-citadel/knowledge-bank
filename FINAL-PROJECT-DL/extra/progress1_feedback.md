# Progress Update #1 Feedback

## Progress
Terdapat dua versi progress, yang komprehensif dibuat oleh aku (User) bersama chat LLM yang menangani progress minggu ini dan yang versi singkat dari versi komprehensif (semua informasi dari versi ini mengambil referensi langsung dari file komprehensif) dalam bentuk ppt dan file ini yang dikumpulkan serta dilihat oleh dosen dalam feedback minggu ini. File komprehensif bisa dilihat di progress_update_1.md, untuk yang berbentuk ppt adalah sebagai berikut:

### Slide Progress Update

**[Slide 1]**

**Rumusan Masalah**
1. Bagaimana perbandingan performa model pada 561 fitur hasil ekstraksi dengan sinyal mentah (Inertial Signals)?
2. Bagaimana performa ANN, LSTM, dan model pembanding (CNN 1D, CNN-LSTM, BiLSTM) pada klasifikasi 6 aktivitas manusia?
3. Kelas aktivitas mana yang sering tertukar, dan apa penyebabnya?

**Kontribusi Penelitian**
- Perbandingan fitur ekstraksi vs sinyal mentah dengan protokol eksperimen yang sama.
- Validation berbasis subjek untuk mencegah data leakage.
- Analisis kesalahan per kelas dan per subjek.

**[Slide 2]**

**Data dan Pembagian**

- Dataset: UCI HAR, 30 subjek, 6 aktivitas, 10.299 window.
- Dua jenis input: 561 fitur hasil ekstraksi, dan sinyal mentah 9 channel (128 timestep × 9).
- Validation diambil dari data train berdasarkan subjek (ID 1, 25, 27), tidak diacak. Alasannya, window pada dataset ini saling overlap, jadi pemisahan acak bisa membuat data yang mirip muncul di train dan validation.

	|Split|Window|Persentase|
	|-----|------|----------|
	|Train|6.220|60,4%|
	|Validation|1.132|11,0%|
	|Test|2.947|28,6%|

- Keenam kelas ada di data validation.
- Normalisasi (z-score) memakai mean dan standar deviasi dari data train saja.


**[Slide 3]**

**Model dan Pengaturan Training**

|Model|Status|
|-----|------|
|ANN (baseline)|Selesai|
|LSTM v1|Selesai|
|GRU, BiLSTM, CNN 1D, CNN-LSTM|on progress|
|ANN pada 561 fitur|on progress|

- ANN: Flatten → Dense(256) → Dropout(0,3) → Dense(128) → Dropout(0,3) → Dense(6).
- LSTM v1: LSTM(64) → Dropout(0,3) → Dense(6).
- Pengaturan sama untuk semua: Adam (lr 1e-3), batch 64, maksimal 100 epoch, early stopping (patience 10), 5 seed.

**[Slide 4]**

**Hasil Sementara**

|Model|Parameter|Accuracy|Macro-F1|
|-----|------|-----|------|
|ANN|328.838|0,9394 ± 0,0042|0,9389 ± 0,0046|
|LSTM v1|19.334|0,9661 ± 0,0132|0,9669 ± 0,0129|

- Rata-rata ± standar deviasi dari 5 seed, pada data validation.
- LSTM lebih tinggi dengan parameter jauh lebih sedikit, tetapi hasilnya lebih bervariasi antar-seed, jadi belum bisa dibilang final.
- Data test belum dipakai.

**[Slide 5]**

**Analisis Kelas yang Tertukar**

- Kesalahan yang paling sering: STANDING diprediksi SITTING, sebanyak 37 window, dan jumlahnya sama di kelima seed ANN, jadi bukan kebetulan dari inisialisasi.
- Semuanya berasal dari subjek 25 (2 dari 4 sesi berdiri).
- Pada sumbu z, rata-rata segmen yang salah ≈ 0,32, sedangkan segmen yang benar ≈ 0,05. Nilai segmen salah masuk ke rentang SITTING, jadi prediksi modelnya masuk akal secara sinyal.
- LSTM hanya memperbaiki sebagian: 17, 0, 20, 37, 37 kesalahan untuk seed 1 sampai 5.
- Penyebab fisiknya (misalnya posisi ponsel) belum bisa dipastikan dari data.

**[Slide 6]**

**Rencana**
- Menjalankan GRU, BiLSTM, CNN 1D, CNN-LSTM, dan ANN pada 561 fitur.
- Membandingkan semua model dan menganalisis kesalahan lintas model.
- Evaluasi test sekali saja, setelah konfigurasi final dipilih.

## Feedback Dosen
Dosen meminta untuk mencari paper rujukan sebagai pembanding. Dosen menyarankan untuk memakai GroupKFold. Tim mengonfirmasi ulang rencana penggunaan GroupKFold, dengan mengklarifikasi apakah benar fold yang nantinya terbentuk akan ada 7 mengingat kami sebelumnya menggunakan 3 subjek sebagai validasi untuk mengejar proposi 15% dari split train untuk dijadikan split val. Dosen memberi komentar bahwa di 3 subjek itu harus ada perwakilan/representasi dari 6 kelas aktivitas. Dosen bertanya apakah 3 subjek untuk validasi terlalu besar waktu atau beban komputasinya dan kami jawab aman aman saja mengingat Waktu training yang cepat. Salah satu anggota kami bertanya bagaimana jika validasinya 5 subjek, pada intinya dosen menjawab bahwa pengubahan proporsi split harus didasarkan pada seberapa representatif kelas aktivitas pada split validasi sebagai bahan uji sebelum testing set, mau itu mengorbankan proporsi testing maupun training. Dosen juga bertanya apakah dari 30 partisipan lengkap semua menjalankan 6 kelas aktivitas itu atau tidak, kami jawab perlu konfirmasi ulang karena saat itu belum siap jawabannya. Dosen mengingatkan untuk mencoba skenario training ANN 561 Fitur. Waktu training harus dicatat untuk setiap eksperimen untuk perbandingan efisiensi waktu, bicara soal waktu, aku bertanya kenapa setiap seed kena early stopping terus menerus dan apakah itu hal yang wajar ditambah aku sudah menggunakan patience 10 sehingga berhenti di epoch 12/13 terus setiap seed. Dosen menjawab kalua tidak pakai patience 10, maka overfittingnya akan seberapa parah? namun aku menjawab tidak tahu dan belum dicoba.
