import colorsys

import pygame

from ui.color_dialog import ColorPickerButton

class ColorManager(object):
    '''
        A ColorManager manages the user's color choices. It lets the user
        pick a color from a palette.
    '''

    def __init__(self):

        self.color = (255,255,255)
        self.color_picker = ColorPickerButton(self)

    def get_color(self): return self.color

    def set_color(self, newValue): self.color = newValue

    def draw(self,window):

        self.color_picker.draw(window)

    def pick_color(self):
    
        self.color_picker.click()

    @staticmethod
    def coords_to_color(x,y,rect):
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

