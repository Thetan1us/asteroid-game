from circleshape import CircleShape
import pygame
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
