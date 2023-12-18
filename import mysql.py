import mysql.connector

import pandas as pd

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="db_uasbigdata"

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Contoh pernyataan SQL SELECT

select_query = "SELECT * FROM db_uasbigdata"

 

# Eksekusi pernyataan SELECT

db_cursor.execute(select_query)

 

# Ambil hasil SELECT

results = db_cursor.fetchall()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()

 

# Konversi hasil SELECT menjadi dataframe pandas

df = pd.DataFrame(results, columns=["id", "kode_provinsi", "nama_provinsi", "kode_kabupaten_kota", "nama_kabupaten_kota", "jumlah_toko", "satuan", "tahun"])

 

# Simpan dataframe sebagai file Excel

df.to_csv("datasetjawabarat.csv", index=False)

 

print("Data telah disimpan dalam file Excel 'data_mahasiswa.csv'") #csv / xlsx

 