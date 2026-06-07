# Implementasi Hash Map Separate Chaining pada Sistem Daftar Kontak Telepon (Nama → Nomor Telepon)

Program ini mengimplementasikan struktur data Hash Map berbasis Separate Chaining untuk mengelola daftar kontak telepon, di mana nama berfungsi sebagai key dan nomor telepon sebagai value. Penentuan posisi penyimpanan data dilakukan melalui fungsi hash. Jika terjadi collision (dua data memiliki indeks yang sama), Separate Chaining akan menyelesaikannya dengan menyusun data tersebut ke dalam linked list pada indeks yang bersangkutan.

Penggunaan Hash Map Separate Chaining membantu pengelolaan data kontak menjadi lebih cepat dan terstruktur. Data dapat dicari, ditambahkan, maupun dihapus dengan efisien, serta tetap dapat menangani collision dengan baik melalui linked list. Struktur ini cocok digunakan pada aplikasi buku telepon atau sistem manajemen kontak.

<img width="1203" height="839" alt="Screenshot 2026-06-07 200539" src="https://github.com/user-attachments/assets/5d927870-6470-4c59-8ce4-5c1a52da3c08" />
<img width="1199" height="773" alt="Screenshot 2026-06-07 200558" src="https://github.com/user-attachments/assets/9fc5a358-0852-4ac5-a624-3a6f1f18106d" />
<img width="1190" height="782" alt="Screenshot 2026-06-07 200612" src="https://github.com/user-attachments/assets/bec3b35b-5cc0-4eeb-b1f9-f11eb11194bf" />
<img width="1188" height="808" alt="Screenshot 2026-06-07 200627" src="https://github.com/user-attachments/assets/952b6d8a-48bd-40fb-9567-56828af48e5a" />
Penjelasan kode perbaris:
pada baris 1 : merupakan elemen dasar untuk menyusun data dalam linked list. Struktur ini digunakan pada setiap bucket hash table untuk mendukung implementasi Hash Map dengan teknik Separate Chaining.

Pada baris 2: mendefinisikan metode __init__ yang berfungsi sebagai konstruktor otomatis saat objek Node diinisialisasi. Metode ini bertanggung jawab untuk mempersiapkan dan menetapkan atribut awal dari node, yaitu key, value, dan next.

Pada baris 3: Variabel self.key digunakan untuk menyimpan nama kontak yang dimasukkan ke dalam node, sehingga tiap node memiliki satu nama yang menjadi kunci utama untuk pencarian.

Pada baris 4: Variabel self.value digunakan untuk menyimpan nomor telepon yang dimasukkan ke dalam node, sehingga tiap node memiliki satu nomor telepon sebagai data yang terkait dengan nama kontak.

Pada baris 5: Variabel self.next digunakan untuk menyimpan referensi ke node berikutnya dalam linked list, awalnya bernilai None karena node baru belum terhubung ke node lain.

Pada baris 8: Pada baris  ini Terdapat kelas HashMapKontak yang dimana kelas ini adalah struktur utama Hash Map yang menggunakan separate chaining untuk mengelola daftar kontak telepon.

Pada baris 9: Pada baris ini ada  method __init__ adalah konstruktor yang otomatis dijalankan saat objek HashMapKontak dibuat, untuk mengatur ukuran hash table dan membuat tabel kosong.

Pada baris 10: Variabel self.SIZE digunakan untuk menyimpan jumlah bucket (indeks) dalam hash table, default-nya adalah 10.

Pada baris 11: Variabel self.table digunakan untuk menyimpan array (list) yang berisi bucket-bucket hash table, awalnya semua elemen bernilai None karena belum ada data.

Pada baris 14: Terdapat method hash_function adalah fungsi yang mengubah nama kontak (string) menjadi indeks bucket (angka) dalam hash table.

Pada baris 15: Variabel total digunakan untuk menyimpan hasil penjumlahan nilai dari setiap karakter dalam nama kontak, awalannya 0.

Pada baris 16:  terdapat Loop for char in key digunakan untuk mengakses setiap karakter dalam string nama kontak secara berurutan.

Pada baris 17: total += ord(char) digunakan untuk menambahkan nilai ASCII dari karakter saat ini ke variabel total.

