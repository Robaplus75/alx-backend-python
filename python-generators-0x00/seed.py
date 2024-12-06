import mysql.connector
from mysql.connector import Error
import csv
import uuid

def connect_db():
    try:
        db_connection = mysql.connector.connect(
                    username="robel",
                    password="123",
                    host="localhost",
                )
        return db_connection
    except Error as e:
        print(e)
        return None

def create_database(connection):
    try:
        db_cursor = connection.cursor()
        db_cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    except Error as e:
        print(e)

def connect_to_prodev():
    try:
        db_connection = mysql.connector.connect(
                    username="robel",
                    password="123",
                    host="localhost"
                )
        db_cursor = db_connection.cursor()
        db_cursor.execute("use ALX_prodev")
        return db_connection
    except Error as e:
        print(e)

def create_table(connection):
    try:
        db_cursor = connection.cursor()
        db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                age DECIMAL(5, 2) NOT NULL
            );
        """)
    except Error as e:
        print("create table error")
        print(e)
    finally:
        db_cursor.close()

def insert_data(connection, data):
    try:
        db_cursor = connection.cursor()
        with open(data, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                db_cursor.execute("INSERT INTO user_data (user_id, name, email, age) VALUES ('{}', '{}', '{}', {});".format(str(uuid.uuid4()), row["name"], row["email"], row["age"]))
        connection.commit()
    except Error as e:
        print("insert data error")
        print(e)
    finally:
        db_cursor.close()
