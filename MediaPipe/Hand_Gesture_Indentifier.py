import cv2
import mediapipe as mp

# Initialize mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Function to detect gestures
def get_gesture(hand_landmarks):
    landmarks = hand_landmarks.landmark

    # Tip landmarks for each finger
    tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky tips
    fingers = []

    # Thumb (x-coordinates comparison since hand may be rotated)
    if landmarks[tips[0]].x < landmarks[tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other four fingers (y-coordinates)
    for id in tips[1:]:
        if landmarks[id].y < landmarks[id - 2].y:
            fingers.append(1)  # Finger is open
        else:
            fingers.append(0)  # Finger is closed

    # Interpret gesture
    if fingers == [0, 0, 0, 0, 0]:
        return "Fist ✊"
    elif fingers == [1, 1, 1, 1, 1]:
        return "Open Palm ✋"
    elif fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up 👍"
    elif fingers == [0, 1, 0, 0, 0]:
        return "Pointing ☝️"
    else:
        return "Unknown"

# OpenCV webcam loop
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame , 1)
    if not ret:
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    gesture = "No Hand"
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = get_gesture(hand_landmarks)

    # Display gesture
    cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Hand Gesture Identifier", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
