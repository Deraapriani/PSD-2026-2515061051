# Program Pengurutan Nilai Kuis Siswa dengan Bubble Sort

Program ini adalah penerapan dari algoritma Bubble Sort untuk menyusun data nilai kuis siswa dalam urutan menaik (dari nilai paling rendah hingga paling tinggi). Aplikasi ini menawarkan fitur input data yang interaktif, menunjukkan perbandingan urutan sebelum dan setelah proses pengurutan, serta menyajikan hasil akhir dalam format daftar peringkat yang terstruktur. Alat ini sangat berguna sebagai acuan dalam menyelesaikan tugas-tugas terkait struktur data maupun sistem pemeringkatan yang sederhana. 

Dalam notasi Big O, kompleksitas waktu Bubble Sort adalah (n^2). Hal ini menjelaskan mengapa poin "efisien untuk data kecil" sangat ditekankan, karena waktu eksekusi akan meningkat secara kuadratik seiring bertambahnya jumlah elemen n.

source code
<img width="970" height="594" alt="Screenshot 2026-04-29 143628" src="https://github.com/user-attachments/assets/c85d6528-c34f-4600-98fc-a904b6050931" />
<img width="901" height="606" alt="Screenshot 2026-04-29 143640" src="https://github.com/user-attachments/assets/72b93ebb-3af9-49d4-881d-40e2554e62fa" />
<img width="798" height="241" alt="Screenshot 2026-04-29 143647" src="https://github.com/user-attachments/assets/391f9463-ccb3-4a1a-8bd9-6e45bb601861" />
Penjelasan Kode Per Baris:

Baris 1: Baris pertama ini isinya fungsi tukar yang gunanya buat memindahkan posisi elemen di dua array berbeda secara bersamaan. Ini penting banget supaya data nama dan nilainya tetap nyambung dan nggak berantakan pas lagi diurutkan.

Baris 2 : Di sini kita pakai variabel bantuan bernama temp_nilai buat nampung data dari indeks ke-i. Tujuannya biar pas nilainya ditimpa, kita masih punya salinan data aslinya di variabel sementara itu.

Baris 3: Pada Baris ini mengganti elemen pada posisi i dengan nilai yang terdapat pada posisi j. Tujuan dari langkah ini adalah untuk menata kembali lokasi angka dalam array sehingga susunannya tepat.

Baris 4: Disini kita Menempatkan nilai yang disimpan sementara terlebih dahulu ke indeks j.

Baris 6: Menempatkan nama dari indeks i ke dalam variabel untuk sementara.

Baris 7: Baris ini bertujuan untuk mengganti elemen pada arr_nama[i] dengan informasi dari arr_nama[j]. Ini dilakukan agar ketika data mengalami pergeseran, identitas siswa tetap terhubung dengan nilai yang mereka miliki.

Baris 8: Menyimpan nama yang terdapat dalam variabel sementara ke indeks j pada array nama, agar data nama dan nilai tetap konsisten setelah proses tukar rampung.

Baris 10: Menggambarkan fungsi bubble_sort yang menerima dua array (nilai dan nama) serta ukuran n, bertujuan untuk mengurutkan kedua array secara bersamaan berdasarkan nilai dari yang terkecil hingga yang terbesar.

Baris 11: Proses iterasi utama (loop luar) yang berjalan sebanyak n-1 kali, di mana setiap siklus mewakili satu tahap lengkap dalam algoritma pengurutan bubble sort.

Baris 12: Proses iterasi dalam (loop dalam) yang membandingkan elemen-elemen dari indeks 0 hingga n-i-1, memastikan elemen terbesar dari tahap tersebut "mengapung" ke posisi terakhir.

Baris 13: Kondisi perbandingan untuk menentukan apakah pertukaran elemen diperlukan, dengan memeriksa apakah nilai pada indeks j lebih kecil dibandingkan nilai pada indeks j+1 untuk mencapai urutan yang naik.

Baris 14: Memanggil metode penggantian dengan parameter daftar nilai, nama, dan indeks j serta j+1 ketika syarat perbandingan dipenuhi, sehingga kedua daftar bertukar untuk menjaga konsistensi data.

Baris 16: Menetapkan fungsi utama sebagai pengendali inti program yang mengatur masukan, pengecekan, pengurutan, dan keluaran secara teratur.

Baris 17: Menginisialisasi blok try-except untuk menangani kemungkinan kesalahan pada masukan dengan aman tanpa menyebabkan program berhenti secara mendadak.

Baris 18: Meminta pengguna untuk memasukkan jumlah siswa, mengubahnya menjadi integer menggunakan int(), dan menyimpannya dalam variabel n untuk digunakan dalam loop berikutnya.

Baris 19: Menangkap kesalahan ValueError yang terjadi ketika pengguna memberikan karakter non-angka untuk jumlah siswa.

