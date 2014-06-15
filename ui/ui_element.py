import pygame

class UIElement(object):
    '''
        A general representation of a UI panel that can be contain buttons
    '''
    anchor_names = 'topleft','topright','bottomleft','bottomright'

    def __init__(self, bounding_box, buttons, anchor):

        self.bounding_box = bounding_box
        self.buttons = buttons
        self.anchor = anchor

    def set_anchor(self, corner):

        assert (corner in UIElement.anchor_names)
        self.anchor = corner

    def get_anchor_offset(self, window):
        if self.anchor == 'topleft':       anchoroffset = window.get_rect().topleft
        elif self.anchor == 'topright':    anchoroffset = window.get_rect().topright
        elif self.anchor == 'bottomleft':  anchoroffset = window.get_rect().bottomleft
        elif self.anchor == 'bottomright': anchoroffset = window.get_rect().bottomright
        return anchoroffset

    def hit(self):

        x,y = pygame.mouse.get_pos()
        return self.bounding_box.collidepoint((x,y))

    def click(self):

        for button in self.buttons:
            button.click(offset=self.bounding_box.topleft)

    def pan(self, mouse_delta):

        self.bounding_box.left += mouse_delta[0]
        self.bounding_box.top += mouse_delta[1]

    def draw(self, window):

        surf = pygame.Surface(self.bounding_box.size)
        surf.fill((128,128,128))

        for button in self.buttons:
            button.draw(surf)

        a_off = self.get_anchor_offset(window)

        off_x = a_off[0] + self.bounding_box.left
        off_y = a_off[1] + self.bounding_box.top

        window.blit(surf, (off_x, off_y))
