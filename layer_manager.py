import pygame

from ui.button import Button

class LayerManager(object):

    def __init__(self):

        self.layers = [Layer(800,600) for i in range(10)]
        self.curlayer = 0
        self.layer_dialog = LayerDialog(self)

    def get_layer(self):

        return self.layers[self.curlayer].get_surface()

    def set_layer(self, layer_index):

        self.curlayer = layer_index

    def pick_layer(self):

        self.layer_dialog.pick_layer()

    def draw_picture(self, window):

        for layer in self.layers:
            layer.draw(window)

    def draw(self, window):

        myfont = pygame.font.SysFont("monospace", 15)

        pygame.draw.rect(window, (255,255,255), pygame.Rect(500,0,200,20))
        label = myfont.render("Current layer {}".format(self.curlayer), 1, (0,0,0))
        window.blit(label, (500,0))

        self.layer_dialog.draw(window)

class Layer(object):

    def __init__(self, w, h):
        self.surface = pygame.Surface((w, h),pygame.SRCALPHA)
        self.surface.fill(0)
        self.location = 0,0
        self.name = "Unnamed layer"

    def get_surface(self):

        return self.surface

    def draw(self, window):

        window.blit(self.surface, self.location)

class LayerDialog(object):

    def __init__(self, layer_manager):

        self.layerbuttons = []
        for i in range(len(layer_manager.layers)):
            layer = layer_manager.layers[i]
            self.layerbuttons.append(LayerButton(layer, layer_manager, (500,30+i*20)))

    def draw(self, window):

        for button in self.layerbuttons:
            button.draw(window)

    def pick_layer(self):

        for button in self.layerbuttons:
            button.click()

class LayerButton(Button):

    def __init__(self, layer, layer_manager, topleft):

        self.layer = layer
        self.layer_manager = layer_manager

        myfont = pygame.font.SysFont("monospace", 15)

        label = myfont.render("Layer: {}".format(layer.name), 1, (0,0,0))
        texture = pygame.Surface(label.get_bounding_rect().size)
        texture.fill((255,255,255))
        texture.blit(label,(-2,-2))

        super(LayerButton, self).__init__(texture, topleft)

    def activate(self):

        i = self.layer_manager.layers.index(self.layer)
        self.layer_manager.set_layer(i)
