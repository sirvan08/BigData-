# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="db_uasbigdata"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan struktur tabel 'mahasiswa'

create_table_query = """

CREATE TABLE db_uasbigdata (

    id INT AUTO_INCREMENT PRIMARY KEY,

    kode_provinsi int(100),

    nama_provinsi VARCHAR(100),

    kode_kabupaten_kota int(100),

    nama_kabupaten_kota varchar(100),

    jumlah_toko int(100),
    
    satuan varchar(100),

    tahun int(100)
    

)

"""

 

# Eksekusi perintah SQL untuk membuat tabel

db_cursor.execute(create_table_query)

 

# Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()