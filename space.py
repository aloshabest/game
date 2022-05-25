import pygame, control
from gun import Gun
from pygame.sprite import Group
from stats import Stats

def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 900))
    pygame.display.set_caption("Космо-защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    control.create_army(screen, aliens)
    stats = Stats()

    while True:
        control.event(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            control.update(bg_color, screen, gun, aliens, bullets)
            control.update_bullets(screen, aliens, bullets)
            control.update_aliens(stats, screen, gun, aliens, bullets)


run()