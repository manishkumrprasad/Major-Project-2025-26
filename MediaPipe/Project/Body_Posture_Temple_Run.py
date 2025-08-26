import cv2
import mediapipe as mp
import pydirectinput

cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence = 0.5 , min_detection_confidence = 0.5)

while cap.isOpened():
    ret , frame = cap.read()
    cv2.line(frame , (0,150) , (640,150) , (0,0,225) , 2)
    frame = cv2.flip(frame , 1)
    frame_y , frame_x , _ = frame.shape

    bgr2_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    result = pose.process(bgr2_rgb)

    if result.pose_landmarks:
        for pose_landmark in result.pose_landmarks.landmark:
            mp_drawing.draw_landmarks(frame , result.pose_landmarks , mp_pose.POSE_CONNECTIONS)

            x0 , y0  = int(result.pose_landmarks.landmark[0].x * frame_x) , int(result.pose_landmarks.landmark[0].y * frame_y)
            
            #print(f"X cordinate = {x0} and Y cordinate = {y0}")


            if y0 < 150 :
                Action = "JUMP"
                cv2.putText(frame , f"Action = {Action}" ,  (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
                pydirectinput.press('up' , interval=1)

    cv2.imshow("Webcam" , frame )
    if cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()