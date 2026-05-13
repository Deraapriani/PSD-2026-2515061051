class StackArray:
    def __init__(self, max_size=50):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1
    def is_empty(self):
        return self.top_idx == -1
    def is_full(self):
        return self.top_idx == self.MAX - 1
    def push(self, x):
        if self.is_full():
            print("Tumpukan piring penuh")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Piring '{x}' ditaruh di atas")
    def pop(self):
        if self.is_empty():
            print("Tidak ada piring")
            return
        print(f"Piring '{self.st[self.top_idx]}' diambil dari atas")
        self.top_idx -= 1
    def peek(self):
        if self.is_empty():
            print("Tidak ada piring")
            return
        print(f"Piring teratas: '{self.st[self.top_idx]}'")
    def display(self):
        if self.is_empty():
            print("Tumpukan piring kosong")
            return
        print("Piring (atas -> bawah): ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=" ")
        print()

def main():
    stack = StackArray(20)
    while True:
        print("\nDapur: Tumpukan Piring ")
        print("1. Letakkan piring")
        print("2. Ambil piring (pakai)")
        print("3. Lihat piring teratas")
        print("4. Lihat semua piring")
        print("5. Keluar")
        cmd = input("Pilih: ").strip()
        if cmd == "1":
            name = input("Nama/ID piring: ")
            stack.push(name)
        elif cmd == "2":
            stack.pop()
        elif cmd == "3":
            stack.peek()
        elif cmd == "4":
            stack.display()
        elif cmd == "5":
            print("Selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()