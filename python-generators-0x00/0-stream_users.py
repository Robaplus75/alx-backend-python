import uuid
from itertools import islice
import csv

def stream_users():
    with open('user_data.csv', 'r') as file:
        read_file = csv.DictReader(file)
        for row in read_file:
            user_id = uuid.uuid4()
            yield {
                'user_id': str(user_id),
                'name': row['name'],
                'email': row['email'],
                'age': row['age'],
            }
