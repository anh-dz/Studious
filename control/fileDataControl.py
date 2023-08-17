import json
from os import path, remove, makedirs
import time, datetime

with open("data/quotes.txt", "r", encoding="utf-8") as f:
    res = f.readlines()
    list_quotes = [i.strip() for i in res]

class fileDataControl:
    def __init__(self):
        self._ntime = datetime.datetime.now()
        self.ntime = self._ntime.strftime("%d/%m/%Y")
        if self.create_folder():  self.default_data()
        self.readDataTime()
        
    def create_folder(self) -> bool:
        if not path.exists(f"data"):
            makedirs(f"data")
            with open(f"data/time.json", "w") as f:
                pass
            return True
        
        return False

    def default_data(self):
        chartDataTime = [
                ['task name', 'time'],
                ['Học', '0'],
                ['Làm việc', '0']
            ]
        dataTime = {f"{self.ntime}":{"Học Toán":0, "Học IELTS":0, "Làm việc":0}}

        with open('data/time.json', 'w', newline='', encoding="utf-8") as jsonfile:
            json.dump(dataTime, jsonfile,  ensure_ascii=False)


    def readDataTime(self):
        with open("data/time.json", "r", encoding="utf-8") as jsonfile:
            self.dataTimeJson = json.load(jsonfile)
        if self.ntime not in self.dataTimeJson:
            with open("data/time.json", "w", encoding="utf-8") as jsonfile:
                    self.dataTimeJson[f"{self.ntime}"] = {"Học Toán":0, "Học IELTS":0, "Làm việc":0}
                    json.dump(self.dataTimeJson, jsonfile,  ensure_ascii=False)

    def writeDataTime(self):
        with open('data/time.json', 'w', newline='', encoding="utf-8") as jsonfile:
            json.dump(self.dataTimeJson, jsonfile,  ensure_ascii=False)

    def dataChart(self, days: str):
        time = []
        totalTime = []
        detailTime = []
        
        with open("data/time.json", "r", encoding="utf-8") as jsonfile:
            datachart = json.load(jsonfile)
            key =  list(datachart[self.ntime].keys())
            for k in key:   detailTime.append([k, 0])
                        
        for i in range(int(days.split(" ")[0])-1, -1, -1):
            last_day = self._ntime - datetime.timedelta(days=i)
            last_day = last_day.strftime('%d/%m/%Y')
            if last_day not in datachart:
                datachart.update({last_day:{"Học Toán":0, "Học IELTS":0, "Làm việc":0}})

        if days == "3 ngày" or days == "7 ngày":
            for i in range(int(days.split(" ")[0])-1, -1, -1):
                last_day = self._ntime - datetime.timedelta(days=i)
                temp = []
                for x in range(len(key)):
                    _t = datachart[last_day.strftime('%d/%m/%Y')][key[x]]
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
                    _t = datachart[last_day.strftime('%d/%m/%Y')][key[x]]
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
                    _t = datachart[last_day.strftime('%d/%m/%Y')][key[x]]
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
                    _t = datachart[last_day.strftime('%d/%m/%Y')][key[x]]
                    detailTime[x][1] += _t
                    temp.append(_t)
                
                if i%60 == 0 and i != 360:
                    time.append(f"{(last_day - datetime.timedelta(days=59)).strftime('%d/%m')}-{last_day.strftime('%d/%m')}")
                    totalTime.append(sum(temp))
                    temp = []
                    
            return [time, totalTime, detailTime]