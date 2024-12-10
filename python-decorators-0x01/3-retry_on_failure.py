import sqlite3 
import functools
import time

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            count = 0
            while count < retries:
                try:
                    result = func(conn, *args, **kwargs)
                    return result
                except Exception as e:
                    count += 1
                    if count >= retries:
                        raise e
                    print(f"Attempt {count} failed. Retrying in {delay} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(*args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

users = fetch_users_with_retry()
print(users)
