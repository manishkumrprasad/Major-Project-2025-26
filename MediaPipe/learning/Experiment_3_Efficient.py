# This program checks whether each finger is open or closed
import mediapipe as mp
import cv2

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

    # Default labels
    cv2.putText(frame, "Thumb Finger", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.putText(frame, "Index Finger", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv2.putText(frame, "Middle Finger", (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.putText(frame, "Ring Finger", (20, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.putText(frame, "Pinky Finger", (20, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

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

            # === Finger status checks ===
            # Thumb (uses x-axis)
            if x2 > x4:  # (assumes right hand; flip logic for left)
                cv2.putText(frame, "Thumb Finger Opened", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            else:
                cv2.putText(frame, "Thumb Finger Closed", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            # Index
            if y8 < y6:
                cv2.putText(frame, "Index Finger Opened", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
            else:
                cv2.putText(frame, "Index Finger Closed", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            # Middle
            if y12 < y10:
                cv2.putText(frame, "Middle Finger Opened", (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            else:
                cv2.putText(frame, "Middle Finger Closed", (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            # Ring
            if y16 < y14:
                cv2.putText(frame, "Ring Finger Opened", (20, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            else:
                cv2.putText(frame, "Ring Finger Closed", (20, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            # Pinky
            if y20 < y18:
                cv2.putText(frame, "Pinky Finger Opened", (20, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
            else:
                cv2.putText(frame, "Pinky Finger Closed", (20, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Finger Status Detector", frame)
    if cv2.waitKey(1) & 0xff == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
