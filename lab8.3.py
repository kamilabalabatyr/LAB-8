import pygame


pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ERASER_COLOR = WHITE  # Цвет фона для ластика

# Переменные
running = True
color = BLACK  # Цвет кисти по умолчанию
mode = "draw"  # Режим ("draw", "rectangle", "circle", "eraser")
start_pos = None  # Начальная точка для фигур

# Основной цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "draw"
            elif event.key == pygame.K_2:
                mode = "rectangle"
            elif event.key == pygame.K_3:
                mode = "circle"
            elif event.key == pygame.K_4:
                mode = "eraser"
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if mode == "rectangle":
                pygame.draw.rect(screen, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif mode == "circle":
                radius = ((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 // 2
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(screen, color, center, int(radius), 2)
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if mode == "draw":
                pygame.draw.line(screen, color, event.pos, event.pos, 3)
            elif mode == "eraser":
                pygame.draw.circle(screen, ERASER_COLOR, event.pos, 10)
    
    pygame.display.update()

pygame.quit()
