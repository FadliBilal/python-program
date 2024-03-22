from rumussegitiga import RumusSegitiga
from rumuslingkaran import RumusLingkaran

class Main:
    def __init__(self):
        self.segitiga = RumusSegitiga(2, 8)
        self.lingkaran = RumusLingkaran(5)

    def hitung_luas_lingkaran(self):
        return self.lingkaran.rumus_luas()

    def hitung_luas_segitiga(self):
        return self.segitiga.rumus_luas()

run = Main()
print("Luas segitiga:", run.hitung_luas_segitiga())
print("Luas lingkaran:", run.hitung_luas_lingkaran())