import pygame

from ui.tool_dialog import ToolDialog
from ui.layer_dialog import LayerDialog
from ui.color_dialog import ColorPickerDialog
from ui.menu_dialog import MenuDialog
from ui.minimap_dialog import MinimapDialog

def get_layout(ui_manager):

    ui_elements = [
        LayerDialog(ui_manager, (200,200)),
        ToolDialog(ui_manager, (10,10), vertical=True),
        ColorPickerDialog(ui_manager,(200,200)),
        MenuDialog(ui_manager, (200,200), vertical=True),
        MinimapDialog(ui_manager, (200,200),(200,200)),
    ]
    
    return ui_elements
