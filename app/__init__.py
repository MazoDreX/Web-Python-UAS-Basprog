from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
load_dotenv()


DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

# MySQL configurations
app.secret_key = 'basprog'
app.config['MYSQL_HOST'] = DATABASE_HOST
app.config['MYSQL_USER'] = DATABASE_USER
app.config['MYSQL_PASSWORD'] = DATABASE_PASSWORD
app.config['MYSQL_DB'] = DATABASE_NAME

try:
    mysql = MySQL(app)
    print("Berhasil terhubung ke database!")
except Exception as e:
    print("Error menghubungkan ke database:", e)

from app import routes

