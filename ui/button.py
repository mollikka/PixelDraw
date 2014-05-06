import pygame

class Button(object):

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

        pass

    def draw(self, window):

        window.blit(self.texture, self.rect.topleft)
