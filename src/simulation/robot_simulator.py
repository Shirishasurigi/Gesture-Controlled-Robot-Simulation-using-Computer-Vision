import pygame
import os
from robot.robot import Robot
from environment.environment import Environment

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (70, 130, 180)
BLACK = (0, 0, 0)


class RobotSimulator:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Gesture Controlled Robot")

        self.clock = pygame.time.Clock()

        self.robot = Robot()

        self.environment = Environment()
        
        asset_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "assets",
                "robot.png"
            )
        )

        print("Loading robot image:", asset_path)

        self.robot_image = pygame.image.load(asset_path).convert_alpha()

        self.robot_image = pygame.transform.scale(
            self.robot_image,
            (90, 90)
        )

    def update(self, command):

        old_x = self.robot.x
        old_y = self.robot.y

        if command == "FORWARD":
            self.robot.move_forward()

        elif command == "BACKWARD":
            self.robot.move_backward()

        elif command == "LEFT":
            self.robot.rotate_left()

        elif command == "RIGHT":
            self.robot.rotate_right()

        
        if command in ["FORWARD", "BACKWARD"]:

            if self.check_collision():

                # Restore previous position
                self.robot.x = old_x
                self.robot.y = old_y

    def check_collision(self):

        robot_rect = self.robot.get_rect()

        
        for wall in self.environment.walls:
            if robot_rect.colliderect(wall):
                print("Wall Collision!")
                return True


        for obstacle in self.environment.obstacles:
            if robot_rect.colliderect(obstacle):
                print("Obstacle Collision!")
                return True

        return False
        

    def draw_robot(self):

        rotated_image = pygame.transform.rotate(
            self.robot_image,
            self.robot.angle
        )

        rect = rotated_image.get_rect(
            center=(self.robot.x, self.robot.y)
        )

        self.screen.blit(rotated_image, rect)

        
                    
    def draw(self):

        self.screen.fill(WHITE)

        self.environment.draw(self.screen)

        self.draw_robot()
        
        font = pygame.font.SysFont("Arial", 20)

        goal_text = font.render("DROP ZONE", True, (0,120,0))
        self.screen.blit(goal_text, (650,80))

        box_text = font.render("BOX", True, (180,0,0))
        self.screen.blit(box_text, (740,505))        
          
        pygame.display.flip()

    def run(self, command):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

        self.update(command)

        self.draw()

        self.clock.tick(60)

        return True