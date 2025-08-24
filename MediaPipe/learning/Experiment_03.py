# This program checks whether the thump is open or closed
import mediapipe as mp
import cv2

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands.Hands(min_tracking_confidence = 0.5 , min_detection_confidence = 0.5 , max_num_hands = 1)
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

        # Default OUTPUT Text
        cv2.putText(frame , "Thumb Fingure " , (20,50) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,255,0) , 2)
        cv2.putText(frame , "Index Fingure " , (20,80) , cv2.FONT_HERSHEY_SIMPLEX ,1, (255,0,0) , 2)
        cv2.putText(frame , "Middle Fingure " , (20,110) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,0,255) , 2)
        cv2.putText(frame , "Ring Fingure " , (20,140) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,255,0) , 2)
        cv2.putText(frame , "Pinky Fingure " , (20,170) , cv2.FONT_HERSHEY_SIMPLEX ,1, (255,0,0) , 2)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame , hand_landmarks)  #whatever landmarks are present in hand_landmarks while be drawen to frame 
                # hand_landmarks = hand_landmarks.landmark
                for id , landmark in enumerate(hand_landmarks.landmark): #hand_landmarks.landmark → is a list of 21 landmarks (points) that MediaPipe detects on the hand.

                    #!id → the index number of the landmark (0, 1, 2, …, 20).
                    #!landmark → the actual landmark object, which contains .x , .y and .z:

                    x = int(landmark.x * frame_x)   #.x means only the x cordinate
                    y = int(landmark.y * frame_y)   #.y means only the y cordinate
                    #print("ID = ",id," X = ", x , " Y = " , y)
                

                    # For Thumb Fingure
                    id4_thumb_TIP = hand_landmarks.landmark[4]
                    id2_thump_PIP = hand_landmarks.landmark[2]

                    # For Index Fingure
                    id8_index_TIP = hand_landmarks.landmark[8]
                    id6_index_PIP = hand_landmarks.landmark[6]
                    
                    # For Middle Fingure
                    id12_index_TIP = hand_landmarks.landmark[12]
                    id10_index_PIP = hand_landmarks.landmark[10]

                    # For Ring Fingure
                    id16_index_TIP = hand_landmarks.landmark[16]
                    id14_index_PIP = hand_landmarks.landmark[14]

                    # For Pinky Fingure
                    id20_index_TIP = hand_landmarks.landmark[20]
                    id18_index_PIP = hand_landmarks.landmark[18]
                    
                    # For Thumb Fingure
                    #Extracting The Cordinate Of The tip and pip thump fingure , only x cordinate is compulsory 
                    x4 , y4 = int(id4_thumb_TIP.x * frame_x) , int(id4_thumb_TIP.y * frame_y)
                    x2 , y2 = int(id2_thump_PIP.x * frame_x) , int(id2_thump_PIP.y * frame_y)
                    
                    # For Index Fingre
                    x8 , y8 = int(id8_index_TIP.x * frame_x) , int(id8_index_TIP.y * frame_y)
                    x6 , y6 = int(id6_index_PIP.x * frame_x) , int(id6_index_PIP.y * frame_y)
                    
                    # For Middle Fingure
                    x12 , y12 = int(id12_index_TIP.x * frame_x) , int(id12_index_TIP.y * frame_y)
                    x10 , y10 = int(id10_index_PIP.x * frame_x) , int(id10_index_PIP.y * frame_y)

                    # For Ring Fingure
                    x16 , y16 = int(id16_index_TIP.x * frame_x) , int(id16_index_TIP.y * frame_y)
                    x14 , y14 = int(id14_index_PIP.x * frame_x) , int(id14_index_PIP.y * frame_y)

                    # For Pinky Fingure
                    x20 , y20 = int(id20_index_TIP.x * frame_x) , int(id20_index_TIP.y * frame_y)
                    x18 , y18 = int(id18_index_PIP.x * frame_x) , int(id18_index_PIP.y * frame_y)

                    # For Thumb Fingure
                    if x2 > x4 :
                        cv2.putText(frame , "Thumb Fingure Opened" , (20,50) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,255,0) , 2)
                    else:
                        cv2.putText(frame , "Thumb Fingure Closed"  , (20,50) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,255,0) , 2)
                    
                    # For Index Fingure
                    if y6 > y8 :
                        cv2.putText(frame , "Index Fingure Opened" , (20,80) , cv2.FONT_HERSHEY_SIMPLEX ,1, (255,0,0) , 2)
                    else:
                        cv2.putText(frame , "Index Fingure Closed"  , (20,80) , cv2.FONT_HERSHEY_SIMPLEX ,1, (255,0,0) , 2)

                    # For Middle Fingure
                    if y10 > y12 :
                        cv2.putText(frame , "Middle Fingure Opened" , (20,110) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,0,255) , 2)
                    else:
                        cv2.putText(frame , "Middle Fingure Closed"  , (20,110) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,0,255) , 2)

                    # For Ring Fingure
                    if y14 > y16 :
                        cv2.putText(frame , "Ring Fingure Opened" , (20,140) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,255,0) , 2)
                    else:
                        cv2.putText(frame , "Ring Fingure Closed"  , (20,140) , cv2.FONT_HERSHEY_SIMPLEX ,1, (0,255,0) , 2)

                    # For Pinky Fingure
                    if y18 > y20 :
                        cv2.putText(frame , "Pinky Fingure Opened" , (20,170) , cv2.FONT_HERSHEY_SIMPLEX ,1, (255,0,0) , 2)
                    else:
                        cv2.putText(frame , "Pinky Fingure Closed"  , (20,170) , cv2.FONT_HERSHEY_SIMPLEX ,1, (255,0,0) , 2)

        cv2.imshow("Fingure Status Detector" , frame)
        if cv2.waitKey(1) & 0xff == 27:
            break

    else:
        break
print("WebCam Frame Size = " , frame_x , frame_y)
#width = frame_x = 480 and height = frame_y = 640
cap.release()
cv2.destroyAllWindows()

# Idea store the if conditon result in a list 
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