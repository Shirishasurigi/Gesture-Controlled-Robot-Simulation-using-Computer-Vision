import sys
import os
import cv2
import numpy as np
import pygame

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

import camera_stream
from simulation.robot_simulator import RobotSimulator

simulator = RobotSimulator()


def generate_simulator():

    while True:

        simulator.run(camera_stream.current_gesture)

        frame = pygame.surfarray.array3d(simulator.screen)

        frame = np.transpose(frame, (1, 0, 2))

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        ret, buffer = cv2.imencode(".jpg", frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )