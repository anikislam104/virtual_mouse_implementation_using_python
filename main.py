import cv2
import mediapipe as mp
cap=cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
