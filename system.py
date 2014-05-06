import pygame

from handle_input import handle
from tool_manager import ToolManager
from color_manager import ColorManager

class System(object):

    def __init__(self):

        self.window = pygame.display.set_mode((640,480))
        self.tool_manager = ToolManager()
        self.color_manager = ColorManager()

    def loop(self):

        while True:

            tool = self.tool_manager.get_tool()
            color = self.color_manager.get_color()
            layer = self.window

            for event in pygame.event.get():
                handle(event,tool,self.color_manager)

            tool.step(layer, color)

            self.color_manager.draw_panel(layer)

            pygame.display.flip()
