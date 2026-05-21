# Simulasi BST implementasi nilai ujian dengan Binary Search Tree(BST) Dasar

Program yang saya gunakan menerapkan struktur data Binary Search Tree (BST) untuk mengelola data nilai ujian siswa secara terorganisasi. Melalui sistem pohon biner, setiap nilai yang diinput akan otomatis menempati posisi yang sesuai dengan prinsip dasar BST. Program ini menyediakan menu interaktif dengan berbagai fungsi, mulai dari penambahan data, penghapusan nilai spesifik, penghitungan total dan jumlah data, hingga penyajian daftar nilai secara berurutan (dari yang terkecil hingga terbesar). Pemanfaatan struktur BST ini menjamin efisiensi dalam manipulasi dan penayangan data tanpa memerlukan proses pengurutan manual kembali.

Pada program ini mempermudah dalam mengelola nilai ujian karena otomatisasi pengurutan data dari kecil ke besar, sehingga mempermudah analisis distribusi nilai serta pencarian nilai tertinggi dan terendah. Fitur hitung total dan jumlah data juga mempercepat penghitungan rata-rata kelas. Selain fungsi praktisnya, program ini menjadi media pembelajaran nyata untuk memahami konsep tree, inorder traversal, serta operasi insert dan delete dalam struktur data.

<img width="1200" height="819" alt="Screenshot 2026-05-21 151412" src="https://github.com/user-attachments/assets/8ad4f096-3b76-4d9f-aef9-df1335173169" />
<img width="1206" height="770" alt="Screenshot 2026-05-21 151429" src="https://github.com/user-attachments/assets/8b7bab06-c10d-469c-bc46-3d3942cb1cd4" />
<img width="1190" height="773" alt="Screenshot 2026-05-21 151444" src="https://github.com/user-attachments/assets/acd53858-514a-49f2-9b91-7f070ed47894" />
<img width="1208" height="754" alt="Screenshot 2026-05-21 151458" src="https://github.com/user-attachments/assets/dbb79d2f-3514-4644-ab29-1ed32010f7f5" />

Penjelasan kode:
Pada baris 1: Terdapat kelas node yang dimana kelas node ini adalah blok dasar dari struktur BST untuk setiap data pada Binary Search Tree.

Pada baris 2:  Terdapat Method `__init__` adalah konstruktor yang otomatis dijalankan saat objek node dibuat, untuk mengatur dan menyiapkan atribut‑atribut awal node tersebut.  

Pada baris 3: Variabel `score` digunakan untuk menyimpan nilai ujian yang dimasukkan ke dalam node, sehingga tiap node memiliki satu nilai yang menjadi data utama.  

Pada baris 4: Variabel `left` digunakan untuk menyimpan alamat anak kiri node, dan awalnya bernilai `None` karena node belum memiliki anak di cabang kiri.  

Pada baris 5: Variabel `right` digunakan untuk menyimpan alamat anak kanan node, dan awalnya juga `None` karena node belum memiliki anak di cabang kanan.
 
Pada baris 8: Kelas `BSTUjian` dibuat sebagai kelas utama yang berfungsi mengatur semua operasi Binary Search Tree. Di dalam kelas ini, berbagai metode seperti penambahan nilai, penghapusan nilai, penampilan data, dan perhitungan statistik didefinisikan sehingga program menjadi lebih terstruktur.

Pada baris 9: Constructor pada kelas `BSTUjian` secara otomatis dijalankan saat sebuah objek dari kelas tersebut dibuat. Di dalam constructor ini, kondisi awal BST disiapkan, sehingga pohon dapat langsung digunakan mengolah data nilai ujian sejak objek pertama kali dibentuk.

Pada baris 10: Variabel `root` berperan sebagai simpul akar utama dari BST, yang menjadi titik awal untuk semua operasi pada pohon. Nilai awalnya adalah `None` karena ketika program baru dijalankan, BST belum memiliki data atau nilai yang dimasukkan, sehingga posisi akar masih kosong.
 
Pada baris 12: Ini terdpat Method `insert` digunakan untuk menambahkan nilai baru ke dalam BST, sehingga nilai tersebut ditempatkan pada posisi yang tepat sesuai aturan pohon biner pencarian.  
 
Pada baris 13: Program mengecek apakah posisi node saat ini masih kosong, yaitu belum ada simpul di lokasi tersebut.  

Pada baris 14: Jika posisi node kosong, program membuat simpul baru yang berisi nilai yang dimasukkan oleh pengguna.  

Pada baris 15: Program membandingkan nilai yang ingin dimasukkan dengan nilai pada node (`root`) saat ini untuk menentukan arah penempatan.  
 
