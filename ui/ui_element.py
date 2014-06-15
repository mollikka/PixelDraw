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

    def get_anchor_offset(self, window):
        if self.anchor == 'topleft':       anchoroffset = window.get_rect().topleft
        elif self.anchor == 'topright':    anchoroffset = window.get_rect().topright
        elif self.anchor == 'bottomleft':  anchoroffset = window.get_rect().bottomleft
        elif self.anchor == 'bottomright': anchoroffset = window.get_rect().bottomright
        return anchoroffset

    def hit(self, offset=(0,0)):

        loc = [i[0]-i[1] for i in zip(pygame.mouse.get_pos(),offset)]
        return self.bounding_box.collidepoint(loc)

    def click(self, offset=(0,0)):

        loc = [sum(i) for i in zip(offset, self.bounding_box.topleft)]

        for button in self.buttons:
            button.click(offset=loc)

    def pan(self, mouse_delta):

        self.bounding_box.left += mouse_delta[0]
        self.bounding_box.top += mouse_delta[1]

    def draw(self, window, offset=(0,0)):

        surf = pygame.Surface(self.bounding_box.size)
        surf.fill((128,128,128))

        for button in self.buttons:
            button.draw(surf)

        location = [sum(i) for i in zip(self.bounding_box.topleft, offset)]

        window.blit(surf, location)
