import queue
import time

def main():
    # Membuat objek queue
    antrian = queue.Queue()

    # masukkin total antrian
    total_antrian = int(input("Masukkan total antrian: "))

    # minta masukkin nama pelanggan dan memasukkannya ke dalam antrian
    for i in range(total_antrian):
        nama_pelanggan = input("Masukkan nama pelanggan ke-{}: ".format(i+1))
        antrian.put(nama_pelanggan)  # Enqueue nama pelanggan ke dalam antrian

    # pemrosesan antrian
    while not antrian.empty():
        nama_pelanggan = antrian.get()  # Dequeue nama pelanggan dari antrian
        print("Melayani pelanggan:", nama_pelanggan)
        time.sleep(30)  # Delay 30 detik untuk melayani pelanggan berikutnya

    print("Semua pelanggan telah dilayani.")

if __name__ == "__main__":
    main()
