import pygame

from handle_input import handle
from tool_manager import ToolManager
from color_manager import ColorManager

class System(object):

    def __init__(self):

        self.winflags = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE
        self.background = (40,40,40)
        self.resize_window((640,480))

        self.tool_manager = ToolManager()
        self.color_manager = ColorManager()

    def resize_window(self, size):

        self.window=pygame.display.set_mode(size,self.winflags)
        self.window.fill(self.background)
        pygame.display.flip()

    def loop(self):

        while True:

            tool = self.tool_manager.get_tool()
            color = self.color_manager.get_color()
            layer = self.window

            for event in pygame.event.get():
                handle(event,self,self.tool_manager,self.color_manager)

            self.tool_manager.step(layer, color)
            self.color_manager.draw(layer)

            pygame.display.flip()
