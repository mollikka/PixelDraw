import pygame

class LayerManager(object):

    def __init__(self):

        self.layers = [Layer(800,600) for i in range(10)]
        self.curlayer = 0

    def get_layer(self):

        return self.layers[self.curlayer].get_surface()

    def set_layer(self, layer_index):

        self.curlayer = layer_index

    def draw_picture(self, window):

        for layer in self.layers:
            layer.draw(window)

    def draw(self, window):

        myfont = pygame.font.SysFont("monospace", 15)

        pygame.draw.rect(window, (255,255,255), pygame.Rect(500,0,200,20))
        label = myfont.render("Current layer {}".format(self.curlayer), 1, (0,0,0))
        window.blit(label, (500,0))

class Layer(object):

    def __init__(self, w, h):
        self.surface = pygame.Surface((w, h),pygame.SRCALPHA)
        self.surface.fill(0)
        self.location = 0,0

    def get_surface(self):

        return self.surface

    def draw(self, window):

        window.blit(self.surface, self.location)
