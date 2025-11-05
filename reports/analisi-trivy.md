# Analisis Hasil Scanning Trivy

**Image:** aplikasi-kompleks:1.0-rentan & aplikasi-kompleks:1.1-aman
**Tanggal:** 5 November 2025
**Penulis:** Erik Triayuda Wijaya


### aplikasi-kompleks:1.0-rentan
Total kerentanan yang ditemukan: 424 

| Tipe | Critical | High | Medium | Low |
|---|---|---|---|---|
| Jumlah | 19 | 44 | 40 | 19 |

Contoh CVE: CVE-2021-31535
"libX11: Missing request lengths checks"

Berdasarkan [www.cve.org](https://www.cve.org):
Versi libx11 sebelum 1.7.1 dapat memberi kemungkinan penyerang untuk melakukan serangan untuk mengeksekusi arbitary code.


### aplikasi-kompleks:1.1-aman
Total kerentanan yang ditemukan: 79

| Tipe | Critical | High | Medium | Low | Unknown |
|---|---|---|---|---|---|
| Jumlah | 0 | 0 | 1 | 78 | 0 |

Pada build terbaru, critical problem yang muncul pada versi sebelumnya kini telah tiada. Hal ini bisa diperiska pada [laporan_bersih.txt](laporan_bersih.txt)


## Kesimpulan
Pada praktikum ini, beberapa poin penting yang dapat diambil (khususnya oleh penulis, saya, Erik Triayuda Wijaya):
- Konfigurasi source file harus dilakukan dengan sangat hati-hati, apabila terdapat perbandingan variabel atau string, harap untuk dilakukan dengan format yang benar.
- Proses build dan running pada docker image/container dapat dilakukan dalam banyak iterasi. Sehingga proses dapat terasa redundan. Sebaiknya, membuat shell script atau bentuk otomasi agar proses build and trial dapat dilakukan lebih cepat.
- Jika menggunakan lebih dari satu servis yang memerlukan running port, sebaiknya untuk sering memeriksa konfigurasi nomor port yang digunakan agar tidak terjadi kesalahan seperti ketidaksesuaian nginx dengan gunicorn.
