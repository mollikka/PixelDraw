import unittest
import pygame
from layer_manager import LayerManager

class TestLayerManager(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.A = LayerManager()

    def test_set_scale(self):
        self.A.set_scale(1)
        self.assertEqual(self.A.picture_scale, 1)
        self.A.set_scale(2)
        self.assertEqual(self.A.picture_scale, 2)
        self.A.set_scale(1000)
        self.assertEqual(self.A.picture_scale, self.A.maxscale)
        self.A.set_scale(0)
        self.assertEqual(self.A.picture_scale, 1)

    def test_coordinate_transformations(self):
        self.A.set_scale(4)
        self.A.picture_position = [100,100]
        loc = self.A.picture_pos_to_screen((0,0))
        self.assertEqual(loc,[400,400])
        loc = self.A.screen_pos_to_picture((50,50))
        self.assertEqual(loc,[-87.5,-87.5])
