class Node:
    def __init__(self, score):
        self.score = score
        self.left = None
        self.right = None


class BSTUjian:
    def __init__(self):
        self.root = None

    def insert(self, root, score):
        if root is None:
            return Node(score)
        if score < root.score:
            root.left = self.insert(root.left, score)
        elif score > root.score:
            root.right = self.insert(root.right, score)
        return root

    def delete(self, root, score):
        if root is None:
            return root
        if score < root.score:
            root.left = self.delete(root.left, score)
        elif score > root.score:
            root.right = self.delete(root.right, score)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            temp = self._min_node(root.right)
            root.score = temp.score
            root.right = self.delete(root.right, temp.score)
        return root

    def _min_node(self, root):
        while root.left:
            root = root.left
        return root

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.score, end=" ")
            self.inorder(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.score + self.sum_nodes(root.left) + self.sum_nodes(root.right)

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


def main():
    bst = BSTUjian()
    pilih = 0
    while pilih != 5:
        print("\n=== BST Nilai Ujian ===")
        print("1. Tambah nilai")
        print("2. Tampilkan nilai urut kecil → besar")
        print("3. Hapus nilai")
        print("4. Jumlah total dan banyak nilai")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                x = int(input("Masukkan nilai: "))
                bst.root = bst.insert(bst.root, x)
                print(f"Nilai {x} ditambahkan.")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            print("Nilai urut: ", end="")
            bst.inorder(bst.root)
            print()
        elif pilih == 3:
            try:
                x = int(input("Hapus nilai: "))
                if bst.root is None:
                    print("BST kosong.")
                else:
                    bst.root = bst.delete(bst.root, x)
                    print(f"Nilai {x} dihapus.")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 4:
            total = bst.sum_nodes(bst.root)
            jumlah = bst.count_nodes(bst.root)
            print(f"Total nilai: {total}, Jumlah nilai: {jumlah}")
        elif pilih == 5:
            print("Selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()