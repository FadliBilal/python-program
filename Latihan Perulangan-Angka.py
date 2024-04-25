#perulangan 2 bilangan dengan if
num1 = int(input("Bilangan Pertama : "))
num2 = int(input("Bilangan Kedua : "))
if num1 > num2:
    print(f'{num1} Lebih Besar dari {num2}')
elif num1 < num2:
    print(f'{num1} Lebih Kecil dari {num2}')
else:
    print("Keduanya sama")

#perulangan 5 bilangan dengan while
while True:
    angka = []
    i = 0
    while i < 5:
        inbil = int(input(f"Masukkan bilangan ke {i + 1} : "))
        angka.append(inbil)
        i += 1
    kecil = besar = angka[0]
    sama = True
    i = 0
    while i < 5:
        if angka[i] < kecil:
            kecil = angka[i]
        if angka[i] > besar:
            besar = angka[i]
        if angka[i] != angka[0]:
            sama = False
        i += 1
    print(f"Bilangan terkecil adalah : {kecil}")
    print(f"Bilangan terbesar adalah : {besar}")
    if sama:
        print("Semua bilangan sama")
    break


