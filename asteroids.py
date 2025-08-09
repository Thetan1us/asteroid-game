from circleshape import CircleShape
import pygame
import random
import constants


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", (self.position[0], self.position[1]), self.radius, 2
        )

    def update(self, dt):
        displacement = self.velocity * dt
        self.position += displacement

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        asteroid1 = Asteroid(self.position[0], self.position[1], self.radius - constants.ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position[0], self.position[1], self.radius - constants.ASTEROID_MIN_RADIUS)
        asteroid1.velocity = self.velocity.rotate(new_angle) * 1.2
        asteroid2.velocity = self.velocity.rotate(-new_angle) * 1.2