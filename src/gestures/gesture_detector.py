class GestureDetector:

    TIP_IDS = [4, 8, 12, 16, 20]

    def fingers_up(self, hand_landmarks):

        fingers = []

        landmarks = hand_landmarks.landmark

        
        if landmarks[4].x < landmarks[3].x:
            fingers.append(1)
        else:
            fingers.append(0)

        
        for tip in self.TIP_IDS[1:]:

            if landmarks[tip].y < landmarks[tip - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def recognize_gesture(self, fingers):

        if fingers == [1,1,1,1,1]:
            return "STOP"

        elif fingers == [0,0,0,0,0]:
            return "BACKWARD"

        elif fingers == [1,0,0,0,0]:
            return "FORWARD"

        elif fingers == [0,1,0,0,0]:
            return "LEFT"

        elif fingers == [0,1,1,0,0]:
            return "RIGHT"

        return "UNKNOWN"