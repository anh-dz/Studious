from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from fileDataControl import fileDataControl

app = Flask(__name__)

#connect to local server file
file = fileDataControl()

#handle countdown time
countdown_end = None
remaining_time = None

@app.route('/')
def index():
    return jsonify({"message": "Countdown API is running!"})

@app.route('/start_countdown', methods=['POST'])
def start_countdown():
    global countdown_end, remaining_time
    data = request.json
    seconds = int(data.get('seconds', 0))
    countdown_end = datetime.now() + timedelta(seconds=seconds)
    remaining_time = None
    return jsonify({"status": "Countdown started", "end_time": countdown_end.isoformat()})

@app.route('/stop_countdown', methods=['POST'])
def stop_countdown():
    global countdown_end, remaining_time
    if countdown_end:
        remaining_time = round((countdown_end - datetime.now()).total_seconds())
        countdown_end = None
    return jsonify({"status": "Countdown stopped", "remaining_time": round(remaining_time)})

@app.route('/continue_countdown', methods=['POST'])
def continue_countdown():
    global countdown_end, remaining_time
    if remaining_time:
        countdown_end = datetime.now() + timedelta(seconds=remaining_time)
        remaining_time = None
    return jsonify({"status": "Countdown continued", "end_time": countdown_end.isoformat()})

@app.route('/get_countdown', methods=['GET'])
def get_countdown():
    global countdown_end, remaining_time
    if countdown_end:
        time_left = (countdown_end - datetime.now()).total_seconds()
        return jsonify({"status": "Countdown running", "time_left": round(time_left)})
    elif remaining_time:
        return jsonify({"status": "Countdown stopped", "remaining_time": remaining_time})
    else:
        return jsonify({"status": "No countdown set"})
    
#export setting data
@app.route('/get_setting', methods=['GET'])
def get_setting():
    global file
    return file.readSettingData()

#export only task
@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    global file
    data = file.readSettingData()['tasks']
    data = {k: v for k, v in data.items() if v["combo"]}
    return data

#export time data
@app.route('/get_time', methods=['GET'])
def get_time():
    global file
    return file.readDataTime()

#export tableweek data
@app.route('/get_tableweek', methods=['GET'])
def get_tableweek():
    global file
    return file.readTableData()

#export describeitem data
@app.route('/get_describeitem', methods=['GET'])
def get_describeitem():
    global file
    return file.readDescribeData()

#Sync data multiplatform
@app.route('/sync_time', methods=['POST'])
def sync_time():
    data = request.json
    return file.writeDataTime(data)
    
@app.route('/sync_setting', methods=['POST'])
def sync_setting():
    data = request.json
    return file.WriteSettingData(data)

@app.route('/sync_tableweek', methods=['POST'])
def sync_tableweek():
    data = request.json
    return file.writeTableData(data)

@app.route('/sync_describeitem', methods=['POST'])
def sync_describeitem():
    data = request.json
    return file.writeDescribeData(data)

#run
if __name__ == '__main__':
    app.run(debug=True)