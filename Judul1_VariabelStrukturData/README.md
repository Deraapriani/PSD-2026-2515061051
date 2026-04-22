Manajemen Memori dan Array/List melalui analogi sebuah rak loker.

Program yang Anda buat merupakan Simulasi Pengelolaan Memori pada List yang menggunakan perbandingan "Loker". Tujuan dari program ini adalah untuk menunjukkan secara visual cara Python menyimpan objek di dalam memori (RAM) melalui struktur data List.Berikut adalah penjelasan singkat tentang aplikasi ini:

Aplikasi ini merupakan suatu software berbasis CLI (Command Line) yang mensimulasikan pengelolaan informasi dalam 5 slot loker sekaligus memberikan gambaran mengenai cara Python menangani alamat memori (RAM).

Ciri-Ciri Utama
Pemeriksaan Memori: Menggunakan fungsi `id()` untuk memantau alamat fisik objek dalam memori yang ditampilkan dalam format Hexadesimal.
Data Struktur: Memanfaatkan List sebagai gambaran dari rak penyimpanan.
Keamanan Input: Memiliki fitur `try-except` (Validasi) untuk mencegah terjadinya kesalahan program jika pengguna salah memberikan input (seperti memasukan huruf pada kolom angka).

Manfaat
1. Pembelajaran: Menunjukkan bahwa variabel dalam Python berfungsi sebagai referensi yang menunjuk ke suatu alamat memori, alih-alih memegang nilai itu sendiri.
2. Pelacakan: Menyajikan fakta bahwa ketika isi loker berubah, alamat memori yang diacu oleh slot tersebut juga akan berubah.

