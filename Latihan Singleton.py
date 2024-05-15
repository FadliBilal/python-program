class Singleton:
    # variabel kelas __instance untuk melacak/mencari instance objek tunggal
    __instance = None

    # buat memeriksa apakah __instance sudah terbuat apa belum
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

# membuat dua objek ke instance Singleton
s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)

# memeriksa apakah kedua objek menunjuk ke instance yang sama
print(s1 is s2)
# kalo benar true

# memastikan atribut pada s1 apakah s2 memiliki nilai yang sama
s1.x = 5
print(s2.x)
