import sys
import pygame

#Ideally this should be the only place outside ui folder importing ui
from ui.tool_dialog import ToolDialog
from ui.layer_dialog import LayerDialog
from ui.color_dialog import ColorPickerButton

from ui.menu import MenuButton


class UIManager(object):
    '''
        A UIManager calls all the dialog elements and other stuff that is drawn
        on the screen.
    '''

    def __init__(self, tool_manager, color_manager, layer_manager, history_manager):

        #initialize the window
        self.winflags = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE
        self.background = (0,0,0)
        self.resize_window((640,480))

        self.tool_manager = tool_manager
        self.color_manager = color_manager
        self.layer_manager = layer_manager
        self.history_manager = history_manager

        self.ui_elements = [
            LayerDialog(self, pygame.Rect(300,0,300,200)),
            ToolDialog(self, pygame.Rect(0,0,50,300)),
        ]

    def resize_window(self, size):
        '''
            Initialize or resize the application window. Size as tuple (w,h)
        '''

        self.window=pygame.display.set_mode(size,self.winflags)
        self.window.fill(self.background)
        pygame.display.flip()

    def draw(self):

        #clear the screen
        self.window.fill(self.background)

        #draw the picture
        self.layer_manager.draw_picture_to_screen(self.window)

        #draw the ui elements
        for element in self.ui_elements:
            element.draw(self.window)

        #show the current layer (this is a hack)
        myfont = pygame.font.SysFont("monospace", 15)
        pygame.draw.rect(self.window, (255,255,255), pygame.Rect(500,0,200,20))
        label = myfont.render("Current layer {}".format(self.layer_manager.curlayer), 1, (0,0,0))
        self.window.blit(label, (500,0))

        #update the screen
        pygame.display.flip()

    def click(self):

            for element in self.ui_elements:
                if element.click(): break

    def handle(self, event):
        '''
            All user input events are caught by the handler which calls other
            modules and asks them to do things
        '''

        #mouse.get_rel must only be called once a step, don't call elsewhere
        #(because it's relative to the last call)
        mouse_delta = pygame.mouse.get_rel()


        mouse_pressed = pygame.mouse.get_pressed()
        mouse_left_pressed, mouse_mid_pressed, mouse_right_pressed = mouse_pressed

        mod_pressed = pygame.key.get_mods()

        #MOUSE HOLD

        if mouse_right_pressed:
            self.layer_manager.pan(mouse_delta)

        #MOUSE PRESS

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #left button
            if event.button == 1:
                self.tool_manager.start_drawing()
                self.history_manager.push_history()
                self.click()
            #scroll up
            elif event.button == 4:
                self.layer_manager.upscale()
            #scroll down
            elif event.button == 5:
                self.layer_manager.downscale()


        elif event.type == pygame.MOUSEBUTTONUP:
            #left button
            if event.button == 1:
                self.tool_manager.stop_drawing()

        #KEY PRESS

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)
                
            #ctrl modifier
            if mod_pressed & pygame.KMOD_CTRL:
                if event.key == pygame.K_z:
                    self.history_manager.pull_history()

        #SYSTEM EVENTS

        elif event.type == pygame.QUIT:
            sys.exit(0)

        elif event.type == pygame.VIDEORESIZE:
            self.resize_window(event.dict['size'])

