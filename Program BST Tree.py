class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None
        self.insert_order = []  # Menyimpan urutan penambahan nilai ke dalam BST

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)  # Jika BST kosong, nilai menjadi root
            self.insert_order.append(key)
        else:
            current = self.root
            while True:
                if key < current.val:
                    if current.left is None:
                        current.left = TreeNode(key)  # Masukkan ke sub-pohon kiri jika lebih kecil
                        self.insert_order.append(key)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = TreeNode(key)  # Masukkan ke sub-pohon kanan jika lebih besar
                        self.insert_order.append(key)
                        break
                    else:
                        current = current.right

    def delete(self, key, root=None):
        if root is None:
            root = self.root

        if key < root.val:
            root.left = self.delete(key, root.left)
        elif key > root.val:
            root.right = self.delete(key, root.right)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._minValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(temp.val, root.right)

        if key in self.insert_order:
            self.insert_order.remove(key)

        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.val:
                index = self.insert_order.index(key)
                return current, index
            elif key < current.val:
                current = current.left
            else:
                current = current.right
        return None, -1

    def display(self):
        return self.insert_order

def main():
    bst = BST()
    while True:
        print("\nMenu:")
        print("1. Tampilkan urutan bilangan")
        print("2. Insert bilangan")
        print("3. Delete bilangan")
        print("4. Search bilangan")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1-5): ")
        if choice == '1':
            print("Urutan bilangan berdasarkan insert: ", bst.display())
        elif choice == '2':
            numbers = input("Masukkan bilangan, dipisahkan oleh spasi: ").split()
            if len(numbers) < 5:
                print("Masukkan minimal 5 bilangan.")
                continue
            for num in numbers:
                bst.insert(int(num))
            print("Bilangan telah ditambahkan.")
        elif choice == '3':
            key = int(input("Masukkan bilangan yang akan dihapus: "))
            bst.delete(key)
            print(f"Bilangan {key} telah dihapus.")
        elif choice == '4':
            key = int(input("Masukkan bilangan yang dicari: "))
            _, index = bst.search(key)
            if index != -1:
                print(f"Bilangan {key} ditemukan di urutan-{index + 1}.")
            else:
                print(f"Bilangan {key} tidak ditemukan di BST.")
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()