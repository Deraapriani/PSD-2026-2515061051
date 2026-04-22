#Manajemen Playlist Lagu dengan ID Memori

Deskripsi Singkat : Program  manajemen ini dirancang dengan sederhana untuk mengatur playlist musik menggunakan Python. Dimana kita sebagai pengguna akan dapat melihat keseluruhan ID memori dari playlist, menampilkan alamat memori (hex) setiap lagu yang ada, menambahkan lagu baru ke bagian akhir daftar, menghapus lagu berdasar nama, atau keluar dari aplikasi melalui menu interaktif yang menggunakan loop while.

Program ini memanfaatkan struktur data list Python sebagai tempat penyimpan utama playlist yang bersifat fleksibel. Operasi dasar CRUD diimplementasikan melalui fungsi bawaan seperti `append()` untuk menambah, `remove()` untuk menghapus, dan `enumerate()` untuk melakukan penelusuran dengan indeks. Keunikan dari program ini adalah penggunaan fungsi `id()` dan `hex(id())` untuk menunjukkan lokasi memori objek, yang bermanfaat untuk memahami konsep pengalamatan memori dan identitas objek dalam Python. Susunan program yang modular dengan fungsi terpisah (`tampilkan_menu()` dan `main()`) membuat kode lebih mudah untuk dibaca serta dirawat.

Sorce code
<img width="1168" height="523" alt="Screenshot 2026-04-22 160547" src="https://github.com/user-attachments/assets/c43b38a4-6abe-449e-9cae-42fad06c4532" />
<img width="1104" height="473" alt="Screenshot 2026-04-22 160556" src="https://github.com/user-attachments/assets/7c78828b-c25e-497a-93cb-73dc4e731b9b" />
<img width="1067" height="241" alt="Screenshot 2026-04-22 160612" src="https://github.com/user-attachments/assets/c82bae28-14ff-4e56-a8f6-594884f63421" />

BARIS 1: Membuat fungsi `tampilkan_menu()` tanpa parameter input. Fungsi ini bertanggung jawab menampilkan lima opsi menu berulang setiap kali loop utama berjalan.

BARIS 2: Menampilkan teks pilihan pertama "Address Memori Playlist" di terminal. Menu ini memungkinkan pengguna melihat ID memori dari seluruh object list playlist.

BARIS 3: Menampilkan teks pilihan kedua "Address Tiap Lagu". Fitur tersebut akan memperlihatkan alamat memori masing-masing lagu dalam playlist menggunakan format hex.

BARIS 4: Menampilkan teks pilihan ketiga "Tambahkan Lagu ke playlist". Memberikan kemampuan bagi user untuk menambahkan lagu baru di ujung daftar playlist.

BARIS 5: Menampilkan teks pilihan keempat "Hapus Lagu dari Playlist". Menyediakan fungsi penghapusan lagu berdasarkan nama yang diinputkan pengguna.

BARIS 6: Menampilkan teks pilihan kelima "Keluar". Pilihan untuk menutup aplikasi dengan pesan selamat tinggal yang sopan.

BARIS 7 : Baris kosong yang digunakan sebagai pembatas visual antar fungsi untuk mempermudah pembacaan struktur kode.

BARIS 8: Membuat fungsi utama `main()` yang mengandung semua logika inti dari aplikasi manajemen playlist.

BARIS 9: Menginisialisasi variabel `playlist` dengan tipe list Python berisi lima string nama lagu awal yang sudah tersedia dalam daftar.

BARIS 10: Mendeklarasikan variabel boolean `running = True` sebagai penanda kontrol untuk mengatur berjalannya loop while utama program.

BARIS 12: Mengaktifkan loop while utama yang terus berjalan selama variabel `running` bernilai `True`, menghasilkan menu yang interaktif dan berulang.

BARIS 13: Memanggil fungsi `tampilkan_menu()` untuk menunjukkan semua pilihan menu pada setiap iterasi dari loop utama.

BARIS 14: Memperkenalkan struktur try-except yang bertujuan untuk melindungi program dari kesalahan konversi data saat menerima input dari pengguna.

BARIS 15: Meminta pengguna untuk memasukkan angka melalui keyboard dengan panduan "Pilih (1-5): ", mengubah input berupa string menjadi integer menggunakan `int()`, kemudian menyimpannya dalam variabel `choice`.

BARIS 16: Membuka blok except yang secara otomatis menangkap kesalahan `ValueError` saat pengguna memberikan huruf atau simbol yang bukan angka.

BARIS 17: Menampilkan pesan kesalahan "Input salah! " ketika fungsi `int()` gagal untuk mengonversi input yang dimasukkan.

BARIS 18: Instruksi `continue` yang langsung membawa eksekusi kembali ke awal loop while, mengesampingkan seluruh blok kondisi if-elif di bagian bawah.

BARIS 19: Baris kosong berfungsi sebagai pemisah visual antara kelompok perintah dalam kode.

BARIS 20: Pemeriksaan if awal yang memverifikasi apakah nilai `choice` adalah 1 untuk menunjukkan alamat memori dari daftar playlist.

BARIS 21: Memformat keluaran dengan f-string untuk menampilkan lokasi memori objek `playlist` menggunakan fungsi bawaan `id(playlist)` yang memberikan angka unik sebagai penanda posisi memori.

BARIS 22: Kondisi elif pertama yang memeriksa `choice == 2`, mengatur proses untuk menampilkan informasi memori dari setiap lagu satu per satu.

BARIS 23: Loop menggunakan `enumerate` yang secara bersamaan menawarkan indeks `i` dan nilai `lagu` untuk setiap item dalam daftar `playlist`.

