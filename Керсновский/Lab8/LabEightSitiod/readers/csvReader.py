import csv

def csv_reader(path, factory):
    with open(path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for obj in list(reader):
            yield factory.create_product(obj)