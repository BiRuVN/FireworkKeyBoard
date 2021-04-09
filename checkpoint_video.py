import cv2
import time
from playsound import playsound
from threading import Thread
import multiprocessing
from datetime import datetime
import json

keyboard = 'qwertyuiop\nasdfghjkl\nzxcvbnm'

coor_keys = dict()
col_gap = int(100/2)
row_gap = int(100/(10-1))
rw = 0
cl = 0
i = 1
for c in keyboard:
    if c == '\n':
        cl += col_gap
        rw = 0
        row_gap = int(100/(10-1-i))
        i += 1
        continue
    coor_keys[c] = (rw, cl)
    rw += row_gap

def run_frame():
    vid = cv2.VideoCapture('sample.mp4')

    if not vid.isOpened():
        print("Error reading file")
        p.terminate()
        return

    fps= float(vid.get(cv2.CAP_PROP_FPS))

    while True:
        success, frame = vid.read()

        if success:
            # time.sleep(1/(fps*2))
            cv2.imshow('frame', frame)
        else:
            break

        ch = cv2.waitKey(30)
        now = datetime.now()
        if ch == 27:
            print('okay')
            # p.terminate()
            break
        elif ch >= 97 and ch <= 122:
            fireworks['data'].append({
                'duration': int((now-start).total_seconds()*1000),
                'coor': coor_keys[chr(ch)]
                })

    vid.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    fireworks = {'data': []}
    p = multiprocessing.Process(target=playsound, args=("sample1.mp3",))
    start = datetime.now()
    p.start()
    run_frame()
    print(fireworks)
    with open('fireworks.json', 'w+') as f:
        json.dump(fireworks, f)

    