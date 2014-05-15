import sys
import pygame

#Ideally this should be the only place outside ui folder importing ui
from ui.tool_dialog import ToolDialog
from ui.layer_dialog import LayerDialog
from ui.color_dialog import ColorPickerDialog
from ui.menu_dialog import MenuDialog

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
            LayerDialog(self, pygame.Rect(500,0,300,200)),
            ToolDialog(self, pygame.Rect(0,0,50,300)),
            ColorPickerDialog(self, pygame.Rect(100,0,320,220)),
            MenuDialog(self, pygame.Rect(0,320,50,100))
        ]

        self.focused_element = None

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

        if self.focused_element:
            self.focused_element.click()

    def pan(self, mouse_delta):

        if self.focused_element:
            self.focused_element.pan(mouse_delta)
        else:
            self.layer_manager.pan(mouse_delta)

    def pick_focused_element(self):

        for element in self.ui_elements:
            if element.hit(): 
                self.focused_element = element
                return

        self.clear_focused_element()

    def clear_focused_element(self):

        self.focused_element = None

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


        #MOUSE PRESS

        if event.type == pygame.MOUSEBUTTONDOWN:
            #left button
            if event.button == 1:
                self.pick_focused_element()

                self.click()

                #not interacting with ui, lets draw
                if not self.focused_element:
                    self.tool_manager.start_drawing()
                    self.history_manager.push_history()

            if event.button == 3:
                self.pick_focused_element()

            #scroll up
            elif event.button == 4:
                self.layer_manager.upscale()
            #scroll down
            elif event.button == 5:
                self.layer_manager.downscale()


        elif event.type == pygame.MOUSEBUTTONUP:
            #left button
            if event.button == 1:
                self.clear_focused_element()
                self.tool_manager.stop_drawing()

            #right button
            if event.button == 3:
                self.clear_focused_element()

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

        #hold events come after click events so that things happen in order
        #button in -> button hold -> button out
        #MOUSE HOLD

        if mouse_right_pressed:
            self.pan(mouse_delta)

