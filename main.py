import pygame
import sys
from settings import *
from player import Player
from level import LEVEL_MAP
from enemy import Enemy #Новая строка

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chains of Oblivion")
        self.clock = pygame.time.Clock()
        self.running = True

        # Создаем игрока в центре экрана (в координатах сетки)
        self.player = Player(10, 10)
        self.enemy = Enemy(10, 5)  # Враг стартует в (10,5) - убедись, что это свободная клетка!

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Движение при нажатии клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.move(dx=-1, map_data=LEVEL_MAP)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.move(dx=1, map_data=LEVEL_MAP)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.move(dy=-1, map_data=LEVEL_MAP)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.move(dy=1, map_data=LEVEL_MAP)

    def draw(self):
        self.screen.fill(BGCOLOR)

        # Рисуем карту
        for row_index, row in enumerate(LEVEL_MAP):
            for col_index, char in enumerate(row):
                if char == '1':
                    # Рисуем стену
                    pygame.draw.rect(self.screen, DARKGREY,
                                     (col_index * TILESIZE, row_index * TILESIZE, TILESIZE, TILESIZE))
                else:
                    # Рисуем пол
                    pygame.draw.rect(self.screen, (35, 35, 40),
                                     (col_index * TILESIZE, row_index * TILESIZE, TILESIZE, TILESIZE), 1)
                self.enemy.draw(self.screen)  # Рисуем врага! Новая строка
                self.player.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()


# Инициализация Pygame
pygame.init()

# Создаем окно 800 на 600 пикселей
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chains of Oblivion - Тест")

# Главный цикл
running = True
while running:
    # Обработка событий (нажатие на крестик и т.д.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Закрашиваем экран темно-серым цветом
    screen.fill((30, 30, 35))

    # Обновляем экран (рисуем всё, что изменилось)
    pygame.display.flip()

pygame.quit()
#upd