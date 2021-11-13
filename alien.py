import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiająca pojedynczego obcego we flocie"""

    def __init__(self, ai_game):
        """Inicjalizacja obecego i zdefiniowanie jego położenia początkowego"""
        super().__init__()
        self.screen = ai_game.screen

        # Wczytanie obrazu obecego i zdefiniowanie jego atrybutu rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obecego w pobliżu lewego górnego rogu ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowanie dodanego poziomu położenia obcego
        self.x = float(self.rect.x)
