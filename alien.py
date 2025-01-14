import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас, що представляє одного прибулюця з флоту"""
    def __init__(self, ai_game):
        """Ініціалізувати прибульця та задати його початкове розташування"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Завантажте чуже зображення та встановіть його атрибут rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Починайте кожного нового прибульця з лівого верхнього кута екрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Зберігайте точне горизонтальне положення прибульця
        self.x = float(self.rect.x)

    def update(self):
        """Пересунути прибульця праворуч чи ліворуч"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Повертає істину, якщо прибулець знаходиться на краю екрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True