import os
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QSplashScreen, QLabel
import sys
from PyQt5.uic import loadUi
import time
from PyQt5.QtCore import *
import cv2
import pyautogui
from keras.models import load_model
from collections import deque
import numpy as np
import cv2
import os
import json
import gesture as gs
from pynput.keyboard import Key,Controller

Keyboard = Controller()

# Load the models built in the previous steps
mlp_model = load_model('../alpha/emnist_mlp_model.h5')
cnn_model = load_model('../alpha/emnist_cnn_model.h5')

# Letters lookup
letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
		   11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
		   21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: '-'}
points = deque(maxlen=512)


# def main():
    # global camera
    # screenshot = 0
    # control = 1
    # # print("Do you want to add gesture for screenshot")
    # # x= input()
    # # if x == "yes":
    # screenshot = alpha()
    # # with open('./data/dygestures.json', 'r') as openfile:
    #     # Reading from json file
    #     json_object = json.load(openfile)
    #
    # print(json_object)
    # f = open('./data/dygestures.json')

    # returns JSON object as
    # a dictionary
    # data = json.load(f)
    # print(data)
    # Iterating through the json
    # list
    # for i in data['emp_details']:
    #     print(i)

    # Closing file
    # f.close()
    # json_object.update(diction)
    #
    # with open('sample.json', 'w') as json_file:
    #     json.dump(json_object, json_file)

    # print("Testing time - yes/no")
    # x = input()
    # if x == "yes":
    #     camera= cv2.VideoCapture(0)
    #     control = alpha()
    # if control == screenshot:
    #     myScreenshot = pyautogui.screenshot()
    #     myScreenshot.save(r'.\xyz2.png')
    #     return 0
    #
    # while (1) :
    #
    #     if control == screenshot:
    #         myScreenshot = pyautogui.screenshot()
    #         myScreenshot.save(r'.\xyz2.png')
    #         return 0
    #     else:
    #         camera = cv2.VideoCapture(0)
    #         control = alpha()


    # print("Start recording")
    # screen=alpha()
    # print("hhhh")
    # print(screen)
    # if x==tab:
    #

    #     camera = cv2.VideoCapture(0)
    #     (grab, frame) = camera.read()
    #     cv2.putText(frame, "TRY", (200, 370),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    #     command = alpha(frame)
    #     if command == pause:
    #         Keyboard.press(Key.space)
    #





# sys.path.insert(1, 'D:\\programming\\Python\\smart_ind_hack\\final\\gestures')


class SplashScreen(QSplashScreen):
	def __init__(self):
		super(QSplashScreen, self).__init__()
		loadUi('SplashScreen.ui', self)
		self.setWindowFlag(Qt.FramelessWindowHint)

	def progress(self):
		for i in range(100):
			time.sleep(0.05)
			self.progressBar.setValue(i)




