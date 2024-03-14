# Fibonansi dengan perulangan rekursif
# Target output BATAS DERET
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

batas = int(input("Masukkan BATAS DERET bilangan Fibonansi : "))

print("Deret Fibonacci:")
for i in range(batas):
    print(fibonacci(i), end=" ")

# Fibonansi dengan perulangan while
# Target Output BATAS BILANGAN dari inputan
i = int(input("Masukkan BATAS DERET bilangan Fibonansi : "))

fibonansi = [0, 1]

if i == 1:
    print("fibonansi angka 1 itu 0")
elif i >= 2:
    print("Hasil Deret Fibonansi hingga", i, "Deret :", end=" ")
    count = 2
    while count < i:
        fibonansilanjut = fibonansi[-1] + fibonansi[-2]
        fibonansi.append(fibonansilanjut)
        count += 1
    for num in fibonansi:
        print(num, end=" ")