class Mahasiswa:
    def __init__(self, nama, nim, semester):
        self.nama = nama   # public method
        self.__nim = nim   # private method
        self.__semester = semester

    @property   # getter
    def nim(self):
        return self.__nim

    @nim.setter  # setter
    def nim(self, nim):
        self.__nim = nim

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, semester):
        self.__semester = semester

    def display_info(self):  # Overriding ke Ketua Dan Komting
        print("- Nama:", self.nama)
        print("- NIM:", self.__nim)
        print("- Semester:", self.__semester)


class HimpunanMahasiswa:
    def __init__(self):
        self.__mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        if mahasiswa.semester < 3:
            raise ValueError(f"Mahasiswa {mahasiswa.nama} harus semester 3 ke atas")
        self.__mahasiswa.append(mahasiswa)


class KetuaHimpunan(Mahasiswa):  # Single Inheritance
    def __init__(self, nama, nim, semester, jabatan):
        super().__init__(nama, nim, semester)
        self.__jabatan = jabatan
        if semester < 4:
            raise ValueError(f"{nama} harus semester 4 ke atas untuk menjadi Kahim")

    def display_info(self):
        super().display_info()
        print("Jabatan:", self.__jabatan)  # Nambahin atribut jabatan


class WakilKetua(KetuaHimpunan):  # Multilevel Inheritance
    def __init__(self, nama, nim, semester, jabatan):
        super().__init__(nama, nim, semester, jabatan)
        if semester < 4:
            raise ValueError(f"{nama} harus semester 4 ke atas untuk menjadi Wakahim")


class Komting(HimpunanMahasiswa, Mahasiswa):
    def __init__(self, nama, nim, semester, jabatan):
        if semester < 4:
            raise ValueError(f"{nama} harus semester 4 ke atas untuk menjadi Komting")
        Mahasiswa.__init__(self, nama, nim, semester)
        HimpunanMahasiswa.__init__(self)
        self.__jabatan = jabatan

    def display_info(self):
        super().display_info()
        print("Jabatan:", self.__jabatan)
