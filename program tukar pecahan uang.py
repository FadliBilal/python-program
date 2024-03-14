def uang(jumlah):
    koleksi = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    kombinasi = {}
    for k in koleksi:
        if jumlah >= k:
            kombinasi[k] = jumlah // k
            jumlah %= k
    return kombinasi

jumlah = int(input("Masukkan jumlah uang yang ingin ditukarkan: "))

kombinasi = uang(jumlah)
if not kombinasi:
    print("Pertukaran nilai mata uang tidak bisa, karena uang mu tidak bisa ditukar dengan yang ada di koleksi")
else:
    print("Pecahan mata uang yang didapat : ")
    for k, hitung in kombinasi.items():
        print(f"{k} x {hitung}")