class Main_UI(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		# uic.loadUi("D:\\programming\\Python\\smart_ind_hack\\final\\GUI\\main.ui", self)
		uic.loadUi("main.ui", self)
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.pushButton.clicked.connect(lambda: app.exit())
		self.pushButton_2.clicked.connect(lambda: self.showFullScreen())
		self.pushButton_3.clicked.connect(lambda: self.showMinimized())
		self.frame_2.mouseMoveEvent = self.MoveWindow
		self.startButton.clicked.connect(self.start_webcam)
		self.stopButton.clicked.connect(self.stop_webcam)
		self.textButton.clicked.connect(self.changeText)
		self.xyz.clicked.connect(self.change_gesture)
		self.label=self.findChild(QLabel,"textlabel")
		self.gs=gs.gesture()
		self.fingers=0
		self.flag_gesture = False
	

		#self.mailButton.clicked.connect(self.query)



		self.toolButton.clicked.connect(lambda: self.Side_Menu_Def_0())

		

		self.frame_5.mousePressEvent = self.Side_Menu_Def_1

	def change_gesture(self):
		self.flag_gesture = ~self.flag_gesture
		print(self.flag_gesture)

	def Side_Menu_Def_0(self):
		if self.frame_4.width() <= 50:
			self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximumWidth")
			self.animation1.setDuration(500)
			self.animation1.setStartValue(35)
			self.animation1.setEndValue(110)
			self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation1.start()

			self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
			self.animation2.setDuration(500)
			self.animation2.setStartValue(35)
			self.animation2.setEndValue(110)
			self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation2.start()

		else:
			self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximumWidth")
			self.animation1.setDuration(500)
			self.animation1.setStartValue(110)
			self.animation1.setEndValue(35)
			self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation1.start()

			self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
			self.animation2.setDuration(500)
			self.animation2.setStartValue(110)
			self.animation2.setEndValue(35)
			self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation2.start()

	def Side_Menu_Def_1(self, Event):
		if Event.button() == QtCore.Qt.LeftButton:
			if self.frame_4.width() >= 50:
				self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximumWidth")
				self.animation1.setDuration(500)
				self.animation1.setStartValue(110)
				self.animation1.setEndValue(35)
				self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
				self.animation1.start()

				self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
				self.animation2.setDuration(500)
				self.animation2.setStartValue(110)
				self.animation2.setEndValue(35)
				self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
				self.animation2.start()
			else:
				pass


	def MoveWindow(self, event):
		if self.isMaximized() == False:
			self.move(self.pos() + event.globalPos() - self.clickPosition)
			self.clickPosition = event.globalPos()
			event.accept()
			pass
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()

	def alpha(self):
		global camera
		global points
		# (grab, frame) = camera.read()
		temp = 1
		prediction1 = 26
		prediction2 = 26
		blackboard = np.zeros((480, 640, 3), dtype=np.uint8)
		alphabet = np.zeros((200, 200, 3), dtype=np.uint8)

		gesture = gs.gesture()

		while True:
			temp += 1
			# camera = cv2.VideoCapture(0)
			# Grab the current paintWindow
			(grabbed, frame) = camera.read()

			frame = cv2.flip(frame, 1)
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			center = None

			flag1, frame = gesture.hands(frame)
			coordinates = gesture.lm(frame)
			# print(flag1)
			# print("gggggggggg")
			# print(coordinates)
			if flag1 == 1:
				center = (coordinates[8][1], coordinates[8][2])
				points.appendleft(center)

			elif len(coordinates) == 0 or flag1 != 1:
				if len(points) != 0:
					blackboard_gray = cv2.cvtColor(blackboard, cv2.COLOR_BGR2GRAY)
					blur1 = cv2.medianBlur(blackboard_gray, 15)
					blur1 = cv2.GaussianBlur(blur1, (5, 5), 0)
					thresh1 = cv2.threshold(blur1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
					blackboard_cnts = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
					print(type(blackboard_cnts))
					if len(blackboard_cnts) >= 1:
						print(len(blackboard_cnts))
						cnt = sorted(blackboard_cnts, key=cv2.contourArea, reverse=True)[0]
						print(cv2.contourArea(cnt))
						if cv2.contourArea(cnt) > 100:
							x, y, w, h = cv2.boundingRect(cnt)
							alphabet = blackboard_gray[y - 10:y + h + 10, x - 10:x + w + 10]
							newImage = cv2.resize(alphabet, (28, 28))
							newImage = np.array(newImage)
							newImage = newImage.astype('float32') / 255
							print("early")
							prediction1 = mlp_model.predict(newImage.reshape(1, 28, 28))[0]
							prediction1 = np.argmax(prediction1)
							print("Pre1")
							prediction2 = cnn_model.predict(newImage.reshape(1, 28, 28, 1))[0]
							prediction2 = np.argmax(prediction2)
							print("Pre2")

					points = deque(maxlen=512)
					print("Poi len", points)
					blackboard = np.zeros((480, 640, 3), dtype=np.uint8)
					print(blackboard)


			else:
				points = deque(maxlen=512)

			for i in range(1, len(points)):
				if points[i - 1] is None or points[i] is None:
					continue
				# print(i)
				cv2.line(frame, points[i - 1], points[i], (0, 0, 0), 2)
				cv2.line(blackboard, points[i - 1], points[i], (255, 255, 255), 8)

			cv2.putText(frame, "Multilayer Perceptron : " + str(letters[int(prediction1) + 1]), (10, 410),
						cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
			cv2.putText(frame, "Convolution Neural Network:  " + str(letters[int(prediction2) + 1]), (10, 440),
						cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

			if str((letters[int(prediction2) + 1])) != "-" and flag1 == 0:
				print(str(letters[int(prediction1) + 1]))
				print(str(letters[int(prediction2) + 1]))
				print("exiting")
				camera.release()
				cv2.destroyAllWindows()
				return str(letters[int(prediction2) + 1])

			cv2.imshow("alphabets Recognition Real Time", frame)

			# If the 'q' key is pressed, stop the loop
			if cv2.waitKey(1) & 0xFF == ord("q"):
				break

		camera.release()
		cv2.destroyAllWindows()

	def start_webcam(self):
		global camera
		screenshot = 0
		control = 1
		# print("Do you want to add gesture for screenshot")
		# x= input()
		# if x == "yes":
		camera = cv2.VideoCapture(0)
		screenshot = self.alpha()

	# with open('./data/dygestures.json', 'r') as openfile:
	#     # Reading from json file
	#     json_object = json.load(openfile)
	#
	# print(json_object)
	# f = open('./data/dygestures.json')

	# returns JSON object as
	# a dictionary
	# data = json.load(f)
	# print(data)
	# Iterating through the json
	# list
	# for i in data['emp_details']:
	#     print(i)

	# Closing file
	# f.close()
	# json_object.update(diction)
	#
	# with open('sample.json', 'w') as json_file:
	#     json.dump(json_object, json_file)

		print("Testing time - yes/no")
		x = input()
		if x == "yes":
			camera= cv2.VideoCapture(0)
			control = self.alpha()
		if control == screenshot:
			myScreenshot = pyautogui.screenshot()
			myScreenshot.save(r'.\xyz2.png')
			return 0

		while (1) :

			if control == screenshot:
				myScreenshot = pyautogui.screenshot()
				myScreenshot.save(r'.\xyz2.png')
				return 0
			else:
				camera = cv2.VideoCapture(0)
				control = self.alpha()
		# self.capture=cv2.VideoCapture(0)
			# self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,401)
			# self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,271)
			#
			# self.timer=QTimer(self)
			# self.timer.timeout.connect(self.update_frame)
			# self.timer.start(5)

	def update_frame(self):
		ret,self.image1=self.capture.read()
		self.fingers, self.image=self.gs.pass_frame(self.image1)
		self.image=cv2.flip(self.image,1)
		self.displayImage(self.image, self.image1,1)

	def stop_webcam(self):
		self.timer.stop()

	def displayImage(self,img, img1,window=1):
		self.gs.execute_action(self.fingers, img1)
		self.label.setText(self.gs.action)
		qformat=QImage.Format_Indexed8
		if (len(img.shape)==3):
			if (img.shape[2]==4):
				qformat=QImage.Format_RGBA8888
			else:
				qformat=QImage.Format_RGB888

		outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
		outImage=outImage.rgbSwapped()

		if window==1:
			self.imglabel.setPixmap(QPixmap.fromImage(outImage))
			self.imglabel.setScaledContents(True)

	def changeText(self):
		self.label.setText(self.gs.action)
		print(self.gs.action)

	#def query(self):




	# Keep looping






if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	splash = SplashScreen()
	splash.show()
	splash.progress()
	window = Main_UI()
	window.show()
	splash.finish(window)
	sys.exit(app.exec_())