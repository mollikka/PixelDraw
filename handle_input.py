import sys
import pygame

def handle(event, tool):

    #print "Event:",event

    if event.type == pygame.QUIT:
        sys.exit(0)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit(0)

    if event.type == pygame.MOUSEBUTTONDOWN:
        tool.left_mouse_down()

    if event.type == pygame.MOUSEBUTTONUP:
        tool.left_mouse_up()
