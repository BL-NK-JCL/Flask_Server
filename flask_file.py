import subprocess

from flask import Flask, request, send_file
app = Flask(__name__)

@app.put("/start_tracking")
def start_tracking():
    f = open('is_detecting.txt', 'w')
    f.write('1')
    f.close()

    subprocess.Popen("source activate GazeTracking", shell=True, stdout=subprocess.PIPE)
    subprocess.Popen('python /Users/woojin/Development/EyeTracking/GazeTracking/blink_detection.py', shell=True, stdout=subprocess.PIPE)

    return "Start"

@app.put("/end_tracking")
def end_tracking():
    f = open('is_detecting.txt', 'w')
    f.write('0')
    f.close()

    return "End"

@app.get("/get-plot")
def get_plot():
    parameter_dict = request.args.to_dict()
    
    year = parameter_dict['year']
    month = parameter_dict['month']
    day = parameter_dict['day']
    hour = parameter_dict['hour']

    if(year == '' or month == '' or day == '' or hour == ''):
        return '누락된 정보가 있습니다.'

    subprocess.run('python /Users/woojin/Development/EyeTracking/GazeTracking/make_plot.py ' + year + ' ' + month + ' ' + day + ' ' + hour, shell=True)
    return send_file('/Users/woojin/Development/EyeTracking/GazeTracking/output.png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)