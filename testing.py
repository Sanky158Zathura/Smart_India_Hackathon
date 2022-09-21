from pynput.keyboard import Key,Controller
keyboard = Controller()
keyboard.press(Key.alt)
# keyboard.press(Key.shift)
keyboard.press(Key.tab)

# import pyautogui
import sys

# sys.path.insert(1, 'X:\\SI_Hackathon\\alpha')
# import alphabet_recognition as asm
# hotkey()
import os
os.system('python ./gest_addn/main.py')
   

# # # import time



# # # while True:
# # # # #     for i in range(10):
# # # # #         keyboard.press(Key.media_volume_up)
# # # # #         keyboard.release(Key.media_volume_up)
# # # # #         time.sleep(0.1)
# # # # #     for i in range(10):
# # # # #         keyboard.press(Key.media_volume_down)
# # # # #         keyboard.release(Key.media_volume_down)
# # # # #         time.sleep(0.1)
# # # # #     keyboard.press(Key.media_play_pause)
# # # #     keyboard.press(Key.f1)
# # # #
# # #     keyboard.press(Key.up)
# # #     break
# # #     # keyboard.press(Key.f4)
# # #     # keyboard.press(Key.enter)
# # #
# # #     # time.sleep(2)
# # # keyboard.press(Key.ctrl)
# # # keyboard.press("P")
# #
# #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # import gesture as gs
# # #
# # # gesture1 = gs.gesture()
# # # gesture1.hands()
# # # # num = gs.totalFingers
# # # # print(num)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# #
# #
# # import win32api
# # from win32con import *
# #
# # #Scroll one up
# # # while True:
# # # newpos = win32api.GetCursorPos()
# # # for i in range(0,100):
# # #     newpos = win32api.GetCursorPos()
# # #     keyboard.press(Key.ctrl)
# # #     win32api.mouse_event(MOUSEEVENTF_WHEEL,newpos[0],newpos[1], 1, 0)
# #     # print(newpos)
# # # # #Scroll one down
# # # win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, -1, 0)
# # newpos = win32api.GetCursorPos()
# #
# # win32api.mouse_event(MOUSEEVENTF_WHEEL,newpos[0],newpos[1], 1, 0)
# #
# # #
# # # #Scroll one to the right
# # # win32api.mouse_event(MOUSEEVENTF_HWHEEL, x, y, 1, 0)
# # #
# # # #Scroll one to the left
# # # win32api.mouse_event(MOUSEEVENTF_HWHEEL, x, y, -1, 0)
# #
# # import pywinauto
# # # import win32api
# # # win32api.mouse_event()
#
# # -*- coding: utf-8 -*-
# from PyQt4 import QtCore, QtGui
# from os import system, chdir, getcwd
# from time import sleep
# from subprocess import Popen
#
# try:
#     _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s
#
# try:
#     _encoding = QtGui.QApplication.UnicodeUTF8
#
#
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig)
#
#
# class MyPopup(QtGui.QWidget):
#     def __init__(self):
#         QtGui.QWidget.__init__(self)
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(_fromUtf8("./about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.setWindowIcon(icon)
#         resolution = QtGui.QDesktopWidget().screenGeometry()
#         self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
#                   (resolution.height() / 2) - (self.frameSize().height() / 2))
#         pic = QtGui.QLabel(self)
#         pic.setGeometry(20, 20, 128, 128)
#         pic.setPixmap(QtGui.QPixmap(getcwd() + "/icon.png"))
#         self.setMinimumSize(QtCore.QSize(420, 300))
#         self.setMaximumSize(QtCore.QSize(420, 300))
#         labele = QtGui.QLabel(self)
#         labele.setGeometry(QtCore.QRect(158, 20, 2000, 50))
#         font = QtGui.QFont()
#         font.setPointSize(26)
#         labele.setText(_translate("MyPopup", "Auto Shutdown", None))
#         labele.setFont(font)
#
#         labelel = QtGui.QLabel(self)
#         labelel.setGeometry(QtCore.QRect(158, 70, 2000, 25))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         labelel.setText(_translate("MyPopup", "Jan Murić", None))
#         labelel.setFont(font)
#
#         labelo = QtGui.QLabel(self)
#         labelo.setGeometry(QtCore.QRect(100, 175, 300, 100))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         labelo.setText(_translate("MyPopup", "FREEWARE\n\nVersion:  1.0\nE-Mail:        janek.muric@gmail.com", None))
#         labelo.setFont(font)
#
#         exitButton = QtGui.QPushButton(self)
#         exitButton.setGeometry(QtCore.QRect(347, 276, 71, 23))
#         exitButton.setText(_translate("MyPopup", "Ok", None))
#         exitButton.clicked.connect(self.quit)
#
#     def quit(self):
#         self.close()
#
#
# class Ui_MainWindow(object):
#     global x
#     x = 0
#
#     def setupUi(self, MainWindow, parent=None):
#         super(Ui_MainWindow, self)
#         MainWindow.setObjectName(_fromUtf8("MainWindow"))
#         MainWindow.resize(261, 390)
#         MainWindow.setMinimumSize(QtCore.QSize(261, 390))
#         MainWindow.setMaximumSize(QtCore.QSize(261, 390))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(_fromUtf8("./icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         MainWindow.setWindowIcon(icon)
#         MainWindow.setUnifiedTitleAndToolBarOnMac(False)
#         self.centralwidget = QtGui.QWidget(MainWindow)
#         self.centralwidget.setMinimumSize(QtCore.QSize(261, 390))
#         self.centralwidget.setMaximumSize(QtCore.QSize(261, 390))
#         self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
#         self.action = QtGui.QComboBox(self.centralwidget)
#         self.action.setGeometry(QtCore.QRect(104, 60, 91, 22))
#         self.action.setObjectName(_fromUtf8("action"))
#         self.action.addItem(_fromUtf8(""))
#         self.action.addItem(_fromUtf8(""))
#         self.action.addItem(_fromUtf8(""))
#         self.action.addItem(_fromUtf8(""))
#         self.label = QtGui.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(20, 10, 221, 21))
#         self.label.setObjectName(_fromUtf8("label"))
#         self.label_2 = QtGui.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(50, 60, 51, 21))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.label_2.setFont(font)
#         self.label_2.setObjectName(_fromUtf8("label_2"))
#         self.groupBox = QtGui.QGroupBox(self.centralwidget)
#         self.groupBox.setGeometry(QtCore.QRect(10, 100, 241, 191))
#         self.groupBox.setObjectName(_fromUtf8("groupBox"))
#         self.selectTime = QtGui.QRadioButton(self.groupBox)
#         self.selectTime.setGeometry(QtCore.QRect(20, 30, 82, 17))
#         self.selectTime.setObjectName(_fromUtf8("selectTime"))
#         self.buttonGroup_2 = QtGui.QButtonGroup(MainWindow)
#         self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
#         self.buttonGroup_2.addButton(self.selectTime)
#         self.selectDate = QtGui.QRadioButton(self.groupBox)
#         self.selectDate.setGeometry(QtCore.QRect(20, 110, 82, 17))
#         self.selectDate.setObjectName(_fromUtf8("selectDate"))
#         self.buttonGroup_2.addButton(self.selectDate)
#         self.label_3 = QtGui.QLabel(self.groupBox)
#         self.label_3.setGeometry(QtCore.QRect(116, 60, 61, 20))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.label_3.setFont(font)
#         self.label_3.setObjectName(_fromUtf8("label_3"))
#         self.relativeTime = QtGui.QTimeEdit(self.groupBox)
#         self.relativeTime.setGeometry(QtCore.QRect(40, 60, 61, 22))
#         self.relativeTime.setObjectName(_fromUtf8("relativeTime"))
#         self.label_4 = QtGui.QLabel(self.groupBox)
#         self.label_4.setGeometry(QtCore.QRect(40, 140, 21, 21))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.label_4.setFont(font)
#         self.label_4.setObjectName(_fromUtf8("label_4"))
#         self.dateTime = QtGui.QDateTimeEdit(self.groupBox)
#         self.dateTime.setGeometry(QtCore.QRect(70, 140, 111, 22))
#         self.dateTime.setObjectName(_fromUtf8("dateTime"))
#         self.forceCheck = QtGui.QCheckBox(self.centralwidget)
#         self.forceCheck.setGeometry(QtCore.QRect(10, 300, 81, 21))
#         self.forceCheck.setObjectName(_fromUtf8("forceCheck"))
#         self.forceCheck.stateChanged.connect(self.changeText)
#         self.startButton = QtGui.QPushButton(self.centralwidget)
#         self.startButton.setGeometry(QtCore.QRect(170, 300, 71, 23))
#         self.startButton.setObjectName(_fromUtf8("startButton"))
#         self.startButton.clicked.connect(self.start)
#         self.label_5 = QtGui.QLabel(self.centralwidget)
#         self.label_5.setGeometry(QtCore.QRect(0, 330, 251, 20))
#         self.label_5.setObjectName(_fromUtf8("label_5"))
#         self.label_5.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_6 = QtGui.QLabel(self.centralwidget)
#         self.label_6.setGeometry(QtCore.QRect(0, 360, 261, 20))
#         self.label_6.setObjectName(_fromUtf8("label_6"))
#         self.label_6.setAlignment(QtCore.Qt.AlignCenter)
#         self.dateTime.setDateTime(QtCore.QDateTime.currentDateTime())
#         self.about = QtGui.QPushButton(self.centralwidget)
#         self.about.setGeometry(QtCore.QRect(240, 0, 21, 21))
#         self.about.setObjectName(_fromUtf8("about"))
#         self.about.clicked.connect(self.aboutWindow)
#         global tim
#         global act
#         global forc
#         tim = QtCore.QTime.currentTime()
#         tim = str(tim.hour()) + ":" + str(tim.minute())
#         act = "Shut Down"
#         forc = ""
#         self.label_3.setEnabled(False)
#         self.relativeTime.setEnabled(False)
#         self.label_4.setEnabled(False)
#         self.dateTime.setEnabled(False)
#         self.selectTime.toggled.connect(self.greyOut2)
#         self.selectDate.toggled.connect(self.greyOut1)
#         self.action.currentIndexChanged.connect(self.changeText)
#         self.dateTime.dateTimeChanged.connect(self.changeText)
#         self.relativeTime.timeChanged.connect(self.changeText)
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(_translate("MainWindow", "Auto Shutdown", None))
#         self.action.setItemText(0, _translate("MainWindow", "Shut Down", None))
#         self.action.setItemText(1, _translate("MainWindow", "Restart", None))
#         self.action.setItemText(2, _translate("MainWindow", "Go to boot menu", None))
#         self.action.setItemText(3, _translate("MainWindow", "Hibernate", None))
#         self.label.setText(_translate("MainWindow", "Please chose an action and then a time for it.", None))
#         self.label_2.setText(_translate("MainWindow", "Action:", None))
#         self.groupBox.setTitle(_translate("MainWindow", "Time Schedule", None))
#         self.selectTime.setText(_translate("MainWindow", "Relative Time", None))
#         self.selectDate.setText(_translate("MainWindow", "Exact Time", None))
#         self.label_3.setText(_translate("MainWindow", "From now", None))
#         self.label_4.setText(_translate("MainWindow", "On", None))
#         self.forceCheck.setText(_translate("MainWindow", "Force Action", None))
#         self.startButton.setText(_translate("MainWindow", "Start", None))
#         self.about.setText(_translate("MainWindow", "?", None))
#         self.label_5.setText(_translate("MainWindow", "Your computer will " + act + " in ", None))
#         self.label_6.setText(_translate("MainWindow", tim + forc, None))
#         self.startButton.setEnabled(False)
#
#     def greyOut1(self):  # selectDate on
#         self.label_3.setEnabled(False)
#         self.relativeTime.setEnabled(False)
#         self.label_4.setEnabled(True)
#         self.dateTime.setEnabled(True)
#         self.startButton.setEnabled(True)
#
#     def greyOut2(self):  # selectTime on
#         self.label_3.setEnabled(True)
#         self.relativeTime.setEnabled(True)
#         self.label_4.setEnabled(False)
#         self.dateTime.setEnabled(False)
#         self.startButton.setEnabled(True)
#
#     def changeText(self):
#         if self.selectDate.isChecked():
#             global forc
#             if self.forceCheck.isChecked():
#                 forc = " (Force)"
#             else:
#                 forc = ""
#
#             act = self.action.currentText()
#             tim = self.dateTime.dateTime()
#             timm = tim.time()
#             dat = tim.date()
#             timee = str(dat.day()) + "." + str(dat.month()) + "." + str(dat.year()) + " " + str(
#                 timm.hour()) + ":" + str(timm.minute())
#             self.label_5.setText(_translate("MainWindow", "Your computer will " + act + " at ", None))
#             self.label_6.setText(_translate("MainWindow", timee + " " + forc, None))
#         else:
#             if self.forceCheck.isChecked():
#                 forc = "(Force)"
#             else:
#                 forc = ""
#
#             act = self.action.currentText()
#             tim = self.relativeTime.time()
#             now = QtCore.QTime.currentTime()
#             hr = now.hour() + tim.hour()
#             mn = now.minute() + tim.minute()
#             timee = str(hr) + ":" + str(mn)
#             self.label_5.setText(_translate("MainWindow", "Your computer will " + act + " at ", None))
#             self.label_6.setText(_translate("MainWindow", timee + forc, None))
#
#     def start(self):
#         global x
#         if x == 0:
#             x = 1
#             palette = QtGui.QPalette()
#             palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.darkGreen)
#             self.label_5.setPalette(palette)
#             self.label_6.setPalette(palette)
#             self.startButton.setText("Stop")
#             self.label_3.setEnabled(False)
#             self.relativeTime.setEnabled(False)
#             self.label_4.setEnabled(False)
#             self.dateTime.setEnabled(False)
#             self.action.setEnabled(False)
#             self.selectTime.setEnabled(False)
#             self.selectDate.setEnabled(False)
#             self.forceCheck.setEnabled(False)
#
#             global f
#             global t
#             global s
#             if self.forceCheck.isChecked():
#                 f = " /f"
#
#             else:
#                 f = ""
#
#             if self.action.currentText() == "Shut Down":
#                 s = "/s"
#
#             elif self.action.currentText() == "Restart":
#                 s = "/r"
#             elif self.action.currentText() == "Go to boot menu":
#                 s = "/o"
#             elif self.action.currentText() == "Hibernate":
#                 s = "/h"
#
#             if self.selectTime.isChecked():
#                 tim = self.relativeTime.time()
#                 now = QtCore.QTime.currentTime()
#
#                 timm = int(tim.hour())
#                 tinn = int(tim.minute())
#                 hsec = timm * 60
#                 hsec = hsec * 60
#                 msec = tinn * 60
#                 t = msec + hsec
#                 chdir(".")
#                 Popen("shutdwn " + s + " /t " + str(t) + f)
#             if self.selectDate.isChecked():
#                 tim = self.dateTime.dateTime()
#                 now = QtCore.QDateTime.currentDateTime()
#                 t = tim.toTime_t() - now.toTime_t()
#                 Popen("shutdwn " + s + " /t " + str(t) + f)
#
#
#
#
#         else:
#             x = 0
#             palette = QtGui.QPalette()
#             palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.black)
#             self.label_5.setPalette(palette)
#             self.label_6.setPalette(palette)
#             chdir(".")
#             Popen("shutdwn /a")
#             self.action.setEnabled(True)
#             self.selectTime.setEnabled(True)
#             self.selectDate.setEnabled(True)
#             self.forceCheck.setEnabled(True)
#             self.startButton.setText("Start")
#
#     @QtCore.pyqtSlot()
#     def aboutWindow(self):
#         self.w = MyPopup()
#         self.w.show()
#
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
# #     sys.exit(app.exec_())
# import time
# import turtle
# from turtle import *
#
# wn = Screen()
# wn.setup(width=1200, height=680)
# wn.bgcolor('black')
# turtle.speed(0)
# color = ['white', 'red']
#
# for i in range(10):
#     turtle.pencolor(color[i % len(color)])
#     turtle.rt(i)
#     turtle.circle(100, i)
#     turtle.fd(i)
#     turtle.rt(10000)
#     turtle.fd(i+20)
# # time.sleep(500)
# myScreenshot = pyautogui.screenshot()
#
# myScreenshot.save(r'.\xyz2.png')
#
# wn.mainloop()
