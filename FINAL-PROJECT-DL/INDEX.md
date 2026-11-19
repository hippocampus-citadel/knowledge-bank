# FINAL PROJECT DEEP LEARNING 

> LLM: baca dulu `SOP.md` dan `PREFERENCES.md`:
> - SOP: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/SOP.md?v=20261116 (setelah membaca kutip baris `Terakhir diperbarui` persis dan kalimat pertama file SOP.md)
> - PREFERENCES: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/PREFERENCES.md?v=20261031
>
> Jika tidak bisa membuka link, minta user menempelkan isinya.

Terakhir diperbarui: 2026-11-19

## Ringkasan
- Tujuan: Mengembangkan dan mengevaluasi model Deep Learning dari dataset UCI Human Activity Recognition sebagai proyek akhir mata kuliah Deep Learning
- Stack: Python (mainly, rinciannya masih belum dapat ditentukan)  
- Tipe: Tugas Proyek Akhir Mata Kuliah Deep Learning

## Status saat ini
Project telah menyelesaikan validasi silang (CV) 7-fold GroupKFold pada 21 peserta train UCI HAR dengan folds.json terkunci, membandingkan ANN sinyal (128×9) dan ANN 561 fitur; ANN 561 fitur menunjukkan akurasi rata-rata 0,9333 ± 0,0388 (macro-F1 0,9339 ± 0,0374) lebih stabil dari ANN sinyal (0,9188 ± 0,0562), namun kenaikan rata-rata berasal dari fold 5 saja sehingga perbedaan tidak signifikan, sementara SD antar fold turun dan akurasi fold terendah naik dari 0,819 ke 0,880. Diagnostik mengidentifikasi peserta 14, 16, 25 sebagai sumber variasi utama akibat kesulitan membedakan SITTING/STANDING dan WALKING/UPSTAIRS. Saat ini tidak ada run berjalan; protokol evaluasi FINAL (latih ulang 21 peserta vs model fold) belum ditetapkan, normalisasi masih mengandung kebocoran kecil dari statistik train lama, template common.py v2.0 belum dikonfirmasi penerapannya ke tim, dan dokumen INDEX.md serta tabel literatur belum diperbarui. Langkah prioritas: jalankan GRU sinyal CV, diagnostik peserta 14/16/25 pada ANN 561 fitur, ulang LSTM/BiLSTM/CNN variant di CV, bandingkan model berpasangan per fold, uji early stopping tanpa patience 10, serta tentukan protokol FINAL dengan dosen.

## Langkah berikutnya
1. Jalankan GRU pada sinyal (CV), dengan NAME pola <model>_<input>_cv_v<N>.
2. Jalankan diagnostik peserta 14, 16, 25 pada ANN 561 fitur (apakah SITTING<->STANDING di peserta 16 membaik dan WALKING->UPSTAIRS di peserta 14 tetap).
3. Ulang LSTM v1 di CV (hasil lama [1,25,27] tidak sebanding), lalu BiLSTM, CNN 1D, CNN-LSTM, dan LSTM v2.

## Keputusan penting (final)
- Judul resmi proyek adalah Klasifikasi Aktivitas Manusia Menggunakan Data Sensor Smartphone
- Dataset yang digunakan adalah Human Activity Recognition Using Smartphones dari UCI Machine Learning Repository
(Daftar lengkap: DECISIONS.md)

## Batasan / requirement khusus
- Deadline: Weekly Progress Report sudah harus ada tanggal 12 November 2026, Deadline final akan menyusul
- Aturan dosen: lihat `REQUIREMENTS.md` 
- Hal yang tidak boleh diubah: `None`

## Konteks tambahan (baca HANYA jika kondisinya terpenuhi)
| File | Baca jika... |
|---|---|
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/STATUS.md?v=20261119 | perlu detail progres |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/REQUIREMENTS.md?v=20261101 | perlu latar belakang / spesifikasi |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/DECISION.md?v=20261119 | akan mengusulkan perubahan arah |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/extra/proposal_feedback.md?v=20261107 | perlu membaca feedback proposal proyek akhir dari dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/extra/progress1_feedback.md?v=20261114 | perlu membaca feedback progress update feedback minggu kedua November proyek akhir dari dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/extra/progress_update_1.md?v=20261114 | perlu membaca progress update feedback minggu kedua November versi lebih komprehensif dari progress1_feedback.md |
