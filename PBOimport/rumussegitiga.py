from induk import Induk

class RumusSegitiga(Induk):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def rumus_luas(self):
        return 0.5 * self.alas * self.tinggi