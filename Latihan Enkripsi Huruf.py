print("Soal No 2")

# mendefinisikan fungsi geser_huruf dengan parameter input_str
def geser_huruf(input_str):
    # Inisialisasi total_angka untuk menyimpan jumlah angka dalam string
    total_angka = 0

    # untuk Loop pertama untuk menghitung total angka dalam string
    for char in input_str:
        if char.isdigit():
            total_angka += int(char)

    # menginisialisasi hasil_output untuk menyimpan hasil dekripsi huruf
    hasil_output = ""

    # Loop kedua untuk menggeser huruf sesuai jumlah angka yang dihitung
    for char in input_str:
        if char.isalpha():
            # Menggeser huruf (dengan memastikan tetap huruf kapital)
            shifted_char = chr((ord(char) - ord('A') + total_angka) % 26 + ord('A'))
            hasil_output += shifted_char

    # Mengembalikan hasil_output yang merupakan hasil dekripsi huruf
    return hasil_output

#
input_str = input("Masukkan string (huruf dan angka): ")
output_str = geser_huruf(input_str)

# Menampilkan hasil output
print(f"hasil geser huruf: {output_str}")
