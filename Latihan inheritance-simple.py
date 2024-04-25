class Kendaraan:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun

    def Spek(self):
        return f"{self.merk} {self.model} ini adalah spesifikasinya."

    def info(self):
        return f"{self.merk} {self.model} ({self.tahun})"

class Mobil(Kendaraan):
    def __init__(self, merk, model, tahun, warna):
        super().__init__(merk, model, tahun)
        self.warna = warna

    def Spek(self):
        return f"{self.warna} {self.merk} {self.model} ini adalah spesifikasinya."

class Motor(Kendaraan):
    def __init__(self, merk, model, tahun, cc_mesin):
        super().__init__(merk, model, tahun)
        self.cc_mesin = cc_mesin

    def Spek(self):
        return f"{self.merk} {self.model} with {self.cc_mesin}ini adalah spesifikasinya."

if __name__ == "__main__":
    mobil = Mobil("Toyota", "Camry", 2020, "Red")
    motor = Motor("Honda", "CBR600RR", 2021, 600)

    print(mobil.info())
    print(mobil.Spek())

    print(motor.info())
    print(motor.Spek())
