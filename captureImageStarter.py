'''
Capture image of User(leptop accsesser)
'''

import cv2,time
from threading import Thread
import queue

class CaptureImageStarter:
    def __init__(self):
        self.q = queue.Queue()
        self.thread1 = Thread(target=self.timer, args=(self.q,))
        self.thread1.start()

        cap = cv2.VideoCapture(0)
        i = 0
        while (True):
            ret, frame = cap.read()
            i += 1
            cv2.imwrite('/home/vikku/Pictures/face/' + str(i) + '.png', frame)

            if not self.q.get():
                break
        print(i,"images..  is Captured.")
        cap.release()

    def timer(self, q):
        for i in range(15):
            q.put(1)
            time.sleep(0.5)
        q.put(0)
