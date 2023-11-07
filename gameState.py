import pygame


from level import Level



class Gamestate():
    def __init__(self, screen):

        self.background = pygame.display.set_mode((1280, 720))

    def state_manager(self, state, screen):
        lvl = Level()
        match state:
            case "start_menu":
                self.start_menu()
            case "lvl1":
                lvl_sprite_group = lvl.lvl_manager("1")
                bg_color = "#1a151f"

                self.main(screen, lvl_sprite_group, bg_color)
            case "lvl2":
                lvl_sprite_group = lvl.lvl_manager("2")
                bg_color = "#1a151f"

                self.main(screen, lvl_sprite_group, bg_color)
        
    def start_menu(self):
         pass


    def main(self, screen, lvl_sprite_group, bg_color):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                print(lvl_sprite_group.layers)
        self.background.fill(bg_color)
        lvl_sprite_group.draw(screen)
        
    

        pygame.display.update()


