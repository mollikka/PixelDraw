import pygame

from tools.pen import Pen

class ToolManager(object):

    def __init__(self):

        self.tool = Pen()

    def get_tool(self):

        return self.tool
