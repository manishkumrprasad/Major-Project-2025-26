"""
Temple Run controller with:
- Swipe (left/right) for turning
- Finger-count detection for jump/slide
"""

import cv2
import mediapipe as mp
import pyautogui
import time
from collections import deque
import numpy as np

# Parameters
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
HISTORY_SECONDS = 0.35
SWIPE_TIME = 0.25
SWIPE_DIST_RATIO = 0.25
COOLDOWN = 0.6
MIN_CONFIDENCE = 0.6

SWIPE_DIST_X = SWIPE_DIST_RATIO * FRAME_WIDTH
SWIPE_DIST_Y = SWIPE_DIST_RATIO * FRAME_HEIGHT

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=MIN_CONFIDENCE,
    min_tracking_confidence=MIN_CONFIDENCE
)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

history = deque()
last_swipe_time = 0.0
last_finger_action_time = 0.0

def get_centroid(landmarks, image_w, image_h):
    pts = np.array([[lm.x * image_w, lm.y * image_h] for lm in landmarks])
    centroid = pts.mean(axis=0)
    return float(centroid[0]), float(centroid[1])

def detect_swipe(history):
    if len(history) < 2:
        return None
    t_latest, (x_latest, y_latest) = history[-1]

    earliest_idx = None
    for i in range(len(history)-2, -1, -1):
        t_i, _ = history[i]
        if t_latest - t_i <= SWIPE_TIME:
            earliest_idx = i
        else:
            break
    if earliest_idx is None:
        return None

    t_earliest, (x_earliest, y_earliest) = history[earliest_idx]
    dx = x_latest - x_earliest
    dy = y_latest - y_earliest
    abs_dx, abs_dy = abs(dx), abs(dy)

    if abs_dx >= abs_dy:
        if abs_dx >= SWIPE_DIST_X:
            return 'right' if dx > 0 else 'left'
    else:
        if abs_dy >= SWIPE_DIST_Y:
            return 'down' if dy > 0 else 'up'
    return None

def count_fingers(hand_landmarks, image_w, image_h):
    """Return number of extended fingers (approximate)."""
    fingers = []

    # Thumb
    if hand_landmarks[4].x < hand_landmarks[3].x:  # right hand assumption
        fingers.append(1)
    else:
        fingers.append(0)

    # Other 4 fingers
    tips_ids = [8, 12, 16, 20]
    for tip in tips_ids:
        if hand_landmarks[tip].y < hand_landmarks[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

print("Gesture controller running. Press 'q' to quit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_h, image_w = frame.shape[:2]
        results = hands.process(frame_rgb)

        now = time.time()
        while history and (now - history[0][0] > HISTORY_SECONDS):
            history.popleft()

        gesture_text = ""

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0].landmark
            cx, cy = get_centroid(hand_landmarks, image_w, image_h)
            history.append((now, (cx, cy)))

            mp_drawing.draw_landmarks(frame, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)
            cv2.circle(frame, (int(cx), int(cy)), 6, (0, 255, 0), -1)

            # Swipe detection
            swipe = detect_swipe(history)
            if swipe and (now - last_swipe_time > COOLDOWN):
                last_swipe_time = now
                gesture_text = f"SWIPE: {swipe.upper()}"
                print(gesture_text)
                if swipe == 'left':
                    pyautogui.press('left')
                elif swipe == 'right':
                    pyautogui.press('right')

            # Finger count detection
            finger_count = count_fingers(hand_landmarks, image_w, image_h)
            if now - last_finger_action_time > COOLDOWN:
                if finger_count == 1:
                    pyautogui.press('up')     # Jump
                    gesture_text = "1 Finger: JUMP"
                    last_finger_action_time = now
                elif finger_count == 2:
                    pyautogui.press('down')   # Slide
                    gesture_text = "2 Fingers: SLIDE"
                    last_finger_action_time = now
                elif finger_count == 5:
                    gesture_text = "5 Fingers: Open Palm"

        cv2.putText(frame, "Gesture: " + (gesture_text if gesture_text else "None"), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.imshow("TempleRun Hand Control", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    hands.close()
    print("Exited.")
