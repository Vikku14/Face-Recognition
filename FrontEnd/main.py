from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os,sys

from setupApplication import SetupAppliction
from faceRecognition import FaceRecognition

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"main.ui"))

class Splash(QMainWindow,FROM_MAIN):
    EMAIL_ADDRESS=''

    def __init__(self, parent = None):
        super(Splash, self).__init__(parent)
        QMainWindow.setWindowTitle(self,"System Breach Notifier")
        QMainWindow.__init__(self)
        self.setupUi(self)
        # pixmap = QPixmap("logo.png")
        # self.splah_image.setPixmap(pixmap.scaled(200, 200))
        self.startButton.clicked.connect(self.modify)

    def modify(self):
        f =open("/home/vikku/PycharmProjects/face_recognition/email.txt",'w+')
        f.writelines(self.email.text())
        f.close()


        SetupAppliction()
        self.name.hide()
        self.startButton.hide()
        self.label_2.hide()
        self.email.hide()
        self.label.setText("{0} pics captured.\n{1} are Applicable".format(SetupAppliction.TOTAL_IMAGES,FaceRecognition.TOTAL_FACES))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = Splash()
    window.show()
    app.exec_()