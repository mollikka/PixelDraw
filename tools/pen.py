import pygame

class Pen(object):

    def __init__(self):

        self.drawing = False
        self.lastpos = pygame.mouse.get_pos()

    def start_drawing(self):

        self.drawing = True
        self.lastpos = pygame.mouse.get_pos()

    def stop_drawing(self):

        self.drawing = False

    def step(self, layer, color):

        mousepos = pygame.mouse.get_pos()

        if self.drawing:

            pygame.draw.line(layer, color, mousepos, self.lastpos)
        
        self.lastpos = mousepos
