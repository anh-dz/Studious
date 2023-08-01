import csv
import json
from os import path, remove, makedirs
import time, datetime

class fileDataControl:
    def __init__(self):
        self.ntime = datetime.datetime.now()
        self.ntime = self.ntime.strftime("%d/%m/%Y")
        if self.create_folder():  self.default_data()
        self.readDataTimeChart()
        self.readDataTime()
        
    def create_folder(self) -> bool:
        if not path.exists(f".\\data"):
            makedirs(f".\\data")
            with open(f".\\data\\time.csv", "w") as f:
                pass
            with open(f".\\data\\time.json", "w") as f:
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
        with open('.\\data\\time.csv', 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            for row in chartDataTime:
                writer.writerow(row)
        
        with open('.\\data\\time.json', 'w', newline='', encoding="utf-8") as jsonfile:
            json.dump(dataTime, jsonfile,  ensure_ascii=False)


    def readDataTime(self):
        with open(".\\data\\time.json", "r", encoding="utf-8") as jsonfile:
            self.dataTimeJson = json.load(jsonfile)
        if self.ntime not in self.dataTimeJson:
            with open(".\\data\\time.json", "w", encoding="utf-8") as jsonfile:
                    self.dataTimeJson[f"{self.ntime}"] = {"Học Toán":0, "Học IELTS":0, "Làm việc":0}
                    json.dump(self.dataTimeJson, jsonfile,  ensure_ascii=False)
    
    def readDataTimeChart(self):
        self.dataTimeCsv = list()

        # Open the CSV file in read mode
        with open(".\\data\\time.csv", 'r', encoding="utf-8") as csvfile:
            # Create a CSV reader object
            reader = csv.reader(csvfile)

            # Read and process each row
            for row in reader:
                self.dataTimeCsv.append(row)

    def writeDataTime(self):
        with open('.\\data\\time.json', 'w', newline='', encoding="utf-8") as jsonfile:
            json.dump(self.dataTimeJson, jsonfile,  ensure_ascii=False)

    def writeDataTimeChart(self,data):
        with open('.\\data\\time.csv', 'w', newline='', encoding="utf-8") as csvfile:
        # Create a CSV writer object
            writer = csv.writer(csvfile)

        # Write the data to the CSV file row by row
        for row in data:
            writer.writerow(row)


