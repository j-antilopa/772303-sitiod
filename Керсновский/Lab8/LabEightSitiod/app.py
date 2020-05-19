from flask import Flask, render_template, request
from readers.csvReader import csv_reader
from readers.xmlReader import xml_reader
from datetime import datetime
from models.models import BusFactory, TrainFactory
from utils.log_manager import create_log

app = Flask(__name__)

@app.route('/schedule')
def schedule():
    type_file = '.'+request.args.get('file_type')
    if type_file == ".xml" and request.args.get("data") == 'bus_schedule':
        data = list(xml_reader('data/' + request.args.get("data") + type_file, factory=BusFactory()))
    elif type_file == ".csv" and request.args.get("data") == 'bus_schedule':
        data = list(csv_reader('data/'+request.args.get("data")+type_file, factory=BusFactory()))
    elif type_file == ".csv":
        data = list(csv_reader('data/' + request.args.get("data") + type_file, factory=TrainFactory()))
    elif type_file == ".xml":
        data = list(xml_reader('data/' + request.args.get("data") + type_file, factory=TrainFactory()))
        data = []
    res = list(filter(lambda item: (request.args.get('station_start') or "") in item.station_start
                                   and (request.args.get('station_end') or "") in item.station_end
                                   and (datetime.strptime(item.time_start, '%Y-%m-%d %H:%M:%S').isoweekday() <= 5
                                   if bool(int(request.args.get("type_day") or 0))
                                   else datetime.strptime(item.time_end, '%Y-%m-%d %H:%M:%S').isoweekday() > 5)
                      , data))
    ip = request.environ['REMOTE_ADDR'] 
    create_log(ip, request.headers.get('Referer'))
    return render_template('schedule.html', data=res, all_data=data)

if __name__ == '__main__':
    app.run()
