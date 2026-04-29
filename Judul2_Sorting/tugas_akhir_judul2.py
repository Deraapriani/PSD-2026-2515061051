def tukar(arr_nilai, arr_nama, i, j):
    temp_nilai = arr_nilai[i]
    arr_nilai[i] = arr_nilai[j]
    arr_nilai[j] = temp_nilai
    
    temp_nama = arr_nama[i]
    arr_nama[i] = arr_nama[j]
    arr_nama[j] = temp_nama

def bubble_sort(arr_nilai, arr_nama, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr_nilai[j] < arr_nilai[j + 1]:  
                tukar(arr_nilai, arr_nama, j, j + 1)

def main():
    try:
        n = int(input("Masukkan jumlah siswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr_nilai = []
    arr_nama = []
    print("Masukkan data siswa satu per satu:")
    for i in range(n):
        nama = input(f"Nama siswa ke-{i+1}: ").strip()
        arr_nama.append(nama)
        
        while True:
            try:
                nilai = int(input(f"Nilai kuis {nama}: "))
                arr_nilai.append(nilai)
                break
            except ValueError:
                print("Nilai nya harus angka!")

    print(f"Data nilai kuis sebelum diurutkan:")
    for i in range(n):
        print(f"{arr_nama[i]}: {arr_nilai[i]}")
    
    bubble_sort(arr_nilai, arr_nama, n)
    
    print("Data nilai kuis setelah diurutkan:")
    for i in range(n):
        print(f"{i+1}. {arr_nama[i]}: {arr_nilai[i]}")

if __name__ == "__main__":
    main()