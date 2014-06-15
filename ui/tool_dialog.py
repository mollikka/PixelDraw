import pygame

from tools.pen import Pen
from tools.eraser import Eraser
from tools.pixel import Pixel
from ui.ui_element import UIElement
from ui.button import Button
from ui import BUTTON_SIZE

class ToolDialog(UIElement):
    '''
        A drawn list of tools that the user can click to pick the one they want
        to use
    '''

    def __init__(self, ui_manager, anchor, topleft, vertical=False):

        tool_manager = ui_manager.tool_manager

        load = pygame.image.load

        tools = [(Pen,'images/pen.png'),
                 (Eraser, 'images/eraser.png'),
                 (Pixel, 'images/pixel.png'),]
        
        buttons = []
        for i,tool in enumerate(tools):
            if vertical: pos = (0,BUTTON_SIZE*i)
            else: pos = (BUTTON_SIZE*i,0)
            
            buttons.append(ToolButton(tool[0], tool_manager, load(tool[1]),pos))

        if vertical: size = (BUTTON_SIZE,BUTTON_SIZE*len(buttons))
        else: size = (BUTTON_SIZE*len(buttons),BUTTON_SIZE)

        super(ToolDialog,self).__init__(pygame.Rect(topleft[0],topleft[1],size[0],size[1]), buttons, anchor)

class ToolButton(Button):
    '''
        A button in a ToolDialog. Clicking it will make the corresponding tool
        active
    '''

    def __init__(self, tool, tool_manager, texture, topleft):

        self.tool = tool()
        self.tool_manager = tool_manager
        super(ToolButton, self).__init__(texture, topleft)

    def activate(self, mouse_position):

        self.tool_manager.set_tool(self.tool)
