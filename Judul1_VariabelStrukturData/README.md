judul Program : Manajemen Playlist Lagu dengan ID Memori

Deskripsi Singkat : Program ini dirancang dengan sederhana untuk mengatur playlist musik menggunakan Python. Pengguna akan dapat melihat keseluruhan ID memori dari playlist, menampilkan alamat memori (hex) setiap lagu yang ada, menambahkan lagu baru ke bagian akhir daftar, menghapus lagu berdasar nama, atau keluar dari aplikasi melalui menu interaktif yang menggunakan loop while.

Program ini memanfaatkan struktur data list Python sebagai tempat penyimpan utama playlist yang bersifat fleksibel. Operasi dasar CRUD diimplementasikan melalui fungsi bawaan seperti `append()` untuk menambah, `remove()` untuk menghapus, dan `enumerate()` untuk melakukan penelusuran dengan indeks. Keunikan dari program ini adalah penggunaan fungsi `id()` dan `hex(id())` untuk menunjukkan lokasi memori objek, yang bermanfaat untuk memahami konsep pengalamatan memori dan identitas objek dalam Python. Susunan program yang modular dengan fungsi terpisah (`tampilkan_menu()` dan `main()`) membuat kode lebih mudah untuk dibaca serta dirawat.

Sorce code
<img width="1168" height="523" alt="Screenshot 2026-04-22 160547" src="https://github.com/user-attachments/assets/c43b38a4-6abe-449e-9cae-42fad06c4532" />
<img width="1104" height="473" alt="Screenshot 2026-04-22 160556" src="https://github.com/user-attachments/assets/7c78828b-c25e-497a-93cb-73dc4e731b9b" />
<img width="1067" height="241" alt="Screenshot 2026-04-22 160612" src="https://github.com/user-attachments/assets/c82bae28-14ff-4e56-a8f6-594884f63421" />


