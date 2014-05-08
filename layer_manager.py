import pygame

from ui.button import Button

class LayerManager(object):
    '''
        A LayerManager sets up a system of layers that can store pictures and
        be drawn on. Basically, it's a representation of the piece of art
        that's being worked on.

        Most tools and other picture manipulation effects should use
        LayerManager().get_layer().get_surface() to get the pygame surface to
        alter
    '''

    def __init__(self):

        self.layers = [Layer(self,800,600) for i in range(10)]
        self.curlayer = 0

        #background surface is shown if all layers are transparent
        self.background = pygame.Surface((800,600))
        self.background.fill((20,20,20))

        #a graphical UI for choosing a layer
        self.layer_dialog = LayerDialog(self)

        #camera panning position
        self.picture_position = [400,100]

    def get_layer(self):
        '''
            Returns the layer object that the user has chosen for editing
        '''

        return self.layers[self.curlayer]

    def set_layer(self, layer_index):
        '''
            Changes the active editing layer
        '''

        self.curlayer = layer_index

    def pick_layer(self):
        '''
            Input handling event for clicking the layer dialog,
            called by handle_input
        '''

        self.layer_dialog.pick_layer()

    def draw_picture(self, window):
        '''
            Renders the whole picture to window
        '''

        pic = pygame.Surface((800,600))
        pic.blit(self.background, (0,0))
        
        for layer in self.layers:
            layer.draw(pic)

        window.blit(pic, self.picture_position)
        


    def pan(self, mouse_delta):
        '''
            Input handling event for panning the picture,
            called by handle_input
        '''

        self.picture_position[0] += mouse_delta[0]
        self.picture_position[1] += mouse_delta[1]

    def draw(self, window):
        '''
            Renders the layer dialog elements to window
        '''

        myfont = pygame.font.SysFont("monospace", 15)

        pygame.draw.rect(window, (255,255,255), pygame.Rect(500,0,200,20))
        label = myfont.render("Current layer {}".format(self.curlayer), 1, (0,0,0))
        window.blit(label, (500,0))

        self.layer_dialog.draw(window)

class Layer(object):

    def __init__(self, layer_manager, w, h):
        self.surface = pygame.Surface((w, h),pygame.SRCALPHA)
        self.surface.fill(0)
        self.layer_manager = layer_manager
        self.location = 0,0
        self.name = "Unnamed layer"

    def get_surface(self):

        return self.surface

    def draw(self, window):

        window.blit(self.surface, self.location)

    def get_mouse_pos(self):

        mouseloc = pygame.mouse.get_pos()
        layerloc = self.location
        pictureloc = self.layer_manager.picture_position

        loc = [mouseloc[i] - layerloc[i] - pictureloc[i] for i in range(2)]

        return loc

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
