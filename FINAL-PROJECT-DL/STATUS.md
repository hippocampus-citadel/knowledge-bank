# STATUS PROJECT

> Terakhir diperbarui: 2026-11-04

**`[CLAUDE @w30 (2026-11-04)]`**

## Saat ini
- Eksplorasi dihentikan atas keputusan user. Belum ada model/baseline. Belum dipastikan apakah ide burung dipilih tim (alternatif: rambu lalu lintas GTSRB).
- Catatan teknis: load_dataset biasa pada BirdSet XCM mengunduh seluruh ±96 GB dan memenuhi disk Colab; pakai streaming=True. Butuh datasets<4.0 (mis. 3.6.0) + trust_remote_code=True (script BirdSet.py). Branch refs/convert/parquet tidak ada. Kolom audio berisi bytes (path None), decode dengan soundfile.

## Langkah berikutnya
1. Susun proposal sesuai bagian 10 REQUIREMENTS.md (internal 5 Nov, presentasi ke dosen 6 Nov).
2. Ajukan ide ke tim dengan framing "klasifikasi suara burung yang robust terhadap noise dan label lemah", bukan "dataset bersih lalu training".
3. Pilih 20-50 spesies dan hitung ulang statistik pada subset final.
4. Split per rekaman/recordist (anti-leakage, REQUIREMENTS poin 25); bandingkan dengan split acak sebagai bukti.
5. Pipeline otomatis (titik awal, belum diuji): sort + merge event (gap 0,5 dtk), padding, jendela tetap 3-5 dtk, buang event terlalu pendek, high-pass/PCEN + augmentasi noise. Semua parameter jadi hiperparameter eksperimen vs baseline jendela tetap.
6. Tes dengar event pendek (apakah panggilan asli atau deteksi keliru).

## Pertanyaan terbuka
- Apakah tim memilih ide burung atau rambu lalu lintas?
- Apa distribusi kelas penuh XCM dan spesies mana yang punya data cukup?
- Apakah ID rekaman (filepath) unik di semua shard, dan apakah event pendek valid?
- Apa penyebab cakupan event >100% dan celah negatif besar (overlap vs urutan list)?
- Apakah ebird_code_secondary kosong berupa list kosong, string kosong, atau None?
- Lisensi share-alike: apa implikasinya jika hasil dipublikasikan?

## Riwayat 
- Selesai sesi ini:
  - Cek klaim awal: Xeno-canto (XC) memang besar (subset XCL BirdSet ±528 rb rekaman). Noise/suara campur terbukti sebagian lewat tes dengar manual (8 klip, 1 penilai: 4 layak, 3 ambigu, 1 tidak layak; angin dominan, burung latar sering ada). Tidak ada dataset HF yang diklaim "bersih" (BirdSet hanya filter kualitas A/B/C; 6s-16khz hanya pra-proses; dataset 105 spesies pihak ketiga, kualitas belum diverifikasi).
  - Dataset yang diuji: DBD-research-group/BirdSet, config XCM. Metadata cukup untuk split anti-leakage (kolom filepath, recordist, lat/long, quality, license, detected_events, peaks, ebird_code_secondary). start_time/end_time kosong, jadi label hanya tingkat rekaman (label lemah).
  - Statistik dari 3000 baris pertama streaming (bias ke shard awal, hanya ±9 spesies, BUKAN distribusi penuh): 1 baris = 1 rekaman unik, 582 recordist, kualitas B 45%/A 32%/C 23%, lisensi ±94% CC BY-NC-SA 4.0, ±38% punya ebird_code_secondary (batas bawah, format "kosong" belum diverifikasi).
  - detected_events berupa list [mulai, akhir] dalam detik. Event mentah bermasalah: overlap/tidak terurut (celah negatif sampai -101 dtk), cakupan >100% pada sebagian rekaman, 36% event <1 dtk, 12% rekaman tanpa event. Setelah sort+merge (gap 0.0/0.5/1.0 dtk): event 46.227/37.787/29.160; <1 dtk 28/23/18%; >10 dtk 1,8/3,8/8,0%.
  - Tes dengar: event-cropping memperjelas target di sebagian klip, tapi angin tetap ada di dalam event. Perbandingan klip-ke-klip yang ketat belum terlaksana (runtime disconnect, klip berganti).
