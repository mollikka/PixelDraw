import pygame

from ui.tool_dialog import ToolDialog
from ui.layer_dialog import LayerDialog
from ui.color_dialog import ColorPickerDialog
from ui.menu_dialog import MenuDialog
from ui.minimap_dialog import MinimapDialog

def get_layout(ui_manager):

    ui_elements = [
        LayerDialog(ui_manager,         'topright',     (-400,10)),
        MenuDialog(ui_manager,          'topleft',      (10,10),    vertical=True),
        ToolDialog(ui_manager,          'topright',     (-60,10),   vertical=True),
        ColorPickerDialog(ui_manager,   'bottomright',  (-200,-200),(200,200)),
        MinimapDialog(ui_manager,       'bottomleft',   (0,-200),   (200,200)),
    ]
    
    return ui_elements
