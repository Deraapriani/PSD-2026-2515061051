judul Program : Manajemen Playlist Lagu dengan ID Memori

Deskripsi Singkat : Program ini dirancang dengan sederhana untuk mengatur playlist musik menggunakan Python. Pengguna akan dapat melihat keseluruhan ID memori dari playlist, menampilkan alamat memori (hex) setiap lagu yang ada, menambahkan lagu baru ke bagian akhir daftar, menghapus lagu berdasar nama, atau keluar dari aplikasi melalui menu interaktif yang menggunakan loop while.

Program ini memanfaatkan struktur data list Python sebagai tempat penyimpan utama playlist yang bersifat fleksibel. Operasi dasar CRUD diimplementasikan melalui fungsi bawaan seperti `append()` untuk menambah, `remove()` untuk menghapus, dan `enumerate()` untuk melakukan penelusuran dengan indeks. Keunikan dari program ini adalah penggunaan fungsi `id()` dan `hex(id())` untuk menunjukkan lokasi memori objek, yang bermanfaat untuk memahami konsep pengalamatan memori dan identitas objek dalam Python. Susunan program yang modular dengan fungsi terpisah (`tampilkan_menu()` dan `main()`) membuat kode lebih mudah untuk dibaca serta dirawat.

 Source Code:<img width="968" height="504" alt="Screenshot 2026-04-22 150726" src="https://github.com/user-attachments/assets/b4dfc80d-b6ba-42e2-bc36-b2d416edf30f" />


<img width="968" height="471" alt="Screenshot 2026-04-22 150802" src="https://github.com/user-attachments/assets/51ad287c-02d3-48e4-abca-398884423a00" />

<img width="708" height="189" alt="Screenshot 2026-04-22 150820" src="https://github.com/user-attachments/assets/88fb2481-54e5-4e41-afbc-2ed140cd288e" />

