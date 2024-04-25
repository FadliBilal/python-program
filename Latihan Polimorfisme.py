class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def hitung_harga(self):
        return self.harga

    def hitung_pajak(self):
        return self.harga * 0.1


class Buku(Produk):
    def __init__(self, nama, harga, penulis):
        super().__init__(nama, harga)
        self.penulis = penulis

    def hitung_pajak(self):
        return 0


class Electronik(Produk):
    def __init__(self, nama, harga, tahun_garansi):
        super().__init__(nama, harga)
        self.tahun_garansi = tahun_garansi

    def hitung_garansi(self):
        return self.tahun_garansi * 0.05

class Perabotan(Produk):
    def __init__(self, nama, harga, material):
        super().__init__(nama, harga)
        self.material = material


def hitung_total_harga(produk):
    total_harga = 0
    total_pajak = 0
    for p in produk:
        total_harga += p.hitung_harga()
        total_pajak += p.hitung_pajak()
    return total_harga + total_pajak


buku1 = Buku("Buku Emyu", 5000, "Ayam")
electronik1 = Electronik("Laptop", 10000, 1)
perabotan1 = Perabotan("Meja", 20000, "Kayu")

total_harga = hitung_total_harga([buku1, electronik1, perabotan1])
print("Total harga semua produk :", total_harga)
