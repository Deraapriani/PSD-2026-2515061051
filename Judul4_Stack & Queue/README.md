# Simulasi tumpukan piring di dapur dengan stack array (LIFO)

Program yang saya gunakan ini yaitu program simulasi tumpukan piring didapus dengan menggunakan stak array yang memiliki prinsip LIFO yaitu last in first out yang dimana stack ini yaitu sebuah tumpukan bekerja di dalam memori komputer menggunakan array (dalam phyton menggunakan list). Disini kita bisa menambah iring dengan push, mengambil piring dengan pop, dan melihat piring paling atas dengan peek dan melihat seluruh  isi tumpukan.

Manfaat dari program ini untuk memahami konsep dari LIFO (Last in, First out)  secara visual, dimana data yang terakhir masuk adalah data yang pertama keluar. Secara teknis kode pada program ini melatih pengelolaan memori dan pencegahan error melalui pengecakan kondisi tumpukan apa penuh atau kosong.

<img width="1116" height="745" alt="Screenshot 2026-05-13 220505" src="https://github.com/user-attachments/assets/ae67e6b7-f3de-4410-b334-da618b44af52" />
<img width="1028" height="724" alt="Screenshot 2026-05-13 220523" src="https://github.com/user-attachments/assets/cb536e44-ffa9-4a20-98a9-f73614ebd341" />
<img width="883" height="475" alt="Screenshot 2026-05-13 220537" src="https://github.com/user-attachments/assets/32d7a916-bb74-4c57-bc5a-8b5793729fe0" />

Penjelasan kode :
Pada  baris 1 : Sebuah class baru bernama StackArray didefinisikan dibaris pertama. Class ini akan berfungsi sebagai model untuk membuat objek stack berbasis array dengan semua metode dan atribut stack dikelompokkan di dalamnya untuk kemudahan penggunaan dan pemeliharaan kode.

Pada baris 2 : Baris kedua berisi definisi constructor __init__ yang secara otomatis dipanggil saat membuat objek baru, menerima parameter max_size dengan nilai default 50 yang menentakan kapasitas maksimum tumpukan piring yang bisa disimpan dalam stack tersebut.

Pada baris 3 :  Dibaris ini menyimpan nilai parameter max_size ke dalam atribut instance self.MAX, sehingga ukuran maksimal stack dapat diakses kapan saja melalui objek tersebut sepanjang lifetime objek.

Pada baris 4 : Pada baris ini dilakukan inisialisasi tumpukan utama berupa list st dengan ukuran sesuai self.MAX, di mana nilai None digunakan sebagai pengisi sementara sebelum piring asli dimasukkan.

Pada baris 5 : variabel top_idx ditetapkan pada nilai -1 sebagai indikator standar bahwa tumpukan masih benar-benar kosong dan belum memiliki elemen.

Pada baris 6 : Pada baris ini mendefinisikan method is_empty() yang bertugas mengecek status kekosongan stack, method ini sangat penting untuk mencegah kesalahan saat melakukan operasi pop atau peek pada stack kosong.

Pada baris 7 : mengimplementasikan logika pengecekan dengan membandingkan top_idx dengan -1, mengembalikan nilai boolean True jika kosong atau False jika sudah berisi minimal satu piring.

Pada baris 8 : Mendefiniskan method is_full() yang dimana fungsinya untuk mengecek apakah stack sudah full kapasitasnya dan juga agar mencegah terjadinya overflow dalam implementasi stack array.

Pada baris 9 : Pada baris ini melakukan perbandingan top_idx dengan MAX-1, mengembalikan True ketika index top sudah berada di posisi terakhir array, menandakan tidak bisa menambah lagi.

Pada baris 10 : Pada baris ini gunanya untuk mendefinisikan method push(self, x) yang merupakan operasi inti stack untuk menambahkan elemen baru (x sebagai nama/ID piring) ke posisi paling atas tumpukan.

Pada baris 11 : Disini akan melakukan pengecekan kondisi penuh sebagai langkah safety pertama sebelum menambah elemen baru.

Pada baris 12 : Disini kita akan melakukan print untuk tumpukan piring penuh.

Pada baris 13 :melakukan return prematur untuk menghentikan eksekusi method jika kondisi penuh terdeteksi, mencegah modifikasi lebih lanjut.

Pada baris 14 : Pada baris ini menaikkan nilai top_idx sebanyak 1 unit untuk menunjuk posisi slot kosong berikutnya di array.

Pada baris 15 : Pada baris ini menyimpan data piring x ke dalam array pada posisi top_idx yang baru, operasi penulisan aktual ke memori.

