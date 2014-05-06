import colorsys

import pygame

class ColorManager(object):

    def __init__(self):

        self.color = (255,255,255)
        self.color_picker_texture = pygame.Surface((0,0))
        self.color_picker_box = pygame.Rect(0,0,300,200)
        self.generate_panel()

    def get_color(self):

        return self.color

    def generate_panel(self):

        w,h = self.color_picker_box.size

        self.color_picker_texture = pygame.Surface((w,h))

        for x in range(w):
            for y in range(h):

                color = self.coords_to_color(x,y)
                pygame.draw.line(self.color_picker_texture, color, (x,y), (x,y))

    def step(self,window):

        window.blit(self.color_picker_texture, (0,0))

    def pick_color(self):

        x,y = pygame.mouse.get_pos()
        
        if self.color_picker_box.collidepoint((x,y)):
            self.color = self.coords_to_color(x,y)

    def coords_to_color(self,x,y):

        w,h = self.color_picker_box.size

        color = colorsys.hls_to_rgb(float(x)/w,float(y)/h,1)
        color = [i*255 for i in color]
        return color

