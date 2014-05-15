import pygame

class UIElement(object):
    '''
        A general representation of a UI panel that can be contain buttons
    '''

    def __init__(self, bounding_box, buttons):

        self.bounding_box = bounding_box
        self.buttons = buttons

    def click(self):

        x,y = pygame.mouse.get_pos()
        if self.bounding_box.collidepoint((x,y)):
            for button in self.buttons:
                button.click(offset=self.bounding_box.topleft)
            return True
        else:
            return False

    def draw(self, window):

        surf = pygame.Surface(self.bounding_box.size)
        surf.fill((128,128,128))

        for button in self.buttons:
            button.draw(surf)

        window.blit(surf, self.bounding_box.topleft)
