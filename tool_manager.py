import pygame

from ui.tool_dialog import ToolDialog
from tools.pen import Pen as DefaultTool

class ToolManager(object):
    '''
        A ToolManager manages the image manipulation tools: lets user
        pick a tool and tells the tool to do things to the picture.
    '''

    def __init__(self):

        self.tool = DefaultTool()
        self.tool_dialog = ToolDialog(self)

    def get_tool(self): return self.tool

    def set_tool(self, newValue): self.tool = newValue

    def step(self, layer, color):

        self.tool.step(layer, color)

    def draw(self, window):

        self.tool_dialog.draw(window)

    def start_drawing(self):

        self.tool.start_drawing()

    def stop_drawing(self):

        self.tool.stop_drawing()

    def pick_tool(self):
    
        self.tool_dialog.pick_tool()
