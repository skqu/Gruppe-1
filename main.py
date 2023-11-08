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



Gamestate = Gamestate()
key = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            key = event.key

    Gamestate.state_manager(state = Gamestate.gameState, screen = screen, dt = dt, key = key) #Gets the gamestate from state module and displays it
    
    
    dt = clock.tick(60) / 1000 #Deltatime

    pygame.display.update() 