import pygame

from tool_manager import ToolManager
from color_manager import ColorManager
from layer_manager import LayerManager
from history_manager import HistoryManager
from ui_manager import UIManager

class System(object):

    def __init__(self):

        #initialize the manager objects for each module
        self.tool_manager = ToolManager()
        self.color_manager = ColorManager()
        self.layer_manager = LayerManager()
        self.history_manager = HistoryManager(self.layer_manager)

        #initialize the user interface
        self.ui_manager = UIManager(self.tool_manager,
                                    self.color_manager,
                                    self.layer_manager,
                                    self.history_manager)

    def step(self):

        tool = self.tool_manager.get_tool()
        color = self.color_manager.get_color()
        layer = self.layer_manager.get_layer()

        #handle events
        for event in pygame.event.get():
            self.ui_manager.handle(event)

        #tools need a step to draw things
        tool.step(layer, color)

        #ask ui manager to draw the user interface
        self.ui_manager.draw()
