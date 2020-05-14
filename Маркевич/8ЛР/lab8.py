import sys
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path

import pandas as pd
from IPython.core.display import display
from bson import Code
from pymongo import MongoClient, DESCENDING

input_file = 'input.csv' 
database_name, collection_name = 'database', 'visit_logs'
client = MongoClient('localhost', 27017)
collection = client[database_name][collection_name]


def show():
    data = pd.read_csv(input_file, header=0, parse_dates=['timestamp'])
    records = data.to_dict(orient='records')

    return data

def load():
    data = pd.read_csv(input_file, header=0, parse_dates=['timestamp'])
    records = data.to_dict(orient='records')

    return collection.insert_many(records).inserted_ids


def task1():
    unique_urls = collection.distinct('url')

    return unique_urls


def task2(url):
    ips = collection \
        .find({'url': url}, {'_id': False, 'ip': True}) \
        .distinct('ip')
    
    return ips


def task3(from_datetime, to_datetime):
    urls_visited_in_date_range = collection \
        .find({'timestamp': {'$lte': to_datetime, '$gte': from_datetime}}) \
        .distinct('url')
    
    return urls_visited_in_date_range


def task4(ip):
    visited_by_user_urls = collection \
        .find({'ip': ip}, {'_id': False, 'url': True}) \
        .distinct('url')
    
    return visited_by_user_urls


def task5():
    map_func = Code('''
        function() {
           emit(this.url, this.time_spent);
        };''')
    reduce_func = Code('''
        function(url, timeSpent) {
           return Array.sum(timeSpent);
        };''') 
    results = collection \
        .map_reduce(map_func, reduce_func, 'records') \
        .find() \
        .sort('value', DESCENDING)

    return list(results)


def task6():
    map_func = Code('''
        function() {
           emit(this.url, 1);
        };''')
    reduce_func = Code('''
        function(url, count) {
           return count.length;
        };''')
    results = collection \
        .map_reduce(map_func, reduce_func, 'records') \
        .find() \
        .sort('value', DESCENDING)

    return list(results)


def task7(from_datetime, to_datetime):
    map_func = Code('''
        function() {
           emit(this.url, 1);
        };''')
    reduce_func = Code('''
        function(url, count) {
           return count.length;
        };''')
    results = collection \
        .map_reduce(map_func, reduce_func, 'records', query={
            'timestamp': {'$lte': to_datetime, '$gte': from_datetime}}) \
        .find() \
        .sort('value', DESCENDING)

    return list(results)


def task8():
    map_func = Code('''
        function() {
           emit(this.ip, {'total_time_spent': this.time_spent, 'total_visits_count': 1});
        };''')
    reduce_func = Code('''
        function(url, values) {
           return values.reduce(
              (acc, cur) => {
                return Object.keys(Object.assign({}, acc, cur)).reduce(
                  (obj, k) => {obj[k] = (acc[k] || 0) + (cur[k] || 0); return obj;}, {})
              }, 
              {'total_time_spent': 0,'total_visits_count': 0}
           );
        };''')
    results = collection \
        .map_reduce(map_func, reduce_func, 'records') \
        .find() \
        .sort([
            ('_id', DESCENDING),
            ('value.total_time_spent', DESCENDING),
            ('value.total_visits_count', DESCENDING)
        ])

    return list(results)


def main():
    while True:
        print('0. show_csv', '1. load_to_db', '2. task1', '3. task2', '4. task3', '5. task4', 
              '6. task5', '7. task6', '8. task7', '9. task8', '10. exit', sep='\n')
        choice = int(input('Choose action:'))
        
        if choice == 0:
            print('Result:', show())
        if choice == 1:
            print('Result:', load())
        if choice == 2:
            print('Result:', task1())
        if choice == 3:
            url = input('which url? ')
            print('Result:', task2(url))
        if choice == 4:
            from_datetime = datetime.fromisoformat(input('input start date: '))
            to_datetime = datetime.fromisoformat(input('input end date: '))
            print('Result:', task3(from_datetime, to_datetime))
        if choice == 5:
            ip = input('which ip? ')
            print('Result:', task4(ip))
        if choice == 6:
            print('Result:', task5())
        if choice == 7:
            print('Result:', task6())
        if choice == 8:
            from_datetime = datetime.fromisoformat(input('input start date: '))
            to_datetime = datetime.fromisoformat(input('input end date: '))
            print('Result:', task7(from_datetime, to_datetime))
        if choice == 9:
            print('Result:', task8())
        if choice == 10:
            break



if __name__ == '__main__':
    main()
