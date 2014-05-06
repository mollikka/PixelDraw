import pygame

from tools.pen import Pen

class ToolManager(object):

    def __init__(self):

        self.tool = Pen()

    def get_tool(self):

        self.tool

    def step(self, layer, color):

        self.tool.step(layer, color)

    def start_drawing(self):

        self.tool.start_drawing()

    def stop_drawing(self):

        self.tool.stop_drawing()
