print("=" * 50)
print("camera_stream loaded")
print(__file__)
print("=" * 50)
import cv2
import mediapipe as mp

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from gestures.gesture_detector import GestureDetector
camera = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

detector = GestureDetector()


current_gesture = "STOP"


def generate_frames():

    global current_gesture

    while True:

        success, frame = camera.read()

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

                current_gesture = detector.recognize_gesture(fingers)

                cv2.putText(
                    frame,
                    f"Gesture : {current_gesture}",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2
                )

        ret, buffer = cv2.imencode(".jpg", frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )