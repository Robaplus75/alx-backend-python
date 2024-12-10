import sqlite3
import functools

def log_queries(orig_func):
    @functools.wraps(orig_func)
    def wrapper(*args, **kwargs):
        from datetime import datetime
        result = orig_func(*args, **kwargs)
        print(result)
        print("Completed at: {}".format(datetime.now()))
        return result
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

users = fetch_all_users(query="SELECT * FROM users")
