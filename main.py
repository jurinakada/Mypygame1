import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("My first Pygame")
clock = pygame.time.Clock()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("pink")

    pygame.draw.circle(screen, "red", player_pos, 40)

    pygame.display.flip()
    clock.tick(60)

