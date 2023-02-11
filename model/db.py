import csv
import random
from datetime import datetime

PATH = './db/notes.csv'

def add_metadata(data):
    if data['id'] == 0:
        data['id'] = random_id()
        data['date'] = datetime.now().strftime('%d.%m.%Y %H:%M')
    return data

def save(data, mod='a'):
    data = add_metadata(data)
    with open(PATH, mod) as db:
        writer = csv.DictWriter(db, fieldnames=list(data.keys()), quoting=csv.QUOTE_NONNUMERIC)
        if is_empty():
            writer.writeheader()
        writer.writerow(data)


def overwrite(data_list):
    with open(PATH, 'w') as db:
        db.write('')
    for data in data_list:
        save(data)


def read():
    with open(PATH, 'r', newline='') as db:
        reader = csv.DictReader(db)
        return list(reader)


def find(key_word):
    notes = read()
    result = []
    for row in notes:
        if (key_word in row['note'].lower()) or (key_word in row['date']):
            result.append(row)
    return result


def is_empty():
    res = read()
    if len(res) == 0:
        return True
    return False


def random_id():
    return random.randint(1, 1000)
