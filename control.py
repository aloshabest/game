import pygame
import sys
from bullet import Bullet

def event(screen, gun, bullets):
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

            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # движение вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            # движение влево
            elif event.key == pygame.K_LEFT:
                gun.mleft = False

def update(bg_color, screen, gun, alien, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw()
    gun.output()
    alien.draw()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)