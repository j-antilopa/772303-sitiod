import sys
from argparse import ArgumentParser
from datetime import datetime
from os import environ
from pathlib import Path
from pprint import pprint

import pandas as pd
from IPython.core.display import display
from bson import Code
from pymongo import MongoClient, DESCENDING

username, password = environ.get('mongo_username'), environ.get('mongo_password')

database_name, collection_name = 'db', 'visit_info'
client = MongoClient('mongo', 27017, username=username, password=password)
db = client[database_name]
collection = db[collection_name]

map_funcs = {
    'task5': Code('''
        function() {
           emit(this.url, this.time_spent);
        };'''),
    'task6': Code('''
        function() {
           emit(this.url, 1);
        };'''),
    'task8': Code('''
        function() {
           emit(this.ip, {'total_time_spent': this.time_spent, 'total_visits_count': 1});
        };''')
}

reduce_funcs = {
    'task5': Code('''
        function(url, timeSpent) {
           return Array.sum(timeSpent);
        };'''),
    'task6': Code('''
        function(url, count) {
           return count.length;
        };'''),
    'task8': Code('''
        function(url, values) {
           return values.reduce(
              (acc, cur) => {
                return Object.keys(Object.assign({}, acc, cur)).reduce(
                  (obj, k) => {obj[k] = (acc[k] || 0) + (cur[k] || 0); return obj;}, {})
              }, 
              {'total_time_spent': 0,'total_visits_count': 0}
           );
        };''')
}


def load_data(args):
    data = pd.read_csv(args.path, header=0, parse_dates=['timestamp'])
    records = data.to_dict(orient='records')
    if args.show:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
            display(data)
        return '', []
    collection.delete_many({})
    return 'Inserted data:', collection.insert_many(records).inserted_ids


def task1(*args):
    unique_urls = collection.distinct('url')
    return 'All unique urls:', unique_urls


def task2(args):
    url = args.url
    ips = collection \
        .find({'url': url}, {'_id': False, 'ip': True}) \
        .distinct('ip')
    return f'All ips visited this url({url}):', ips


def task3(args):
    from_datetime, to_datetime = args.dates
    urls_visited_in_date_range = collection \
        .find({'timestamp': {'$lte': to_datetime, '$gte': from_datetime}}) \
        .distinct('url')
    return f'All urls visited from {from_datetime} to {to_datetime}:', urls_visited_in_date_range


def task4(args):
    ip = args.ip
    visited_by_user_urls = collection \
        .find({'ip': ip}, {'_id': False, 'url': True}) \
        .distinct('url')
    return f'All visited urls from this ip({ip}):', visited_by_user_urls


def task5(*args):
    results = collection \
        .map_reduce(map_funcs['task5'], reduce_funcs['task5'], 'records') \
        .find() \
        .sort('value', DESCENDING)
    return 'All urls with total visit time:', list(results)


def task6(*args):
    results = collection \
        .map_reduce(map_funcs['task6'], reduce_funcs['task6'], 'records') \
        .find() \
        .sort('value', DESCENDING)
    return 'All urls with visits amount:', list(results)


def task7(args):
    from_datetime, to_datetime = args.dates
    results = collection \
        .map_reduce(map_funcs['task6'], reduce_funcs['task6'], 'records', query={
            'timestamp': {'$lte': to_datetime, '$gte': from_datetime}}) \
        .find() \
        .sort('value', DESCENDING)

    return 'All urls with visits amount (visited in concrete datetime range):', list(results)


def task8(args):
    default_sort_list = [
        ('_id', DESCENDING),
        ('value.total_time_spent', DESCENDING),
        ('value.total_visits_count', DESCENDING)
    ]
    sort_list = [default_sort_list[i] for i in args.order]
    results = collection \
        .map_reduce(map_funcs['task8'], reduce_funcs['task8'], 'records') \
        .find() \
        .sort(sort_list)
    return 'All ips with total visits amount and time spent:', list(results)


def _create_parser():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    load_data_parser = subparsers.add_parser('load_data')
    load_data_parser.add_argument('path', nargs='?', type=Path)
    load_data_parser.add_argument('-s', '--show', action='store_true', default=False)
    load_data_parser.set_defaults(func=load_data)

    task1_parser = subparsers.add_parser('task1')
    task1_parser.set_defaults(func=task1)

    task5_parser = subparsers.add_parser('task5')
    task5_parser.set_defaults(func=task5)

    task6_parser = subparsers.add_parser('task6')
    task6_parser.set_defaults(func=task6)

    task2_parser = subparsers.add_parser('task2')
    task2_parser.add_argument('url', nargs='?', type=str)
    task2_parser.set_defaults(func=task2)

    task3_parser = subparsers.add_parser('task3')
    task3_parser.add_argument('dates', nargs=2, type=datetime.fromisoformat)
    task3_parser.set_defaults(func=task3)

    task4_parser = subparsers.add_parser('task4')
    task4_parser.add_argument('ip', nargs='?', type=str)
    task4_parser.set_defaults(func=task4)

    task7_parser = subparsers.add_parser('task7')
    task7_parser.add_argument('dates', nargs=2, type=datetime.fromisoformat)
    task7_parser.set_defaults(func=task7)

    task8_parser = subparsers.add_parser('task8')
    task8_parser.add_argument('-o', '--order', nargs='+', type=int, default=[0, 1, 2], choices=range(3))
    task8_parser.set_defaults(func=task8)

    return parser


def main():
    parser = _create_parser()
    args = parser.parse_args(sys.argv[1:])

    title, values = getattr(args, 'func', lambda v: print('Error!'))(args)
    print(title)
    pprint(values, indent=1, width=120)


if __name__ == '__main__':
    main()
