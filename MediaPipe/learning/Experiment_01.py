import mediapipe as mp
import cv2

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands.Hands(min_tracking_confidence = 0.5 , min_detection_confidence = 0.5 , max_num_hands = 2)
# Hands = mp_hands.Hands(min_tracking_confidence = 0.5 , min_detection_confidence = 0.5)
mp_drawing = mp.solutions.drawing_utils

ideight_x , ideight_y , idfour_x , idfour_y =  0 , 0 , 0 ,0

while cap.isOpened:

    ret , frame = cap.read()
    if ret:
        
        frame = cv2.flip(frame , 1)
        frame_y , frame_x , _ = frame.shape #frame.shape return y cordinate then x cordinate like (y,x)

        rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
        result = mp_hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame , hand_landmarks )  #whatever landmarks are present in hand_landmarks while be drawen to frame 
                # hand_landmarks = hand_landmarks.landmark
                for id , landmark in enumerate(hand_landmarks.landmark): #hand_landmarks.landmark → is a list of 21 landmarks (points) that MediaPipe detects on the hand.

                    #!id → the index number of the landmark (0, 1, 2, …, 20).
                    #!landmark → the actual landmark object, which contains .x , .y and .z:

                    x = int(landmark.x * frame_x)   #.x means only the x cordinate
                    y = int(landmark.y * frame_y)   #.y means only the y cordinate
                    #print("ID = ",id," X = ", x , " Y = " , y)

                    if id == 4 or id == 8:


                        if id == 8:
                            ideight_x = x
                            ideight_y = y
                            cv2.circle(img = frame , center= (x , y) , radius=15 , color=(0,255,255) , thickness= 1)
                        elif id == 4:
                            idfour_x = x
                            idfour_y = y
                            if ideight_x == idfour_x and ideight_y == idfour_y:
                                print("Action Trigerred")
                                print(f"ID 8 Cordinate = {ideight_x,ideight_y} And ID 4 Cordinate = {idfour_x,idfour_y}")
                            
                        # if id 4 landmarks distance from frame and id 8 landmark distance from frame is same then we want to print something on the terminal

        cv2.imshow("Webcam" , frame)
        if cv2.waitKey(1) & 0xff == 27:
            break

    else:
        break
print("WebCam Frame Size = " , frame_x , frame_y)
#width = frame_x = 480 and height = frame_y = 640
cap.release()
cv2.destroyAllWindows()

'''
0  → Wrist  
1  → Thumb CMC  
2  → Thumb MCP  
3  → Thumb IP  
4  → Thumb tip  

5  → Index finger MCP  
6  → Index finger PIP  
7  → Index finger DIP  
8  → Index finger tip  

9  → Middle finger MCP  
10 → Middle finger PIP  
11 → Middle finger DIP  
12 → Middle finger tip  

13 → Ring finger MCP  
14 → Ring finger PIP  
15 → Ring finger DIP  
16 → Ring finger tip  

17 → Pinky MCP  
18 → Pinky PIP  
19 → Pinky DIP  
20 → Pinky tip

'''