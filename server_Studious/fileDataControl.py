import json
import csv
from os import path, remove, makedirs
import datetime
from PyQt6.QtWidgets import *
import sys
sys.stdout.reconfigure(encoding='utf-8')

class fileDataControl:
    def __init__(self, id:str):
        self.user = id
        self._ntime = datetime.datetime.now()
        self.ntime = self._ntime.strftime("%d/%m/%Y")
        self.monday = (self._ntime - datetime.timedelta(days=self._ntime.weekday())).strftime("%d/%m/%Y")
        if self.create_folder():  self.default_data()
        self.readDataTime()
        
    def create_folder(self) -> bool:
        if not path.exists("data"):
            makedirs("data")
        if not path.exists(f"data/{self.user}_data"):
            makedirs(f"data/{self.user}_data")
            with open(f"data/{self.user}_data/time.json", "w") as f:
                pass
            with open(f"data/{self.user}_data/tableWeek.csv", "w") as f:
                pass
            with open(f"data/{self.user}_data/describeItem.csv", "w") as f:
                pass
            with open(f"data/{self.user}_data/settings.json", 'w') as f:
                pass
            return True
        else:
            if not path.exists(f"data/{self.user}_data/time.json"):
                with open(f"data/{self.user}_data/time.json", 'w') as f:
                    pass
                return True
            if not path.exists(f"data/{self.user}_data/tableWeek.csv"):
                with open(f"data/{self.user}_data/tableWeek.csv", 'w') as f:
                    pass
                return True
            if not path.exists(f"data/{self.user}_data/describeItem.csv"):
                with open(f"data/{self.user}_data/describeItem.txt", 'w') as f:
                    pass
                return True
            if not path.exists(f"data/{self.user}_data/settings.json"):
                with open(f"data/{self.user}_data/settings.json", 'w') as f:
                    pass
                return True
        return False

    def default_data(self):
        dataTime = {f"{self.ntime}":{"Học Toán": 0.0, "Học Văn": 0.0, "Học Tiếng Anh": 0.0}}

        Wdata = [[self.monday,'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'],
                 ['', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '']]

        dataSettings = {"main": {"sound": True, "label": "0"}, 
                        "settings": {"musicType": 0, "autostart": False, "noti": False, "autosession": False, "space": False}, 
                        "tasks": {"1": {"combo": "Học Toán", "work": 25, "rest": 5}, "2": {"combo": "Học Văn", "work": 25, "rest": 5}, "3": {"combo": "Học Tiếng Anh", "work": 25, "rest": 5}, 
                                  "4": {"combo": "", "work": 25, "rest": 5}, "5": {"combo": "", "work": 25, "rest": 5}, "6": {"combo": "", "work": 25, "rest": 5}, 
                                  "7": {"combo": "", "work": 25, "rest": 5}}}

        describeData = [['']*7]*7

        self.dataTimeJson = dataTime

        with open(f'data/{self.user}_data/time.json', 'w', newline='', encoding="utf-8") as jsonfile:
            json.dump(dataTime, jsonfile,  ensure_ascii=False)

        with open(f'data/{self.user}_data/settings.json', 'w', newline='', encoding="utf-8") as jsonfile:
            json.dump(dataSettings, jsonfile,  ensure_ascii=False)

        with open(f"data/{self.user}_data/tableWeek.csv", "w", encoding="utf-8", newline='') as csv_file:
            writer = csv.writer(csv_file)
            
            # Write each row of data to the CSV file
            for row in Wdata:
                writer.writerow(row)

        with open(f'data/{self.user}_data/describeItem.csv', 'w', newline='', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            
            # Write each row of data to the CSV file
            for row in describeData:
                writer.writerow(row)


    def readDataTime(self):
        with open(f"data/{self.user}_data/time.json", "r", encoding="utf-8") as jsonfile:
            self.dataTimeJson = json.load(jsonfile)
        if self.ntime not in self.dataTimeJson:
            with open(f"data/{self.user}_data/time.json", "w", encoding="utf-8") as jsonfile:
                    self.dataTimeJson[f"{self.ntime}"] = {}
                    json.dump(self.dataTimeJson, jsonfile,  ensure_ascii=False)
        return self.dataTimeJson

    def writeDataTime(self, data):
        with open(f'data/{self.user}_data/time.json', 'w', newline='', encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile,  ensure_ascii=False)

    def totalTimeDay(self):
        _temp = []
        for i in self.lb:
            _temp.append(self.dataTimeJson[self.ntime][i])
        s = sum(_temp)
        if s < 1:
            return f"Bạn đã sử dụng pomodoro được {round(s*60)} phút"
        elif s == int(s):    return f"Bạn đã sử dụng pomodoro được {int(s)} giờ"
        else:   return f"Bạn đã sử dụng pomodoro được {int(s)} giờ {round((s%1)*60)} phút"

    def dataChart(self, days: str):
        time = []
        totalTime = []
        detailTime = []
        
        with open(f"data/{self.user}_data/time.json", "r", encoding="utf-8") as jsonfile:
            datachart = json.load(jsonfile)
            key =  list(datachart[self.ntime].keys())
            for k in key:   detailTime.append([k, 0])
                        
        for i in range(int(days.split(" ")[0])-1, -1, -1):
            last_day = self._ntime - datetime.timedelta(days=i)
            last_day = last_day.strftime('%d/%m/%Y')
            if last_day not in datachart:
                datachart.update({last_day:{"Học Toán":0, "Học IELTS":0, "Làm việc":0}})

        if days == "1 ngày":
            for i in range(int(days.split(" ")[0])-1, -1, -1):
                last_day = self._ntime - datetime.timedelta(days=i)
                temp = []
                for x in range(len(key)):
                    try:_t = datachart[last_day.strftime('%d/%m/%Y')][key[x]]
                    except: _t = 0
                    detailTime[x][1] += _t
                    temp.append(_t)
                    
                time.append(last_day.strftime('%d/%m'))
                totalTime.append(sum(temp))
            
            return [time, totalTime, detailTime]

        elif days == "3 ngày" or days == "7 ngày":
            for i in range(int(days.split(" ")[0])-1, -1, -1):
                last_day = self._ntime - datetime.timedelta(days=i)
                temp = []
                for x in range(len(key)):
                    try:_t = datachart[last_day.strftime('%d/%m/%Y')][key[x]]
                    except: _t = 0
                    detailTime[x][1] += _t
                    temp.append(_t)
                    
                time.append(last_day.strftime('%d/%m'))
                totalTime.append(sum(temp))
            
            return [time, totalTime, detailTime]
        elif days == "30 ngày":
            temp = []
            for i in range(int(days.split(" ")[0])-3, -1, -1):
                last_day = self._ntime - datetime.timedelta(days=i)
                for x in range(len(key)):
                    try:_t = datachart[last_day.strftime('%d/%m/%Y')][key[x]]
                    except: _t = 0
                    detailTime[x][1] += _t
                    temp.append(_t)
                
                if i%7 == 0 and i != 27:
                    time.append(f"{(last_day - datetime.timedelta(days=6)).strftime('%d/%m')}-{last_day.strftime('%d/%m')}")
                    totalTime.append(sum(temp))
                    temp = []

            return [time, totalTime, detailTime]
        
        elif days == "90 ngày":
            temp = []
            for i in range(int(days.split(" ")[0])-1, -1, -1):
                last_day = self._ntime - datetime.timedelta(days=i)
                for x in range(len(key)):
                    try:_t = datachart[last_day.strftime('%d/%m/%Y')][key[x]]
                    except: _t = 0
                    detailTime[x][1] += _t
                    temp.append(_t)
                
                if i%30 == 0 and i != 90:
                    time.append(f"{(last_day - datetime.timedelta(days=29)).strftime('%d/%m')}-{last_day.strftime('%d/%m')}")
                    totalTime.append(sum(temp))
                    temp = []
                    
            return [time, totalTime, detailTime]
        
        elif days == "365 ngày":
            temp = []
            for i in range(int(days.split(" ")[0])-6, -1, -1):
                last_day = self._ntime - datetime.timedelta(days=i)
                for x in range(len(key)):
                    try:_t = datachart[last_day.strftime('%d/%m/%Y')][key[x]]
                    except: _t = 0
                    detailTime[x][1] += _t
                    temp.append(_t)
                
                if i%60 == 0 and i != 360:
                    time.append(f"{(last_day - datetime.timedelta(days=59)).strftime('%d/%m')}-{last_day.strftime('%d/%m')}")
                    totalTime.append(sum(temp))
                    temp = []
                    
            return [time, totalTime, detailTime]
        
    def dataTableWeek(self):
        pass

    def writeTableData(self, data):

        self._table_data = data
        with open(f"data/{self.user}_data/tableWeek.csv" , mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            
            # Write each row of data to the CSV file
            for row in self._table_data:
                writer.writerow(row)

    def readTableData(self):
        self._table_data = []
        with open(f"data/{self.user}_data/tableWeek.csv" , mode="r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            
            # Read each row of data from the CSV file
            for row in reader:
                self._table_data.append(row)
        if self._table_data[0][0] != self.monday:
            self._table_data[0][0] = self.monday
        return self._table_data

    def setTableData(self, wgt):
        self.readTableData()
        for i, row in enumerate(self._table_data):
            if i == 0:  pass
            else:
                for j, column in enumerate(row):
                    if j == 0:  pass
                    else:
                        item = QTableWidgetItem(column)
                        wgt.tableWidget.setItem(i-1, j-1, item)

    def writeDescribeData(self, data):
        with open(f'data/{self.user}_data/describeItem.csv', 'w', newline='', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            
            # Write each row of data to the CSV file
            for row in data:
                writer.writerow(row)
    
    def readDescribeData(self):
        data = []
        with open(f'data/{self.user}_data/describeItem.csv', 'r', newline='', encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            
            # Read each row of data from the CSV file
            for row in reader:
                data.append(row)
        return list(data)
    
    def readSettingData(self):
        data = dict()
        with open(f"data/{self.user}_data/settings.json", 'r', newline="", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
        return data
    
    def WriteSettingData(self, data):
        with open(f"data/{self.user}_data/settings.json", 'w', newline="", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile,  ensure_ascii=False)

    def checkLabelTask(self, data):
        check = False
        current_key = []
        default = list(self.dataTimeJson[f"{self.ntime}"].keys())
        ndata = {}
        for i in data:
            current_key.append(i[0])

        for i in current_key:
            if i in default:    pass
            else:   
                default.append(i)
                check = True
        for i in default:
            if i in current_key:    pass
            else:   
                default.remove(i)
                check = True

        for i in default:
            ndata.update({i:0})


        if check:
            dataTime = {f"{self.ntime}":ndata}
            with open(f'data/{self.user}_data/time.json', 'w', newline='', encoding="utf-8") as jsonfile:
                json.dump(dataTime, jsonfile,  ensure_ascii=False)