Pada baris 16: Jika nilai yang dimasukkan lebih kecil, data akan dimasukkan ke subtree kiri secara rekursif, sesuai aturan BST bahwa nilai yang lebih kecil ditempatkan di sebelah kiri.  

Pada baris 17: Jika nilai yang dimasukkan lebih besar dari nilai node saat ini.  

Pada baris 18: Program memasukkan data ke subtree kanan secara rekursif, karena dalam BST nilai yang lebih besar ditempatkan di sebelah kanan.  

Pada baris 19: Terdapat  Method ini mengembalikan `root` setelah proses penambahan selesai, sehingga struktur BST tetap terhubung dan siap untuk operasi berikutnya.

Pada baris 21: Method `delete` digunakan untuk menghapus nilai tertentu dari BST agar nilai yang tidak diperlukan dapat dikeluarkan dari struktur pohon.  
 
Pada baris 22- 23: Pada baris tersebut Jika pohon kosong atau node yang ingin dihapus tidak ditemukan, program langsung mengembalikan `root` tanpa melakukan perubahan apapun pada struktur BST.  
 
Pada baris 24 dan 25: Jika nilai yang dicari lebih kecil dari nilai pada `root` saat ini, proses pencarian dilanjutkan ke subtree kiri secara rekursif.  

Pada baris 26 dan 27: Jika nilai yang dicari lebih besar dari nilai pada `root`, pencarian dilanjutkan ke subtree kanan.  
  
Pada baris 28: Bagian ini dijalankan ketika node yang ingin dihapus berhasil ditemukan di dalam BST.  

Pada baris 29-30: Jika node yang dihapus tidak memiliki anak kiri, maka node tersebut digantikan oleh anak kanannya sehingga struktur pohon tetap terhubung.  
 
Pada baris 31 -32: Jika node tidak memiliki anak kanan, node tersebut digantikan oleh anak kirinya sebagai pengganti posisi node yang dihapus.  
 
Pada baris 33: Jika node memiliki dua anak, program mencari node terkecil di subtree kanan untuk menjadi pengganti node yang dihapus.  
 
Pada baris 34: Nilai node yang dihapus kemudian diganti dengan nilai dari node terkecil tersebut agar keterurutan BST tetap terjaga.  

Pada baris 35: Node pengganti tersebut kemudian dihapus dari posisi lamanya pada subtree kanan agar tidak terjadi duplikasi nilai di pohon.  
  
Pada baris 36: Setelah seluruh proses penghapusan selesai, method ini mengembalikan `root` agar struktur BST tetap utuh dan siap untuk operasi berikutnya.

Pada baris 38: Method bernama `_min_node` berfungsi untuk menemukan node yang memiliki nilai paling kecil dalam sebuah subtree.

Pada baris 39-40: Disini Selama masih ada node di sebelah kiri, program akan terus berpindah ke arah kiri. Hal ini dilakukan karena dalam struktur BST, nilai yang paling kecil selalu terletak di ujung paling kiri dari pohon.

Pada baris 41: Setelah mencapai node paling kiri (yang tidak memiliki anak kiri lagi), node tersebut dikembalikan sebagai nilai terkecil.

Pada baris 43: Terdapat  Method `inorder` didefinisikan untuk menampilkan seluruh data nilai ujian yang tersimpan dalam BST secara terurut dari yang terkecil hingga terbesar. Ini merupakan metode traversal standar pada BST.

Pada baris 44: Sebelum memproses lebih lanjut, program terlebih dahulu memeriksa apakah node yang sedang dikunjungi tidak bernilai kosong (None). Pengecekan ini penting untuk mencegah error saat mencoba mengakses atribut dari node yang tidak ada.

Pada baris 45: Disini Program memulai penelusuran dengan mengunjungi seluruh subtree bagian kiri terlebih dahulu secara rekursif. Hal ini karena dalam BST, semua nilai yang lebih kecil dari node saat ini berada di sisi kiri.

Pada baris 46: Setelah semua node di subtree kiri selesai diproses, barulah nilai dari node saat ini dicetak ke layar. Posisi pencetakan di antara traversal kiri dan kanan inilah yang membuat urutan keluaran menjadi terurut.

Pada baris 47: Terakhir, program melanjutkan penelusuran ke subtree bagian kanan secara rekursif. Nilai-nilai yang lebih besar dari node saat ini akan dicetak setelahnya, sehingga urutan ascending pun terbentuk secara alami.

Pada Baris 49: Method sum_nodes digunakan untuk menghitung total seluruh nilai ujian pada BST.

Padqa Baris 50–51: Disini Jika node kosong, maka program mengembalikan nilai 0.

Padaa Baris 52: Program menjumlahkan nilai node saat ini ditambah seluruh node kiri dan kanan secara rekursif.

Pada baris 54: Terdapat Method `count_nodes` berfungsi untuk menghitung seluruh node yang ada di dalam BST.

