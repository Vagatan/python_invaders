import pygame

class Ship:
    """Klasa przeznaczona do zarządzania statkiem kosmicznym"""

    def __init__(self, ai_game):
        """Inicjalizacja staku kosmicznego i jego położenie początkowe"""

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Wyświetlanie statku kosmicznego w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)
