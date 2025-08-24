# This program checks whether each finger is open or closed
import mediapipe as mp
import cv2
import pyautogui

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands.Hands(
    min_tracking_confidence=0.5,
    min_detection_confidence=0.5,
    max_num_hands=1
)
mp_drawing = mp.solutions.drawing_utils

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_y, frame_x, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hands.process(rgb_frame)
    out_result = "None"
    # cv2.putText(frame, f"Gesture = {out_result}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.line(frame , (150,0) , (150,480) , (0,0,255) , 2)
    cv2.line(frame , (490,0) , (490,480) , (0,0,255) , 2)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks )
            # mp_drawing.draw_landmarks(frame, hand_landmarks , mp.solutions.hands.HAND_CONNECTIONS) #also joints the landmark from one another

            # === Extract needed landmarks once per frame ===
            # Thumb
            x4, y4 = int(hand_landmarks.landmark[4].x * frame_x), int(hand_landmarks.landmark[4].y * frame_y)
            x2, y2 = int(hand_landmarks.landmark[2].x * frame_x), int(hand_landmarks.landmark[2].y * frame_y)

            # Index
            x8, y8 = int(hand_landmarks.landmark[8].x * frame_x), int(hand_landmarks.landmark[8].y * frame_y)
            x6, y6 = int(hand_landmarks.landmark[6].x * frame_x), int(hand_landmarks.landmark[6].y * frame_y)

            # Middle
            x12, y12 = int(hand_landmarks.landmark[12].x * frame_x), int(hand_landmarks.landmark[12].y * frame_y)
            x10, y10 = int(hand_landmarks.landmark[10].x * frame_x), int(hand_landmarks.landmark[10].y * frame_y)

            # Ring
            x16, y16 = int(hand_landmarks.landmark[16].x * frame_x), int(hand_landmarks.landmark[16].y * frame_y)
            x14, y14 = int(hand_landmarks.landmark[14].x * frame_x), int(hand_landmarks.landmark[14].y * frame_y)

            # Pinky
            x20, y20 = int(hand_landmarks.landmark[20].x * frame_x), int(hand_landmarks.landmark[20].y * frame_y)
            x18, y18 = int(hand_landmarks.landmark[18].x * frame_x), int(hand_landmarks.landmark[18].y * frame_y)

            #Slide
            if x2 < x4 and  y8 > y6 and y12 > y10 and y16 > y14 and y20 > y18:
                action = "SLIDE"#jump when hend gesture is in fist mode
                out_result = "Fist"
                cv2.putText(frame, f"Gesture = {out_result} , Action = {action}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
                # pyautogui.typewrite(['down'] , 1)
                pyautogui.press('down')

            #Doing Nothing
            elif (y2 > y4 or x2 > x4) and  y8 > y6 and y12 > y10 and y16 > y14 and y20 > y18:
                out_result = "Thumbs Up"
                cv2.putText(frame, f"Gesture = {out_result}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

            #Jump
            elif x2 < x4 and  y8 < y6 and y12 < y10 and y16 < y14 and y20 < y18:
                action = "JUMP"
                out_result = "Four Fingurs Open"
                cv2.putText(frame, f"Gesture = {out_result} , Action = {action}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
                # pyautogui.typewrite(['up'] , 1)
                pyautogui.press('up')
            # Move Left
            elif x4 < 150:
                action = "MOVE LEFT"
                out_result = "Moving LEft"
                cv2.putText(frame, f"Gesture = {out_result} , Action = {action}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
                pyautogui.press('left')
            # Move Right
            elif x20 > 490:
                action = "MOVE RIGHT"
                out_result = "Moving Right"
                cv2.putText(frame, f"Gesture = {out_result} , Action = {action}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
                pyautogui.press('right')
            else:
                action = "nothing"#no action when 5 fingers are shown
                out_result = "None"
                cv2.putText(frame, f"Gesture = {out_result}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.imshow("Finger Status Detector", frame)
    if cv2.waitKey(1) & 0xff == 27:  # ESC to quit
        break

print("WebCam Frame Size = " , frame_x , frame_y)
cap.release()
cv2.destroyAllWindows()

# Idea 01
# Divide the frame into three parts(left,center , right) and see if the hand is in left half or right half 
# if it is in first half then move left and if in third half move right
# if the hand is in center do nothing

# Idea 02
# we can write the logic if 
        #only one fingure is open do this
        #if two fingures are open do this
        #if three fingures are open do this
        #and so on

# Idea 03
# if the thumb fingure is x distance from left side of the frame move left
# If the pinky fingure is x distance from left side of the frame move right 