Pada baris 55-56: Program mengecek apakah node sedang kosong. Jika ya, maka dikembalikan nilai 0 sebagai dasar perhitungan.

Pada baris 57: Jika node tidak kosong, program menjumlahkan node saat ini (bernilai 1) dengan total node dari subtree kiri dan subtree kanan secara rekursif.

Pada baris 60: Fungsi `main` berperan sebagai inti program yang mengendalikan seluruh alur menu interaktif.

Pada baris 61: Program menciptakan sebuah objek BST baru dengan nama `bst` yang akan digunakan untuk mengelola data nilai ujian.

Pada baris 62: Variabel `pilih` disiapkan untuk menampung angka pilihan menu yang dimasukkan oleh pengguna.

Pada baris 63: Perulangan `while` digunakan agar menu terus muncul berulang kali hingga pengguna memilih opsi keluar dari program.

Pada Baris 64–69: Program menampilkan daftar menu seperti tambah nilai, tampilkan nilai, hapus nilai, menghitung total nilai, dan keluar program.

Pada Baris 71 : Terdapat Blok `try` digunakan untuk membungkus kode yang berpotensi menimbulkan error. Dalam hal ini, program akan mencoba membaca input pilihan menu dari pengguna.

Pada Baris 72: Program meminta pengguna mengetikkan pilihan melalui fungsi `input()`. Nilai yang dimasukkan kemudian dikonversi menjadi bilangan bulat dengan `int()` dan hasilnya disimpan ke dalam variabel `pilih`.

Pada Baris 73: Terdpat Bagian `except ValueError` akan aktif apabila pengguna memasukkan data yang bukan angka, seperti huruf, tanda baca, atau karakter khusus lainnya.

Pada Baris 74: Program menampilkan pesan "Input tidak valid!" sebagai pemberitahuan bahwa masukan pengguna tidak sesuai dengan yang diharapkan.

Pada Baris 75: Perintah `continue` berfungsi untuk melompat kembali ke awal perulangan menu, sehingga kode-kode setelahnya tidak akan dieksekusi.

Pada Baris 76: Program melakukan pengecekan apakah pilihan yang dimasukkan pengguna adalah angka 1, yaitu opsi untuk menambah nilai ujian.

Pada Baris 78: Blok `try` kembali digunakan untuk mengantisipasi kemungkinan kesalahan input ketika pengguna memasukkan nilai ujian yang akan ditambahkan.

Pada Baris 79: Program meminta pengguna mengetikkan nilai ujian. Input tersebut kemudian dikonversi menjadi bilangan bulat dan disimpan ke dalam variabel `x`.

Pada Baris80: Program memanggil method `insert()` untuk menyisipkan nilai yang telah dimasukkan ke dalam struktur BST. Setelah proses penambahan selesai, root dari BST diperbarui dengan hasil kembalian method tersebut.

Pada Baris 81: Program menampilkan pesan konfirmasi bahwa nilai berhasil ditambahkan ke dalam BST.

Pada Baris 82: Bagian `except ValueError` berfungsi untuk menangkap kesalahan yang terjadi jika pengguna memasukkan data yang bukan berupa angka, misalnya huruf atau simbol.

Pada Baris83:  Program mencetak pesan "Input tidak valid!" untuk memberitahukan pengguna bahwa masukan yang diberikan tidak sesuai.

Pada Baris 84: Program memeriksa apakah pilihan yang dipilih pengguna adalah angka 2, yaitu opsi untuk menampilkan data nilai ujian secara berurutan.

Pada Baris85:  Program mencetak teks "Nilai urut:" di layar. Parameter `end=""` membuat teks tersebut tidak diakhiri dengan baris baru, sehingga hasil pencetakan nilai berikutnya akan berada di baris yang sama.

Pada Baris 86:  Method `inorder()` dipanggil untuk menjalankan traversal secara inorder. Method ini akan mencetak semua nilai yang tersimpan dalam BST mulai dari yang terkecil hingga yang terbesar.

Pada Baris 87: Setelah seluruh nilai selesai dicetak, program mencetak baris kosong untuk memindahkan kursor ke baris baru, sehingga tampilan menjadi lebih rapi.

Pada Baris 88: Program melakukan pengecekan apakah pilihan pengguna adalah angka 3, yaitu opsi untuk menghapus nilai ujian dari BST.

Pada Baris89: disini terdapat lagi Blok `try` digunakan kembali untuk mengantisipasi kemungkinan terjadinya kesalahan saat pengguna memasukkan data.

Pada Baris 90 :Program meminta pengguna mengetikkan nilai ujian yang ingin dihapus dari dalam BST.

Pada Baris 91: Disni Program memeriksa terlebih dahulu yang dimana memastikan apakah BST dalam keadaan kosong atau tidak.

