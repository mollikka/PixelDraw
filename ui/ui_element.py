import pygame

class UIElement(object):
    '''
        A general representation of a UI panel that can be contain buttons
    '''

    def __init__(self, bounding_box, buttons):

        self.bounding_box = bounding_box
        self.buttons = buttons

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

        window.blit(surf, self.bounding_box.topleft)
