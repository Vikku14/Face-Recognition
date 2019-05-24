import os,sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    if not os.path.exists("/home/vikku/PycharmProjects/face_recognition/SPLUNG"): # to check database is set or not(SPLUNG is flag)
        from FrontEnd.main import Splash

        app = QApplication(sys.argv)
        window = Splash()
        window.show()
        app.exec_()
    else:
        from FrontEnd.mainDone import MainDone

        app = QApplication(sys.argv)
        window = MainDone()
        window.show()
        app.exec_()