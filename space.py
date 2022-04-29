import pygame, control
from gun import Gun

def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 900))
    pygame.display.set_caption("Космо-защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        control.event(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()

run()