BARIS 24: Menghasilkan keluaran yang terformat `[indeks] 'nama_lagu': 0xalamat_hex` melalui `hex(id(lagu))`, yang mengubah ID memori dalam bentuk integer menjadi format heksadesimal yang lebih mudah dimengerti.

BARIS 25: Blok elif kedua (`choice == 3`) yang mengaktifkan proses penambahan lagu baru ke dalam daftar playlist.

BARIS 26: Mengumpulkan input untuk nama lagu tambahan, dan fungsi `. strip()` menghilangkan spasi yang ada di awal dan akhir string yang dimasukkan oleh pengguna.

BARIS 27: KESALAHAN FATAL - `if lagu: playlist. append(lagu); print(f"[{(playlist)-1}] {lagu}")`
- Kesalahan sintaks: Ekspresi `{(playlist)-1}` tidak valid karena operasi pengurangan tidak berlaku untuk list
- Solusi yang benar: `print(f"[{len(playlist)-1}] {lagu}")` untuk menampilkan indeks posisi lagu yang baru saja dimasukkan

BARIS 28: Blok elif ketiga (`choice == 4`) yang bertanggung jawab atas tindakan penghapusan lagu dari daftar playlist.

BARIS 29: Validasi defensif yang memastikan bahwa `playlist` tidak kosong sebelum pengulangan, untuk menghindari kesalahan saat runtime pada struktur data yang kosong.

BARIS 30: Menampilkan seluruh isi dari `playlist` secara langsung agar pengguna dapat mengenali lagu yang ingin dihapus.

BARIS 31: Memperoleh input nama lagu yang ingin dihapus, dan `. strip()` diterapkan kembali untuk menstandarkan input yang diberikan oleh pengguna.

BARIS 32: Operator `in` memastikan ada elemen `hapus` dalam struktur `playlist`. Apabila ditemukan, fungsi `remove()` menghapus kemunculan pertama yang sama disertai dengan notifikasi konfirmasi "OK".

BARIS 33: Kondisi elif ke-4 (`choice == 5`) yang bertanggung jawab atas penghentian aplikasi.

BARIS 34: Mengirimkan pesan penutup "Sistem dimatikan. Terima kasih" sebagai ucapan selamat tinggal yang resmi kepada pengguna.

BARIS 35: BUG KRITIS 2 - `berjalan = False` mengacu pada variabel yang tidak ada
- Perbaikan yang tepat: `running = False` untuk menghentikan loop while secara normal

BARIS 36: Baris kosong berfungsi sebagai pemisah visual antara bagian-bagian dari kode program.

BARIS 37: Kondisi else terakhir yang menangkap input tidak valid seperti 0, 6, 7, angka negatif, dan masukan lainnya.BARIS 38: Mengeluarkan pesan kesalahan "Pilihan menu tidak tersedia. " untuk setiap masukan di luar rentang 1-5.

BARIS 39: Baris kosong yang menutup blok kode dengan rapi.

BARIS 40: Standar praktik Python `if __name__ == "__main__":` yang memastikan fungsi `main()` hanya dijalankan ketika file dieksekusi secara langsung (bukan diimpor sebagai modul).

BARIS 41: Memanggil fungsi utama `main()` sebagai titik awal jalannya program dari awal hingga akhir.

Output Program:
<img width="426" height="183" alt="Screenshot 2026-04-22 173834" src="https://github.com/user-attachments/assets/97ae5e08-a3b8-4ee6-b8d1-27466ec0e3ed" />

ketika kita ketik 1 munculaddres memori playlist, 1 digunakan untuk menampilkan alamat memori dari objek daftar putar. Angka 2158183298816 menunjukkan lokasi tertentu di RAM di mana struktur data ini disimpan. Alamat memori ini tetap sama selama program berjalan, meskipun isi dalam daftar tersebut mengalami perubahan.

<img width="445" height="155" alt="Screenshot 2026-04-22 173847" src="https://github.com/user-attachments/assets/2e291e20-a281-445e-bd1a-80c8f857ab68" />

Bagian ini mengungkapkan bahwa setiap lagu memiliki 'ruang penyimpanan' yang unik. Kode hex(id(lagu)) digunakan untuk menunjukkan alamat yang spesifik. Hal ini menjelaskan bahwa playlist kita sebetulnya mirip dengan buku alamat; ia tidak menyimpan lagu secara fisik, melainkan hanya mencatat daftar koordinat atau petunjuk tentang lokasi setiap lirik lagu di dalam sistem. parafrasekan bahasa mudah

<img width="383" height="208" alt="Screenshot 2026-04-22 173902" src="https://github.com/user-attachments/assets/bc125f81-d2ef-4626-bc25-23080a21aa68" />

dimana pada kode ini ketika kita ketik3 muncul outputnya yaitu saat menambahkan lagu baru "better up" program langsung menambahkan ke list. output better up menunjukan bahwa lagu berhasil masuk ke indeks 5 data ke 6.

<img width="888" height="95" alt="Screenshot 2026-04-22 173922" src="https://github.com/user-attachments/assets/4b627d58-66c6-4d66-96a6-805701d930ba" />

Ketika kita memasukan angka 4  maka program menampilkan isi list terbaru, lalu kita diminta input judul yang mau kita hapus dilist sebelumnya. Disini kita meminta hapus lagu "like that" dengan menggunakan metode .remove() yg mencari berdasarkan nilai bukan indeks.


<img width="437" height="241" alt="Screenshot 2026-04-22 173928" src="https://github.com/user-attachments/assets/21cd91da-7ad5-4316-a120-d3d23aa3c729" />

Terakhir ketika kita masukan angka 5 maka program akan mencetak dan menghentikan program.

Link Youtube:
