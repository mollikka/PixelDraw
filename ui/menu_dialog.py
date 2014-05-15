import tkFileDialog

from pygame import Surface, image
from Tkinter import Tk
from Tkinter import Button as Tkbutton
from tools.tool import Tool
from ui.button import Button as Ownbutton
from ui.ui_element import UIElement

class MenuDialog(UIElement):

    def __init__(self, ui_manager, bounding_box):

        buttons = [MenuButton(ui_manager, (0,0))]

        super(MenuDialog, self).__init__(bounding_box, buttons)

class MenuPopup(object):

    def __init__(self, layer_manager):

        self.layers = layer_manager

        self.options = {}
        self.options['defaultextension'] = '.png'
        self.options['filetypes'] = [('Portable Network Graphics', '.png'), ('Bitmap', '.bmp'),
            ('Truevision TGA', '.tga'), ('JPEG image', '.jpg'), ('all files', '.*')]
        self.options['initialfile'] = 'untitled.png'

        menuwindow = Tk()
        new_file = Tkbutton(menuwindow, text="New file...", command=self.button_action)
        save = Tkbutton(menuwindow, text="Save as...", command=self.save_as)
        load = Tkbutton(menuwindow, text="Load file...", command=self.button_action)

        new_file.pack()
        save.pack()
        load.pack()

        menuwindow.focus()
        menuwindow.mainloop()

    def button_action(self):
        pass

    def save_as(self):

        #get filename
        filename = tkFileDialog.asksaveasfilename(**self.options)
 
        #saving goes here
        if filename:
            open(filename, 'w')
            surface = self.layers.background.copy()
            self.layers.draw_picture(surface)
            image.save(surface, filename)


class MenuButton(Ownbutton):

    def __init__(self, ui_manager, topleft):

        super(MenuButton, self).__init__(image.load('images/menu.png'),topleft)
        self.layers = ui_manager.layer_manager

    def activate(self):

        MenuPopup(self.layers)
