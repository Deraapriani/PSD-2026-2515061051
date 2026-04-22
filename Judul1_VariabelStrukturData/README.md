judul Program : Manajemen Playlist Lagu dengan ID Memori

Deskripsi Singkat : Program ini dirancang dengan sederhana untuk mengatur playlist musik menggunakan Python. Pengguna akan dapat melihat keseluruhan ID memori dari playlist, menampilkan alamat memori (hex) setiap lagu yang ada, menambahkan lagu baru ke bagian akhir daftar, menghapus lagu berdasar nama, atau keluar dari aplikasi melalui menu interaktif yang menggunakan loop while.

Program ini memanfaatkan struktur data list Python sebagai tempat penyimpan utama playlist yang bersifat fleksibel. Operasi dasar CRUD diimplementasikan melalui fungsi bawaan seperti `append()` untuk menambah, `remove()` untuk menghapus, dan `enumerate()` untuk melakukan penelusuran dengan indeks. Keunikan dari program ini adalah penggunaan fungsi `id()` dan `hex(id())` untuk menunjukkan lokasi memori objek, yang bermanfaat untuk memahami konsep pengalamatan memori dan identitas objek dalam Python. Susunan program yang modular dengan fungsi terpisah (`tampilkan_menu()` dan `main()`) membuat kode lebih mudah untuk dibaca serta dirawat.

 Source Code:
