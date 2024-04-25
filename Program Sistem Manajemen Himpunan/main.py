from fileinduk import Mahasiswa, HimpunanMahasiswa, KetuaHimpunan, WakilKetua, Komting


class AnggotaHarian:
    def __init__(self):
        self.mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        if mahasiswa.semester < 3:
            raise ValueError(f"Mahasiswa {mahasiswa.nama} harus semester 3 ke atas untuk bisa masuk anggota hima")
        self.mahasiswa.append(mahasiswa)
        print(f"- {mahasiswa.nama} berhasil ditambahkan sebagai Anggota Harian himpunan.")

    def display_info(self):  # Polimorfisme
        for mhs in self.mahasiswa:
            print("- Nama:", mhs.nama, "| Semester : ", mhs.semester)


mhs1 = Mahasiswa("Dol", "123456", 2)
mhs2 = Mahasiswa("Doe", "654321", 14)

himpunan = HimpunanMahasiswa()

try:

    harian = AnggotaHarian()
    harian.tambah_mahasiswa(mhs1)
    harian.tambah_mahasiswa(mhs2)

    ketua = KetuaHimpunan("Andi", "12345", 5, "Ketua Umum")
    wakil_ketua = WakilKetua("Andini", "54321", 4, "Wakil Ketua")
    perwakilan = Komting("Andha", "32145", 4, "Komting Mahasiswa")

except ValueError as e:
    print("Error:", e)
else:
    print("==== Info Himpunan ====")
    ketua.display_info()
    print()
    wakil_ketua.display_info()
    print()
    perwakilan.display_info()
    print()
    print("Info Daftar Anggota Harian")
    harian.display_info()
