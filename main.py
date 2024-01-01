import pygame
import pandas as pd
import numpy as np
import sys

pygame.init()

# Set up Display

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Serf to Savior")
clock = pygame.time.Clock()

test_surface = pygame.Surface((200,200))
test_surface.fill("Orchid")



# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(test_surface,(200,100))
 

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()