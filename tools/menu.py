import tkFileDialog

from Tkinter import Tk
from tools.tool import Tool
from ui.button import Button

class MenuPopup(object):

    def __init__(self):

        menuwindow = Tk()
        new_file = Button(menuwindow, text="New file...", command=self.button_action)
        save = Button(menuwindow, text="Save as...", command=self.save_as)
        load = Button(menuwindow, text="Load file...", command=self.button_action)

        new_file.pack()
        save.pack()
        load.pack()

        menuwindow.focus()
        menuwindow.mainloop()

    def button_action(self):
        pass

    def save_as(self):

        #get filename
        filename = tkFileDialog.asksaveasfilename()
 
        #saving goes here
        if filename:
            open(filename, 'w')

class MenuButton(Button):

    def __init__(self, tool, tool_manager, texture, topleft):

        super(MenuButton, self).__init__(texture, topleft)

    def activate(self):

        MenuPopup()
