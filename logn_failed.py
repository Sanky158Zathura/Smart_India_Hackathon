import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

class mainUI(QMainWindow):
    def __init__(self):
        super(mainUI, self).__init__()
        loadUi("login_failed.ui", self)

# main
if __name__=='__main__':
    app = QApplication(sys.argv)
    login = mainUI()
    login.setFixedWidth(1000)
    login.setFixedHeight(410)
    login.show()
    app.exec_()