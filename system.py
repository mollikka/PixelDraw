import pygame

from handle_input import handle
from tool_manager import ToolManager
from color_manager import ColorManager
from layer_manager import LayerManager

class System(object):

    def __init__(self):

        self.winflags = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE
        self.background = (40,40,40)
        self.resize_window((640,480))

        self.tool_manager = ToolManager()
        self.color_manager = ColorManager()
        self.layer_manager = LayerManager()

    def resize_window(self, size):

        self.window=pygame.display.set_mode(size,self.winflags)
        self.window.fill(self.background)
        pygame.display.flip()

    def loop(self):

        while True:

            tool = self.tool_manager.get_tool()
            color = self.color_manager.get_color()
            layer = self.layer_manager.get_layer()

            for event in pygame.event.get():
                handle(event,self,self.tool_manager,self.color_manager,self.layer_manager)

            self.tool_manager.step(layer, color)

            self.window.fill(self.background)
            self.layer_manager.draw_picture(self.window)

            self.layer_manager.draw(self.window)
            self.color_manager.draw(self.window)
            self.tool_manager.draw(self.window)



            pygame.display.flip()
