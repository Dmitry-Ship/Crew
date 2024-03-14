import pygame
import random

# initialize pygame
pygame.init()

# screen dimensions
screen_width = 800
screen_height = 600

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooter Game")

# player
player_size = 50
player_x = screen_width // 2
player_y = screen_height - player_size
player_speed = 5

# projectile
projectile_size = 10
projectile_speed = 7
projectiles = []

# enemy
enemy_size = 30
enemy_speed = 3
enemies = []

# score
score = 0

# game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < screen_width - player_size:
        player_x += player_speed

    if keys[pygame.K_SPACE]:
        projectiles.append([player_x + player_size//2, player_y])

    if random.randint(0, 100) < 2:
        enemies.append([random.randint(0, screen_width-enemy_size), 0])

    for projectile in projectiles:
        pygame.draw.rect(screen, black, (projectile[0], projectile[1], projectile_size, projectile_size))
        projectile[1] -= projectile_speed

    for enemy in enemies:
        pygame.draw.rect(screen, black, (enemy[0], enemy[1], enemy_size, enemy_size))
        enemy[1] += enemy_speed

    for enemy in enemies[:]:
        for projectile in projectiles[:]:
            if enemy[0] <= projectile[0] <= enemy[0] + enemy_size and enemy[1] <= projectile[1] <= enemy[1] + enemy_size:
                enemies.remove(enemy)
                projectiles.remove(projectile)
                score += 1

        if enemy[0] <= player_x <= enemy[0] + enemy_size and enemy[1] <= player_y <= enemy[1] + enemy_size:
            running = False

    pygame.draw.rect(screen, black, (player_x, player_y, player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()