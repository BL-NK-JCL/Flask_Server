import cv2
from gaze_tracking import GazeTracking
from datetime import datetime, timedelta
import subprocess

gaze = GazeTracking()
detecting = True

time_gap = 5

def add_to_file(detection_start, blink_count):
    f = open("blink_data.txt", 'a')
    detection_start = datetime.now()

    f.write(detection_start.strftime('%Y/%m/%d %H:%M:%S') + " " + str(blink_count) + "\r\n")
    f.close()

def get_blink_1_second(detection_start, last_blinked, webcam):
    is_blinking = False
    blink_count = 0
    
    while(detection_start + timedelta(seconds=1)  > datetime.now()):
        _, frame = webcam.read()
        gaze.refresh(frame)

        frame = gaze.annotated_frame()

        if gaze.is_blinking():
            if(is_blinking == False):
                subprocess.run(['nightlight', 'off'])

                blink_count += 1
                is_blinking = True

            last_blinked[0] = datetime.now()

        else:
            if last_blinked[0] + timedelta(seconds=time_gap) < datetime.now():
                subprocess.run(['nightlight', 'on'])
        
            is_blinking = False

    add_to_file(detection_start, blink_count)

def detect_start():
    last_updated = datetime.now()
    last_blinked = [ datetime.now() ]

    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)

    count = 0

    while True:
        f = open('is_detecting.txt', 'r')
        line = f.readline()

        if int(line) == 0:
            break

        if last_updated + timedelta(seconds=1) < datetime.now():
            last_updated = datetime.now()

            get_blink_1_second(last_updated, last_blinked, webcam)
            count += 1

    subprocess.run(['nightlight', 'off'])

    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    f = open('bluelight_settings.txt', 'r')
    time_gap = int(f.readline())
    
    detect_start()