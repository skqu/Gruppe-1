import pygame

from modules.level import Level

class Gamestate():
    def __init__(self):

        self.background = pygame.display.set_mode((1280, 720)) #Background size

    def state_manager(self, state, screen): #Manages the diffentent states
        level = Level()
        match state: #Each state is customized in the switch eg - backgroundcolor, display elements
            case "start_menu":
                self.start_menu()
            case "lvl1":
                lvl_sprite_group = level.lvl_manager("1")
                bg_color = "#1a151f"

                self.main(screen, lvl_sprite_group, bg_color)
            case "lvl2":
                lvl_sprite_group = level.lvl_manager("2")
                bg_color = "#1a151f"

                self.main(screen, lvl_sprite_group, bg_color)
        
    def start_menu(self):
         pass


    def main(self, screen, lvl_sprite_group, bg_color): #The main game state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                #print(lvl_sprite_group)
                pass
        self.background.fill(bg_color)
        lvl_sprite_group.draw(screen)
        
    

        pygame.display.update()


