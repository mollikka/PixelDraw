import colorsys

import pygame

from ui.ui_element import UIElement
from ui.button import Button

class ColorPickerDialog(UIElement):

    def __init__(self, ui_manager, bounding_box):

        buttons = [ColorPickerButton(ui_manager)]

        super(ColorPickerDialog, self).__init__(bounding_box, buttons)

class ColorPickerButton(Button):
    '''
        A palette that sets the active color to the one user clicked on
    '''

    def __init__(self, ui_manager):

        self.color_manager = ui_manager.color_manager

        w,h = 300,200

        texture = pygame.Surface((w,h))
        bounding_box = pygame.Rect(0,0,w,h)

        for x in range(w):
            for y in range(h):

                color = self.coords_to_color(x,y,pygame.Rect(0,0,w,h))
                pygame.draw.line(texture, color, (x,y), (x,y))

        super(ColorPickerButton, self).__init__(texture, (0,0))

    def activate(self, mouse_position):

        x,y = mouse_position
        color = self.coords_to_color(x,y,self.rect)
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
