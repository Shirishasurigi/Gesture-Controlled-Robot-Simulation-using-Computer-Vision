import pygame


GRAY = (95, 95, 95)
BROWN = (120, 70, 25)
GREEN = (40, 180, 40)
RED = (220, 60, 60)


class Environment:

    def __init__(self):

        
        self.walls = [
            pygame.Rect(0, 0, 800, 20),      # Top
            pygame.Rect(0, 580, 800, 20),    # Bottom
            pygame.Rect(0, 0, 20, 600),      # Left
            pygame.Rect(780, 0, 20, 600),    # Right
            
            # Inner walls
            pygame.Rect(120, 120, 25, 250),
            pygame.Rect(500, 150, 25, 220)
        ]

        
        self.obstacles = [
            pygame.Rect(260, 420, 70, 70)
        ]

        
        self.goal = pygame.Rect(680, 70, 50, 50)

        
        self.box = pygame.Rect(620, 420, 40, 40)

    def draw(self, screen):

        self.draw_grid(screen)

        
        for wall in self.walls:
            pygame.draw.rect(screen, GRAY, wall)

        
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, BROWN, obstacle)

        
        pygame.draw.rect(
            screen,
            GREEN, 
            self.goal,
            border_radius=8
        )

        
        pygame.draw.rect(
            screen, 
            RED,
            self.box,
            border_radius=5
        )

    def draw_grid(self, screen):

        GRID_SIZE = 40

        color = (225, 225, 225)

        width = screen.get_width()
        height = screen.get_height()

        for x in range(0, width, GRID_SIZE):
            pygame.draw.line(color=color,
                             surface=screen,
                             start_pos=(x, 0),
                             end_pos=(x, height))

        for y in range(0, height, GRID_SIZE):
            pygame.draw.line(color=color,
                             surface=screen,
                             start_pos=(0, y),
                             end_pos=(width, y))