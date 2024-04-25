class Orang:
    def __init__(self, nama, pekerjaan, usia):
        self.nama = nama
        self.__pekerjaan = pekerjaan
        self.__usia = usia

    @property
    def pekerjaan(self):
        return self.__pekerjaan

    @pekerjaan.setter
    def pekerjaan(self, pekerjaan):
        self.__pekerjaan = pekerjaan

    @property
    def usia(self):
        return self.__usia

    @usia.setter
    def usia(self, usia):
        self.__usia = usia

# Objek
dona = Orang("Dona", "Guru", 35)
malik = Orang("Malik", "Dokter", 40)

print(f"Dona: Pekerjaannya adalah {dona.pekerjaan}, Usianya adalah {dona.usia} tahun")
print(f"Malik: Pekerjaannya adalah {malik.pekerjaan}, Usianya adalah {malik.usia} tahun")