Pada Baris 92: Apabila BST ternyata kosong, program akan menampilkan pesan "BST kosong." karena tidak ada data yang bisa dihapus.

Pada Baris 93: Bagian `else` akan dijalankan jika BST ternyata tidak kosong dan memiliki satu atau lebih data.

Pada Baris 94: Program memanggil method `delete()` untuk melakukan proses penghapusan nilai yang telah dimasukkan oleh pengguna.

Pada Baris 95: Setelah proses penghapusan selesai, program menampilkan pesan konfirmasi bahwa nilai berhasil dihapus dari BST.

Pada Baris96 : Bagian `except ValueError` berfungsi untuk menangkap kesalahan jika pengguna memasukkan data yang bukan berupa angka.

Pada Baris 97: Program menampilkan pesan "Input tidak valid!" sebagai pemberitahuan bahwa masukan yang diberikan tidak sesuai.

Pada Baris 98: Program melakukan pengecekan apakah pilihan yang dimasukkan pengguna adalah angka 4, yaitu opsi untuk melihat ringkasan statistik dari data nilai ujian.

Pada Baris 99: Method sum_nodes() dipanggil untuk menjumlahkan seluruh nilai yang tersimpan di setiap node dalam BST. Hasil penjumlahan ini akan mewakili total keseluruhan nilai ujian.

Pada Baris100: Pada Method count_nodes() digunakan untuk menghitung berapa banyak node atau jumlah data yang terdapat dalam BST. Method ini akan mengembalikan angka yang merepresentasikan banyaknya nilai ujian yang tersimpan.

Pada Baris 101 : Program menampilkan kedua hasil perhitungan tersebut ke layar, yaitu total nilai dan jumlah node, sehingga pengguna dapat melihat ringkasan data secara lengkap.

Pada Baris 102: Dimana Program akan mengecek apakah pengguna memilih menu nomor 5.

Pada Baris 103 : Program menampilkan pesan "Selesai." sebelum keluar dari program.

Pada Baris104:  Blok `else` akan dieksekusi apabila pengguna memasukkan angka pilihan yang tidak termasuk dalam rentang 1 sampai 5, misalnya 6, 7, atau angka lainnya di luar menu yang tersedia.

Pada Baris 105: Program menampilkan pesan "Pilihan tidak valid!" untuk memberitahukan pengguna bahwa angka yang dimasukkan tidak sesuai dengan opsi menu yang disediakan.

Pada Baris 108:  Program melakukan pengecekan apakah file Python ini sedang dieksekusi secara langsung sebagai program utama, bukan diimpor sebagai modul ke dalam program lain.

Pada Baris 109: Apabila hasil pengecekan menunjukkan bahwa file dijalankan langsung, maka fungsi `main()` akan dipanggil untuk memulai menjalankan program BST nilai ujian.

Output:
<img width="479" height="762" alt="Screenshot 2026-05-21 180356" src="https://github.com/user-attachments/assets/6fba2afd-98d5-4ce0-8c07-5f8cb0efbdb8" />
Dimana output ini keluar sesuai yang kita masukkan disitem yaitu 5 pilihan disini kita pilih 1 dan sistem memintta kita memasukkan nnilai disini saya memasukkan nilai 7, dan disgtem mengembalikan ke pilihan 5 itu dan kita memilih 1 untuk memasukkan nilai disini memasukkan nilai 8, dan kembali lagi kita memilih 1 dan memasukkkan nilai 9 dan 9 ditambahkan.
<img width="489" height="670" alt="Screenshot 2026-05-21 180433" src="https://github.com/user-attachments/assets/dbf85dcf-058c-43d0-8725-b1f4d1f3a2a0" />
Disini kita memasukkan kembali pilihan 1 dan memasukkan nilai 6 dan kalo sudah memasukkan nilai kita memilih nomor 2 dimana akan menampilkan nilai  urut dari terkecil ke terbesar dimana disini keluar nilai urutnya: 6 7 8 9 .terus kita memilih nomor 3 dimana akan hapus nilai dan keluar nilai apa yang ingin kita hapus. Disini saya menghapus nilai 7 dan nilai 7 dihapus.

<img width="493" height="542" alt="Screenshot 2026-05-21 180446" src="https://github.com/user-attachments/assets/bc1158cf-af39-4cb6-ba15-a00335eab631" />

Lanjut saya memilih nomor 4 dimana nomor 4 ini akan muncul jumlah total dan banyak nilainya. Maka akan keluar total nilainya 23 dan jumlah nilainya 3 karena satu sudah dihapus. dan lannjut pilih 5 dimana 5 akan keluar sistem selesai.

Link Youtube:
https://youtu.be/eeohkA4LohA?si=q9qoK-Oz8MlKPYC-
