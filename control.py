import pygame
import sys
from bullet import Bullet
from aliens import Alien
import time


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


def update(bg_color, screen, stats, scr, gun, aliens, bullets):
    screen.fill(bg_color)
    scr.show_score()
    for bullet in bullets.sprites():
        bullet.draw()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, scr, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        scr.image_score()
        check_high_score(stats, scr)
        scr.image_guns()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)



def gun_kill(stats, screen, scr, gun, aliens, bullets):
    if stats.guns_left > 0:
        stats.guns_left -= 1
        scr.image_guns()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        time.sleep(1)
        gun.create_gun()
    else:
        stats.run_game = False
        sys.exit()


def update_aliens(stats, screen, scr, gun, aliens, bullets):
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, scr, gun, aliens, bullets)
    alines_check(stats, screen, scr, gun, aliens, bullets)


def alines_check(stats, screen, scr, gun, aliens, bullets):
    screen_rect = screen.get_rect()
    for i in aliens.sprites():
        if i.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, scr, gun, aliens, bullets)
            break


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


def check_high_score(stats, scr):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scr.image_high_score()
        with open('record.txt', 'w') as f:
            f.write(str(stats.high_score))