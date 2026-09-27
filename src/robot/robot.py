import pygame
import math


class Robot:

    def __init__(self):

        self.x = 400
        self.y = 300

        self.width = 80
        self.height = 50

        self.angle = 0

        self.speed = 4

    def move_forward(self):

        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))

    def move_backward(self):

        self.x -= self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
    
    def rotate_left(self):

        self.angle += 3

    def rotate_right(self):

        self.angle -= 3
    
    def get_rect(self):

        return pygame.Rect(
            self.x - self.width // 2,
            self.y - self.height // 2,
            self.width,
            self.height
        )