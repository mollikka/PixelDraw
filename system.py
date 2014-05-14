import pygame

from handle_input import handle
from tool_manager import ToolManager
from color_manager import ColorManager
from layer_manager import LayerManager

from tools.menu import MenuPopup
from tools.menu import MenuButton

class System(object):

    def __init__(self):

        #initialize the window
        self.winflags = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE
        self.background = (0,0,0)
        self.resize_window((640,480))

        #initialize the manager objects for each module
        self.tool_manager = ToolManager()
        self.color_manager = ColorManager()
        self.layer_manager = LayerManager()

        menubutton = MenuButton(MenuPopup, self.tool_manager, pygame.image.load('images/menu.png'),(0,150))

    def resize_window(self, size):
        '''
            Initialize or resize the application window. Size as tuple (w,h)
        '''

        self.window=pygame.display.set_mode(size,self.winflags)
        self.window.fill(self.background)
        pygame.display.flip()

    def step(self):

        tool = self.tool_manager.get_tool()
        color = self.color_manager.get_color()
        layer = self.layer_manager.get_layer()

        #handle events
        for event in pygame.event.get():
            handle(event,self,self.tool_manager,self.color_manager,self.layer_manager)

        self.tool_manager.step(layer, color)

        #clear the screen
        self.window.fill(self.background)
        self.layer_manager.draw_picture_to_screen(self.window)

        #ask each manager object to draw the stuff related to their module
        self.layer_manager.draw(self.window)
        self.color_manager.draw(self.window)
        self.tool_manager.draw(self.window)

        #update the screen
        pygame.display.flip()
