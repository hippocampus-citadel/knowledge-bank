# Hasil Evaluasi Proposal Final Project PCD oleh Dosen

> 5 November 2026

Karena proposal dibuat dalam bentuk PPT, dosen menngevaluasi isi dari slide presentasi kami. Singkatnya, project dan ide kami telah diterima oleh dosen dan siap untuk lanjut dan membuat progress report selanjutnya.

Salah satu isi slide yang paling disorot adalah pada bagian Kontribusi Utama berikut:
```
- Pipeline preprocessing adaptif berbasis aturan (OpenCV) dan quality gate
- Studi ablation per tahap dengan degradasi terkontrol pada dataset [8]
- Prototipe aplikasi web skrining awal, bukan diagnosis medis
```

Poin yang paling disorot adalah poin kedua yang dinilai bertentangan dengan rancangan ablasi yang kami buat berikut:

1. Original Raw Photo (tanpa preprocessing)
2. Per Tahap Preprocessing (Beberapa tahap preprocessing diuji performanya secara terpisah untuk melihat kontribusi dari setiap tahap)
3. Kombinasi (Menggabungkan semua tahap preprocessing)

Karena isi pada poin kedua tersebut, kami dinilai perlu melakukan studi ablasi terhadap rujukan 8 (Ahmed SMF, Ghori MH, Khalid A, Nooruddin A, Adnan N, Lal A, Umer F. Annotated intraoral image dataset for dental caries detection. Sci Data. 2025;12(1):1297. doi:10.1038/s41597-025-05647-9) sehingga kami perlu menggunakan split train/val/test yang sama (Sudah tersedia, cek review dataset di STATUS.md) lalu poin ablasinya dilakukan dengan preprocessing yang berbeda atau pemilihan model yang berbeda barulah kami boleh menerapkan rancangan ablasi yang kami buat. Rujukan pada poin 2 itu sendiri sebenarnya ditujukan untuk menunjuk referensi artikel ilmiah dari dataset yang kami gunakan ke rujukan 8 tersebut. Padahal kami sendiri tidak bermaksud untuk mengikuti metode yang digunakan pada artikel tersebut.
