import sys
import pygame

def handle(event, system, tool_manager, color_manager):

    #print "Event:",event

    if event.type == pygame.QUIT:
        sys.exit(0)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit(0)

    if event.type == pygame.MOUSEBUTTONDOWN:
        tool_manager.start_drawing()
        color_manager.pick_color()

    if event.type == pygame.MOUSEBUTTONUP:
        tool_manager.stop_drawing()

    if event.type == pygame.VIDEORESIZE:
        system.resize_window(event.dict['size'])
