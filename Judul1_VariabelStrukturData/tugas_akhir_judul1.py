def tampilkan_menu():
    print("1. Address Memori Playlist")
    print("2. Address Tiap Lagu")
    print("3. Tambahkan Lagu ke playlist")
    print("4. Hapus Lagu dari Playlist")
    print("5. Keluar")

def main():
    playlist = ["sheesh", "really like you", "monsters", "we go up", "like that"]
    berjalan = True
    
    while berjalan:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih (1-5): "))
        except:
            print("Input salah!")
            continue

        if pilihan == 1:
            print(f"Playlist: {id(playlist)}")
        elif pilihan == 2:
            for i, lagu in enumerate(playlist):
                print(f"[{i}] '{lagu}': {hex(id(lagu))}")
        elif pilihan == 3:
            lagu = input("Lagu: ").strip()
            if lagu: playlist.append(lagu); print(f"[{len(playlist)-1}] {lagu}")
        elif pilihan == 4:
            if playlist:
                print(playlist)
                hapus = input("Hapus: ").strip()
                if hapus in playlist: playlist.remove(hapus); print("OK")
        elif pilihan == 5:
            print("Sistem dimatikan. Terima kasih")
            berjalan = False
            
        else:
            print("Pilihan menu tidak tersedia.")

if __name__ == "__main__":
    main()