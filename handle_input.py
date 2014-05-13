import sys
import pygame

def handle(event, system, tool_manager, color_manager, layer_manager,
            history_manager):
    '''
        All user input events are caught by the handler which calls other
        modules and asks them to do things
    '''

    #mouse.get_rel must only be called once a step, don't call elsewhere
    #(because it's relative to the last call)
    mouse_delta = pygame.mouse.get_rel()


    mouse_pressed = pygame.mouse.get_pressed()
    mouse_left_pressed, mouse_mid_pressed, mouse_right_pressed = mouse_pressed

    mod_pressed = pygame.key.get_mods()

    #MOUSE HOLD

    if mouse_right_pressed:
        layer_manager.pan(mouse_delta)

    #MOUSE PRESS

    elif event.type == pygame.MOUSEBUTTONDOWN:
        #left button
        if event.button == 1:
            tool_manager.start_drawing()
            color_manager.pick_color()
            layer_manager.pick_layer()
            history_manager.push_history()
        #scroll up
        elif event.button == 4:
            layer_manager.upscale()
        #scroll down
        elif event.button == 5:
            layer_manager.downscale()


    elif event.type == pygame.MOUSEBUTTONUP:
        #left button
        if event.button == 1:
            tool_manager.stop_drawing()
            tool_manager.pick_tool()

    #KEY PRESS

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit(0)
            
        #ctrl modifier
        if mod_pressed & pygame.KMOD_CTRL:
            if event.key == pygame.K_z:
                history_manager.pull_history()

    #SYSTEM EVENTS

    elif event.type == pygame.QUIT:
        sys.exit(0)

    elif event.type == pygame.VIDEORESIZE:
        system.resize_window(event.dict['size'])

