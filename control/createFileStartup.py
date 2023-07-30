import csv
from os import path, remove, makedirs

class default_file:
    def __init__(self):
        if self.create_folder():  self.default_data()
        self.readDataTime()
        
    def create_folder(self) -> bool:
        if not path.exists(f".\\data"):
            makedirs(f".\\data")
            # with open(f"..\\data\\settings.json", "w") as f:
            #     pass

            # with open(f"..\\data\\day.json", "w") as f:
            #     pass

            with open(f".\\data\\time.csv", "w") as f:
                pass
            return True
        
        return False

    def default_data(self):
        data = [
                ['task name', 'Age'],
                ['study', '0'],
                ['work', '0']
            ]
        # settings_data = {"alarmDur": 30, "startWithSys": False, "openUI": True, "sound": True}
        # with open(f"..\\data\\settings.json", "w") as outfile:
        #     json.dump(settings_data, outfile)
        # Open the CSV file in write mode
        with open('.\\data\\time.csv', 'w', newline='') as csvfile:
            # Create a CSV writer object
            writer = csv.writer(csvfile)

            # Write the data to the CSV file row by row
            for row in data:
                writer.writerow(row)
    
    def readDataTime(self):
        self.data_time = list()

        # Open the CSV file in read mode
        with open(".\\data\\time.csv", 'r', newline='') as csvfile:
            # Create a CSV reader object
            reader = csv.reader(csvfile)

            # Read and process each row
            for row in reader:
                self.data_time.append(row)
    def writeDataTime(self,data):
        with open('.\\data\\time.csv', 'w', newline='') as csvfile:
        # Create a CSV writer object
            writer = csv.writer(csvfile)

        # Write the data to the CSV file row by row
        for row in data:
            writer.writerow(row)


