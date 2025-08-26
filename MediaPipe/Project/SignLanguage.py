import mediapipe as mp 
import cv2


cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands.Hands(min_tracking_confidence = 0.5 , min_detection_confidence = 0.5 , max_num_hands = 1)
mp_drawing = mp.solutions.drawing_utils


while cap.isOpened():

    ret , frame = cap.read()
    frame = cv2.flip(frame , 1)
    bgr2rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    result = mp_hands.process(bgr2rgb)
    frame_y , frame_x , _ = frame.shape
    # cv2.putText(frame ,f"Sign Language : None" ,(20,20) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)
    
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame , hand_landmarks)
            

            x4 , y4 = (hand_landmarks.landmark[4].x * frame_x) , ( hand_landmarks.landmark[4].y * frame_y)
            x6 , y6 = (hand_landmarks.landmark[6].x * frame_x) , ( hand_landmarks.landmark[6].y * frame_y)
            x10 , y10 = (hand_landmarks.landmark[10].x * frame_x) , ( hand_landmarks.landmark[10].y * frame_y)
            x14 , y14 = (hand_landmarks.landmark[14].x * frame_x) , ( hand_landmarks.landmark[14].y * frame_y)
            x18 , y18 = (hand_landmarks.landmark[18].x * frame_x) , ( hand_landmarks.landmark[18].y * frame_y)
            
            if y4 > y6 and y6 == y10 and y10 > y14 and y14 > y18:
                action = "A"
                cv2.putText(frame ,f"Sign Language = {action}" ,(20,20) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)



    cv2.imshow("Sign Language Detector" , frame)
    if cv2.waitKey(1) & 0xff == 27:
        break
    
cap.release()
cv2.destroyAllWindows()