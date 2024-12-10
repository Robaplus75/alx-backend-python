#!/usr/bin/env python3
import mysql.connector

class DatabaseConnection:
    def __init__(self, user, host, password):
        self.user = user
        self.host = host
        self.password = password

    def __enter__(self):
        db_conn = mysql.connector.connect(user=self.user, host=self.host, password=self.password)
        return db_conn

    def __exit__(self, exc_type, exc_value, traceback):
        db_conn.close()
        return False


with DatabaseConnection('robel', 'localhost', '123') as db:
    db_cursor = db.cursor()
    db_cursor.execute("use airbnb_db;")
    db_cursor.execute("SELECT * FROM User;")

    rows = db_cursor.fetchall()

    for row in rows:
        print(row)
