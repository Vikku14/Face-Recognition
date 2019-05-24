from faceRecognition import FaceRecognition
from captureImageStarter import CaptureImageStarter
from sendMail import email
import os,time
from FrontEnd.main import Splash
try:
    import httplib
except:
    import http.client as httplib

def isinternet():
    conn= httplib.HTTPConnection("www.google.com",timeout=5)
    try:
        conn.request("HEAD","/")
        conn.close()
        return True
    except:
        conn.close()
        return False

if __name__ == '__main__':
    if os.path.exists("/home/vikku/PycharmProjects/face_recognition/SPLUNG"):

        CaptureImageStarter()

        FaceRecognition().predict_faces()

        if FaceRecognition.FLAG:
            print("Making Animated.gif")
            animatedGif= '/home/vikku/PycharmProjects/face_recognition/result.gif'
            Compressed_animatedGif= '/home/vikku/PycharmProjects/face_recognition/animated.gif'
            os.system('convert -delay 20 -loop 0 /home/vikku/Pictures/face/*.png {}'.format(animatedGif)) # make gif
            os.system('convert {0} -fuzz 10%  -layers Optimize {1}'.format(animatedGif,Compressed_animatedGif))# make compressed gif

            while not isinternet():
                print("NO Internet Connection..")
                time.sleep(60)
            else:
                try:
                    print("Sending email..")
                    print(Splash.EMAIL_ADDRESS)
                    email()
                except:
                    print("Email cannot be send..")