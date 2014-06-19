import tkFileDialog

import pygame
from pygame import image, Rect
from Tkinter import Tk, Entry, Label, Toplevel
from Tkinter import Button as Tkbutton
from tools.tool import Tool
from ui.button import Button as Ownbutton
from ui.ui_element import UIElement
from ui import BUTTON_SIZE

global ROOT
ROOT = Tk()
ROOT.withdraw()

class MenuDialog(UIElement):

    def __init__(self, ui_manager, anchor, topleft, vertical=False):

        button_classes = [NewButton, SaveButton, LoadButton]

        buttons = []
        for i,button in enumerate(button_classes):
            if vertical: pos = (0,BUTTON_SIZE*i)
            else: pos = (BUTTON_SIZE*i,0)
            buttons.append(button(ui_manager, pos))

        if vertical: size = (BUTTON_SIZE,BUTTON_SIZE*len(buttons))
        else: size = (BUTTON_SIZE*len(buttons),BUTTON_SIZE)

        super(MenuDialog, self).__init__( Rect(topleft[0],topleft[1],size[0],size[1]), buttons, anchor)

class MenuButton(Ownbutton):

    def __init__(self, ui_manager, texture, topleft):

        self.layer_manager = ui_manager.layer_manager
        self.history_manager = ui_manager.history_manager

        self.options = {}
        self.options['defaultextension'] = '.png'
        self.options['filetypes'] = [('Portable Network Graphics', '.png'), ('Bitmap', '.bmp'),
            ('Truevision TGA', '.tga'), ('JPEG image', '.jpg'), ('all files', '.*')]

        super(MenuButton, self).__init__(texture,topleft)

    def new_file(self):

        NewFilePopup(self.layer_manager, self.history_manager)

    def load(self):

        #get filename
        filename = tkFileDialog.askopenfilename(**self.options)
   
        #load image
        if filename:
            surf = pygame.image.load(filename)
            self.layer_manager.new_image(surf)
            self.history_manager.clear_history()

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
            pygame.image.save(surface, filename)


class NewButton(MenuButton):

    def __init__(self, ui_manager, topleft):

        super(NewButton, self).__init__(ui_manager, image.load('images/new_file.png'),topleft)

    def activate(self, mouse_position):

        self.new_file()

class SaveButton(MenuButton):

    def __init__(self, ui_manager, topleft):

        super(SaveButton, self).__init__(ui_manager, image.load('images/save_file.png'),topleft)

    def activate(self, mouse_position):

        self.save_as()

class LoadButton(MenuButton):

    def __init__(self, ui_manager, topleft):

        super(LoadButton, self).__init__(ui_manager, image.load('images/load_file.png'),topleft)

    def activate(self, mouse_position):

        self.load()



class NewFilePopup(object):

    def __init__(self, layer_manager ,history_manager):

        self.layer_manager = layer_manager
        self.history_manager = history_manager

        self.dialog = Toplevel(ROOT)

        self.wbox = Entry(self.dialog)
        self.hbox = Entry(self.dialog)

        wlabel = Label(self.dialog, text="Width: ")
        hlabel = Label(self.dialog, text="Height: ")
        
        ok = Tkbutton(self.dialog, text="OK", command=self.ok)
        cancel = Tkbutton(self.dialog, text="Cancel", command=self.cancel)

        wlabel.pack()
        self.wbox.pack()
        hlabel.pack()
        self.hbox.pack()
        ok.pack()
        cancel.pack()

        self.dialog.protocol('WM_DELETE_WINDOW', self.cancel)


        self.dialog.mainloop()

    def ok(self):

        w = int(self.wbox.get())
        h = int(self.hbox.get())

        surface = pygame.Surface((w,h), pygame.SRCALPHA)
        self.layer_manager.new_image(surface)

        self.dialog.destroy()
        global ROOT
        ROOT.quit()
        ROOT = Tk()
        ROOT.withdraw()

    def cancel(self):

        self.dialog.destroy()
        global ROOT
        ROOT.quit()
        ROOT = Tk()
        ROOT.withdraw()
