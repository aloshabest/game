import pygame
import sys
from bullet import Bullet
from aliens import Alien

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

def update(bg_color, screen, gun, aliens, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_aliens(aliens):
    aliens.update()

def create_army(screen, aliens):
    alien = Alien(screen)
    alien_width = alien.rect.width
    num_alien_x = int((1000 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    num_alien_y = int((900 - 100 - 2 * alien_height) / alien_height)

    for row_num in range(num_alien_y - 1):
        for alien_num in range(num_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_num
            alien.y = alien_height + alien_height * row_num
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_num
            aliens.add(alien)


