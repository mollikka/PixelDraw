import pygame

from ui.ui_element import UIElement
from ui.button import Button

class MinimapDialog(UIElement):

    def __init__(self, ui_manager, bounding_box):

        buttons = [
            MinimapButton(ui_manager,(0,0)),
        ]

        super(MinimapDialog,self).__init__(bounding_box, buttons)

class MinimapButton(Button):

    def __init__(self, ui_manager, topleft):

        self.layer_manager = ui_manager.layer_manager
        
        texture = pygame.Surface((100,100))
        self.layer_manager.draw_picture(texture)
        super(MinimapButton, self).__init__(texture, topleft)

    def draw(self, surface):

        self.texture.blit(self.layer_manager.background, (0,0))
        self.layer_manager.draw_picture(self.texture)
        super(MinimapButton, self).draw(surface)