Pada baris 18 : return total % self.SIZE digunakan untuk mengembalikan indeks akhir dengan mengambil sisa pembagian total nilai ASCII dengan SIZE, sehingga indeks berada dalam range valid.

Pada baris 21: Terdapat method insert adalah fungsi untuk menambahkan kontak baru atau update kontak yang sudah ada berdasarkan nama.

Pada baris 22: terdpat  index = self.hash_function(key) digunakan untuk menghitung indeks bucket tempat kontak akan disimpan menggunakan fungsi hash.

Pada baris 23: current = self.table[index] digunakan untuk mengambil node pertama di bucket pada indeks tersebut (bisa None jika bucket kosong).

Pada baris 25: Loop while current is not None digunakan untuk menelusuri linked list di bucket tersebut mencari kontak dengan nama yang sama.

Pada baris 26: if current.key == key: digunakan untuk memeriksa apakah node saat ini memiliki nama kontak yang sama dengan yang ingin ditambahkan.

Pada baris 27: Jika nama sama, current.value = value digunakan untuk update nomor telepon kontak yang sudah ada

Pada baris 28 : return untuk mengembalikan ke fungsi

Pada baris 29: current = current.next digunakan untuk pindah ke node berikutnya dalam linked list jika nama belum ditemukan.

Pada baris 31: new_node = Node(key, value) digunakan untuk membuat node baru jika kontak dengan nama tersebut belum ada 

Pada baris 29: new_node.next = self.table[index] digunakan untuk membuat node baru menunjuk ke node pertama yang sebelumnya ada di bucket ini.

Pada baris 30: self.table[index] = new_node digunakan untuk membuat node baru menjadi node pertama di bucket tersebut

Pada baris 36: Terdapat method search adalah fungsi untuk mencari kontak berdasarkan nama dan mengembalikan node jika ditemukan.

Pada baris 37: index = self.hash_function(key) digunakan untuk menghitung indeks bucket tempat kontak mungkin tersimpan.

Pada baris 38: current = self.table[index] digunakan untuk mengambil node pertama di bucket pada indeks tersebut.

Pada baris 40: Loop while current is not None digunakan untuk menelusuri linked list di bucket tersebut mencari nama kontak yang cocok.

Pada baris 41: if current.key == key: digunakan untuk memeriksa apakah node saat ini memiliki nama kontak yang dicari.

Pada baris 42: Jika nama ditemukan, return current digunakan untuk mengembalikan node tersebut (berisi key dan value).

Pada baris 43: current = current.next digunakan untuk pindah ke node berikutnya jika nama belum ditemukan

Pada baris 45: Terdapat return None digunakan untuk mengembalikan None jika kontak dengan nama tersebut tidak ditemukan setelah menelusuri seluruh linked list.

Pada baris 48: Terdapat method remove_key adalah fungsi untuk menghapus kontak berdasarkan nama dari hash table.

Pada baris 49: index = self.hash_function(key) digunakan untuk menghitung indeks bucket tempat kontak yang akan dihapus berada.

Pada baris 50: current = self.table[index] digunakan untuk mengambil node pertama di bucket pada indeks tersebut.

Pada baris 51: prev = None digunakan untuk menyimpan node sebelumnya dalam linked list, awalnya None karena belum ada node sebelumnya.

Pada baris 53: Loop while current is not None digunakan untuk menelusuri linked list mencari kontak dengan nama yang akan dihapus.

Pada baris 54: if current.key == key: digunakan untuk memeriksa apakah node saat ini adalah kontak yang akan dihapus.

Pada baris 55: if prev is None: digunakan untuk memeriksa apakah node yang akan dihapus adalah node pertama di bucket.

Pada baris 56: Jika node pertama, self.table[index] = current.next digunakan untuk membuat node berikutnya menjadi node pertama di bucket tersebut.

Pada baris 57: else: untuk kasus node yang dihapus bukan node pertama.

Pada baris 58: prev.next = current.next digunakan untuk melewati node yang dihapus dengan membuat node sebelumnya menunjuk ke node setelah node yang dihapus.

Pada baris 59: return True digunakan untuk mengembalikan True jika kontak berhasil dihapus.

