import pygame
from settings import *

class Player:
    def __init__(self, x, y):
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.color = CYAN

    def draw(self, screen):
        # Рисуем игрока как квадрат
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, dx=0, dy=0):
        # dx и dy — это направление (-1, 0 или 1)
        self.x += dx * TILESIZE
        self.y += dy * TILESIZE
