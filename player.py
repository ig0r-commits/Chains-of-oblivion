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

    def move(self, dx=0, dy=0, map_data=None):
        # 1. Вычисляем будущую позицию в сетке (grid coordinates)
        # Мы делим текущую координату на размер плитки и прибавляем направление
        target_grid_x = (self.x // TILESIZE) + dx
        target_grid_y = (self.y // TILESIZE) + dy

        # 2. Проверяем: не является ли эта клетка стеной?
        # В списках сначала идет индекс строки (y), потом столбца (x)
        if map_data[target_grid_y][target_grid_x] != '1':
            # Если это не '1', значит путь свободен!
            self.x += dx * TILESIZE
            self.y += dy * TILESIZE

