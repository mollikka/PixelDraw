import pygame

from ui.ui_element import UIElement
from ui.button import Button

class MinimapDialog(UIElement):

    def __init__(self, ui_manager, anchor, topleft, size):

        buttons = [
            MinimapButton(ui_manager,(10,10),size),
        ]

        super(MinimapDialog,self).__init__(pygame.Rect(topleft[0],topleft[1],size[0],size[1]), buttons, anchor)

class MinimapButton(Button):

    def __init__(self, ui_manager, topleft, size):

        self.layer_manager = ui_manager.layer_manager
        self.ui_manager = ui_manager
        
        self.midpoint = size[0]/2 -10, size[1]/2 - 10
        texture = pygame.Surface((self.midpoint[0]*2,self.midpoint[1]*2))
        super(MinimapButton, self).__init__(texture, topleft)

    def activate(self, mouse_position):

        x,y = mouse_position

        image_center = self.layer_manager.bounding_box.center
        
        new_viewpos = [image_center[0] - x + self.midpoint[0], image_center[1] - y + self.midpoint[1]]

        self.layer_manager.bounding_box.center = new_viewpos

    def draw(self, surface):

        surf= pygame.Surface(self.layer_manager.bounding_box.size)
        surf.blit(self.layer_manager.background, (0,0))
        self.layer_manager.draw_picture(surf)

        winsize = self.ui_manager.window.get_size()
        winhalf = [winsize[i]/2 for i in range(2)]
        viewhalf = self.layer_manager.screen_pos_to_picture(winhalf)

        picpos = self.layer_manager.bounding_box.topleft
        minimappos = [-viewhalf[0] + self.midpoint[0], -viewhalf[1] + self.midpoint[1]]

        self.texture.fill((128,0,0))
        self.texture.blit(surf, minimappos)
        super(MinimapButton, self).draw(surface)
