class Orang:
    def __init__(self, nama, pekerjaan=None, usia=None):
        self.nama = nama
        self._pekerjaan = pekerjaan
        self._usia = usia

    @property
    def pekerjaan(self):
        return self._pekerjaan

    @pekerjaan.setter
    def pekerjaan(self, value):
        self._pekerjaan = value

    @property
    def usia(self):
        return self._usia

    @usia.setter
    def usia(self, value):
        self._usia = value

dona = Orang("Dona")
malik = Orang("Malik")

dona.pekerjaan = "Guru"
dona.usia = 35

malik.pekerjaan = "Dokter"
malik.usia = 40

print(f"Informasi Dona: Pekerjaan {dona.pekerjaan}, Usia : {dona.usia} tahun")
print(f"Informasi Malik: Pekerjaan {malik.pekerjaan}, Usia : {malik.usia} tahun")
