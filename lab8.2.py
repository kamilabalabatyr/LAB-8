import pygame
import random

pygame.init()

# Константы
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20  # Размер клетки
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Начальные параметры змейки
snake = [(WIDTH // 2, HEIGHT // 2)]  # Координаты змеи
snake_dir = (CELL_SIZE, 0)  # Движение (изначально вправо)
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
score = 0
level = 1
speed = 10

# Функция для генерации еды
def generate_food():
    while True:
        new_food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        if new_food not in snake:
            return new_food

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)
    
    # Движение змейки
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Проверка на выход за границы
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    
    # Проверка на столкновение с собой
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    # Проверка на поедание еды
    if new_head == food:
        score += 1
        food = generate_food()
        if score % 4 == 0:  # Каждые 4 очка - новый уровень
            level += 1
            speed += 2
    else:
        snake.pop()
    
    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    
    # Отрисовка еды
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    
    # Отображение счёта и уровня
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
