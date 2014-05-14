import pygame

from ui.button import Button

class LayerDialog(object):
    '''
        A drawn list of layers that the user can click to pick the one they want
        to edit
    '''

    def __init__(self, ui_manager):

        layer_manager = ui_manager.layer_manager

        self.layerbuttons = []
        for i in range(len(layer_manager.layers)):
            self.layerbuttons.append(LayerButton(i, layer_manager, (500,30+i*20)))

    def draw(self, window):

        for button in self.layerbuttons:
            button.draw(window)

    def click(self):

        for button in self.layerbuttons:
            button.click()

class LayerButton(Button):
    '''
        A button in a LayerDialog. Clicking it will make the corresponding layer
        active
    '''

    def __init__(self, layerindex, layer_manager, topleft):

        layername = layer_manager.layers[layerindex].name
        self.layerindex = layerindex
        self.layer_manager = layer_manager

        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Layer: {}".format(layername), 1, (0,0,0))
        texture = pygame.Surface(label.get_bounding_rect().size)
        texture.fill((255,255,255))
        texture.blit(label,(-2,-2))

        super(LayerButton, self).__init__(texture, topleft)

    def activate(self):

        self.layer_manager.set_layer(self.layerindex)
