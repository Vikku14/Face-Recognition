from faceRecognition import FaceRecognition
from captureImageStarter import CaptureImageStarter

import cv2
import os,time


class SetupAppliction():
    TOTAL_IMAGES=0
    def __init__(self):

        if not os.path.exists("/home/vikku/PycharmProjects/face_recognition/SPLUNG"):
            f= open('/home/vikku/PycharmProjects/face_recognition/SPLUNG','w')
            f.close()

            self.create_directory()

            i = 0
            while (True):
                cap = cv2.VideoCapture(0)
                if cap.isOpened():
                    ret, frame = cap.read()
                    cv2.imshow("PRESS 'q' WHEN DONE", frame)
                    key= cv2.waitKey(80)
                    i += 1
                    cv2.imwrite('/home/vikku/PycharmProjects/face_recognition/trainning_data/s1/' + str(i) + '.jpg', frame)

                    if key == ord('q'):
                        break
                cap.release()
                time.sleep(2.5)
            print(i, "images..  is Captured.")
            SetupAppliction.TOTAL_IMAGES=i
            cap.release()
            cv2.destroyAllWindows()

            FaceRecognition().populate_face()


        else:
            self.create_directory()

            # TODO give warnning to user that his data has been removed. if he wants rebuild it(recommended).Not Compulsory.

            print("ALL DONE")

    def create_directory(self):

        directory = '/home/vikku/PycharmProjects/face_recognition/trainning_data/s1/'
        if not os.path.exists(directory):
            os.makedirs(directory)
