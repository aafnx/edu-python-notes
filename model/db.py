import csv

PATH = './db/notes.csv'
# columns = ['date', 'note']


def save(data):
    with open(PATH, 'a', newline='') as db:
        writer = csv.DictWriter(db, fieldnames=list(data.keys()), quoting=csv.QUOTE_NONNUMERIC)
        if is_empty():
          writer.writeheader()
        writer.writerow(data)

def read():
    with open(PATH, 'r', newline='') as db:
        reader = csv.DictReader(db) 
        result = []
        for row in reader:
            result.append(row)
        return result

def is_empty():
    res = read()
    if len(res) == 0:
        return True
    return False
