import pygame


#Color Rectangle
RED = (100,23,165)
WIDTH_RECT = 50
HEIGHT_RECT = 30

def draw_rect(window,x,y):
    pygame.draw.rect(window, RED,(int(x),int(y), WIDTH_RECT, HEIGHT_RECT))






