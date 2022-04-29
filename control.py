import pygame
import sys

def event(gun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # движение вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            # движение влево
            elif event.key == pygame.K_LEFT:
                gun.mleft = True

        elif event.type == pygame.KEYUP:
            # движение вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            # движение влево
            elif event.key == pygame.K_LEFT:
                gun.mleft = False