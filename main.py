import pygame
from sys import exit

#from level import Level
from gameState import Gamestate


pygame.init()

screen_x = 1280
screen_y = 720

screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Dungeon Game")



clock = pygame.time.Clock()
dt = 0

gameState = "lvl1"

Gamestate = Gamestate(screen)

while True:

    Gamestate.state_manager(state = gameState, screen = screen)

    dt = clock.tick(60) / 1000

