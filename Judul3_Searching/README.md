# Simulasi pencarian lagu di playlist musik HP dengan Sequential Search (linear search).

Program yang kita gunakan ini adalah penerapan algoritma Sequential Search untuk mencari judul lagu di dalam playlist musik yang tidak terurut yang dimana banyak lagu yang kita masukkan. Aplikasi ini memeriksa data satu per satu dari awal sampai lagu yang dicari ditemukan, lalu menampilkan berapa kali lagu tersebut muncul dalam playlist tanpa harus mengurutkan terlebih dahulu.

Metode pencarian ini sangat berguna untuk pencarian sederhana pada data kecil atau data yang belum terurut karena kita tidak harus mengurutkan data terlebih dahulu, seperti daftar lagu di HP. Kompleksitas waktunya adalah O(n), sehingga semakin banyak data, semakin lama juga proses pencariannya yang akan kita cari.


<img width="1715" height="456" alt="Screenshot 2026-05-07 082629" src="https://github.com/user-attachments/assets/23d8d5a6-629d-43e4-94c7-63128335c7b3" />
<img width="1699" height="426" alt="Screenshot 2026-05-07 082646" src="https://github.com/user-attachments/assets/cd6af621-62cf-4f3b-8703-14737238fdbb" />
Penjelasan kode perbaris
Pada baris 1: Mendefinisikan fungsi pencarian dengan tiga parameter penting. Parameter pertama adalah data yang berisi seluruh daftar lagu dalam bentuk list, parameter kedua n menunjukkan total jumlah lagu dalam playlist, dan parameter ketiga target adalah judul lagu yang sedang dicari oleh pengguna. Fungsi ini akan mengembalikan angka yang menunjukkan berapa kali judul tersebut muncul.

Pada baris 2 : variabel i dibuat dan diatur ke nilai 0. Tujuannya adalah untuk menandai posisi lagu yang sedang diakses di dalam list, di mana angka 0 merepresentasikan lagu pertama dalam daftar

Pada baris 3: Pada baris ini kita membuat variabel counter dan mengisinya dengan nilai 0. Variabel ini bertugas menghitung total kemunculan judul lagu yang dicari. Setiap kali ditemukan kecocokan, nilainya akan bertambah satu.

Pada baris 4: Memulai loop while yang akan terus berjalan selama nilai i masih kurang dari n (total jumlah lagu). Loop ini memastikan program memeriksa setiap lagu satu per satu dari awal sampai akhir daftar.

Pada baris 5:Disini kita melakukan pengecekan kondisi if untuk membandingkan lagu di posisi i dengan judul yang dicari (target). Jika keduanya sama persis, maka lagu tersebut cocok dengan yang dicari.

Pada baris 6: Ketika kita menemukan data yang cocok, maka nilai counter ditambah satu menggunakan operator +=. Ini berarti program berhasil menemukan satu kemunculan lagi dari judul lagu yang ingin kita dicari.

Pada baris 7: Variabel i ditambah satu agar program berpindah ke lagu berikutnya dalam daftar. Tanpa perintah ini, program akan stuck memeriksa lagu yang sama berulang kali.

Pada baris 8: Setelah semua lagu diperiksa (loop selesai), fungsi mengembalikan nilai counter yang berisi total kemunculan judul lagu yang dicari.

Pada Baris 11: Mendeklarasikan fungsi main() ini sebagai prosedur utama yang mengendalikan seluruh logika dan jalannya eksekusi program tersebut.

Pada Baris 12 : Di baris ini kita menyusun sebuah list bernama playlist yang menampung 9 judul lagu K-Pop yang kita masukkan diprogram. Di dalamnya, judul "dalla dalla" dituliskan dua kali guna menguji kemampuan program dalam mendeteksi data ganda (duplikat).

Pada Baris 13 : Mengukur total elemen di dalam list menggunakan fungsi len(), lalu menyimpan angka tersebut (yaitu 9) ke dalam variabel n.

Pada Baris 14: Disini kita menginformasikan isi playlist kepada pengguna dengan mencetaknya ke layar menggunakan teknik f-string agar daftar lagu terlihat jelas sebelum proses pencarian dimulai.

