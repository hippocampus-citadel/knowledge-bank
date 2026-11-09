**LAPORAN EKSPERIMEN**  
**Replikasi Parsial Makalah Rujukan dan Penetapan Baseline Ablasi pada Dataset Citra Intraoral untuk Deteksi Karies**

1. **Latar Belakang dan Tujuan**

Penelitian ini menguji pengaruh teknik pengolahan citra digital terhadap deteksi karies pada foto intraoral. Dataset yang dipakai adalah dataset anotasi citra intraoral karya Ahmed dkk. (Scientific Data, 2025), yang menjadi rujukan utama kami. Sebelum merancang ablasi preprocessing, kami melakukan replikasi pelatihan pada dataset dan split benchmark yang dirilis penulis. Replikasi ini bertujuan sebagai uji kewajaran (sanity check), untuk memastikan pipeline pelatihan dan evaluasi kami berjalan benar, dan angka yang dilaporkan penulis berada pada kisaran yang masuk akal. Replikasi tidak dimaksudkan membuktikan atau menyangkal klaim penulis, dan tidak dipakai sebagai baseline ablasi. 

2. **Temuan Analisis Eksploratif terhadap Benchmark**

Sebelum pelatihan, kami menganalisis isi dari dua versi dataset yang disediakan peneliti yakni dataset raw dan benchmark. Temuan yang relevan adalah sebagai berikut. 

Benchmark berisi 6.266 gambar (5.011 latih, 627 validasi, 628 uji), berbeda dari 6.313 gambar yang dilaporkan makalah. Nama berkas memuat nomor set yang berurutan, kode retraktor, dan timestamp pengambilan gambar. Foto dengan dan tanpa retraktor dari satu sesi umumnya berpasangan dengan selisih waktu sekitar sembilan menit, sehingga diduga satu pasien menghasilkan satu set pada tiap subset, dengan perkiraan sekitar 560 pasien. Identitas pasien resmi tidak tersedia, sehingga ini inferensi kami.

Temuan terpenting pada split benchmark, 65,6 persen set foto (736 dari 1.122) memiliki gambar yang tersebar di lebih dari satu split, dan 88,3 persen pasangan retraktor dan tanpa retraktor terpisah antar split. Ini menunjukkan split dilakukan secara acak per gambar, sehingga foto dari sesi yang sama muncul di data latih dan data uji (kebocoran data). Besarnya dampak terhadap metrik belum terukur, tetapi arahnya hampir pasti menaikkan skor.

Temuan lain: makna label kelas 0 dan 1 tidak terdokumentasi di paket data dengan kelas 1 sekitar sembilan persen dari total anotasi bounding box, anotasi berupa kotak pembatas di sekitar gigi berkaries, bukan kontur lesi. Sekitar 90 persen gambar positif berasal dari view oklusal dan sebagian kotak berada di luar batas gambar atau berukuran nol (23 kotak pada subset tanpa retraktor, seluruhnya view frontal atau lateral). Dugaan kami penyebabnya orientasi EXIF yang bermasalah, tetapi belum dibuktikan.

3. **Replikasi pada Split Benchmark**

Konfigurasi mengikuti Tabel 1 makalah: YOLOv8s, optimizer Adam, 164 epoch, batch 64\. Parameter yang tidak disebut makalah kami isi dengan nilai bawaan atau asumsi seperti ukuran gambar 640, seed 0, bobot awal COCO, dan seluruh hyperparameter serta augmentasi bawaan Ultralytics. Pelatihan berjalan di GPU Tesla T4 (makalah memakai RTX 4090).

Karena batas pemakaian GPU dan memori sistem, pelatihan terhenti dua kali dan dilanjutkan dari checkpoint, yaitu setelah epoch 86 dan epoch 134\. Pada kelanjutan, batch diturunkan menjadi 32 dan jumlah worker menjadi satu. Versi Ultralytics berubah selama proses (8.4.204, 8.4.207, 8.4.208). Kurva latih epoch 87 sampai 134 hilang karena catatan hasil tidak tersinkron dengan benar; bobot dan evaluasi tidak terpengaruh. Pada split validasi, Ultralytics membaca 625 gambar, berbeda dari 627 pada analisis berkas; selisih ini belum kami jelaskan.

Hasil akhir pada data uji dengan bobot terbaik (dipilih berdasarkan validasi): 

* Untuk penilaian multi-kelas: presisi 0,751, recall 0,761, mAP50 0,771, dan mAP50-95 0,614.   
* Untuk penilaian satu kelas (semua kelas digabung): presisi 0,790, recall 0,876, mAP50 0,911, dan mAP50-95 0,722.   
* Pada validasi, mAP50 multi-kelas 0,799 dan satu kelas 0,921. 

Makalah melaporkan presisi 0,828, recall 0,807, dan mAP50 0,841, tanpa menyebut definisi penilaian maupun split yang dipakai. Pada kelas minoritas (kelas 1, hanya 36 instance di validasi), mAP50 hanya 0,679 dibanding 0,918 pada kelas 0, sehingga rata-rata multi-kelas tertarik turun. Pada epoch 86, mAP50 uji adalah 0,741 (multi-kelas) dan 0,895 (satu kelas), sehingga fase akhir jadwal menambah sekitar 0,03 hingga 0,02 mAP50.

4. **Interpretasi Hasil Replikasi**

