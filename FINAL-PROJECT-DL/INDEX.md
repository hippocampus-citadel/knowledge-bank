# FINAL PROJECT DEEP LEARNING 

> LLM: baca dulu `SOP.md` dan `PREFERENCES.md`:
> - SOP: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/SOP.md?v=20261114 (setelah membaca kutip baris `Terakhir diperbarui` persis dan kalimat pertama file SOP.md)
> - PREFERENCES: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/PREFERENCES.md?v=20261031
>
> Jika tidak bisa membuka link, minta user menempelkan isinya.

Terakhir diperbarui: 2026-11-15

## Ringkasan
- Tujuan: Mengembangkan dan mengevaluasi model Deep Learning dari dataset UCI Human Activity Recognition sebagai proyek akhir mata kuliah Deep Learning
- Stack: Python (mainly, rinciannya masih belum dapat ditentukan)  
- Tipe: Tugas Proyek Akhir Mata Kuliah Deep Learning

## Status saat ini
Sesi ini menyelesaikan riset literatur dengan menetapkan tiga pembanding valid (Anguita, TCN-GRU, Xia) dan mencatat lima sumber lain sebagai tidak sebanding karena kelalaian protokol atau inkonsistensi data. Saat ini tidak ada eksperimen baru yang berjalan, INDEX.md usang, tabel literatur serta proposal belum ditulis, dan verifikasi kode Vazan serta paper Mutegeki & Han masih tertunda. Langkah prioritas adalah menyusun tabel literatur dan memperbaiki proposal, memperbaiki INDEX.md, menstandarisasi lokasi dataset v2 untuk EDA, menentukan skema GroupKFold, lalu menjalankan eksperimen ANN 561 fitur dan GRU sebagai baseline. Keputusan metodologi baru menetapkan pemilihan konfigurasi via validasi per peserta, pelaporan akurasi dan macro-F1, serta tidak menargetkan angka di atas 97 persen.

## Langkah berikutnya
1. Tulis tabel literatur (kolom: split, input, konfigurasi dipilih dengan apa, metrik, status) dan lengkapi proposal (rumusan masalah + referensi).
2. Perbaiki INDEX.md.
3. Seragamkan lokasi dataset v2, lalu jalankan EDA v2.

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
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/STATUS.md?v=20261115 | perlu detail progres |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/REQUIREMENTS.md?v=20261101 | perlu latar belakang / spesifikasi |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/DECISION.md?v=20261115 | akan mengusulkan perubahan arah |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/extra/proposal_feedback.md?v=20261107 | perlu membaca feedback proposal proyek akhir dari dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/extra/progress1_feedback.md?v=20261114 | perlu membaca feedback progress update feedback minggu kedua November proyek akhir dari dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-DL/extra/progress_update_1.md?v=20261114 | perlu membaca progress update feedback minggu kedua November versi lebih komprehensif dari progress1_feedback.md |
