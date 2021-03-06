import pygame
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("img/m_pushka.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.center = float(self.rect.centerx)


    def output(self):
        self.screen.blit(self.image, self.rect)


    def update_gun(self):
        self.rect.centerx = self.center

        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 2.5

        if self.mleft and self.rect.left > 0:
            self.center -= 2.5


    def create_gun(self):
        self.center = self.screen_rect.centerx