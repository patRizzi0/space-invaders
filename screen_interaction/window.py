# @Patrick
# Initialise et retourne la fenêtre principale de Pygame avec les dimensions spécifiées.

import pygame

def create_window(width, height):
    pygame.init()
    return pygame.display.set_mode((width, height))