Baris 20: Menampilkan pesan error yang informatif "Input tidak valid! " agar pengguna menyadari kesalahan dalam masukan yang diberikan.

Baris 21: Menghentikan proses eksekusi fungsi utama dengan return jika masukan yang diberikan tidak valid, untuk mencegah program melanjutkan ke tahap berikutnya.

**Baris 24:** Menginisialisasi array kosong arr_nilai untuk menyimpan semua nilai kuis siswa yang akan dimasukkan nanti.

**Baris 25:** Menginisialisasi array kosong arr_nama untuk menyimpan nama-nama siswa agar dapat diproses bersamaan dengan nilai.

Baris 26: Menampilkan instruksi yang jelas kepada pengguna agar memahami bahwa data siswa harus dimasukkan satu per satu secara berurutan.

Baris 27: Memulai loop for yang akan berjalan sebanyak n kali sesuai jumlah siswa yang sudah diinput sebelumnya.

Baris 28: Meminta input nama siswa ke-(i+1) dengan format dinamis dan membersihkan spasi berlebih menggunakan strip().

Baris 29: Menambahkan nama siswa yang baru diinput ke dalam array arr_nama menggunakan method append().

Baris 31: Memulai loop while True tak terhingga untuk memastikan input nilai kuis selalu valid sebelum melanjutkan.

Baris 32: Memulai blok try untuk melakukan konversi input nilai ke integer dengan penanganan error.

Baris 33:Meminta input nilai kuis siswa dengan menampilkan nama siswa terkait agar user tahu data mana yang sedang diinput.

Baris 34:Nilai numerik yang baru dimasukkan user langsung ditambahkan ke dalam kumpulan data nilai siswa yang sudah tersimpan sebelumnya.

Baris 35: Loop validasi input dihentikan karena program sudah memastikan data nilai yang masuk benar dan siap diproses.

Baris 36:Bagian ini menangkap kesalahan ketika user memasukkan karakter huruf atau simbol padahal diharapkan input berupa angka.

Baris 37:Menampilkan notifikasi kesalahan yang menginformasikan user bahwa input nilai harus berbentuk angka murni.

Baris 40: Mencetak judul informasi yang menandakan data berikutnya adalah kondisi awal sebelum pengurutan dilakukan.

Baris 41:Melakukan iterasi melalui seluruh rekaman siswa untuk menampilkan informasi lengkapnya secara berurutan.

Baris 42: Menghasilkan output berpasangan nama siswa dan nilai kuis sesuai dengan posisi asli saat data diinput.

Baris 44:Memanggil fungsi pengurutan untuk mengubah posisi semua elemen berdasarkan nilai dari terkecil hingga terbesar.

Baris 46: Mencetak header penanda bahwa daftar selanjutnya sudah dalam kondisi terurut secara ascending.

Baris 47:Mengulang proses penelusuran data untuk mengambil informasi setelah pengurutan selesai dilakukan.

Baris 48:Menampilkan hasil final dengan format terstruktur: nomor urut, nama siswa, dan nilai kuisnya.

Baris 51: Pengecekan standar yang menjamin kode hanya dieksekusi saat file dijalankan langsung, bukan diimpor sebagai modul.

Baris 52: Disni Instruksi penutup yang memicu eksekusi fungsi utama untuk memulai seluruh proses program dari awal.
Panggil fungsi utama

output
<img width="627" height="260" alt="Screenshot 2026-04-29 190629" src="https://github.com/user-attachments/assets/50c1370c-ec41-496a-8350-4f4552832dba" />

pada output ini ketika user diminta memasukan jumlah siswa yang dimana kita masukan 4 siswa. lalu kita masukkan satu persatu. Yang pertama kita masukkan nama siswa yaitu dera dan nilai kuisnya sebesar 88, kedua masukkan nama ruka dengan nilainya 90, ketika masukkan nama ahyeon dengan nilainya 78, dan terakhir kita masukkan nama ryujin dan nilainya yaitu 99.
<img width="531" height="134" alt="Screenshot 2026-04-29 190639" src="https://github.com/user-attachments/assets/c2dae1f6-013d-4b68-9ee2-6c9583e9721b" />

Dilanjutkan dengan output yang keluar yaitu data sebelum diurutkan yaitu dera : 88, ruka : 90, ahyeon: 78 dan ryujiin : 99

<img width="546" height="158" alt="Screenshot 2026-04-29 190645" src="https://github.com/user-attachments/assets/a5657354-d56a-49eb-a482-7575478eb18c" />

Pada output ini keluar nilai dengan kuis yang sudah diurutkan sesuai permintaan yaitu dari terbesar ke nilai terkecil yang berarti diurutkan pertama yaitu ryujin :99,ruka : 90, dera : 88, ahyeon: 78
dan selesai program dihentikan.

Link Youtube
