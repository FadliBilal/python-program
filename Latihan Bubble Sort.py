#Soal 1
def print_matriks(matriks):
    for baris in matriks:
        print(baris)
def tambah_matriks(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil
matriks1 = [
    [3, 6, 2],
    [8, 1, 9],
    [1, 2, 1]
]
matriks2 = [
    [1, 3, 4],
    [1, 3, 4],
    [3, 2, 1]
]
hasil = tambah_matriks(matriks1, matriks2)
print("Hasil Penjumlahan:")
print_matriks(hasil)
#Soal 2
buku_perpustakaan = []
def tampil_data():
    if not buku_perpustakaan:
        print("Perpustakaan kosong.")
    else:
        print("Data buku perpustakaan:")
        print("ID\tJudul\tPengarang\tTahun Terbit")
        for buku in buku_perpustakaan:
            print("\t".join(str(x) for x in buku))

def tambah_data(id_buku, judul, pengarang, tahun_terbit):
    buku_perpustakaan.append([id_buku, judul, pengarang, tahun_terbit])
    print("Data buku berhasil ditambahkan.")

def ubah_data(id_buku, judul_baru, pengarang_baru, tahun_terbit_baru):
    for buku in buku_perpustakaan:
        if buku[0] == id_buku:
            buku[1] = judul_baru
            buku[2] = pengarang_baru
            buku[3] = tahun_terbit_baru
            print("Data buku berhasil diubah.")
            return
    print("ID buku tidak ditemukan.")

def hapus_data(id_buku):
    for buku in buku_perpustakaan:
        if buku[0] == id_buku:
            buku_perpustakaan.remove(buku)
            print("Data buku berhasil dihapus.")
            return
    print("ID buku tidak ditemukan.")

# Contoh penggunaan:
tambah_data(1, "Python Programming", "John Doe", 2020)
tambah_data(2, "Data Structures", "Jane Smith", 2019)
tambah_data(3, "Machine Learning", "Alice Johnson", 2021)

tampil_data()

ubah_data(2, "Algorithms", "Jane Doe", 2018)
hapus_data(3)

tampil_data()

#Soal 3
def bubble_sort(list):
    n = len(list)
    for i in range(n-1):
        tukar = False
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                tukar = True
        if not tukar:
            break
def binary_search(list, x):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list[mid] < x:
            low = mid + 1
        elif list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
list = [64, 34, 25, 12, 22, 11, 90]
x = 22
bubble_sort(list)
print("List yang sudah diurutkan: ", list)
result = binary_search(list, x)
if result != -1:
    print("Elemen ditemukan pada index:", str(result))
else:
    print("Elemen tidak ditemukan dalam listay")
