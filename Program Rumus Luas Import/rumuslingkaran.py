from induk import Induk

class RumusLingkaran(Induk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def rumus_luas(self):
        return 3.14 * self.jari_jari ** 2
