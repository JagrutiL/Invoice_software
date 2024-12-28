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

# print("Connected to the database.")

# cursor.execute("""CREATE DATABASE `invoice`;
# USE `invoice`;""")


# sql_query = """DROP TABLE IF EXISTS `user`;"""
# cursor.execute(sql_query)



# cursor.execute("""CREATE TABLE user (
#   id int NOT NULL AUTO_INCREMENT,
#   user_id int NOT NULL,
#   user_name varchar(128) NOT NULL,
#   email varchar(64) NOT NULL,
#   password varchar(32) NOT NULL,
#   mobile varchar(10) NOT NULL,
#   admin tinyint NOT NULL DEFAULT '0' COMMENT '0-Not Defined, 1-Admin, 2-Local User',
#   active tinyint NOT NULL DEFAULT '0' COMMENT '0-Not Defined, 1-Inactive, 2-Active',
#   date_created datetime NOT NULL,
#   PRIMARY KEY (id)
# ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf16)""")


# sql_query = """DROP TABLE IF EXISTS `payment_details`;"""
# cursor.execute(sql_query)



# cursor.execute("""
# CREATE TABLE payment_details (
#   id INT NOT NULL AUTO_INCREMENT,
#   item_name VARCHAR(255) NOT NULL,
#   details TEXT,
#   vendor_name VARCHAR(255) NOT NULL,
#   quantity INT DEFAULT NULL,
#   amount FLOAT,
#   payment VARCHAR(100),
#   user_id int NOT NULL,
#   admin tinyint NOT NULL DEFAULT '0' COMMENT '0-Not Defined, 1-Admin, 2-Local User', 
#   status tinyint NOT NULL DEFAULT '0' COMMENT '0-Pending, 1-Approved, 2-Payment Done upload Invoice, 3-Completed, 4-Rejected' 
#   PRIMARY KEY (id)
# ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf16;
# """)


# print("created successfully")



