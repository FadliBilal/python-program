# baris code dibawah ini untuk mengimport modul 'datetime' untuk bekerja dengan informasi tanggal dan waktu
from datetime import datetime

# baris code dibawah ini untuk membuat fungsi untuk membuat tagihan
def create_bill(customer_name, products, total_payment, change):
    # baris code dibawah ini untuk mendapatkan waktu transaksi
    transaction_time = datetime.now().strftime("%d-%m-%Y %H-%M-%S WIB-Jakarta")

    # baris code dibawah ini untuk membuat nama file .txt nya saat program selesai
    bill_name = f"{customer_name}_{transaction_time}.txt"

    # code dibawah ini untuk membuka file .txt tagihan
    with open(bill_name, 'w') as bill_file:
        # code dibawah ini untuk menuliskan header
        bill_file.write("========== Yes Cafe - Tagihan ==========\n")
        bill_file.write(f"Tagihan untuk : {customer_name}\n")
        bill_file.write(f"Tanggal       : {transaction_time}\n")
        bill_file.write("===========================================\n")

        # code dibawah ini untuk menuliskan informasi produk .txt nya
        for product in products:
            name, price, quantity = product
            product_line = f"{name} ({quantity}x IDR {price:.2f})   : IDR {quantity * price:.2f}"
            bill_file.write(f"{product_line}\n")

        # code dibawah ini untuk menuliskan informasi total pembayaran
        bill_file.write("===========================================\n")
        bill_file.write(f"Total Pembayaran  : IDR {total_payment:.2f}\n")
        bill_file.write(f"Uang Dibayar      : IDR {total_payment + change:.2f}\n")
        bill_file.write(f"Uang Kembalian    : IDR {change:.2f}\n")
        bill_file.write("============== Terima Kasih ==============")

    # baris code dibawah ini untuk menampilkan pesan bahwa tagihan telah dibuat dan disimpan
    print(f"Tagihan telah dibuat dan disimpan dalam file: {bill_name}")


# baris code dibawah ini untuk fungsi utama untuk menjalankan program
def main():
    # code dibawah ini untuk menginisialisasikan variabel
    customer_name = input("Masukkan nama pembeli: ")
    products = []

    # code dibawah ini untuk meminta input informasi produk hingga string kosong dimasukkan
    while True:
        product_name = input("Masukkan nama produk (untuk selesai kosongkan inputan lalu enter): ")
        if not product_name:
            break
        price = float(input("Masukkan harga satuan produk: "))
        quantity = int(input("Masukkan jumlah produk yang dibeli: "))
        products.append((product_name, price, quantity))

    # baris code dibawah ini untuk menghitung total biaya
    total_payment = sum([price * quantity for _, price, quantity in products])

    # baris code dibawah ini untuk meminta input jumlah uang yang dibayar oleh pelanggan
    payment = float(input("Masukkan jumlah uang yang dibayar oleh pelanggan: "))

    # baris code dibawah ini untuk menghitung kembalian yang harus dikembalikan kepada pelanggan
    change = payment - total_payment

    # baris code dibawah ini untuk membuat dan menyimpan file tagihan
    create_bill(customer_name, products, total_payment, change)


# code dibawah ini untuk menjalankan fungsi utama jika skrip ini dieksekusi
if __name__ == "__main__":
    main()
