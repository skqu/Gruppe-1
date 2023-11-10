import pygame
from sys import exit

from modules.state import State_manager


# !! Requires "pytmx" install with pip !!


pygame.init()

screen_x = 1280
screen_y = 720

screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Dungeon Game") 


clock = pygame.time.Clock()
dt = 0

key_pressed = ""
mouse_click = (0,0)

state_manager = State_manager(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            key_pressed = event.key
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = pygame.mouse.get_pos()

    
    state_manager.draw(dt = dt, key = key_pressed, mouse_click = mouse_click) #Gets the gamestate from state module and displays it
    
    
    dt = clock.tick(60) / 1000 #Deltatime

    pygame.display.update()  