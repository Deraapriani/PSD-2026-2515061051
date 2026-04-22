def tampilkan_menu():
    print("1. Address Memori Playlist")
    print("2. Address Tiap Lagu")
    print("3. Tambahkan Lagu ke playlist")
    print("4. Hapus Lagu dari Playlist")
    print("5. Keluar")

def main():
    playlist = ["sheesh", "really like you", "monsters", "we go up", "like that"]
    running = True
    
    while running:
        tampilkan_menu()
        try:
            choice = int(input("Pilih (1-5): "))
        except:
            print("Input salah!")
            continue

        if choice == 1:
            print(f"Playlist: {id(playlist)}")
        elif choice == 2:
            for i, lagu in enumerate(playlist):
                print(f"[{i}] '{lagu}': {hex(id(lagu))}")
        elif choice == 3:
            lagu = input("Lagu: ").strip()
            if lagu: playlist.append(lagu); print(f"[{(playlist)-1}] {lagu}")
        elif choice == 4:
            if playlist:
                print(playlist)
                hapus = input("Hapus: ").strip()
                if hapus in playlist: playlist.remove(hapus); print("OK")
        elif choice == 5:
            print("Sistem dimatikan. Terima kasih")
            berjalan = False
            
        else:
            print("Pilihan menu tidak tersedia.")

if __name__ == "__main__":
    main()