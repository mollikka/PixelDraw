class HistoryManager(object):
    '''
        A HistoryManager manages the previous versions of the picture.
        It lets the user undo their changes.
    '''

    def __init__(self, layer_manager):

        self.history = []
        self.layer_manager = layer_manager
        self.maxhistory = 10

    def push_history(self):

        oldversion = []
        for layer in self.layer_manager.layers:
            oldversion.append(layer.copy())
        self.history.append(oldversion)

        #if we went over the limit, forget the first events
        l = len(self.history)
        m = self.maxhistory
        if l > m:
            self.history = self.history[l-m:]

    def pull_history(self):

        if len(self.history) > 0:
            oldversion = self.history.pop()
            self.layer_manager.layers = oldversion
