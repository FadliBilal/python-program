import mysql.connector

class Database:
    def __init__(self, host="localhost", user="root", password="", database="db_sepatu"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()

    def create_database(self):
        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
        conn.close()

    def create_table_sepatu(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sepatu (
            kode VARCHAR(50) PRIMARY KEY,
            merk VARCHAR(255),
            ukuran INT,
            harga INT
        )
        """)

    def insert(self, sepatu):
        query = "INSERT INTO sepatu (kode, merk, ukuran, harga) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (sepatu.kode, sepatu.merk, sepatu.ukuran, sepatu.harga))
        self.conn.commit()

    def read(self):
        self.cursor.execute("SELECT * FROM sepatu")
        result = self.cursor.fetchall()
        return result

    def update(self, sepatu):
        query = "UPDATE sepatu SET merk=%s, ukuran=%s, harga=%s WHERE kode=%s"
        self.cursor.execute(query, (sepatu.merk, sepatu.ukuran, sepatu.harga, sepatu.kode))
        self.conn.commit()

    def delete(self, kode):
        query = "DELETE FROM sepatu WHERE kode=%s"
        self.cursor.execute(query, (kode,))
        self.conn.commit()

    def close(self):
        self.conn.close()


class Sepatu:
    def __init__(self, kode, merk, ukuran, harga):
        self.kode = kode
        self.merk = merk
        self.ukuran = ukuran
        self.harga = harga


def main():
    db = Database()
    db.create_database()
    db.connect()
    db.create_table_sepatu()

    while True:
        print("\n=== APLIKASI CRUD SEPATU ===")
        print("1. Tambah Data Sepatu")
        print("2. Lihat Data Sepatu")
        print("3. Update Data Sepatu")
        print("4. Hapus Data Sepatu")
        print("5. Keluar")

        try:
            pilihan = int(input("Masukkan pilihan (1/2/3/4/5): "))
        except ValueError:
            print("Masukkan pilihan berupa angka")
            continue

        if pilihan == 1:
            kode = input("Kode sepatu: ")
            merk = input("Merk sepatu: ")
            ukuran = int(input("Ukuran sepatu: "))
            harga = int(input("Harga sepatu: Rp "))
            sepatu = Sepatu(kode, merk, ukuran, harga)
            db.insert(sepatu)
            print("Data sepatu berhasil ditambahkan")
        elif pilihan == 2:
            result = db.read()
            if not result:
                print("Tidak ada data sepatu")
            else:
                print("\nData Sepatu:")
                for row in result:
                    print("Kode:", row[0])
                    print("Merk:", row[1])
                    print("Ukuran:", row[2])
                    print("Harga: Rp ", row[3])
                    print("--------------------")
        elif pilihan == 3:
            kode = input("Masukkan kode sepatu yang ingin diupdate: ")
            merk = input("Merk baru: ")
            ukuran = int(input("Ukuran baru: "))
            harga = int(input("Harga baru: Rp "))
            sepatu = Sepatu(kode, merk, ukuran, harga)
            db.update(sepatu)
            print("Data sepatu berhasil diupdate")
        elif pilihan == 4:
            kode = input("Masukkan kode sepatu yang ingin dihapus: ")
            db.delete(kode)
            print("Data sepatu berhasil dihapus")
        elif pilihan == 5:
            break
        else:
            print("Pilihan tidak valid")

    db.close()
    print("Program selesai")


if __name__ == "__main__":
    main()