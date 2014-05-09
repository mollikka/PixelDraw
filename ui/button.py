import pygame

class Button(object):
    '''
        A general representation of an UI element that can be clicked to do
        something
    '''

    def __init__(self, image_surface, topleft):

        self.texture = image_surface
        self.rect = self.texture.get_rect()
        self.rect.move_ip(topleft)

    def get_rect(self): return self.rect

    def click(self):

        x,y = pygame.mouse.get_pos()
        if self.rect.collidepoint((x,y)):
            self.activate()

    def activate(self):
        '''For a typical button, just rewrite activate'''
        pass

    def draw(self, window):

        window.blit(self.texture, self.rect.topleft)
