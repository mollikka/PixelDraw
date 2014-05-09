class Tool(object):

    def __init__(self):

        self.drawing = False
        self.lastpos = None

    def start_drawing(self):
        '''User event called by handle input'''
        self.drawing = True
        self.lastpos = None

    def stop_drawing(self):
        '''User event called by handle input'''
        self.drawing = False

    def step(self, layer, color):

        mousepos = layer.get_mouse_pos()

        if self.drawing and self.lastpos is not None:

            self.action(layer.get_surface(), color, mousepos, self.lastpos)

        self.lastpos = mousepos

    def action(self, surface, color, mouse_position, last_mouse_position):
        '''Just rewrite action for typical tools'''
        pass

