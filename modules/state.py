import pygame

from modules.level import Level
from modules.hero import Hero



class Gamestate():
    def __init__(self):
        
        self.gameState = "start_menu"
        self.background = pygame.display.set_mode((1280, 720)) #Background size

        self.level_1 = Level(name = "Level 1", stage_nr = 1, bg_color = "#1a151f")
        self.level_2 = Level(name = "Level 2", stage_nr = 2, bg_color = "#1a151f")

        self.hero = Hero(250, 250)
        
        self.paused = False
        

    def state_manager(self, state, screen, dt, key): #Manages the diffentent states
        
        match state: #Each state is customized in the switch eg - backgroundcolor, display elements
            case "start_menu":
            
                white = (255, 255, 255)
                black = (0, 0, 0)
                bg_color = black
                
                font = pygame.font.Font("./font/Pixeltype.ttf", 48)
                screen_text = font.render("Press Space to Start", True, white)

                self.start_menu(screen, bg_color, screen_text, key)

            case "pause_game":
                pass
            
            case "restart_game":
                pass
    
            case "lvl1":

                self.main(screen = screen, hero = self.hero, dt = dt, level = self.level_1)

            case "lvl2":
                
                 self.main(screen = screen, hero = self.hero, dt = dt, level = self.level_2)

        



    def start_menu(self, screen ,bg_color, screen_text, key): # Display the start menu
        

        if key == pygame.K_SPACE:
            self.gameState = "lvl1"
        

        self.background.fill(bg_color)
        screen.blit(screen_text, (250, 450))

        
        

    def main(self, screen, hero ,dt, level): #The main game state

        

        key = pygame.key.get_pressed()
            
    
        hero.movement(key, level.get_lvl_walls(), dt)


        self.background.fill(level.bg_color)

        level.get_lvl_floor().draw(screen)
        level.get_lvl_walls().draw(screen)
        
        screen.blit(hero.draw()[0], hero.draw()[1])
        


