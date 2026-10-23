import random
import pygame
from settings import CELL, WIDTH, HEIGHT, RED


class Food:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, CELL, CELL)
        self.respawn([])

    def respawn(self, snake_body):
        # random lại cho tới khi không trùng thân rắn
        while True:
            pos = (random.randrange(0, WIDTH, CELL),
                   random.randrange(0, HEIGHT, CELL))
            if pos not in snake_body:
                self.rect.topleft = pos
                break

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)