import pygame

from ui.ui_element import UIElement
from ui.button import Button

class LayerDialog(UIElement):
    '''
        A drawn list of layers that the user can click to pick the one they want
        to edit
    '''

    def __init__(self, ui_manager, bounding_box):

        layer_manager = ui_manager.layer_manager

        layerbuttons = []
        for i in range(len(layer_manager.layers)):
            layerbuttons.append(LayerButton(i, layer_manager, (0,i*20)))

        super(LayerDialog, self).__init__(bounding_box, layerbuttons)

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

    def activate(self, mouse_position):

        self.layer_manager.set_layer(self.layerindex)
