import pygame

class Eraser(object):

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

            #TODO: this is placeholder, maybe use blending modes to erase somehow?
            pygame.draw.circle(layer, (0,0,0,0), mousepos, 10)

        self.lastpos = mousepos
