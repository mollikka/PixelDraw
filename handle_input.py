import sys
import pygame

def handle(event, system, tool_manager, color_manager, layer_manager):

    #mouse.get_rel must only be called once a step, don't call elsewhere
    #(it's relative to the last call)
    mouse_delta = pygame.mouse.get_rel()


    mouse_left_pressed, mouse_mid_pressed, mouse_right_pressed = pygame.mouse.get_pressed()

    if mouse_right_pressed:
        layer_manager.pan(mouse_delta)


    if event.type == pygame.QUIT:
        sys.exit(0)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            tool_manager.start_drawing()
            color_manager.pick_color()
            layer_manager.pick_layer()

    elif event.type == pygame.MOUSEBUTTONUP:
        tool_manager.stop_drawing()
        tool_manager.pick_tool()

    elif event.type == pygame.VIDEORESIZE:
        system.resize_window(event.dict['size'])

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit(0)
