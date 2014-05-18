import pygame

from tools.pen import Pen as DefaultTool

class ToolManager(object):
    '''
        A ToolManager manages the image manipulation tools: lets user
        pick a tool and tells the tool to do things to the picture.
    '''

    def __init__(self):

        self.tool = DefaultTool()

    def get_tool(self): return self.tool

    def set_tool(self, newValue): self.tool = newValue
