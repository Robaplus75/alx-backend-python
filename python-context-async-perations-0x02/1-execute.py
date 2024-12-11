#!/bin/env python3

import mysql.connector

class ExecuteQuery:
    def __init__(self, query, parameter=None):
        self.query = query
        self.parameter = parameter

    def __enter__(self):
        db_conn = mysql.connector.connect(user="robel", host="localhost", password="123")
        db_cursor = db_conn.cursor()
        db_cursor.execute("use airbnb_db")
        if self.parameter:
            db_cursor.execute(self.query, self.parameter)
        else:
            db_cursor.execute(self.query)

        output = db_cursor.fetchall()
        return output

    def __exit__(self, exc_type, exc_value, traceback):
        return False

with ExecuteQuery("SELECT * FROM users WHERE age > ?", 25) as output:
    for row in output:
        print(row)
