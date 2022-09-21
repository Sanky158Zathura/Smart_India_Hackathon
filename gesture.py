import cv2
import HandTracking as htm

totalFingers = 0
fingers = []
import time

flag = -1
from pygame.time import delay

from pynput.keyboard import Key, Controller
import win32api
from win32con import *

keyboard = Controller()
prev = 0
num = 1


class gesture():
    def __init__(self):
        # self.wcam = 640
        # self.hcam = 480
        # self.cap = cv2.VideoCapture(0)
        # self.cap.set(3, self.wcam)
        # self.cap.set(4, self.hcam)
        self.tipIds = [4, 8, 12, 16, 20]
        self.x = 0
        self.y = 0
        self.z1 = 0
        self.z2 = 0
        self.z3 = 0
        self.action = "No action"
        self.detector = htm.handDetector(detectionCon=0.75)
        self.previous = 0
        self.present = 0
        self.c = 1

    def hands(self, img, draw):

        img = self.detector.findHands(img, draw)
        lmlist = self.detector.findPosition(img, draw=False)

        if len(lmlist) != 0:
            global fingers
            fingers = []
            if lmlist[self.tipIds[0]][1] > lmlist[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):
                if lmlist[self.tipIds[id]][2] < lmlist[self.tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            global totalFingers
            global flag
            # if len(fingers) != 0:
            #     print(lmlist[4][2]-lmlist[8][2])
            # print(abs(lmlist[0][2]-lmlist[17][2]) > abs(lmlist[0][1]-lmlist[17][1]))
            if lmlist[4][2] - lmlist[8][2] < 30 and fingers[2]:
                print("Super")
            # if lmlist[0][2]-lmlist[17][2] > 100 or lmlist[0][2]-lmlist[17][2] < -75:
            #     totalFingers= fingers.count(1)
            if abs(lmlist[0][2] - lmlist[17][2]) > abs(lmlist[0][1] - lmlist[17][1]):
                totalFingers = fingers.count(1)
            else:
                totalFingers = 20
                if lmlist[4][2] > lmlist[3][2]:
                    print("Thumbs down")
                    flag = 1
                elif lmlist[4][2] < lmlist[3][2]:
                    print("Thumbs up")
                    flag = 2
                else:
                    flag = 0

                # print(lmlist[4][2]-lmlist[8][2])

            # cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
            #             10, (255, 0, 0), 25)

            return totalFingers, img
        return 0, img
        # i = 0
        # for i in range(0, 20):
        #     fingers.append(totalFingers)
        #     i = i + 1
        # i = 0
        # for i in range(0, 4):
        #     if fingers.count(i) > 12:
        #         totalFingers = i

    def direction(self, img):

        img = self.detector.findHands(img)
        lmlist = self.detector.findPosition(img, draw=False)
        # print(self.x)
        # print(fingers)

        dirn = -1
        if len(lmlist) != 0:

            if self.y - lmlist[0][2] > 10:
                dirn = 0
            elif self.y - lmlist[0][2] < -10:
                dirn = 1
            elif self.x - lmlist[0][1] > 10:
                dirn = 2
            elif self.x - lmlist[0][1] < -10:
                dirn = 3
            elif ((self.z1 - lmlist[4][2]) - (self.z2 - lmlist[8][2])) < -8 and fingers == [1, 1, 0, 0, 0]:
                dirn = 4
                # print("Zoom in")
            elif ((self.z1 - lmlist[4][2]) - (self.z2 - lmlist[8][2])) > 8 and fingers == [1, 1, 0, 0, 0]:
                dirn = 5
                # print("Zoom out")
            # if (self.z2  - lmlist[8][2])*(-self.z3 + lmlist[8][1]) > 100:
            #     print("clockwise")
            # elif (self.z2  - lmlist[8][2])*(-self.z3 + lmlist[8][1]) < -100:
            #     print("Anti")
            # print((self.z2  - lmlist[8][2])*(-self.z3 + lmlist[8][1]))
            self.x = lmlist[0][1]
            self.y = lmlist[0][2]
            self.z1 = lmlist[4][2]
            self.z2 = lmlist[8][2]
            # self.z3 = lmlist[8][1]
            # print("fffffffffff")
            # print(totalFingers)

            return dirn

    def pass_frame(self, img):
        totalFingers, img = self.hands(img, True)
        return totalFingers, img

    # def systemsetting(self, img):
    #     print("Entered system setting")                         #system settings
    #     finger=self.hands(img)
    #     global prev
    #     global flag
    #         # prev=finger
    #     direct = self.direction(img)
    #     if finger == 1:                           #1 for volume up and down
    #         prev = 1
    #         if direct == 0:
    #             keyboard.press(Key.media_volume_up)
    #             self.action="Volume up"
    #             print("entered volume up")
    #         elif direct == 1:
    #             keyboard.press(Key.media_volume_down)
    #             self.action="Volume down"
    #             print("Entered volume down")
    #     elif finger == 2:                                  #2 for volume mute and unmute
    #         print("finger==2")
    #         if prev != finger:
    #             prev = 2
    #             keyboard.press(Key.media_volume_mute)
    #             self.action="Volume Muted"
    #             print("Muted")
    #
    #     elif finger == 3:                        #3 for play/pause
    #
    #         if prev != finger:
    #             prev = 3
    #             keyboard.press(Key.media_play_pause)
    #             self.action="Play/Pause"
    #
    #     # elif finger == 4:  # to fast forward and revert back while playing youtube video
    #     #     if direct == 2:
    #     #         keyboard.press("l")
    #     #         self.action="Forward"
    #     #     elif direct == 3:
    #     #         keyboard.press("j")
    #     #         self.action="Backward"
    #     #
    #     elif finger == 4:# to fast forward and revert back while playing youtube video
    #         keyboard.press(Key.alt)
    #         if direct == 2 :
    #             keyboard.release(Key.shift)
    #             keyboard.press(Key.tab)
    #             self.action="next tab"
    #         elif direct == 3:
    #             keyboard.press(Key.shift)
    #             keyboard.press(Key.tab)
    #             self.action="previous tab"
    #
    #         if flag :
    #             flag = 0
    #             keyboard.release(Key.alt)
    #             keyboard.release(Key.shift)
    #     else :
    #         prev = finger
    #     prev =5
    #

    #
    # def photo_viewer(self, img):
    #     prev=0
    #     finger=self.hands(img)
    #         # prev=finger
    #     direct = self.direction(img)
    #     if finger == 1:                           #1 for volume up and down
    #         prev = 1
    #         if direct == 2 :
    #             keyboard.press(Key.left)
    #             keyboard.release(Key.left)
    #             self.action="Previous"
    #         if direct == 3:
    #              keyboard.press(Key.right)
    #              keyboard.release(Key.right)
    #              self.action="Next"
    #         elif direct == 0:
    #             keyboard.press(Key.up)
    #             keyboard.release(Key.up)
    #             self.action="Up"
    #         elif direct == 1:
    #             keyboard.press(Key.down)
    #             keyboard.release(Key.down)
    #             self.action="Down"
    #     elif finger == 2:                                  #2 for volume mute and unmute
    #
    #         newpos = win32api.GetCursorPos()
    #
    #         if direct == 4:
    #             for i in range(0,200):
    #                 keyboard.press(Key.ctrl)
    #                 win32api.mouse_event(MOUSEEVENTF_WHEEL,newpos[0],newpos[1], -1, 0)
    #                 print("gggggggggggggggggggg")
    #                 self.action="Zoom in"
    #         elif direct ==5:
    #             for i in range(0,200):
    #                 keyboard.press(Key.ctrl)
    #                 win32api.mouse_event(MOUSEEVENTF_WHEEL,newpos[0],newpos[1], 1, 0)
    #                 print("gggggggggggggggggggg")
    #                 self.action="Zoom Out"
    #
    #                 # print(newpos)
    #         if prev != finger:
    #             prev = 2
    #
    #     else :
    #         prev = finger
    #         keyboard.release(Key.ctrl)
    #     prev =5

    # def document(self, img):
    #     prev = 0
    #     finger = self.hands(img)
    #
    #     direct = self.direction(img)
    #     if finger == 1:      # 1 for volume up and down based on direction of finger
    #         prev = 1
    #         if direct == 0:
    #             keyboard.press(Key.page_up)
    #             keyboard.release(Key.page_up)
    #             self.action="Page Up"
    #         elif direct == 1:
    #             keyboard.press(Key.page_down)
    #             keyboard.release(Key.page_down)
    #             self.action="Page Down"
    #     elif finger == 2:
    #         prev = 2
    #         keyboard.press(Key.f12)
    #         self.action="Save as"
    #     elif finger == 3 and prev != finger:
    #         prev = 3
    #         keyboard.press(Key.ctrl)
    #         keyboard.press("p")
    #         keyboard.release(Key.ctrl)
    #         self.action="Print"
    #     elif finger == 4 and prev != finger:
    #         prev = 4
    #         keyboard.press(Key.alt)
    #         keyboard.press(Key.f4)
    #         keyboard.press(Key.enter)
    #         keyboard.release(Key.alt)
    #         self.action="Close"
    #     else:
    #         prev = finger
    #

    def execute_action(self, totalfingers, img):

        if totalfingers == 5:
            self.previous = 0;
            self.action = "No action"
            self.c = 1

        else:
            if self.previous == 0:
                if self.c % 3 == 0:
                    self.previous = totalfingers
                self.c += 1

            self.present = totalfingers
            global prev

            # if self.previous==1:        # SYSTEM SETTING
            #     if self.present == 0:
            #         prev = 0
            #         self.action = "System Settings"
            #         pass
            #     elif self.present==1 :
            #         prev = 1
            #         self.action="Volume"
            #         direct = self.direction(img)
            #                   #1 for volume up and down
            #
            #         if direct == 0:
            #             keyboard.press(Key.media_volume_up)
            #             self.action="Volume up"
            #             print("entered volume up")
            #         elif direct == 1:
            #             keyboard.press(Key.media_volume_down)
            #             self.action="Volume down"
            #             print("Entered volume down")
            #
            #
            #     # elif finger==1 and self.direction(img)==1:
            #     #     self.action="volume down"
            #     elif self.present==2 and prev!=2:
            #         prev = 2
            #         self.action="Mute"
            #         keyboard.press(Key.media_volume_mute)
            #         self.action="Volume Muted"
            #         print("Muted")
            #     elif self.present==3 and prev !=3:
            #         prev = 3
            #         keyboard.press(Key.media_play_pause)
            #         self.action="Play/pause"
            #
            #     elif self.present == 4 :  # to fast forward and revert back while playing youtube video
            #         prev = 4
            #         direct = self.direction(img)
            #         if direct == 2:
            #             keyboard.press("l")
            #             self.action="Forward"
            #         elif direct == 3:
            #             keyboard.press("j")
            #             self.action="Backward"

            # elif self.present == 4:  # to fast forward and revert back while playing youtube video
            #     keyboard.press(Key.alt)
            #     if direct == 2:
            #         keyboard.release(Key.shift)
            #         keyboard.press(Key.tab)
            #         self.action = "next tab"
            #     elif direct == 3:
            #         keyboard.press(Key.shift)
            #         keyboard.press(Key.tab)
            #         self.action = "previous tab"
            #
            #     if flag:
            #         flag = 0
            #         keyboard.release(Key.alt)
            #         keyboard.release(Key.shift)

            # elif self.previous==2:      # PHOTO VIEWER
            #     if self.present==1 :
            #         prev = 1
            #         self.action = "PREV / NEXT photos"
            #         direct = self.direction(img)
            #         if direct == 2 :
            #             keyboard.press(Key.right)
            #             keyboard.release(Key.right)
            #             self.action="Previous"
            #         if direct == 3:
            #             keyboard.press(Key.left)
            #             keyboard.release(Key.left)
            #             self.action="Next"
            #         elif direct == 0:
            #             keyboard.press(Key.up)
            #             keyboard.release(Key.up)
            #             self.action="Up"
            #         elif direct == 1:
            #             keyboard.press(Key.down)
            #             keyboard.release(Key.down)
            #             self.action="Down"
            #     elif self.present==2:
            #
            #         newpos = win32api.GetCursorPos()
            #         direct =  self.direction(img)
            #         if direct == 4:
            #             for i in range(0,100):
            #                 keyboard.press(Key.ctrl)
            #                 win32api.mouse_event(MOUSEEVENTF_WHEEL,newpos[0],newpos[1], 1, 0)
            #                 # print("gggggggggggggggggggg")
            #                 self.action="Zoom in"
            #         elif direct ==5:
            #             for i in range(0,100):
            #                 keyboard.press(Key.ctrl)
            #                 win32api.mouse_event(MOUSEEVENTF_WHEEL,newpos[0],newpos[1], -1, 0)
            #                 # print("gggggggggggggggggggg")
            #                 self.action="Zoom Out"
            #
            #         keyboard.release(Key.ctrl)
            #
            global flag
            if self.previous == 1:  # DOCUMENT
                if self.present == 1:
                    self.action = "Page up/down"
                    prev = 1
                    direct = self.direction(img)
                    if direct == 0:
                        keyboard.press(Key.page_up)
                        keyboard.release(Key.page_up)
                        self.action = "Page Up"
                    elif direct == 1:
                        keyboard.press(Key.page_down)
                        keyboard.release(Key.page_down)
                        self.action = "Page Down"
                elif self.present == 2 and prev != 2:
                    self.action = "Save as"
                    prev = 2
                    keyboard.press(Key.f12)
                elif self.present == 3 and prev != 3:
                    self.action = "Print"
                    prev = 3
                    keyboard.press(Key.ctrl)
                    keyboard.press("p")
                    keyboard.release(Key.ctrl)
                elif self.present == 4 and prev != 4:
                    self.action = "Close"
                    prev = 4
                    keyboard.press(Key.alt)
                    keyboard.press(Key.f4)
                    # for i in range (0,100):
                    keyboard.release(Key.alt)
                    # for i in range(0,1000):
                    #     pass

                    # time.sleep(2)
                    # keyboard.press(Key.enter)
                if flag == 1:
                    keyboard.press(Key.esc)
                    self.action = "thumbs down"
                    totalfingers = 5
                elif flag == 3:
                    keyboard.press(Key.enter)
                    self.action = "thumbs up"
                    keyboard.release(Key.enter)
                    totalfingers = 5

            print("previous = ", self.previous, "present = ", self.present)


def main():
    cap = cv2.VideoCapture(0)
    g1 = gesture()
    while True:
        temp = g1.hands()
        # print(temp)
        g1.direction()


if __name__ == '__main__':
    main()