Pada baris 16 : Disini kita akan  memberikan konfirmasi sukses kepada user dengan format string f yang menampilkan nama piring spesifik yang baru ditambahkan.

Pada baris 17 : Disini ada pop ()  yang dimana mendefinisikan method pop() yang bertugas mengambil dan "menghapus" piring dari posisi paling atas stack, simulasi mengambil piring untuk digunakan.

Pada baris 18 : Disini kita akan melakukan pengecekam kondisi agar mengetahui adanya underflow.

Pada baris 19 : Disini akan print jika tidak ada piring

Pada baris 20 :  Disini ada return yang dimana untuk keluar dari method jika stack dalam keadaan kosong.

Pada baris 21 : Disini akan menampilkan informasi dari piring yang akan diambil dari posisi top sebelum bear benar dihapus.

Pada baris 22 : menurunkan top_idx sebanyak 1, secara efektif "menghapus" piring tanpa benar-benar menghapus data dari array (space efficient).

Pada baris 23 : Pada baris ini terdapat peek () yang dimana peek ini untuk  melihat piring diatas tanpa mengubah struktu pad stack.

Pada baris 24 : Pada baris ini yaitu mengecek pada bagian tumpukan apakah dalam keadaan kosong atau tidak. dan akan memanggil metode is_empty() yang biasanya akan mengembalikan nilai true jika tidak ada data.

Pada baris 25 : Jika kondisi diatas yaitu is_empty bernilai true maka program akan mencetak atau print bahwasanya tumpukan kosong.

Pada baris 26 : Disini digunakan return untuk menghentikan eksekusi pada metode peek setelah pesan tidak ada piring.

Pada baris 27 : disini sebagai perintah untuk menampilkan inforamsi dari piring yng berada pada posisi paling atas tanpa mengubah isi tumpukan.

Pada baris 28 : Pada baris ini terdapat method display () untuk visualisasi lengkap isi stack dari atas ke bawah.

Pada baris 29 : Pada baris ini kita melakukan pengecekan kondisi awal. Program memanggil fungsi is_empty ()  untuk mengetahui apakah tumpukan piring sedang kosong atau tidak.

Pada baris 30 : DIsini sama sasja jika kondisi true maka program akan mencetak teks ini sebagai pemberitahuan bahwa tidak ada data yang bisa ditampilkan.

Pada baris 31 : Perintah ini berfungsi untuk langsung keluar dari fungsi. Jika tumpukan sudah dipastikan kosong, program tidak perlu melanjutkan ke baris di bawahnya untuk mencoba mencetak data yang memang tidak ada.

Pada baris 32 : Baris ini mencetak teks judul sebagai pembuka. Parameter end="" sangat penting di sini; fungsinya adalah agar teks selanjutnya dicetak di baris yang sama

Pada baris 33 : Logika tumpukan yang dimana akan melakukan perulangan mundur yang dimana jika self.top_idx  mulai dari indels atas, -1 berhenti jika mencapai angkat -1, dan -1 melangkah mundur

Pada baris 34 : Diisni akan mengambil piring pada indeks ke i daris list self.st dan akani  mencetaknya. Dan parameter end="" digunakan agar nama setiap piring dipisahkan denga spasi.

Pada baris 35 :Didalam perulangan selesai akan ada print kosong ini untuk mevcetak baris baru.

Pada baris 37 : Pada baris ini fungsi main() untuk menjalankan program

Pada baris 38 : Disini pada stack dengan kapasitas 20 piring 

Pada baris 39 : Disini while true untuk terus berjalan sampai user akan memilih keluar.

Pada baris 40 : Padaa baris ini akan mencetak dari judul pada menu layar. Dimana simbol \n diawal teks berfungsi untuk memberikan satu baris kosong.

Pada baris 41 : tampilan instruksi bagi pengguna jika ingin menambah piring ke dalam tumpukan. Dalam konsep struktur data Stack, pilihan ini biasanya akan memicu fungsi push.

Pada baris 42 : Baris ini menginformasikan bahwa angka "2" digunakan untuk mengambil piring yang ada di posisi paling atas. Dalam pemrograman, ini adalah aksi pop.

Pada baris 43 : Pada baris ini Pilihan ketiga ini disediakan bagi pengguna yang hanya ingin mengintip atau melihat identitas piring paling atas tanpa benar-benar mengambilnya dari tumpukan.

Pada baris 44 : untuk menjalankan fungsi yang akan mencetak seluruh daftar piring yang ada di dalam tumpukan, mulai dari yang paling atas hingga paling bawah.

Pada baris 45 : untuk menghentikan program secara normal.

