# Program Pengurutan Nilai Kuis Siswa dengan Bubble Sort

Program ini adalah penerapan dari algoritma Bubble Sort untuk menyusun data nilai kuis siswa dalam urutan menaik (dari nilai paling rendah hingga paling tinggi). Aplikasi ini menawarkan fitur input data yang interaktif, menunjukkan perbandingan urutan sebelum dan setelah proses pengurutan, serta menyajikan hasil akhir dalam format daftar peringkat yang terstruktur. Alat ini sangat berguna sebagai acuan dalam menyelesaikan tugas-tugas terkait struktur data maupun sistem pemeringkatan yang sederhana. 

Dalam notasi Big O, kompleksitas waktu Bubble Sort adalah (n^2). Hal ini menjelaskan mengapa poin "efisien untuk data kecil" sangat ditekankan, karena waktu eksekusi akan meningkat secara kuadratik seiring bertambahnya jumlah elemen n.

source code
<img width="970" height="594" alt="Screenshot 2026-04-29 143628" src="https://github.com/user-attachments/assets/c85d6528-c34f-4600-98fc-a904b6050931" />
<img width="901" height="606" alt="Screenshot 2026-04-29 143640" src="https://github.com/user-attachments/assets/72b93ebb-3af9-49d4-881d-40e2554e62fa" />
<img width="798" height="241" alt="Screenshot 2026-04-29 143647" src="https://github.com/user-attachments/assets/391f9463-ccb3-4a1a-8bd9-6e45bb601861" />
Penjelasan Kode Per Baris:

Baris 1: `def tukar(arr_nilai, arr_nama, i, j):`
Fungsi dari 'tukar' ini digunakan untuk dua array yang memiliki keterkaitan satu sama lain.
Baris 2: `temp_nilai = arr_nilai[i]`
Disini bisa dilihat dengan Menempatkan nilai dari indeks i ke dalam variabel sementara.
Baris 3: `arr_nilai[i] = arr_nilai[j]`
Memindahkan nilai dari indeks j ke indeks i.
Baris 4: `arr_nilai[j] = temp_nilai`
Menempatkan nilai yang disimpan sementara ke indeks j.
Baris 6: `temp_nama = arr_nama[i]`
Menempatkan nama dari indeks i ke dalam variabel sementara.
Baris 7: `arr_nama[i] = arr_nama[j]`
Memindahkan nama dari indeks j ke indeks i.
Baris 8: `arr_nama[j] = temp_nama`
Menempatkan nama yang disimpan sementara di posisi j.
Baris 10: `def bubble_sort(arr_nilai, arr_nama, n):`
Mendefinisikan fungsi untuk mengurutkan dengan metode bubble sort.
Baris 11: `for i in range(n - 1):`
Loop luar: Pada loop ini kita melakukan iterasi sebanyak n-1 kali.
Baris 12: `for j in range(n - i - 1):`
Loop dalam: Pada loop luar disini kita membandingkan elemen hingga elemen terakhir.
Baris 13: `if arr_nilai[j] < arr_nilai[j + 1]:`
Membandingkan nilai pada indeks j dengan j+1 (ascending).
Baris 14: `tukar(arr_nilai, arr_nama, j, j + 1)`
Memanggil fungsi tukar jika kondisinya memenuhi syarat.
Baris 16: `def main():`
Def main ini digunakan sebagai Definisi fungsi utama dari program.
Baris 17: `try:`
Memulai blok untuk menangani pengecualian.
Baris 18: `n = int(input("Masukkan jumlah siswa: "))`
Meminta input untuk jumlah siswa yang akan dimasukkan.
Baris 19: `except ValueError:`
Menangkap kesalahan ketika input tidak berupa angka.
Baris 20: `print("Input tidak valid! ")`
Menampilkan pesan kesalahan kepada pengguna.
Baris 21: `return`
Menghentikan eksekusi pada fungsi utama.
Baris 24: arr_nilai = []
Siapkan list kosong untuk menyimpan nilai
Baris 25: arr_nama = []
Siapkan list kosong untuk menyimpan nama
Baris 26: print("Silakan masukkan data siswa satu per satu:")
Berikan instruksi
Baris 27: for i in range(n):
Lakukan input sebanyak n kali
Baris 28: nama = input(f"Masukkan nama siswa ke-{i+1}: "). strip()
Minta input nama siswa
Baris 29: arr_nama. append(nama)
Simpan nama ke dalam list
Baris 31: while True:
Mulai loop untuk memvalidasi input nilai
Baris 32: try:
Awali proses validasi nilai
Baris 33: nilai = int(input(f"Masukkan nilai kuis {nama}: "))
Minta input nilai kuis
Baris 34: arr_nilai. append(nilai)
Simpan nilai ke dalam list
Baris 35: break
Akhiri loop validasi
Baris 36: except ValueError:
Tangani kesalahan input jika bukan angka
Baris 37: print("Nilai harus berupa angka! ")
Pesan kesalahan untuk nilai
Baris 40: print(f"Data nilai kuis sebelum diurutkan:")
Tampilkan judul data awal
Baris 41: for i in range(n):
Lakukan iterasi untuk menampilkan data awal
Baris 42: print(f"{arr_nama[i]}: {arr_nilai[i]}")
Tampilkan nama dan nilai
Baris 44: bubble_sort(arr_nilai, arr_nama, n)
Laksanakan pengurutan bubble sort
Baris 46: print("Data nilai kuis setelah diurutkan:")
Judul hasil pengurutan
Baris 47: for i in range(n):
Lakukan iterasi untuk menampilkan hasil
Baris 48: print(f"{i+1}. {arr_nama[i]}: {arr_nilai[i]}")
Tampilkan urutan, nama, dan nilai
Baris 51: if __name__ == "__main__":
Periksa apakah file dijalankan secara langsung
Baris 52: main()
Panggil fungsi utama
