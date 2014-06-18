import pygame

from ui.ui_element import UIElement
from ui.button import Button
from ui import BUTTON_SIZE

class ColorPaletteDialog(UIElement):
    '''
        A drawn palette of discrete colors that the user can click to pick the color they want
        to use
    '''

    def __init__(self, ui_manager, anchor, topleft, vertical=False):

        color_manager = ui_manager.color_manager

        load = pygame.image.load

        colors = [
(  0,  0,  0),
(  0,  0,255),
(  0,255,  0),
(  0,255,255),
(255,  0,  0),
(255,  0,255),
(255,255,  0),
(255,255,255),]
        
        buttons = []
        for i,color in enumerate(colors):
            if vertical: pos = (0,BUTTON_SIZE*i)
            else: pos = (BUTTON_SIZE*i,0)
            
            buttons.append(ColorButton(color, color_manager, pos))

        if vertical: size = (BUTTON_SIZE,BUTTON_SIZE*len(buttons))
        else: size = (BUTTON_SIZE*len(buttons),BUTTON_SIZE)

        super(ColorPaletteDialog,self).__init__(pygame.Rect(topleft[0],topleft[1],size[0],size[1]), buttons, anchor)

class ColorButton(Button):
    '''
        A button in a ColorPaletteDialog. Clicking it will make the corresponding color
        active
    '''

    def __init__(self, color, color_manager, topleft):

        self.color = color
        self.color_manager = color_manager
        texture = pygame.Surface((BUTTON_SIZE, BUTTON_SIZE))
        texture.fill(color)
        super(ColorButton, self).__init__(texture, topleft)

    def activate(self, mouse_position):

        self.color_manager.set_color(self.color)
