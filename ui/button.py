import pygame

class Button(object):
    '''
        A button is a part of an UIElement that does something when clicked
    '''

    def __init__(self, image_surface, topleft):

        super(Button, self).__init__()
        self.texture = image_surface
        self.rect = self.texture.get_rect()
        self.rect.move_ip(topleft)

    def click(self, offset = (0,0)):

        x,y = pygame.mouse.get_pos()
        x0,y0 = offset #panel-to-world offset
        
        if self.rect.collidepoint((x-x0,y-y0)):
            x0 += self.rect.top #button-to-panel offset
            y0 += self.rect.left
            self.activate((x-x0,y-y0))

    def activate(self, mouse_position):
        '''For a typical button, just rewrite activate'''
        pass

    def draw(self, window):

        window.blit(self.texture, self.rect.topleft)
