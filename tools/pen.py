import pygame

class Pen(object):

    def __init__(self):

        self.drawing = False
        self.lastpos = pygame.mouse.get_pos()

    def left_mouse_down(self):

        self.drawing = True
        self.lastpos = pygame.mouse.get_pos()

    def left_mouse_up(self):

        self.drawing = False

    def step(self, layer, color):

        mousepos = pygame.mouse.get_pos()

        if self.drawing:

            pygame.draw.line(layer, color, mousepos, self.lastpos)
        
        self.lastpos = mousepos
