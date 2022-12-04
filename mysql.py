# mysql-connector-python kütüphanesini kurun
#!pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

# MySQL veritabanı ayarlarını yapın
DB_HOST = "localhost"
DB_USERNAME = "root"
DB_PASSWORD = "password"
DB_NAME = "mydb"
DB_TABLE = "users"

# MySQL veritabanına bağlanın
try:
    connection = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_NAME)
    cursor = connection.cursor()
except Error as error:
    print(f"Veritabanına bağlanırken hata oluştu: {error}")

# Kullanıcı adı ve parolayı kontrol eden bir fonksiyon yazın
def check_user(username, password):
    # Kullanıcı adı ve parolasını kontrol eden bir SQL sorgusu yazın
    query = f"SELECT * FROM {DB_TABLE} WHERE username = '{username}' AND password = '{password}'"

    # Sorguyu çalıştırın
    cursor.execute(query)

    # Eğer kullanıcı mevcutsa True, değilse False döndürün
    return cursor.fetchone() is not None

# Kullanıcı adı ve parolayı alan bir form oluşturun
username = input("Kullanıcı adı: ")
password = input("Parola: ")

# Kullanıcı adı ve parolasını kontrol edin
if check_user(username, password):
    print("Giriş başarılı")
else:
    print("Kullanıcı adı veya parola hatalı")

# MySQL veritabanı bağlantısını kapatın
cursor.close()
connection.close()
