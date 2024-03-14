# Inisialisasi variabel
daftar_belanja = []
total_belanja = 0

# Fungsi untuk menambahkan item baru ke dalam daftar belanja
def tambah_item():
    nama_item = input("Masukkan nama item: ")
    harga_item = float(input("Masukkan harga item: "))
    item = {"nama": nama_item, "harga": harga_item}
    daftar_belanja.append(item)
    print(f"{nama_item} ditambahkan ke dalam daftar belanja.")

# Fungsi untuk menghapus item yang sudah dibeli dari daftar belanja
def hapus_item():
    if not daftar_belanja:
        print("Daftar belanja kosong.")
        return

    print("Daftar Belanja:")
    for i, item in enumerate(daftar_belanja, 1):
        print(f"{i}. {item['nama']} - Rp {item['harga']}")

    index_hapus = int(input("Masukkan nomor item yang ingin dihapus: ")) - 1

    if 0 <= index_hapus < len(daftar_belanja):
        item_terhapus = daftar_belanja.pop(index_hapus)
        print(f"{item_terhapus['nama']} dihapus dari daftar belanja.")
    else:
        print("Nomor item tidak valid.")

# Fungsi untuk menampilkan daftar belanja saat ini beserta total belanja
def tampilkan_daftar():
    if not daftar_belanja:
        print("Daftar belanja kosong.")
        return

    print("Daftar Belanja:")
    linum = 0
    for item in daftar_belanja:
        linum += 1
        print(f"{linum}. {item['nama']} - Rp {item['harga']}")

    hitung_total_belanja()

# Fungsi untuk menghitung total belanja
def hitung_total_belanja():
    global total_belanja
    total_belanja = sum(item['harga'] for item in daftar_belanja)
    print(f"Total Belanja: Rp {total_belanja}")

# Program utama
while True:
    print("\nMenu:")
    print("1. Tambah Item")
    print("2. Hapus Item")
    print("3. Tampilkan Daftar Belanja")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == "1":
        tambah_item()
    elif pilihan == "2":
        hapus_item()
    elif pilihan == "3":
        tampilkan_daftar()
    elif pilihan == "4":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Masukkan angka 1-4.")