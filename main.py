import sys

import system

def main():
    try:
        import pygame
    except ImportError:
        print "Couldn't find a Pygame installation"

    pygame.init()

    v = system.System()
    v.loop()

if __name__ == '__main__':
    sys.exit(main())
