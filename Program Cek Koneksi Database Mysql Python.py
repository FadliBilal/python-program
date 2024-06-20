import mysql.connector

def cek_koneksi():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=""
        )
        if conn.is_connected():
            print("Terhubung dengan MySQL database")
    except mysql.connector.Error as e:
        print(f"Error koneksi | {e}")
    finally:
        conn.close()

cek_koneksi()