import math
import mediapipe as mp
import cv2

cap = cv2.VideoCapture(1)
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

                    id4 = hand_landmarks.landmark[4]
                    id8 = hand_landmarks.landmark[8]

                    x4 , y4 = int(id4.x * frame_x) , int(id4.y * frame_y)
                    x8 , y8 = int(id8.x * frame_x) , int(id8.y * frame_y)
                    
                    #putting circle on the landmark 4 and 8
                    cv2.circle(frame , (x4 , y4) , 20 , (0,0,255) , 2 )
                    cv2.circle(frame , (x8 , y8) , 20 , (255,0,0) , 2 )

                    # now i want to calculate the distance between the above two points
                    dist = math.hypot(x8 - x4 , y8 - y4) # similar to math.sqrt((x8 - x4)**2 + (y8 - y4)**2)
                    int_dist = int(dist)
                    cv2.putText(frame ,
                                    f"Distance {int_dist} px", #text
                                    (10,80),                   #Posiiton
                                    cv2.FONT_HERSHEY_SIMPLEX , #font
                                    0.8,                         #font scale
                                    (0,255,0),                 #color
                                    1,                         #thicknes
                                    cv2.LINE_AA)

                    if dist <= 50:
                        cv2.putText(frame ,
                                    "Distance Less Than 50px", #text
                                    (10,50),                   #Posiiton
                                    cv2.FONT_HERSHEY_SIMPLEX , #font
                                    1,                         #font scale
                                    (0,255,0),                 #color
                                    1,                         #thicknes
                                    cv2.LINE_AA)               #smoothness
                    else:
                        cv2.putText(frame ,
                                    "Distance Greater Than 50px", #text
                                    (10,50),                   #Posiiton
                                    cv2.FONT_HERSHEY_SIMPLEX , #font
                                    1,                         #font scale
                                    (0,255,0),                 #color
                                    1,                         #thicknes
                                    cv2.LINE_AA)               #smoothness
        cv2.imshow("Webcam" , frame)
        if cv2.waitKey(1) & 0xff == 27:
            break

    else:
        break
print("WebCam Frame Size = " , frame_x , frame_y)
#width = frame_x = 480 and height = frame_y = 640
cap.release()
cv2.destroyAllWindows()

