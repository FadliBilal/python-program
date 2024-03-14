print("Soal No 3")

def main():
    # menginisialisasi dictionary untuk menyimpan nama peserta dan jumlah kehadiran pada setiap webinar
    peserta_webinar = {}

    # Input jumlah webinar 3 dari program berdasarkan soal yang diberikan
    jumlah_webinar = 3

    # Loop untuk setiap webinar
    for i in range(1, jumlah_webinar + 1):
        # Input jumlah peserta pada webinar ke-i
        jumlah_peserta = int(input(f"Jumlah peserta webinar {i}: "))

        # Loop untuk setiap peserta pada webinar ke-i
        for j in range(1, jumlah_peserta + 1):
            nama_peserta = input(f"Nama {j} pada webinar {i}: ")

            # Menambahkan nama peserta ke dictionary dan mengupdate jumlah kehadiran
            peserta_webinar[nama_peserta] = peserta_webinar.get(nama_peserta, 0) + 1

    # Menampilkan peserta yang mengikuti webinar dan jumlah kehadiran mereka
    print("\nPeserta yang datang di webinar:")
    for nama, kehadiran in peserta_webinar.items():
        print(f"{nama} ({kehadiran}), ", end="")

    # Menampilkan peserta yang mengikuti semua webinar
    print("\n\nPeserta yang datang di seluruh webinar:")
    for nama, kehadiran in peserta_webinar.items():
        if kehadiran == jumlah_webinar:
            print(nama)

if __name__ == "__main__":
    main()