from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from fileDataControl import fileDataControl

app = Flask(__name__)

#User info
Users = {}

@app.route('/')
def index():
    return jsonify({"message": "Countdown API is running!"})

@app.route("/connect", methods=['POST'])
def connect():
    user = request.headers.get('user')
    Users[f'{user}'] = controlFunc(f'{user}')
    return "Success"

@app.route('/start_countdown', methods=['POST'])
def start_countdown():
    user = request.headers.get('user')
    data = request.json
    seconds = int(data.get('seconds', 0))
    current_task = data.get("current_task", 0)
    try:    Users[f'{user}']
    except: Users[f'{user}'] = controlFunc(f'{user}')
    return Users[f'{user}'].start_countdown(seconds, current_task)

@app.route('/stop_countdown', methods=['POST'])
def stop_countdown():
    user = request.headers.get('user')
    if Users[f'{user}'].countdown_end:
        Users[f'{user}'].remaining_time = round((Users[f'{user}'].countdown_end - datetime.now()).total_seconds())
        Users[f'{user}'].countdown_end = None
    return jsonify({"status": "Countdown stopped", "remaining_time": round( Users[f'{user}'].remaining_time)})

@app.route('/continue_countdown', methods=['POST'])
def continue_countdown():
    user = request.headers.get('user')
    if  Users[f'{user}'].remaining_time:
        Users[f'{user}'].countdown_end = datetime.now() + timedelta(seconds=Users[f'{user}'].remaining_time)
        Users[f'{user}'].remaining_time = None
    return jsonify({"status": "Countdown continued", "end_time": Users[f'{user}'].countdown_end.isoformat()})

@app.route('/get_countdown', methods=['GET'])
def get_countdown():
    user = request.headers.get('user')
    if Users[f'{user}'].countdown_end != None:
        time_left = (Users[f'{user}'].countdown_end - datetime.now()).total_seconds()
        return jsonify({"status": "Countdown running", "time_left": round(time_left)})
    elif Users[f'{user}'].remaining_time:
        return jsonify({"status": "Countdown stopped", "remaining_time": Users[f'{user}'].remaining_time})
    else:
        return jsonify({"status": "No countdown set"})
    
#export setting data
@app.route('/get_setting', methods=['GET'])
def get_setting():
    user = request.headers.get('user')
    return Users[f"{user}"].file.readSettingData()

#export only task
@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    user = request.headers.get('user')
    data = Users[f"{user}"].file.readSettingData()['tasks']
    data = {k: v for k, v in data.items() if v["combo"]}
    return data

#export current task
@app.route("/get_current_tasks", methods=['GET'])
def get_current_task():
    user = request.headers.get('user')
    return Users[f'{user}'].current_task

#export time data
@app.route('/get_time', methods=['GET'])
def get_time():
    user = request.headers.get('user')
    w = Users[f"{user}"].file.readDataTime()
    w = dict((key[:5], sum(w[key].values())) for (key, value) in w.items())
    if len(w)>7:
        w = w[:7]
    return w

#export sum data
@app.route('/get_sum_data', methods=['GET'])
def get_sum_data():
    user = request.headers.get('user')
    w = Users[f"{user}"].file.readDataTime()
    fs = w[next(iter(w))]
    sum_data = {subject: 0 for subject in fs}
    for day in w:
        for subject in w[day]:
            sum_data[subject]+=w[day][subject]
    return sum_data

#export tableweek data
@app.route('/get_tableweek', methods=['GET'])
def get_tableweek():
    user = request.headers.get('user')
    return Users[f"{user}"].file.readTableData()

#export describeitem data
@app.route('/get_describeitem', methods=['GET'])
def get_describeitem():
    user = request.headers.get('user')
    return Users[f"{user}"].file.readDescribeData()

#Sync data multiplatform
@app.route('/sync_time', methods=['POST'])
def sync_time():
    data = request.json
    user = request.headers.get('user')
    Users[f"{user}"].file.writeDataTime(data)
    return "success"
    
@app.route('/sync_setting', methods=['POST'])
def sync_setting():
    data = request.json
    user = request.headers.get('user')
    Users[f"{user}"].file.WriteSettingData(data)
    return "success"

@app.route('/sync_tableweek', methods=['POST'])
def sync_tableweek():
    data = request.json
    user = request.headers.get('user')
    Users[f"{user}"].file.writeTableData(data)
    return "success"

@app.route('/sync_describeitem', methods=['POST'])
def sync_describeitem():
    data = request.json
    user = request.headers.get('user')
    Users[f"{user}"].file.writeDescribeData(data)
    return "success"

@app.route('/sync_timeData', methods=['POST'])
def receive_post():
    #Data trả về sẽ có dạng: ["Học toán", 5]
    data = request.get_json()
    user = request.headers.get('user')
    Users[f"{user}"].file.readDataTime()
    Users[f"{user}"].file.dataTimeJson[Users[f"{user}"].file.ntime][data[0]] += round((data[1]/60)/60, 1)
    Users[f"{user}"].file.writeDataTime(Users[f"{user}"].file.dataTimeJson)
    return "Success"

class controlFunc:
    def __init__(self, id:str) -> None:
        self.user = id
        self.file = fileDataControl(id)
        self.countdown_end = None
        self.remaining_time = None
        self.current_task = None
    def start_countdown(self, seconds, current_task):
        self.current_task = current_task
        self.countdown_end = datetime.now() + timedelta(seconds=seconds)
        self.remaining_time = None
        return jsonify({"status": "Countdown started", "end_time": self.countdown_end.isoformat()})

#run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
