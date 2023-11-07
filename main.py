import pygame
from sys import exit

from modules.state import Gamestate

# !! KRÆVER "pytmx" install med pip !!



pygame.init()

screen_x = 1280
screen_y = 720

screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Dungeon Game")


clock = pygame.time.Clock()
dt = 0



gameState = "lvl1" #Change gamestate ex lvl1 & lvl2

Gamestate = Gamestate(screen)

while True:

    Gamestate.state_manager(state = gameState, screen = screen) #Gets the gamestate from state module and displays it

    dt = clock.tick(60) / 1000 #Deltatime

