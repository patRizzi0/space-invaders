# @Patrick
# Vérifie si l'événement actuel correspond à la fermeture de la fenêtre (clic sur la croix).

import pygame

def event_quit(event):
    return event.type == pygame.QUIT