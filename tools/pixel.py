import pygame

from tools.tool import Tool

class Pixel(Tool):

    def action(self, surface, color, mouse_position, last_mouse_position):

        mouse_position = [int(mouse_position[i]) for i in range(2)]
        surface.set_at(mouse_position, color)