Pada baris 46 : Baris ini menampilkan teks "Pilih: " untuk mengambil masukan pengguna melalui fungsi input(), kemudian menggunakan .strip() untuk menghapus spasi yang tidak diinginkan. Hasil ketikan yang sudah bersih tersebut disimpan ke dalam variabel cmd agar bisa diproses oleh program ke tahap berikutnya.

Pada baris 47 : Disni memeriksa apakah nilai cmd persis sama dengan string "1". Jika benar, program menjalankan blok kode di bawahnya yang terindentasi.

Pada baris 48 :meminta pengguna memasukkan nama atau ID piring dan menyimpannya ke variabel name sebagai string.

Pada baris 49 : memanggil method push() pada objek stack untuk menambahkan elemen name ke posisi teratas stack mengikuti prinsip LIFO (Last In First Out).

Pada baris 50 : Baris ini menggunakan **elif** sebagai alternatif pengecekan yang hanya akan berjalan jika pilihan pertama salah, guna memastikan apakah isi variabel cmd adalah angka dua.

Pada baris 51 : Pada stack.pop () ini menghapus dan mengembalikan elemen teratas dari stack. Jika stack kosong, biasanya akan menimbulkan error atau mengembalikan None.

Pada baris 52 : Memriksa apakah nilai dari cmd bernilai 3

Pada baris 53 : Pada stack.peek() ini  untuk menampilkan elemen atau mengembalikan elemen atas pada stack tanpa menghapus.

Pada baris 54 : Memriksa apakah nilai dari cmd bernilai 4

Pada baris 55 :menampilkan semua elemen dalam stack, biasanya dari bawah ke atas atau atas ke bawah tergantung implementasinya, dalam format yang mudah dibaca.

Pada baris 56 : Memriksa apakah nilai dari cmd bernilai 5

Pada baris 57 : disini akan mencetak pesan selesai memberitahu ke pengguna progrm selesai

Pada baris 58 : Perintah break menghentikan eksekusi loop while yang mengelilingi kode ini, sehingga program keluar dari loop dan melanjutkan ke kode berikutnya.

Pada baris 59 : Bagian ini bekerja saat input pengguna tidak sesuai dengan angka 1-5, sehingga program akan menampilkan pesan kesalahan dan secara otomatis mengulang instruksi untuk meminta masukan yang benar.

Pada baris 60 :untuk menampilkan pesan peringatan di layar jika input yang dimasukkan pengguna tidak sesuai dengan pilihan menu yang tersedia.

Pada baris 62 :berfungsi sebagai pengecekan utama untuk memastikan bahwa fungsi main() hanya akan dijalankan apabila file tersebut dieksekusi secara langsung

Pada baris 63 : pemanggilan fungsi main() menjadi titik awal dimulainya seluruh alur logika program dari awal hingga selesai.

Outputnya:
<img width="1310" height="778" alt="Screenshot 2026-05-13 232347" src="https://github.com/user-attachments/assets/9777587c-122c-416d-a55f-99a3bc1e399f" />
 DIsini output keluar dan kita memilih 1 dimana diminta masukan nama atau id piring saya memakai P01 dan keluar piring P01 diaruh diatas selanjutnya kita diminta memilih 1-1 dan saya  memilij1 dan memasukkan id   P02 dimana P02 ditrauh diatas, dan masukkan lagi 1 dan disuruh masukann id lagi P03

<img width="1303" height="721" alt="Screenshot 2026-05-13 232431" src="https://github.com/user-attachments/assets/24f20837-2b39-435d-a3cf-1af4d770adac" />

DIsini piring P03 ditaruh diatas, dan keluar lagi ouput disuruh memilih dan saya memilih nomr 4 dimana keluar urutan piring dari atas sampai bawah yaitu P03 P02 P01 dan saya memilij nomor 3 dimana lihat piring teratas yang dimana yang teratas adalah P03,

<img width="1291" height="681" alt="Screenshot 2026-05-13 232510" src="https://github.com/user-attachments/assets/1093cc7d-be6e-4e75-83d6-573b7a92f3b8" />

Disini saya memilih nomor 2 yaitu ambil piring yang akan dipakai yaitu keluar piring P03 daimbil dari atas, dan pilih 2 dan keluar piring P02 diambil dari atas dan memilih 3 yaitu lihat piring teratas yaitu P01

<img width="1258" height="486" alt="Screenshot 2026-05-13 232521" src="https://github.com/user-attachments/assets/701862a8-dbfb-4eea-b7b7-9bbc05885da2" />

Disini kita memilih nomor 4 dimana lihat semua piring yaitu keluar dari atas sampe bawah yaitu P01 dan memilih 5 untuk keluar dan program selesai.

LINK YOUTUBE:



