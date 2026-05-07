def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = ["dalla dalla", "monsters", "wannabe", "icy" , "dalla dalla" , "choom" , "psycho", "like that", "i love 3000"]
    n = len(data)
    print(f"Playlist lagu: {data}")
    while True:
        try:
            target = input("Masukkan judul lagu yang akan dicari: ")
            break
        except:
            print("Input tidak valid, silakan masukkan judul lagu!")
    
    counter = sequential_search(data, n, target)
    if counter > 0:
        print(f"Lagu '{target}' ditemukan sebanyak {counter} kali.")
    else:
        print(f"Lagu '{target}' tidak ditemukan.")


if __name__ == "__main__":
    main()