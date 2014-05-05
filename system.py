import pygame

from handle_input import handle
from tool_manager import ToolManager

class System(object):

    def __init__(self):

        self.window = pygame.display.set_mode((640,480))
        self.tool_manager = ToolManager()

    def loop(self):

        while True:

            tool = self.tool_manager.get_tool()
            color = (255,255,255)
            layer = self.window

            for event in pygame.event.get():
                handle(event,tool)

            tool.step(layer, color)

            pygame.display.flip()
