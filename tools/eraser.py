import pygame

from tools.tool import Tool

class Eraser(Tool):

    def action(self, surface, color, mouse_position, last_mouse_position):

        pygame.draw.line(surface, (0,0,0,0), mouse_position, last_mouse_position, 10)
