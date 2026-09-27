import cv2
import mediapipe as mp

from gestures.gesture_detector import GestureDetector
from simulation.robot_simulator import RobotSimulator

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


def start_camera():
    cap = cv2.VideoCapture(0)

    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )
    
    detector = GestureDetector()
    simulator = RobotSimulator()

    command = "STOP"

    while True:
        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

                fingers = detector.fingers_up(hand_landmarks)
                print(fingers)
                command = detector.recognize_gesture(fingers)

                cv2.putText(
                    frame,
                    f"Fingers: {fingers}",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Command: {command}",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (225, 255, 0),
                    2
                )
                  
                h, w, _ = frame.shape

                for idx, landmark in enumerate(hand_landmarks.landmark):
                    x = int(landmark.x * w)
                    y = int(landmark.y * h)

                    cv2.putText(
                        frame,
                        str(idx),
                        (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (255, 0, 0),
                        2
                    )
        
        running = simulator.run(command)

        if not running:
            break

        cv2.imshow("Gesture Robot", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()