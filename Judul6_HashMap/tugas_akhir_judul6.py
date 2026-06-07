class Node:
    def __init__(self, key, value):
        self.key = key         
        self.value = value      
        self.next = None


class HashMapKontak:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    # Fungsi hash untuk string
    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.SIZE

    # Menambahkan kontak
    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    # Mencari kontak
    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    # Menghapus kontak
    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next

        return False

    # Menampilkan semua daftar kontak
    def display(self):
        print("\n=== DAFTAR KONTAK ===")
        for i in range(self.SIZE):
            print(f"Index {i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(f"[{current.key} : {current.value}] -> ", end="")
                current = current.next

            print("None")


def main():
    kontak = HashMapKontak()

    # Menambahkan kontak
    kontak.insert("ryujin", "081234567890")
    kontak.insert("ahyeon", "082345678901")
    kontak.insert("ruka", "083456789012")
    kontak.insert("love", "084567890123")

    kontak.display()

    # Mencari kontak
    nama = "ruka"
    hasil = kontak.search(nama)

    if hasil is not None:
        print(f"\nNomor telepon {nama}: {hasil.value}")
    else:
        print(f"\nKontak {nama} tidak ditemukan")

    # Menghapus kontak
    kontak.remove_key("ryujin")

    print("\nSetelah kontak ryujin dihapus:")
    kontak.display()


if __name__ == "__main__":
    main()