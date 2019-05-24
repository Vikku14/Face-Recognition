from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os,sys

FROM_MAINDone,_ = loadUiType(os.path.join(os.path.dirname(__file__),"mainDone.ui"))

class MainDone(QMainWindow,FROM_MAINDone):


    def __init__(self, parent = None):
        super(MainDone, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        # pixmap = QPixmap("logo.png")
        # self.splah_image.setPixmap(pixmap.scaled(200, 200))



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MainDone()
    window.show()
    app.exec_()