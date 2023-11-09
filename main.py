import pygame
from sys import exit

from modules.state import Gamestate


# !! Requires "pytmx" install with pip !!


pygame.init()

screen_x = 1280
screen_y = 720

screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Dungeon Game") 


clock = pygame.time.Clock()
dt = 0



Gamestate = Gamestate(screen, screen_x, screen_y)
key = None
mouse_pos = None


tick = pygame.time.get_ticks()
cooldown = 300    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            key = event.key
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_pos)

    Gamestate.state_manager(screen = screen, dt = dt, key = key, mouse_pos = mouse_pos, tick = tick, cooldown = cooldown) #Gets the gamestate from state module and displays it
    
    
    dt = clock.tick(60) / 1000 #Deltatime
    #print(clock.get_fps())
    
    pygame.display.update()  