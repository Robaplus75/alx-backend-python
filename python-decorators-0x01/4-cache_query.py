import sqlite3 

import functools
import time

query_cache = {}

def cache_query(func):
    @functools.wraps(func)
    def wrapper(query, *args, **kwargs):
        if cache_query[query]:
            return cache_query[query]
        else:
            result = func(query, *args, **kwargs)
            cache_query[query] = result
            return result
    return wrapper
        
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
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

users = fetch_users_with_cache(query="SELECT * FROM users")
users_again = fetch_users_with_cache(query="SELECT * FROM users")
