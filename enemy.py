import pygame
from settings import *

class Enemy:
    def __init__(self, x, y):
        # Координаты врага в сетке (умножаем на TILESIZE, чтобы получить пиксели)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.color = RED # Цвет врага
        self.hp = 1 # Пока просто 1 HP

    def draw(self, screen):
        # Рисуем врага как красный квадрат
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    # Пока враг не умеет двигаться, этот метод будет пустым
    def update(self, player_x, player_y, map_data):
        pass
