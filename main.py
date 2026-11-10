import pygame
from screen_interaction.window import create_window
from square.square_init import draw_rect
from player import player
from input.directions_wasd import input_handler


from settings import WIDTH, HEIGHT, FPS
#Window init
window = create_window(WIDTH, HEIGHT)

#spawn_point
player_1 = player(300.0, 150.0)

# s = s0 + v * dt
def mru_1D(player_1,dt):
    player_1["x"] += player_1["v_x"] * dt

    pygame.init()
    time = pygame.time.Clock()

    running = True
    while running:
        running = input_handler(player_1)

        window.fill((0, 0, 0))

        dt_ms = time.tick(FPS)
        dt = dt_ms / 1000


        mru_1D(player_1,dt) #Moto Rettilineo Uniforme

        draw_rect(window,player_1["x"],player_1["y"])


        pygame.display.flip()

        pygame.quit()