Pada baris 15 : KIta membuat sebuah blok perulangan yang akan terus beroperasi secara berkelanjutan. Tujuannya adalah untuk menjamin bahwa pengguna memberikan input yang benar. jika belum valid, sistem akan terus mengulang permintaan input tersebut hingga perintah break dieksekusi.

Pada Baris 16: Membuka blok try sebagai langkah awal penanganan pengecualian. Baris ini berfungsi untuk menguji kode di dalamnya dan mengantisipasi jika terjadi kesalahan fatal atau error saat eksekusi.

Pada Baris 17: Menginstruksikan program untuk meminta masukan dari pengguna dengan pesan teks tertentu. Data yang kita masukkan atau cari akan ditangkap dan disimpan ke dalam variabel target dengan tipe data string.

Pada Baris 18: Perintah break disini berfungsi untuk memutus perulangan secara paksa. Instruksi ini hanya akan tercapai jika proses pengambilan input pada baris sebelumnya berjalan lancar tanpa interupsi kesalahan.

Pada Baris 19: Bagian except bertindak sebagai "jaring pengaman" yang menangkap segala bentuk gangguan atau error yang muncul dari blok try. Jika terjadi kendala, alur program akan dialihkan langsung ke bagian ini.

Pada Baris 20: Memberikan umpan balik kepada pengguna berupa pesan peringatan jika input bermasalah. Karena berada di bawah blok except dalam perulangan, program akan secara otomatis kembali ke awal untuk meminta input ulang hingga benar.

Pada Baris 22: Menjalankan fungsi sequential_search dengan mengirimkan tiga argumen (daftar lagu, nilai n, dan judul target). Hasil penghitungan dari fungsi tersebut kemudian ditampung dalam variabel counter.

Pada baris 22: Disini kita Menggunakan struktur percabangan untuk memeriksa nilai di dalam variabel counter. Kondisi ini mengevaluasi apakah ditemukan setidaknya satu kecocokan judul lagu di dalam daftar. Jika benar nilai lebih besar dari nol, maka blok kode di bawahnya akan dijalankan.

Pada Baris  23 : Menampilkan informasi keberhasilan pencarian kepada pengguna. Dengan bantuan f-string, program menyisipkan judul lagu yang dicari beserta jumlah total kemunculannya secara dinamis ke dalam pesan yang muncul di layar.

Pada baris 24: Menyediakan jalur alternatif lain jika kondisi pada baris 22 tidak terpenuhi. Bagian ini otomatis dieksekusi apabila nilai counter adalah 0, yang menandakan bahwa judul lagu yang dicari sama sekali tidak ada di dalam playlist tersebut.

Pada baris 25: Memberikan umpan balik negatif kepada pengguna. Program menginformasikan secara spesifik bahwa judul lagu yang dimasukkan tidak dapat ditemukan di seluruh daftar lagu yang tersedia.

Output
<img width="1378" height="106" alt="Screenshot 2026-05-07 082925" src="https://github.com/user-attachments/assets/53c7b7b6-ca8d-48bd-a88d-ee43159c5563" />
Dimana di ouput ini ketika kita jalankan akan keluar playlist lagu yang sesuai dengan yang kita masukkan di kode diatas. Dan akan keluar kata masukkan judul yang akan kita cari. Disini saya akan memasukkan judul "dalla dalla" yang dimana ketika kita masukkan akan keluar "Lagu 'dalla dalla' ditemukan sebanyak 2 kali sesuai dengan playlist yang kita masukakan.

<img width="1359" height="81" alt="Screenshot 2026-05-07 082909" src="https://github.com/user-attachments/assets/d56c6246-5770-48ff-8ab9-991ac80ddb3f" />
Dimana di ouput ini ketika kita jalankan akan keluar playlist lagu yang sesuai dengan yang kita masukkan di kode diatas. Dan akan keluar kata masukkan judul yang akan kita cari. Disini saya akan memasukkan judul "wannabe" yang dimana ketika kita masukkan akan keluar "Lagu 'wannabe' ditemukan sebanyak 1 kali.

LINK YOUTUBE:

