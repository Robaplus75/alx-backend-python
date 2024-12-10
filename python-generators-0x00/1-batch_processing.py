from mysql.connector import Error
from config import Config
import mysql.connector

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user['age'] > 25]
        for user in filtered_users:
            print(user)  
        return filtered_users

def stream_users_in_batches(batch_size):
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='airbnb_sys',
            password=Config.PASSWORD,
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            yield rows
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()
