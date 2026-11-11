import pygame


#Color Rectangle
WHITE = (255,255,165)
WIDTH_RECT = 5
HEIGHT_RECT = 10

def draw_laser(window,x,y):
    pygame.draw.rect(window, WHITE,(int(x),int(y), WIDTH_RECT, HEIGHT_RECT))