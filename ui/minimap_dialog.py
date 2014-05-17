import pygame

from ui.ui_element import UIElement
from ui.button import Button

class MinimapDialog(UIElement):

    def __init__(self, ui_manager, bounding_box):

        buttons = [
            MinimapButton(ui_manager,(10,10)),
        ]

        super(MinimapDialog,self).__init__(bounding_box, buttons)

class MinimapButton(Button):

    def __init__(self, ui_manager, topleft):

        self.layer_manager = ui_manager.layer_manager
        self.ui_manager = ui_manager
        
        texture = pygame.Surface((100,100))
        super(MinimapButton, self).__init__(texture, topleft)

    def draw(self, surface):

        surf= pygame.Surface(self.layer_manager.bounding_box.size)
        surf.blit(self.layer_manager.background, (0,0))
        self.layer_manager.draw_picture(surf)

        winsize = self.ui_manager.window.get_size()
        winhalf = [winsize[i]/2 for i in range(2)]
        viewhalf = self.layer_manager.screen_pos_to_picture(winhalf)

        picpos = self.layer_manager.bounding_box.topleft
        minimappos = [-viewhalf[i] + 50 for i in range(2)]

        self.texture.fill((128,0,0))
        self.texture.blit(surf, minimappos)
        super(MinimapButton, self).draw(surface)
