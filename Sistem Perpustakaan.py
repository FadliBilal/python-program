from collections import deque

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []
        self.history = deque()

    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        return results

    def display_search_results(self, results):
        if not results:
            print("Buku tidak ditemukan.")
        else:
            for book in results:
                status = "Tersedia" if book.available else "Dipinjam"
                print(f"ID: {book.book_id}, Judul: {book.title}, Penulis: {book.author}, Status: {status}")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                self.history.append(book)
                print(f"Buku {book.title} berhasil dipinjam.")
                return
        print("Buku tidak tersedia atau sudah dipinjam.")

    def return_book(self, book_id):
        for book in self.history:
            if book.book_id == book_id:
                book.available = True
                print(f"Buku {book.title} berhasil dikembalikan.")
                return
        print("Buku tidak ditemukan dalam riwayat peminjaman.")

    def add_book(self, title, author):
        new_id = len(self.books) + 1
        new_book = Book(new_id, title, author)
        self.books.append(new_book)
        print(f"Buku {title} berhasil ditambahkan dengan ID {new_id}.")

    def edit_book(self, book_id, new_title, new_author):
        for book in self.books:
            if book.book_id == book_id:
                book.title = new_title
                book.author = new_author
                print(f"Informasi buku berhasil diubah.")
                return
        print("Buku tidak ditemukan.")

    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Buku {book.title} berhasil dihapus.")
                return
        print("Buku tidak ditemukan.")

    def display_collection(self):
        if not self.books:
            print("Koleksi Buku masih kosong.")
        else:
            print("Koleksi Buku:")
            for book in self.books:
                status = "Tersedia" if book.available else "Dipinjam"
                print(f"ID: {book.book_id}, Judul: {book.title}, Penulis: {book.author}, Status: {status}")

    def display_history(self):
        print("Riwayat Peminjaman:")
        for book in self.history:
            status = "Dikembalikan" if book.available else "Dipinjam"
            print(f"ID: {book.book_id}, Judul: {book.title}, Penulis: {book.author}, Status: {status}")
        linum = 0
        for book in self.books:
            linum += 1
            status = "Tersedia" if book.available else "Dipinjam"
            print(f"{linum} ID: {book.book_id}, Judul: {book.title}, Penulis: {book.author}, Status: {status}")

    def display_history(self):
        print("Riwayat Peminjaman:")
        linum = 0
        for book in self.history:
            linum += 1
            status = "Dikembalikan" if book.available else "Dipinjam"
            print(f"{linum} ID: {book.book_id}, Judul: {book.title}, Penulis: {book.author}, Status: {status}")

def main():
    library = Library()

    while True:
        print("\nMenu Perpustakaan :")
        print("1. Cari Buku")
        print("2. Pinjam Buku")
        print("3. Kembalikan Buku")
        print("4. Lihat Riwayat")
        print("5. Tambah Buku Baru")
        print("6. Edit Data Buku")
        print("7. Hapus Buku")
        print("8. Lihat Koleksi Buku")
        print("9. Keluar")

        choice = input("Pilih menu (1-9): ")

        if choice == '1':
            keyword = input("Masukkan judul atau penulis buku: ")
            results = library.search_book(keyword)
            library.display_search_results(results)
        elif choice == '2':
            book_id = int(input("Masukkan ID buku yang ingin dipinjam: "))
            library.borrow_book(book_id)
        elif choice == '3':
            book_id = int(input("Masukkan ID buku yang ingin dikembalikan: "))
            library.return_book(book_id)
        elif choice == '4':
            library.display_history()
        elif choice == '5':
            title = input("Masukkan judul buku baru: ")
            author = input("Masukkan penulis buku baru: ")
            library.add_book(title, author)
        elif choice == '6':
            book_id = int(input("Masukkan ID buku yang ingin diubah: "))
            new_title = input("Masukkan judul baru: ")
            new_author = input("Masukkan penulis baru: ")
            library.edit_book(book_id, new_title, new_author)
        elif choice == '7':
            book_id = int(input("Masukkan ID buku yang ingin dihapus: "))
            library.delete_book(book_id)
        elif choice == '8':
            print("==============")
            library.display_collection()
            print("==============")
        elif choice == '9':
            print("Terima kasih. Sampai jumpa kembali.") #Re-run untuk menjalankan program
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