Hasilnya lebih rendah dari makalah pada penilaian multi-kelas dan lebih tinggi pada penilaian satu kelas. Karena definisi penilaian makalah tidak diketahui, split yang dipakai mengalami data leakage, hanya satu seed yang dijalankan, dan GPU, batch, serta versi pustaka berbeda, kami tidak menyatakan replikasi berhasil maupun gagal. Kesimpulan yang kami pegang lebih sempit: pipeline berfungsi, model belajar, dan angkanya berada pada kisaran yang sama dengan makalah. Konfigurasi penulis layak dijadikan acuan dasar, tetapi angka mereka tidak kami pakai sebagai target atau dasar klaim perbandingan. Kami juga menyatakan bahwa asal bobot terbaik tidak sepenuhnya pasti karena kurva epoch 87 sampai 134 hilang, namun melihat angka validasinya yang melampaui rekor sebelumnya menunjukkan bobot itu ditulis pada fase akhir pelatihan.

5. **Alasan Membuat Split Baru**

Ablasi menuntut bahwa selisih antar kondisi mencerminkan efek preprocessing, bukan artefak evaluasi. Dengan split yang bocor, model dapat menghafal ciri sesi atau pasien yang sama antara data latih dan data uji, sehingga skor menggembung dan efek preprocessing yang kecil dapat tertutup atau terdistorsi. Karena itu kami tidak memakai split benchmark yang digunakan oleh peneliti (Ahmed, dkk.) untuk eksperimen utama, dan menyajikan hal ini sebagai keterbatasan benchmark, bukan sebagai penilaian atas makalah.

Kami membuat split baru, dataset\_split\_v2, dengan komposisi yang meniru benchmark, yaitu foto dengan dan tanpa retractor. Gambar pilot dikecualikan karena penamaannya berbeda sehingga tidak dapat dikelompokkan. Pembagian dilakukan per grup, bukan per gambar. Satu grup mencakup set foto yang berurutan dengan selisih waktu hingga 30 menit (dugaan foto ulang) serta pasangan set retraktor dan tanpa retraktor dengan selisih waktu hingga 60 menit. Pembagian distratifikasi menurut ada tidaknya positif pada view oklusal, positif pada view lain, dan status berpasangan, dengan proporsi 70, 15, dan 15 persen serta seed 42\. Pemeriksaan otomatis memastikan tiap grup berada di tepat satu split. Karena tidak ada identitas pasien resmi, kebocoran diminimalkan tetapi tidak dapat dijamin nol. Pada pelatihan, Ultralytics mengecualikan otomatis 14 gambar latih dan 2 gambar validasi karena koordinat label di luar batas; kami tidak memperbaiki label tersebut sehingga perlakuan sama pada semua kondisi.

6. **Baseline Ablasi dan Hasil Awal**

Baseline ablasi adalah model tanpa preprocessing (kondisi raw) yang dilatih pada dataset\_split\_v2, dengan konfigurasi mengikuti acuan penulis disertai deviasi yang dicatat: 50 epoch, batch 32, ukuran gambar 640, optimizer Adam, satu worker, bobot awal COCO, Ultralytics 8.4.207. Seluruh kondisi ablasi akan memakai konfigurasi dan split yang identik, sehingga satu satunya variabel yang berubah adalah preprocessing. Dasar ablasi kami adalah kontrol internal ini, bukan angka penulis sehingga perbandingan dengan angka absolut makalah tidak dilakukan.

Hasil seed 0 pada data uji, penilaian satu kelas: presisi 0,814, recall 0,847, mAP50 0,902, mAP50-95 0,721. Penilaian multi-kelas: mAP50 0,708. Pada subset, mAP50 tanpa retraktor 0,916 dan dengan retraktor 0,893, namun selisih ini belum bermakna dengan satu seed. Run seed 0 sempat hilang akibat kegagalan penyimpanan dan diulang; mAP50 validasi multi-kelas ulang (0,694) hampir sama dengan run pertama (0,695), yang mendukung stabilitas konfigurasi (satu pasang angka saja). Seed 1 dan 2 serta interval kepercayaan bootstrap per grup masih akan dijalankan.

7. **Justifikasi Deviasi dan Batas Perbandingan**

Pengurangan menjadi 50 epoch dipilih karena anggaran GPU. Satu run 164 epoch memerlukan sekitar 4,5 jam, sedangkan ablasi memerlukan banyak kondisi dikali beberapa seed. Pada saat replikasi paper (Ahmed, dkk.), mAP50 validasi naik dari 0,765 ke 0,799 pada fase akhir jadwal, sehingga kami tidak mengasumsikan 50 epoch sudah jenuh. Jadwal learning rate Ultralytics diskalakan terhadap jumlah epoch, tetapi kecukupan 50 epoch harus ditunjukkan dengan raw dan satu kondisi terbaik akan dilatih pada 50 dan 164 epoch dalam beberapa seed, dengan margin yang ditetapkan sebelumnya, lalu dilihat apakah peringkat dan arah efek preprocessing tetap sama. Kami hanya akan menyatakan tidak terdeteksi perbedaan bermakna, bukan kesetaraan.

Aturan perbandingan yang kami pegang: semua kondisi berbagi split, konfigurasi, dan metrik; metrik utama (satu kelas pada data uji) dan kriteria kontribusi ditetapkan sebelum eksperimen; data uji dipakai sekali per run; tidak ada penyetelan yang lebih banyak untuk kondisi usulan; hasil negatif dilaporkan.

8. **Keterbatasan**

Hasil baru satu seed; replikasi parsial dan berbeda protokol; kebocoran pada split baru hanya diminimalkan karena tidak ada identitas pasien; makna kelas belum diketahui; selisih 625 dan 627 gambar validasi belum dijelaskan; dataset berasal dari lingkungan terkontrol dengan kasus karies yang terkonsentrasi di view oklusal, sehingga tidak mewakili populasi skrining umum.

Isi sendiri sebelum dipakai: jumlah gambar dan grup pada split uji v2, tingkat pemasangan set retraktor dan tanpa retraktor, serta angka seed 1 dan 2 bila sudah selesai.

