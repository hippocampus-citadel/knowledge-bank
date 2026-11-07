# Hasil Evaluasi Proposal Final Project DL oleh Dosen

> 6 November 2026

Karena proposal dibuat dalam bentuk PPT, dosen menngevaluasi isi dari slide presentasi kami. Singkatnya, project dan ide kami telah diterima oleh dosen dan siap untuk lanjut dan membuat progress report selanjutnya.

## Slide Proposal
Berikut ringkasan isi dari setiap slide PPT Proposal:

**Slide 1 - Dataset**

Dataset: Human Activity Recognition Using Smartphones (UCI HAR)

Sumber: UCI Machine Learning Repository

10.299 sampel, 561 Fitur 30 partisipan

6 kelas aktivitas: 
- Walking
- Walking Upstairs
- Walking Downstairs
- Sitting
- Standing
- Laying

Link Dataset [https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones]

**Slide 2 - Distribusi Kelas**

LAYING: 1944, STANDING: 1906, SITTING: 1777, WALKING: 1722, WALKING_UPSTAIRS: 1544, WALKING_DOWNSTAIRS: 1406

Distribusi target sangat seimbang (berkisar antara ~1.406 hingga 1.944 sampel per kelas), sehingga aman dari bias kelas mayoritas.

**Slide 3 - Redundansi Fitur**

Meskipun terdapat 561 fitur asli, analisis PCA membuktikan bahwa 65 komponen utama saja sudah mampu menjelaskan 90% variansi data. Hal ini membuktikan adanya multikolinearitas yang sangat tinggi antar-sinyal sensor.

**Slide 4 - Pembagian Data**

Menggunakan pembagian train dan test bawaan dataset (Train: 7.352 sampel | Test: 2.947 sampel). 15% data train digunakan sebagai validation (~1.103 sampel)

**Slide 5 - Metode**
- ANN (baseline)
- LSTM
- GRU

Karena dataset berbentuk time series sehingga model sequence seperti LSTM dan GRU sesuai untuk digunakan.

**Slide 6 - Evaluasi yang Direncanakan**

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## Feedback Dosen
Datasetnya UCI HAR, splitnya sudah bawaan dari dataset. UCI HAR itu bukan sequential, dia itu hasil rekayasa per windows. Di foldernya UCI HAR ada folder Inertia Signals, itu yang dipakai untuk LSTM dan bukan yang memiliki 561 fitur meskipun set yang memiliki 561 fitur itu masih bisa dimasukkan ke dalam RNN. Tidak apa apa menggunakan 561 fitur itu sebagai perbandingan, hasil dari fitur yang sudah diekstrak (561 fitur) vs yang Inertia Signals dengan LSTM. Split data validasinya coba diambil dari data train antara 10-15%, ada kesalahan angka yang dilihat oleh dosen pada Pie Diagram yang disajikan dalam proposal yang memperlihatkan split train/val/test yang di claim 70/15/15. Split HARUS berdasarkan ID orang/participant-nya untuk mencegah data leakage, misal ada 30 participants setelah dilakukan split, training ada 24 participant ambil 4-5 participant sebagai validasi. Kalau ID participants tidak ada kemungkinan akan random atau pakai cara lain sebisa mungkin tidak leakage. Modifikasi atau kebaruannya bisa memakai CNN 1D, CNN-LSTM, BiLSTM. Untuk GRU sebenarnya tidak jauh beda dengan LSTM dan biasanya hasilnya mirip mirip tapi tetap digunakan tidak masalah. Sebagai tambahan, dosen juga meminta untuk melakukan analisis sample yang kelasnya sering tertukar di semua percobaan berbagai model. Proposal juga perlu dilengkapi lagi dengan rumusan masalah dan referensi yang digunakan
