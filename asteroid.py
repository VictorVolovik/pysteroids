import random
import pygame
from circleshape import CircleShape
from constants import (
    ASTEROID_MIN_RADIUS,
)


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = pygame.Color(255, 255, 255)  # white
        line_width = 2
        pygame.draw.circle(screen, color, self.position, self.radius, line_width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1_velocity = self.velocity.rotate(random_angle)
            asteroid_2_velocity = self.velocity.rotate(-random_angle)

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid_1.velocity = asteroid_1_velocity * 1.2

            asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid_2.velocity = asteroid_2_velocity * 1.2
