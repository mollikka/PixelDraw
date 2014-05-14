import pygame

class ColorManager(object):
    '''
        A ColorManager manages the user's color choices. It lets the user
        pick a color from a palette.
    '''

    def __init__(self):

        self.color = (255,255,255)

    def get_color(self): return self.color

    def set_color(self, newValue): self.color = newValue

