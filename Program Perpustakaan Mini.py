print("Soal No 1")

class Perpustakaan:
    def __init__(self):
        # menginisialisasi perpustakaan dengan dictionary untuk menyimpan rak-rak dan buku-buku di setiap rak
        self.rak_perpustakaan = {}

    def TambahRak(self, nama_rak):
        # fungsi untuk menambahkan rak ke dalam perpustakaan
        if nama_rak not in self.rak_perpustakaan:
            self.rak_perpustakaan[nama_rak] = []
            print(f"Rak '{nama_rak}' berhasil ditambahkan.")
        else:
            print(f"Rak '{nama_rak}' tidak dapat ditambahkan karena sudah ada dalam perpustakaan.")

    def TambahBuku(self, nama_rak, nama_buku, nama_pengarang, tahun_terbit):
        # Fungsi untuk menambahkan buku ke dalam rak di perpustakaan
        if nama_rak not in self.rak_perpustakaan:
            # Jika rak belum ada, tanyakan apakah pengguna ingin menambahkannya
            print(f"Rak '{nama_rak}' rak belum ada dalam perpustakaan.")
            tambah_rak = input("Apakah Anda ingin menambah rak ini di perpustakaan? jika iya klik y / jika tidak klik n (y/n): ").lower()

            if tambah_rak == "y":
                self.TambahRak(nama_rak)
            # Jika tidak maka tidak dapat ditambahkan
            else:
                print("Buku tidak ditambahkan karena rak belum ada.")
                return

        # untuk membuat objek buku baru
        buku_baru = {
            "Nama Buku": nama_buku,
            "Pengarang": nama_pengarang,
            "Tahun Terbit": tahun_terbit
        }

        # menambahkan buku ke dalam rak di perpustakaan
        self.rak_perpustakaan[nama_rak].append(buku_baru)
        print(f"Buku '{nama_buku}' berhasil ditambahkan ke rak '{nama_rak}'.")

    def CariBuku(self, nama_buku):
        # fungsi untuk mencari informasi buku berdasarkan nama buku
        buku_ditemukan = False

        # loop melalui setiap rak dan buku di perpustakaan
        for rak, daftar_buku in self.rak_perpustakaan.items():
            for buku in daftar_buku:
                if buku["Nama Buku"] == nama_buku:
                    # Jika buku ditemukan, akan menampilkampilkan informasi buku
                    print(f"Informasi buku '{nama_buku}':")
                    print(f"Nama Buku: {buku['Nama Buku']}")
                    print(f"Rak : {rak}")
                    print(f"Pengarang: {buku['Pengarang']}")
                    print(f"Tahun Terbit: {buku['Tahun Terbit']}")
                    buku_ditemukan = True
                    break

        # jika buku tidak ditemukan, memberikan notifikasi
        if not buku_ditemukan:
            print(f"Buku '{nama_buku}' tidak ditemukan dalam perpustakaan.")

def main():
    # fungsi utama program
    perpustakaan_saya = Perpustakaan()

    while True:
        # menu utama program
        print("\nMenu Sistem Perpustakaan sederhana:")
        print("1. Tambah Rak")
        print("2. Tambah Buku")
        print("3. Cari Buku")
        print("0. Keluar")

        pilihan = input("Pilih menu nomer(0-3): ")

        if pilihan == "1":
            # Pilihan untuk menambah rak
            nama_rak = input("Masukkan nama rak: ")
            perpustakaan_saya.TambahRak(nama_rak)
        elif pilihan == "2":
            # Pilihan untuk menambah buku
            nama_rak = input("Masukkan nama rak: ")
            nama_buku = input("Masukkan nama buku: ")
            nama_pengarang = input("Masukkan nama pengarang: ")
            tahun_terbit = input("Masukkan tahun terbit: ")
            perpustakaan_saya.TambahBuku(nama_rak, nama_buku, nama_pengarang, tahun_terbit)
        elif pilihan == "3":
            # Pilihan untuk mencari buku
            nama_buku = input("Masukkan nama buku yang dicari: ")
            perpustakaan_saya.CariBuku(nama_buku)
        elif pilihan == "0":
            # Keluar dari program
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()