import mediapipe as mp
import cv2
import pyautogui

cap = cv2.VideoCapture(1)
prev_x , prev_y = 0 , 0
smoothening = 5
screen_w, screen_h = pyautogui.size()
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode = False,
    max_num_hands = 2,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
)

mp_drawing = mp.solutions.drawing_utils

while cap.isOpened():
    ret , frame = cap.read()
    frame = cv2.flip(frame , 1)
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in  result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame , hand_landmarks , mp_hands.HAND_CONNECTIONS)

            #hand_landmarks
            #This object holds all the detected points of the hand found by MediaPipe.
            #Each hand has 21 landmarks (fixed positions like fingertip, joints, wrist, etc.).

           
            x = hand_landmarks.landmark[8].x
            y = hand_landmarks.landmark[8].y

            cx, cy = int(x * screen_w), int(y * screen_h)

            curr_x = prev_x + (cx - prev_x) / smoothening
            curr_y = prev_y + (cy - prev_y) / smoothening
            
            prev_x, prev_y = curr_x, curr_y
            pyautogui.moveTo(curr_x, curr_y)

    cv2.imshow("Webcam" , frame)

    if cv2.waitKey(1) & 0Xff == 27:
        break

cap.release()
cv2.destroyAllWindows()