Pada baris 60: prev = current dan current = current.next digunakan untuk maju ke node berikutnya dalam linked list.

Pada baris 64: return False digunakan untuk mengembalikan False jika kontak tidak ditemukan setelah menelusuri seluruh linked list.

Pada baris67: Terdapat method display adalah fungsi untuk menampilkan semua kontak dalam hash table secara lengkap.

Pada baris 68:  digunakan untuk mencetak judul daftar kontak.

Pada baris 69:Pada baris ini terdapat  for i in range(self.SIZE):hang  digunakan untuk loop setiap bucket dari indeks 0 sampai SIZE-1.

Pada baris70: print(f"Index {i}: ", end="") digunakan untuk mencetak nomor index bucket saat ini.

Pada baris 71: current = self.table[i] digunakan untuk mengambil node pertama di bucket ke-i.

Pada baris 73: Loop while current is not None digunakan untuk menelusuri semua node dalam linked list di bucket tersebut.

Pada baris 74: pada baris ini digunakan untuk mencetak setiap kontak dalam format [nama : nomor].

Pada baris 75: current = current.next digunakan untuk maju ke node berikutnya dalam linked list.

Pada baris 77: print("None") digunakan untuk mencetak akhir linked list setelah semua node dalam bucket sudah dicetak.

Pada baris 80: Terdapat fungsi main adalah program utama yang menjalankan contoh penggunaan Hash Map Kontak.

Pada baris 81: kontak = HashMapKontak() digunakan untuk membuat objek HashMap untuk daftar kontak dengan ukuran default 10.

Pada baris 84 - 87: pada baris ini kontak.insert digunakan untuk menambahkan 4 kontak baru ke dalam hash table (ryujin, ahyeon, ruka, love).

Pada baris 89: kontak.display() digunakan untuk menampilkan semua kontak yang sudah dimasukkan.

Pada baris 92: di baris ini kita akan mencari nama = "ruka" digunakan untuk menyimpan nama kontak yang akan dicari.

Pada baris 91: hasil = kontak.search(nama) digunakan untuk mencari kontak dengan nama "ruka" dan menyimpan hasilnya.

Pada baris 95: if hasil is not None: digunakan untuk memeriksa apakah kontak ditemukan.

Pada baris 96: Pada baris  ini digunakan untuk mencetak nomor telepon jika kontak ditemukan.

Pada baris  97: else: dan print digunakan untuk mencetak pesan jika kontak tidak ditemukan.

Pada baris 100: pada baris ini kontak.remove_key("ryujin") digunakan untuk menghapus kontak bernama "ryujin" dari hash table.

Pada baris 103: print("\nSetelah kontak ryujin dihapus:") digunakan untuk mencetak pesan sebelum menampilkan daftar kontak setelah penghapusan.

Pada baris 104: kontak.display() digunakan untuk menampilkan daftar kontak setelah kontak "ryujin" dihapus.

Pada baris 107: if __name__ == "__main__": digunakan untuk memeriksa apakah file ini dijalankan sebagai program utama.

Pada baris 106: main() digunakan untuk memanggil fungsi main sehingga program mulai berjalan.

Outputnya 
<img width="656" height="754" alt="Screenshot 2026-06-07 204649" src="https://github.com/user-attachments/assets/c33922c1-fa5a-4268-b79d-844b9141397e" />

Penjelasan outputnya :  menunjukkan bahwa data kontak berhasil disimpan ke dalam hash table pada index yang berbeda-beda sesuai hasil fungsi hash. Setiap kontak hanya menempati satu bucket, sehingga pada tampilan awal semua data masih terpisah dan belum terjadi collision.

Baris `Nomor telepon ruka: 083456789012` menandakan bahwa program berhasil menemukan kontak dengan nama **ruka** lalu menampilkan nomor teleponnya. Ini berarti proses pencarian data berjalan dengan benar.

Setelah kontak **ryujin** dihapus, tampilan hash table menunjukkan bahwa index tempat ryujin sebelumnya tersimpan berubah menjadi `None`. Hal ini membuktikan bahwa proses penghapusan data berhasil, sementara kontak lain seperti **ahyeon**, **ruka**, dan **love** tetap ada.

Link Youtube:
https://youtu.be/Pt_EDygkixI
