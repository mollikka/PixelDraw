import pygame

from tools.tool import Tool

class Pen(Tool):

    def action(self, surface, color, mouse_position, last_mouse_position):

        pygame.draw.line(surface, color, mouse_position, last_mouse_position, 5)
