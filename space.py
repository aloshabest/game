import pygame, control
from gun import Gun
from pygame.sprite import Group
from aliens import Alien

def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 900))
    pygame.display.set_caption("Космо-защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    alien = Alien(screen)

    while True:
        control.event(screen, gun, bullets)
        gun.update_gun()
        control.update(bg_color, screen, gun, alien, bullets)
        control.update_bullets(bullets)

run()