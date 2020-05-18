import json

import pandas as pd
import pymongo
from bson.code import Code


def convert_csv_to_json(csv_file_path='data.csv', json_file_path='data.json'):
    data = pd.read_csv(csv_file_path)
    data.to_json(json_file_path, 'records')


def load_json_into_db(file_path='data.json'):
    with pymongo.MongoClient("mongodb://localhost:27017/") as client:
        db = client["main_db"]
        col = db["server_log"]
        col.drop()

        with open(file_path) as f:
            file_data = json.load(f)

        col.insert_many(file_data)


def generate_urls_list():
    with pymongo.MongoClient("mongodb://localhost:27017/") as client:
        db = client["main_db"]
        col = db["server_log"]

        for each in col.find({}, {"_id": 0, "URL": 1}).sort("URL"):
            print(each)


def generate_ips_list_who_visited_url(url):
    with pymongo.MongoClient("mongodb://localhost:27017/") as client:
        db = client["main_db"]
        col = db["server_log"]

        for each in col.find({"URL": url}, {"_id": 0, "IP": 1}):
            print(each)


def generate_urls_visited_in_certain_time_period(start_timestamp,
                                                 end_timestamp):
    with pymongo.MongoClient("mongodb://localhost:27017/") as client:
        db = client["main_db"]
        col = db["server_log"]

        for each in col.find(
                {"timeStamp": {"$gt": start_timestamp, "$lt": end_timestamp}},
                {"_id": 0, "URL": 1}
        ).sort("URL"):
            print(each)


def generate_urls_visited_by_certain_ip(ip):
    with pymongo.MongoClient("mongodb://localhost:27017/") as client:
        db = client["main_db"]
        col = db["server_log"]

        for each in col.find({"IP": ip}, {"_id": 0, "URL": 1}).distinct("URL"):
            print(each)


def generate_urls_list_with_total_time_spent():
    map = Code("""function map() {
    var urls = this.URL;
    var length = this.timeSpent;
    emit(urls, length);
    };""")

    reduce = Code("""function reduce(key, values) {
    var totalTimeSpent = 0;
    for (var i = 0; i < values.length; i++) {
        totalTimeSpent += values[i];
    }
    return totalTimeSpent;
    };""")

    with pymongo.MongoClient("mongodb://localhost:27017/") as client:
        db = client["main_db"]
        col = db["server_log"]
        results_col = 1.map_reduce(map, reduce, 'results')

        for each in results_col.find().sort("value", pymongo.DESCENDING):
            print(each)


def generate_urls_list_with_visit_sum():
    map = Code("""function map() {
    var urls = this.URL;
    emit(urls, 1);
    };""")

    reduce = Code("""function reduce(key, values) {
    var count = 0;
    for (var i = 0; i < values.length; i++) {
        count += values[i];
    }
    return count;
    };""")

    with pymongo.MongoClient("mongodb://localhost:27017/") as client:
        db = client["main_db"]
        col = db["server_log"]
        results_col = col.map_reduce(map, reduce, 'results')

        for each in results_col.find().sort("value", pymongo.DESCENDING):
            print(each)


def generate_urls_list_with_days_time_count(start_timestamp, end_timestamp):
    map = Code("""function map() {
    var url = this.URL;
    var date = new Date(this.timeStamp * 1000);
    emit({url: url, date: date}, 1);
    };""")

    reduce = Code("""function reduce(key, values) {
    var count = 0;
    for (var i = 0; i < values.length; i++) {
        count += values[i];
    }
    return count;
    };""")

    with pymongo.MongoClient("mongodb://localhost:27017/") as client:
        db = client["main_db"]
        col = db["server_log"]
        results_col = col.map_reduce(map,
                                     reduce,
                                     'results',
                                     query={
                                         "timeStamp": {"$gt": start_timestamp,
                                                       "$lt": end_timestamp}})

        for each in results_col.find().sort("value", pymongo.DESCENDING).sort(
                "_id", pymongo.DESCENDING
        ):
            print(each)


def generate_ips_list_with_amount_and_time_spent_sum():
    map_count = Code("""function map() {
    var ip = this.IP;
    emit(ip, 1);
    };""")

    map_time_spent = Code("""function map() {
    var ip = this.IP;
    var timeSpent = this.timeSpent;
    emit(ip, timeSpent);
    };""")

    reduce_sum = Code("""function reduce(key, values) {
    var count = 0;
    for (var i = 0; i < values.length; i++) {
        count += values[i];
    }
    return count;
    };""")

    with pymongo.MongoClient("mongodb://localhost:27017/") as client:
        db = client["main_db"]
        col = db["server_log"]
        results_count = col.map_reduce(map_count, reduce_sum, 'results_count')
        results_time_spent = col.map_reduce(map_time_spent,
                                            reduce_sum,
                                            'results_time_spent')

        for each in results_count.find():
            for time_spent in results_time_spent.find({"_id": each['_id']}):
                current_item = each
                current_item['time_spent'] = time_spent['value']
                print(current_item)


if __name__ == "__main__":
    while True:
        print('',
              '1) Из CSV в JSON',
              '2) Из JSON в БД',
              '3) Весь список',
              '4) Поиск посетителей по URL',
              '5) Поиск URL-ов по временному периоду',
              '6) Поиск URL-ов по IP посетителя',
              '7) Суммарное время посещения каждого ресурса',
              '8) Суммарное количество посещений каждого ресурса',
              '9) Количества посещений каждого ресурса в день за заданный период',
              '10) Список суммарное количества и суммарной длительности посещений ресурсов',
              '11) Выход из программы', sep='\n')
        try:
            choice = int(input('Выберите действие: '))

            if not 0 < choice < 12:
                raise ValueError

            if choice == 1:
                convert_csv_to_json()
            if choice == 2:
                load_json_into_db()
            if choice == 3:
                generate_urls_list()
            if choice == 4:
                url = input('Введите URL: ')
                generate_ips_list_who_visited_url(url)
            if choice == 5:
                start_timestamp = int(input('От: '))
                end_timestamp = int(input('До: '))
                generate_urls_visited_in_certain_time_period(start_timestamp,
                                                             end_timestamp)
            if choice == 6:
                ip = input('Введите IP: ')
                generate_urls_visited_by_certain_ip(ip)
            if choice == 7:
                generate_urls_list_with_total_time_spent()
            if choice == 8:
                generate_urls_list_with_visit_sum()
            if choice == 9:
                start_timestamp = int(input('От: '))
                end_timestamp = int(input('До: '))
                generate_urls_list_with_days_time_count(start_timestamp,
                                                        end_timestamp)
            if choice == 10:
                generate_ips_list_with_amount_and_time_spent_sum()
            if choice == 11:
                break

        except ValueError:
            print('неправильный ввод')
            continue