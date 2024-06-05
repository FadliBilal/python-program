# Inisialisasi data perpustakaan sebagai dictionary
perpustakaan = {
    "001": "Buku ALgoritma | Ditulis Bilal",
    "002": "Buku Statistika | Ditulis Bara",
    "003": "Buku Indonesia | Ditulis Ilham"
}

def insert(perpustakaan, id_buku, info_buku):
    if id_buku in perpustakaan:
        print("Data Sudah Ada")
    else:
        perpustakaan[id_buku] = info_buku
        print("Data berhasil ditambahkan")

def update(perpustakaan, id_buku, info_buku):
    if id_buku in perpustakaan:
        perpustakaan[id_buku] = info_buku
        print("Data berhasil diupdate")
    else:
        print("Data tidak ditemukan")

def delete(perpustakaan, id_buku):
    if id_buku in perpustakaan:
        del perpustakaan[id_buku]
        print("Data berhasil dihapus")
    else:
        print("Data tidak ditemukan")

def display_info(perpustakaan):
    if perpustakaan:
        print("=== LIST BUKU PERPUSTAKAAN ===")
        for id_buku, info_buku in perpustakaan.items():
            print(f"ID Buku: {id_buku}, Informasi Buku: {info_buku}")
    else:
        print("Tidak ada data buku di perpustakaan")

# Menambahkan data baru ke perpustakaan
insert(perpustakaan, "001", "Buku PBO | Ditulis Azar")
insert(perpustakaan, "004", "Buku Ipa | Ditulis Hendra")

update(perpustakaan, "002", "Buku Biologi | Ditulis Hendra")

delete(perpustakaan, "001")

display_info(perpustakaan)