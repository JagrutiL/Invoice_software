import mysql.connector as mysql
import MySQLdb

class Database:
    @staticmethod
    def connect_dbs():
        dbPrefix = 'invoice'
        connection = MySQLdb.connect(
            user = 'root',
            passwd = 'root',
            host = 'localhost',
            db= dbPrefix
        )
        return connection

connection = Database.connect_dbs()
cursor = connection.cursor() 

print("Connected to the database.")

# cursor.execute("""CREATE DATABASE `invoice`;
# USE `invoice`;""")
