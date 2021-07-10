import cv2
import numpy as np

widthImg = 640
heightImg = 480

cap = cv2.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
cap.set(10,150)
def preProcessing(img):
    imgGray = cv2.cvtColor((img, cv2.COLOR_BGR2GRAY))
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur,200,200)


while True:
    success, img= cap.read()
    cv2.resize(img,(widthImg, heightImg))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break