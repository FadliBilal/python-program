while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = angka1 / angka2
        print("Hasil pembagian:", hasil)
        break
    except ZeroDivisionError:
        print("Error: Pembagian dengan angka nol tidak diizinkan.")
    except ValueError:
        print("Error: Masukan harus berupa bilangan numerik.")
