import csv
import json
from os import path, remove, makedirs
import time, datetime

class fileDataControl:
    def __init__(self):
        if self.create_folder():  self.default_data()
        self.readDataTimeChart()
        
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
                ['study', '0'],
                ['work', '0']
            ]
        ntime = datetime.datetime.now()
        ntime = ntime.strftime("%d/%m/%Y")
        dataTime = {f"{ntime}":{"study":0, "work":0}}
        with open('.\\data\\time.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for row in chartDataTime:
                writer.writerow(row)
        
        with open('.\\data\\time.json', 'w', newline='') as jsonfile:
            json.dump(dataTime, jsonfile)
    
    def readDataTimeChart(self):
        self.data_time = list()

        # Open the CSV file in read mode
        with open(".\\data\\time.csv", 'r', newline='') as csvfile:
            # Create a CSV reader object
            reader = csv.reader(csvfile)

            # Read and process each row
            for row in reader:
                self.data_time.append(row)
                
    def writeDataTimeChart(self,data):
        with open('.\\data\\time.csv', 'w', newline='') as csvfile:
        # Create a CSV writer object
            writer = csv.writer(csvfile)

        # Write the data to the CSV file row by row
        for row in data:
            writer.writerow(row)


