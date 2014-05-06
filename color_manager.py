import colorsys

import pygame

class ColorManager(object):

    def __init__(self):

        self.color = (255,255,255)
        self.panel = pygame.Surface((0,0))
        self.w = 300
        self.h = 200
        self.generate_panel()

    def get_color(self):

        return self.color

    def generate_panel(self):

        self.panel = pygame.Surface((self.w,self.h))

        for x in range(self.w):
            for y in range(self.h):

                color = self.coords_to_color(x,y)
                pygame.draw.line(self.panel, color, (x,y), (x,y))

    def draw_panel(self,window):

        window.blit(self.panel, (0,0))

    def left_mouse_down(self):

        x,y = pygame.mouse.get_pos()
        
        if x < self.w and y < self.h:
            self.color = self.coords_to_color(x,y)

    def coords_to_color(self,x,y):

        color = colorsys.hls_to_rgb(float(x)/self.w,float(y)/self.h,1)
        color = [i*255 for i in color]
        return color

