import cv2
import mediapipe as mp
import pyautogui as pag
cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width,screen_height=pag.size()

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_height, frame_width, _ = frame.shape
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    # print(hands)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                print(x,y)
                if id==8:
                    cv2.circle(frame, (x,y), 20, (0,255,255))
                    index_x=screen_width/frame_width*x
                    index_y=screen_height/frame_height*y
                    pag.moveTo(index_x,index_y)
                # cv2.circle(frame, (x,y), 20, (0,255,255))
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
