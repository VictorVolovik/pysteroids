import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = pygame.Color(255, 255, 255)  # white
        line_width = 2
        pygame.draw.circle(screen, color, self.position, self.radius, line_width)
    
    def update(self, dt):
        self.position += self.velocity * dt