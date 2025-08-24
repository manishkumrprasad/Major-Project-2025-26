import mediapipe as mp
import cv2
import pyautogui
import time
from collections import deque

# === Setup ===
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands.Hands(
    min_tracking_confidence=0.5,
    min_detection_confidence=0.5,
    max_num_hands=1
)
mp_drawing = mp.solutions.drawing_utils

# For smoothing
actions = deque(maxlen=5)

# Cooldown setup
last_action_time = 0
cooldown = 0.4  # seconds between key presses

def perform_action(action):
    global last_action_time
    if time.time() - last_action_time > cooldown:
        if action == "JUMP":
            pyautogui.press("up")
        elif action == "SLIDE":
            pyautogui.press("down")
        elif action == "MOVE LEFT":
            pyautogui.press("left")
        elif action == "MOVE RIGHT":
            pyautogui.press("right")
        last_action_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_y, frame_x, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hands.process(rgb_frame)
    action = "NONE"

    # Dynamic boundaries
    left_boundary = int(frame_x * 0.25)
    right_boundary = int(frame_x * 0.75)

    # Draw guide lines
    cv2.line(frame, (left_boundary, 0), (left_boundary, frame_y), (0, 0, 255), 2)
    cv2.line(frame, (right_boundary, 0), (right_boundary, frame_y), (0, 0, 255), 2)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks)

            # Extract landmarks
            lm = hand_landmarks.landmark
            def coord(id): return int(lm[id].x * frame_x), int(lm[id].y * frame_y)

            x2, y2 = coord(2)   # thumb knuckle
            x4, y4 = coord(4)   # thumb tip
            x6, y6 = coord(6)   # index knuckle
            x8, y8 = coord(8)   # index tip
            x10, y10 = coord(10)
            x12, y12 = coord(12)
            x14, y14 = coord(14)
            x16, y16 = coord(16)
            x18, y18 = coord(18)
            x20, y20 = coord(20)

            # === Gesture Logic ===
            # Slide (fist-like)
            if x2 < x4 and y8 > y6 and y12 > y10 and y16 > y14 and y20 > y18:
                action = "SLIDE"

            # Jump (4 fingers open)
            elif x2 < x4 and y8 < y6 and y12 < y10 and y16 < y14 and y20 < y18:
                action = "JUMP"

            # Move Left
            elif x4 < left_boundary:
                action = "MOVE LEFT"

            # Move Right
            elif x20 > right_boundary:
                action = "MOVE RIGHT"

            # Default = None
            else:
                action = "NONE"

    # Smooth actions
    actions.append(action)
    if actions.count(action) > 3 and action != "NONE":
        perform_action(action)

    # Show feedback
    cv2.putText(frame, f"Action = {action}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("Temple Run Controller", frame)

    if cv2.waitKey(1) & 0xff == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
