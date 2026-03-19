import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("My first Pygame")
#player object settings
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
player_speed = 300

#enemy object settings
enemy_pos = pygame.Vector2(100, 100)

enemy_pos2 = pygame.Vector2(200, 200)


clock = pygame.time.Clock()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("pink")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += player_speed * dt

    pygame.draw.circle(screen,"blue",enemy_pos, 100)
    enemy_pos.x += 100 * dt
    
    pygame.draw.rect(screen,"yellow",pygame.Rect(enemy_pos2.x, enemy_pos2.y, 100, 100))
    enemy_pos2.y += 100 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000

