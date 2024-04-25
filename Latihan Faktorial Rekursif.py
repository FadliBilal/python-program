# Faktorial dengan perulangan rekursif
n = int(input('Masukkan angka yang mau difaktorin : '))
def faktorial(n):
    if n > 1:
        print(f'{n} X {n - 1} = {n * (n - 1)}')
        return n * faktorial(n - 1)
    return 1

print(f'hasil faktor {n} = {faktorial(n)}')