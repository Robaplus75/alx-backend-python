seed = __import__('seed')

def find_average():
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    average = total_age / count
    print(f"Average age of users: {average}")

def stream_user_ages():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row['age']

