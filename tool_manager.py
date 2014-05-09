import pygame

from tools.pen import Pen
from tools.eraser import Eraser
from ui.button import Button

class ToolManager(object):
    '''
        A ToolManager manages manages the image manipulation tools: let's user
        pick a tool and tells the tool to do things to the picture.
    '''

    def __init__(self):

        self.tool = Pen()
        self.tool_dialog = ToolDialog(self)

    def get_tool(self): self.tool

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
        ]

    def draw(self, window):

        for button in self.toolbuttons:
            button.draw(window)

    def pick_tool(self):

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
