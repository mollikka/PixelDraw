import colorsys

import pygame

from ui.button import Button

class ColorPickerButton(Button):
    '''
        A palette that sets the active color to the one user clicked on
    '''

    def __init__(self,color_manager):

        self.color_manager = color_manager

        X,Y = 100,0
        w,h = 300,200

        texture = pygame.Surface((w,h))
        bounding_box = pygame.Rect(X,Y,w,h)

        for x in range(w):
            for y in range(h):

                color = self.coords_to_color(x,y,pygame.Rect(0,0,w,h))
                pygame.draw.line(texture, color, (x,y), (x,y))

        super(ColorPickerButton, self).__init__(texture, (X,Y))

    def activate(self):

        x,y = pygame.mouse.get_pos()
        color = self.coords_to_color(x,y,self.get_rect())
        self.color_manager.set_color(color)

    def coords_to_color(self, x,y,rect):
        '''
            Gets the HLS color of the given coordinates (relative to size of
            rect). Lightness goes down (y), hue goes right (x)
        '''

        x -= rect.left
        y -= rect.top
        w,h = rect.size

        color = colorsys.hls_to_rgb(float(x)/w,float(y)/h,1)
        color = [i*255 for i in color]
        return color
