import pygame
from screen_interaction.window import create_window
from square.square_init import draw_rect
from player import player
from window_barrier.barriers import set_barriers
from input.directions_wasd import input_handler
from entity_laser import laser
from square.laser_init import draw_laser


from settings import WIDTH, HEIGHT, FPS
#Window init
window = create_window(WIDTH, HEIGHT)

#spawn_point
player_1 = player(300.0, 400.0)
laser_1 = laser(player_1["x"], player_1["y"])

# s = s0 + v * dt
def mru_1D_horizontal(player_1,dt):
    player_1["x"] += player_1["v_x"] * dt

def mru_1D_vertical(laser_1,dt_laser):
    #@Patrick
    #ça c'est pour les laser. Mouvement verical
    laser_1["y"] += laser_1["v_y"] * dt_laser

time = pygame.time.Clock()

running = True
while running:
    running = input_handler(player_1, laser_1)
    
    dt_ms = time.tick(FPS)
    dt = dt_ms / 1000

    mru_1D_horizontal(player_1,dt) #Moto Rettilineo Uniforme
    set_barriers(player_1, laser_1)

    if(laser_1["is_fired"] == False):
        laser_1["x"] = player_1["x"]
        laser_1["y"] = player_1["y"]
    else:
        mru_1D_vertical(laser_1,dt) #Moto Rettilineo Uniforme

    #Remplir la fenetre
    window.fill((0, 0, 0))

    #Dessiner les entités
    draw_rect(window,player_1["x"],player_1["y"])
    if(laser_1["is_fired"] == True):
        draw_laser(window, laser_1["x"], laser_1["y"])
    
    pygame.display.flip()

pygame.quit()