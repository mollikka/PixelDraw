import unittest
import pygame
from layer_manager import LayerManager
from history_manager import HistoryManager

class TestHistoryManager(unittest.TestCase):

    def setUp(self):

        pygame.init()
        self.A = LayerManager()
        self.B = HistoryManager(self.A)

    def test_history(self):

        #test pushing history
        self.B.maxhistory = 3
        self.assertEqual(len(self.B.history),0)
        self.B.push_history()
        self.assertEqual(len(self.B.history),1)
        self.B.push_history()
        self.B.push_history()
        self.assertEqual(len(self.B.history),3)
        
        L0 = self.B.history[0]
        L1 = self.B.history[1]
        L2 = self.B.history[2]
        
        self.B.push_history()
        self.assertEqual(len(self.B.history),3)
        self.assertEqual(self.B.history[0],L1)
        self.assertEqual(self.B.history[1],L2)

        #test pulling history
        self.B.pull_history()
        self.B.pull_history()
        self.assertEqual(self.A.layers,L2)
        self.B.pull_history()
        self.assertEqual(self.A.layers,L1)
        self.assertEqual(len(self.B.history),0)
        
        #nothing should happen because the history is empty
        self.B.pull_history()
        self.assertEqual(self.A.layers,L1)
        self.assertEqual(len(self.B.history),0)
