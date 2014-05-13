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

