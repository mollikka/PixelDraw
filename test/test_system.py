import unittest
import pygame
import system

class TestSystemManager(unittest.TestCase):

    def test_system(self):
        pygame.init()
        self.v = system.System()
        self.v.step()
