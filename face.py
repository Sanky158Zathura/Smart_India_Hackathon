import cv2
import time
import face_recognition
import os

img1 = []

cTime = 0
pTime = 0
c = 0
u = 0
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:

    rt, frame = cap.read()
    resized_frame = cv2.resize(frame, None, fx=0.25, fy=0.25)

    if (len(img1) == 0 or u == 1):
        try:
            img1 = face_recognition.load_image_file("photo.jpg")
            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            face = face_recognition.face_locations(img1)[0]
            # print("entered")
            encodeFace = face_recognition.face_encodings(img1)[0]
            # print(encodeFace)
            u = 0
        except Exception as e:
            filePath = os.getcwd()
            cv2.imwrite(filePath + "\photo.jpg", resized_frame)
            print("Exception raised ", e)
            u = 1
            continue
    resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        face_live = face_recognition.face_locations(resized_frame)[0]
        print("no of faces : ", len(face_recognition.face_locations(frame)))
        encodeFace_live = face_recognition.face_encodings(frame)[0]

        res = face_recognition.compare_faces([encodeFace], encodeFace_live)
        distance = face_recognition.face_distance([encodeFace], encodeFace_live)
        print(res, distance)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # print(fps, resized_frame.shape)

    # cv2.rectangle(frame, (face_live[3]*4, face_live[0]*4), (face_live[1]*4,
    #                                                         face_live[2]*4), (0, 255, 0), 2)

    if cv2.waitKey(1) == 13:
        break

    cv2.imshow('image', frame)
    c = c + 1

cap.release()
cv2.destroyAllWindows()