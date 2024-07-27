"""
Import module yang dibutuhkan seperti flask, dotenv, mysql, dan app.utils.function
"""
from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL
from app.utils.function import make_table, matkul_TI_insert
import os

app = Flask(__name__) #Inisialisasi Flask
load_dotenv() #buka file .env

#Ambil data dari .env
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

#Konfigurasi database mysql
app.secret_key = 'basprog'
app.config['MYSQL_HOST'] = DATABASE_HOST
app.config['MYSQL_USER'] = DATABASE_USER
app.config['MYSQL_PASSWORD'] = DATABASE_PASSWORD
app.config['MYSQL_DB'] = DATABASE_NAME

"""
Hubungkan aplikasi ke database mysql dengan modul mysql
"""
try:
    mysql = MySQL(app)
    print("Berhasil terhubung ke database!")
    try:
        with app.app_context(): #Buat tabel jika belum ada
            make_table(mysql.connection) 
        print("Tabel Mahasiswa, Matakuliah_TI, Mahasiswa_Matakuliah telah dibuat")
        try:
            with app.app_context(): #Masukan data matakuliah_TI
                matkul_TI_insert(mysql.connection)
        except Exception as e:
            print("Error menambahkan data matakuliah_TI:", e)
    except Exception as e:
        print("Error membuat tabel:", e)
except Exception as e:
    print("Error menghubungkan ke database:", e)


from app import routes #Import routes

