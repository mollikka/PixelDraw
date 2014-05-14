import pygame

from tools.pen import Pen
from tools.eraser import Eraser
from tools.pixel import Pixel
from ui.button import Button

class ToolDialog(object):
    '''
        A drawn list of tools that the user can click to pick the one they want
        to use
    '''

    def __init__(self, tool_manager):

        load = pygame.image.load

        self.toolbuttons = [
            ToolButton(Pen, tool_manager, load('images/pen.png'),(0,0)),
            ToolButton(Eraser, tool_manager, load('images/eraser.png'),(0,50)),
            ToolButton(Pixel, tool_manager, load('images/pixel.png'),(0,100)),
        ]

    def draw(self, window):

        for button in self.toolbuttons:
            button.draw(window)

    def click(self):

        for button in self.toolbuttons:
            button.click()

class ToolButton(Button):
    '''
        A button in a ToolDialog. Clicking it will make the corresponding tool
        active
    '''

    def __init__(self, tool, tool_manager, texture, topleft):

        self.tool = tool()
        self.tool_manager = tool_manager
        super(ToolButton, self).__init__(texture, topleft)

    def activate(self):

        self.tool_manager.set_tool(self.tool)
