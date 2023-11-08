import pygame
import time
from modules.level import Level
from modules.hero import Hero



class Gamestate():
    def __init__(self):
        
        self.gameState = "start_menu"
        self.prevGameState = ""
        self.background = pygame.display.set_mode((1280, 720)) #Background size

        self.level_1 = Level(name = "Level 1", stage_nr = 1, bg_color = "#1a151f", hero_spawn = [300, 300])
        self.level_2 = Level(name = "Level 2", stage_nr = 2, bg_color = "#1a151f", hero_spawn = [300, 200])

        self.hero = Hero(250, 250)
        
        self.paused = False
        self.mouse_pos = (0,0)

    def state_manager(self, screen, dt, key, mouse_pos = (0,0)): #Manages the diffentent states
        self.mouse_pos = mouse_pos
        match self.gameState: #Each state is customized in the switch eg - backgroundcolor, display elements
            case "start_menu":
                
                white = (255, 255, 255)
                black = (0, 0, 0)
                bg_color = black
                
                font = pygame.font.Font("./font/NebulousRegular.ttf", 48)
                screen_text = font.render("Press Space to Start", True, white)

            
                self.start_menu(screen, bg_color, screen_text, key)

            case "pause_game":
                white = (255, 255, 255)
                black = (0, 0, 0)
                bg_color = black
                
                font = pygame.font.Font("./font/NebulousRegular.ttf", 70)
                title = font.render("Paused", True, white)
                
                font = pygame.font.Font("./font/NebulousRegular.ttf", 30)
                subtext = font.render("Press space to continue", True, white)


                font = pygame.font.Font("./font/NebulousRegular.ttf", 30)
                btn_text = font.render("Restart", True, white)
                btn_rect = btn_text.get_rect(topleft =(100,200))

                elemets = title, subtext, btn_text, btn_rect

                self.pause_menu(screen, bg_color, elemets, key)
            
            case "restart_game":
                pass
    
            case "lvl1":
                self.main(screen = screen, hero = self.hero, dt = dt, level = self.level_1, key = key)

            case "lvl2":
                
                 self.main(screen = screen, hero = self.hero, dt = dt, level = self.level_2, key = key)

        



    def start_menu(self, screen ,bg_color, screen_text, key): # Display the start menu
        if key == pygame.K_SPACE:
            self.gameState = "lvl2"
            self.hero.rect.center = self.level_1.hero_spawn 

        self.background.fill(bg_color)
        screen.blit(screen_text, (100, 550))


    def pause_menu(self, screen ,bg_color, elemets, key):
        
        if elemets[3].collidepoint(self.mouse_pos): #Restart game
            self.mouse_pos = (0,0)
            self.gameState = "lvl1"
            self.hero.rect.center = self.level_1.hero_spawn 

        if key == pygame.K_SPACE:
            key == pygame.K_0
            self.paused = False
            self.gameState = self.prevGameState
            

        self.background.fill(bg_color)
        screen.blit(elemets[0], (100, 50))
        screen.blit(elemets[1], (100, 120))
        
        screen.blit(elemets[2], elemets[3])
        

            
    def main(self, screen, hero ,dt, level, key): #The main game state

        if key == pygame.K_ESCAPE:
            
            if not self.paused:
                self.paused = True
                self.prevGameState = self.gameState
                self.gameState = "pause_game"
 


        key = pygame.key.get_pressed()
        hero.movement(key, level.get_lvl_walls(), dt)


        self.background.fill(level.bg_color)

        level.get_lvl_floor().draw(screen)
        level.get_lvl_walls().draw(screen)
        
        screen.blit(hero.draw()[0], hero.draw()[1])
            



