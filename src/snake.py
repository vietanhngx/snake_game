import pygame
from settings import CELL, WIDTH, HEIGHT, GREEN

START_POS = (200, 200)


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.body = [START_POS]
        self.direction = (0, 0)

    @property
    def head(self):
        return self.body[0]

    def set_direction(self, new_dir):
        # chặn quay đầu ngược 180 độ
        if (new_dir[0] + self.direction[0],
                new_dir[1] + self.direction[1]) != (0, 0):
            self.direction = new_dir

    def next_head(self):
        return (self.head[0] + self.direction[0],
                self.head[1] + self.direction[1])

    def move(self, grow=False):
        self.body.insert(0, self.next_head())
        if not grow:
            self.body.pop()

    def is_dead(self):
        x, y = self.head
        return (self.head in self.body[1:]
                or x < 0 or x >= WIDTH
                or y < 0 or y >= HEIGHT)

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, CELL, CELL))