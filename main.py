import pygame

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
