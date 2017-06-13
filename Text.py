import pygame, time, random, sys, os
import Globals as gl

class Text:
    def __init__(self, text="Tekst domyślny",
                 position=(0,0),
                 font_size = 42,
                 text_color = pygame.color.THECOLORS['black'],
                 font='fm3.ttf'):
        self.text = text
        self.text_color = text_color
        self.position = position
        self.font = pygame.font.Font(os.path.join(os.getcwd(), 'fonts',font), font_size)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        

    def draw(self, surface, where=None):
        self.image = self.font.render(str(self.text), 1, self.text_color)
        self.rect = self.image.get_rect()
        if where == 'center':
            self.rect.center = self.position
        else:
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        surface.blit(self.image, self.rect)
