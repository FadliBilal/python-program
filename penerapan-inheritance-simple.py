#Program Class Kendaraan
class Kendaraan:
    def __init__(self, nama, penumpang):
        self.nama = nama
        self.penumpang = penumpang

    def menambahkan_penumpang(self, penumpang_baru):
        self.penumpang.append(penumpang_baru)


class Motor(Kendaraan):
    def __init__(self, nama, penumpang):
        super().__init__(nama, penumpang)
        self.standar_terpasang = False

    def pasang_standar(self):
        self.standar_terpasang = True


# objek
motor = Motor("Honda", ["Azhar", "Bima"])

#output
print(f"Penumpang motor {motor.nama}: {motor.penumpang}")
print(f"Standar terpasang : {motor.standar_terpasang}")

motor.pasang_standar() #sesudah perintah ini maka pasang standar jadi true
print(f"Standar terpasang : {motor.standar_terpasang}")