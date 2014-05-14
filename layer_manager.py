import pygame

from ui.layer_dialog import LayerDialog

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

        self.bounding_box = pygame.Rect(400,100,800,600)

        w,h = self.bounding_box.size

        self.layers = [Layer(self,w,h) for i in range(10)]
        self.curlayer = 0

        #background surface is shown if all layers are transparent
        self.background = pygame.Surface((w,h))
        self.background.fill((20,20,20))

        #a graphical UI for choosing a layer
        self.layer_dialog = LayerDialog(self)

        #camera zoom
        self.picture_scale = 1
        self.maxscale = 64

    def get_layer(self):

        return self.layers[self.curlayer]

    def set_layer(self, layer_index):

        self.curlayer = layer_index

    def pick_layer(self):
        '''
            Input handling event for clicking the layer dialog,
            called by handle_input
        '''

        self.layer_dialog.pick_layer()

    def draw_picture(self, surface):
        '''
            Render the 1:1 pixel picture (= all the layers) to surface
        '''

        for layer in self.layers:
            layer.draw(surface)

    def set_scale(self, newValue):
    
        mpos = pygame.mouse.get_pos()
        
        #move corner to old mouse location
        focus = self.screen_pos_to_picture(mpos)
        pos = self.bounding_box.topleft
        self.bounding_box.topleft = [pos[i] + focus[i] for i in range(2)]
        
        #scale
        self.picture_scale = min(self.maxscale,max(1,newValue))
        
        #move corner to new mouse location
        focus = self.screen_pos_to_picture(mpos)
        self.bounding_box.topleft = [pos[i] + focus[i] for i in range(2)]

    def upscale(self):
    
        self.set_scale(self.picture_scale*2)

    def downscale(self):
    
        self.set_scale(self.picture_scale/2)


    def screen_pos_to_picture(self, loc):
        '''transform xy tuple on screen to xy tuple in the picture'''

        pictureloc = self.bounding_box.topleft
        picturescale = self.picture_scale

        loc = [int(loc[i]/picturescale - pictureloc[i]) for i in range(2)]

        return loc

    def picture_pos_to_screen(self, loc):
        '''transform xy tuple in the picture to xy tuple on screen'''

        pictureloc = self.bounding_box.topleft
        picturescale = self.picture_scale

        loc = [int((loc[i]+ pictureloc[i])*picturescale)  for i in range(2)]

        return loc

    def draw_picture_to_screen(self, window):
        '''
            Renders the whole picture to window. Applies picture_position and
            background color
        '''
        scale = self.picture_scale
        pos = self.bounding_box.topleft

        #draw the natural 1:1 pixel image
        pic = pygame.Surface((800,600))
        pic.blit(self.background, (0,0))
        self.draw_picture(pic)

        #find the area in picture that shows up on the screen
        spic_topleft = self.screen_pos_to_picture((0,0))
        spic_botright = self.screen_pos_to_picture(window.get_size())
        spic_size = [spic_botright[i] - spic_topleft[i] +1 for i in range(2)] #+1 because that prevents a < 1 pixel gap from being drawn when zoomed
        #create a surface that is fills the screen in picture coordinates
        spic = pygame.Surface(spic_size, pygame.SRCALPHA)
        spic.blit(pic, pos)

        #create an upscaled surface that will actually fill the screen
        spic_size_scaled = [spic_size[i]*scale for i in range(2)]
        scaledpic = pygame.transform.scale(spic, spic_size_scaled)
        window.blit(scaledpic, (0,0))

    def pan(self, mouse_delta):
        '''
            Input handling event for panning the picture,
            called by handle_input
        '''
        scale = self.picture_scale

        self.bounding_box.left += mouse_delta[0]/float(scale)
        self.bounding_box.top += mouse_delta[1]/float(scale)

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
    '''
        A Layer is a wrapper for a Surface that is meant to be drawn on by the
        user.
    '''

    def __init__(self, layer_manager, w, h):
        self.surface = pygame.Surface((w, h),pygame.SRCALPHA)
        self.surface.fill(0)
        self.layer_manager = layer_manager
        self.name = "Unnamed layer"

    def get_surface(self):

        return self.surface

    def copy(self):

        w,h = self.surface.get_size()
        clone = Layer(self.layer_manager, w, h)
        clone.surface = self.surface.copy()
        clone.name = self.name
        return clone

    def draw(self, window):

        window.blit(self.surface, (0,0))

    def get_mouse_pos(self):

        mouseloc = pygame.mouse.get_pos()

        loc = self.layer_manager.screen_pos_to_picture(mouseloc)

        return loc
