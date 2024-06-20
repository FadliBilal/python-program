import mysql.connector

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        if connection.is_connected():
            print("Berhasil terhubung dengan database")
    except Exception as e:
        print(f"Error tidak ditemukan database: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()


if __name__ == '__main__':
    host = "localhost"
    user = "yourusername"  # user localhost kamu (jika masih eror coba ganti root karena dasarnya root)
    password = "yourpassword"  # password localhost kamu (jika tidak ada kosongkan saja)
    database = "yourdatabase"  # nama database yang mau kamu hubungkan

    create_connection(host, user, password, database)
