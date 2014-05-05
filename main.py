import sys

import system

if __name__ == '__main__':

    try:
        import pygame
    except ImportError:
        print "Couldn't find a Pygame installation"

    pygame.init()

    v = system.System()
    v.loop()
