import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import cv2
from PyQt5.QtCore import Qt


class mainUI(QMainWindow):
    def __init__(self):
        super(mainUI, self).__init__()
        loadUi("final.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.LOGIN.clicked.connect(self.gotowebcam)
    def gotowebcam(self):
        widget.setCurrentIndex(widget.currentIndex()+1)




class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()
# main
if __name__=='__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    login = mainUI()
    webcam = MainWindow()
    widget.addWidget(login)
    widget.addWidget(webcam)
    widget.setFixedHeight(501)
    widget.setFixedWidth(801)
    widget.show()
    app.exec_()
