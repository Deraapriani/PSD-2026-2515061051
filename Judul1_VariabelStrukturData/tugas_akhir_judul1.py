def tampilkan_menu():
    print("1. Cek Address memori rak")
    print("2. Cek Address Tiap Loker")
    print("3. Isi Barang ke Semua Slot")
    print("4. Keluar")

def main():
    loker = [0] * 5
    berjalan = True
    while berjalan:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-4): "))
        except ValueError:
            print("Error: Harap masukkan angka yang valid!")
            continue

        if pilihan == 1:
            print(f"Alamat memori objek Rak Loker: {id(loker)}")

        elif pilihan == 2:
            print("Detail Alamat Memori tiap Slot:")
            for i in range(len(loker)):
                print(f"Slot [{i}] | Isi: {loker[i]} | Address: {hex(id(loker[i]))}")

        elif pilihan == 3:
            print("Silakan masukkan ID Barang (angka) untuk 5 slot:")
            for i in range(5):
                while True:
                    try:
                        loker[i] = int(input(f"ID Barang untuk Slot ke-{i}: "))
                        break
                    except ValueError:
                        print("Input tidak valid! Masukkan angka ID Barang.")
            
            print(f"Status Loker Terbaru: {loker}")

        elif pilihan == 4:
            print("Sistem dimatikan. Terima kasih")
            berjalan = False
        
        else:
            print("Pilihan menu tidak tersedia.")

if __name__ == "__main__":
    main()