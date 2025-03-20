import pygame
import random

# Инициализация pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Загрузка изображений
car_image = pygame.image.load("car.webp")  # Машина игрока
coin_image = pygame.image.load("coin.png")  # Монета
road_image = pygame.image.load("road.jpg")  # Фон дороги

# Масштабируем изображения
car_width, car_height = 200, 150
car_image = pygame.transform.scale(car_image, (car_width, car_height))
coin_image = pygame.transform.scale(coin_image, (50, 50))

# Позиция машины
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Монеты
coins = []  # Список монет
coin_spawn_timer = 0  # Таймер появления монет
coin_spawn_delay = 100  # Задержка появления монет (в кадрах)
coins_collected = 0  # Количество собранных монет

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)  # Очистка экрана
    screen.blit(road_image, (0, 0))  # Отображение дороги
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Управление машиной
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed
    
    # Спавн монет
    if coin_spawn_timer >= coin_spawn_delay:
        coin_x = random.randint(50, WIDTH - 50)
        coin_y = -30
        coins.append([coin_x, coin_y])
        coin_spawn_timer = 0
    else:
        coin_spawn_timer += 1
    
    # Движение монет
    for coin in coins[:]:
        coin[1] += 5  # Двигаем монеты вниз
        if coin[1] > HEIGHT:
            coins.remove(coin)  # Удаляем монеты, вышедшие за экран
    
    # Проверка на сбор монеты
    for coin in coins[:]:
        if car_x < coin[0] < car_x + car_width and car_y < coin[1] < car_y + car_height:
            coins.remove(coin)
            coins_collected += 1
    
    # Отображение машины и монет
    screen.blit(car_image, (car_x, car_y))
    for coin in coins:
        screen.blit(coin_image, (coin[0], coin[1]))
    
    # Отображение счёта
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Coins: {coins_collected}", True, RED)
    screen.blit(score_text, (WIDTH - 150, 20))
    
    pygame.display.update()
    clock.tick(30)  # Ограничение FPS

pygame.quit()
