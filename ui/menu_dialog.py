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

    def __init__(self, ui_manager):

        self.layer_manager = ui_manager.layer_manager
        self.history_manager = ui_manager.history_manager

        self.options = {}
        self.options['defaultextension'] = '.png'
        self.options['filetypes'] = [('Portable Network Graphics', '.png'), ('Bitmap', '.bmp'),
            ('Truevision TGA', '.tga'), ('JPEG image', '.jpg'), ('all files', '.*')]

        self.menuwindow = Tk()
        new_f = Tkbutton(self.menuwindow, text="New file...", command=self.new_file)
        save = Tkbutton(self.menuwindow, text="Save as...", command=self.save_as)
        load = Tkbutton(self.menuwindow, text="Load file...", command=self.load)

        new_f.pack()
        save.pack()
        load.pack()

        self.menuwindow.mainloop()

    def new_file(self):
        pass

    def load(self):

        #get filename
        filename = tkFileDialog.askopenfilename(**self.options)
   
        #load image
        if filename:
            surf = image.load(filename)
            self.layer_manager.new_image(surf)
            self.history_manager.clear_history()
            self.menuwindow.destroy()


    def save_as(self):

        #set default filename
        self.options['initialfile'] = 'untitled.png'

        #get filename
        filename = tkFileDialog.asksaveasfilename(**self.options)
 
        #saving goes here
        if filename:
            open(filename, 'w')
            surface = self.layer_manager.background.copy()
            self.layer_manager.draw_picture(surface)
            image.save(surface, filename)
            self.menuwindow.destroy()


class MenuButton(Ownbutton):

    def __init__(self, ui_manager, topleft):

        super(MenuButton, self).__init__(image.load('images/menu.png'),topleft)
        self.ui_manager = ui_manager

    def activate(self, mouse_position):

        MenuPopup(self.ui_manager)
