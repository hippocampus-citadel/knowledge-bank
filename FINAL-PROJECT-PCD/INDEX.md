# FINAL PROJECT PCD - Sistem Skrining Awal Kesehatan Gigi Berbasis Kamera Smartphone

> LLM: baca dulu `SOP.md` dan `PREFERENCES.md`:
> - SOP: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/SOP.md
> - PREFERENCES: https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/PREFERENCES.md
>
> Jika tidak bisa membuka link, minta user menempelkan isinya.

Terakhir diperbarui: 2026-10-31

## Ringkasan
- Tujuan: Mengembangkan prototipe sistem skrining awal yang menganalisis foto rongga mulut dari kamera smartphone untuk menampilkan indikasi beberapa kondisi gigi dan gusi.
- Tipe: Tugas Kuliah untuk Proyek Akhir Mata Kuliah Pemrosesan Citra Digital (PCD)
- Stack: [WAJIB] -> Python, OpenCV. [PERKIRAAN SEMENTARA]: PyTorch/Ultralytics YOLO, FastAPI, serta Flutter atau web responsif (Pilihan frontend dan deployment belum final)
- Batas Klaim: Alat ditujukan untuk skrining/edukasi awal, bukan diagnosis medis dan bukan pengganti pemeriksaan dokter gigi.

## Status saat ini
Update status per 31 Oktober 2026 (sesi review dataset) mengonfirmasi bahwa analisis Dataset Zenodo (DOI 10.5281/zenodo.14827784, CC BY 4.0) via *script* lokal berhasil memverifikasi total 6.265 gambar (termasuk 2.752 *no_retractors* dari ~560 pasien berusia 10–24 tahun) serta menemukan kebocoran fatal pada *split benchmark* bawaan (65,6% set tersebar di >1 *split*). Untuk mengatasi hal ini, user sementara telah mengunci *split* buatan berbasis grup (*seed* 42, 70/15/15) dan menyepakati penggunaan seluruh 5 *view* dengan metrik utama berfokus pada *view* oklusal, sementara hambatan seperti kejelasan label kelas 0/1, akses GPU/pakar, serta penulisan proposal yang tenggatnya 4 November 2026 menjadi prioritas penanganan berikutnya.

(Detail lengkap: STATUS.md)

## Langkah berikutnya
1. Tulis proposal; angka di atas dipakai untuk deskripsi dataset dan keterbatasan.
2. Tulis klaim sesuai data: deteksi lesi karies pada foto intraoral, metrik utama di view oklusal, frontal/lateral deskriptif; BUKAN skrining populasi umum dan bukan klaim foto pengguna awam; populasi terbatas remaja/dewasa muda (abstrak: usia 10–24, Medium).
3. Konfirmasi makna kelas 0/1 dari teks penuh makalah (Nature/PMC dibuka manual; akses otomatis diblokir) atau penulis. Sementara pakai evaluasi satu kelas (`single_cls`) sebagai metrik utama.
4. Cek visual beberapa dari 23 kotak bermasalah.
5. Setelah proposal: kurva belajar (25/50/100% data latih), baseline YOLO di `dataset_split`, lalu pipeline preprocessing. Karena daya uji rendah (±383 grup latih, 83 grup uji), pertimbangkan 5-fold per grup + bootstrap per grup + beberapa seed.
     
## Keputusan penting (final)
- Tema project yang diambil adalah skrining kesehatan gigi via kamera smartphone. Alasan: Keputusan tim yang sudah final
- Sistem final akan terdiri dari layer pemrosesan citra + deteksi dan layer aplikasi web. Alasan: Ketentuan dari dosen untuk layer deteksi dibungkus aplikasi dan bukan notebook python biasa
- Preprocessing dan kualitas foto sebelum deteksi menjadi fokus kontribusi yang akan diuji. Alasan: lihat rubrik penilaian di REQUIREMENTS.md

(Daftar lengkap: DECISIONS.md)

## Batasan / requirement khusus
- Deadline: 4 November 2026 untuk Proposal Sementara (BUKAN DEADLINE FINAL)
- Aturan dosen: lihat REQUIREMENTS.md
- Hal yang tidak boleh diubah: Tema Skrining Gigi via Kamera Smartphone (Boleh diubah jika judul ditolak dosen setelah 4 November 2026)

## Konteks tambahan (baca HANYA jika kondisinya terpenuhi)
| File | Baca jika... |
|---|---|
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/STATUS.md | perlu detail progres |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/REQUIREMENTS.md | perlu mengetahui detail spesifik ketentuan dari dosen |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/DECISIONS.md | akan mengusulkan perubahan arah |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/intenal_teams_files/literature-review.md | butuh melihat hasil literature review yang telah dikumpulkan |
| https://raw.githubusercontent.com/hippocampus-citadel/knowledge-bank/main/FINAL-PROJECT-PCD/extras/log_history.md | perlu meninjau apa saja yang telah dilakukan di sesi sesi sebelumnya |
