import pygame
from modules.level import Level
from modules.hero import Hero
from modules.Monster import Monster



class State_manager():
    # Hvad sker der med state manager hvis i opretter en instance flere forskellige steder ?
    def __init__(self, screen):
        
        self.screen = screen
        self.screen_size = screen.get_size()    

        self.states = []

        self.tick_timer = pygame.time.get_ticks()
         
        self.current_state = "start_menu"
        self.prevGameState = ""
        self.current_lvl = 1

        self.paused = False
        
        self.background = pygame.display.set_mode(self.screen_size) #Background size
        


    #States

# I kunne have oprettet en game class som har en metode, AddMenu
    #Start menu
        self.start_menu = Menu("pause", "#000000")    
        self.start_menu.add_text("Press space to start", "./font/NebulousRegular.ttf", 48, "white", (100, 650))


    #Pause menu
        self.pause_menu = Menu("pause", "#000000")
        self.pause_menu.add_text("Pause", "./font/NebulousRegular.ttf", 70, "white", (100, 100))
        self.pause_menu.add_text("Press space to continue", "./font/NebulousRegular.ttf", 30, "white", (100, 200))
        self.pause_menu.add_button("Restart", "./font/NebulousRegular.ttf", 30, "white", (100, 300))
        self.pause_menu.add_text("DEBUG Press n for next level", "./font/NebulousRegular.ttf", 30, "white", (100, 650))


    #Game
        self.hero = Hero(250, 200)

        # Oprettelse af level kunne være håndteret i loops og lister. 
        #Level 1
        self.level_1 = Level(name = "Level 1", stage_nr = 1, bg_color = "#1a151f", hero_spawn = [200, 100])
        self.monster_1_1 = Monster(500, 300)

        self.level_1.add_monsters([self.monster_1_1])

 

        #Level 2
        self.level_2 = Level(name = "Level 2", stage_nr = 2, bg_color = "#1a151f", hero_spawn = [300, 100])
        self.monster_2_1 = Monster(900, 300)
        self.monster_2_2 = Monster(900, 350)

        self.level_2.add_monsters([self.monster_2_1, self.monster_2_2])


        #Level 3
        self.level_3 = Level(name = "Level 2", stage_nr = 3, bg_color = "#1a151f", hero_spawn = [300, 100])
        self.monster_3_1 = Monster(850, 300)
        self.monster_3_2 = Monster(700, 300)
        self.monster_3_3 = Monster(700, 300)

        self.level_3.add_monsters([self.monster_2_1, self.monster_2_2, self.monster_3_3])


    def change_state(self, state):
        self.current_state = state
         
    def next_lvl(self):
        self.current_lvl += 1
        
       

    # Vær opmærksom på jeres navngivning af metoder - menu (start_menu) har også en draw. Men det er ikke recursive tilbage til denne. 
    def draw(self, dt, key, mouse_click = (-1,-1)): #draws the diffentent states
        self.mouse_click = mouse_click
        match self.current_state: 
            
            case "start_menu":
                if key == pygame.K_SPACE:
                    self.change_state("game")
                    self.current_lvl = 1
                    

                self.start_menu.draw(self.screen, self.background)


            case "pause_game":
                if  self.pause_menu.elements[2][1].collidepoint(self.mouse_click): #Restart game
                    self.mouse_click = (-1,-1)
                    self.change_state("start_menu")
                    self.hero.set_pos(self.level_1.hero_spawn)
                    self.paused = False

                if key == pygame.K_n:
                    key == pygame.K_0
                    self.next_lvl()
                    self.paused = False
                    self.change_state("game")

                if key == pygame.K_SPACE:
                    key == pygame.K_0
                    self.paused = False
                    self.change_state("game")
                
                self.pause_menu.draw(self.screen, self.background )


            case "game":
                if key == pygame.K_ESCAPE:
                    if not self.paused:
                        self.paused = True
                        self.change_state("pause_game")

                match self.current_lvl:
                    case 1:
                        self.level_1.draw(self.screen, self.background, dt)
                        key = pygame.key.get_pressed()
                        self.hero.movement(key, self.level_2.get_lvl_walls(), dt)
                    case 2:
                        self.level_2.draw(self.screen, self.background, dt)
                        key = pygame.key.get_pressed()
                        self.hero.movement(key, self.level_2.get_lvl_walls(), dt)
                    case 3:
                        self.level_3.draw(self.screen, self.background, dt)
                        key = pygame.key.get_pressed()
                        self.hero.movement(key, self.level_3.get_lvl_walls(), dt)


                self.screen.blit(self.hero.draw()[0], self.hero.draw()[1])

                font = pygame.font.Font(None, 48)
                health_text = font.render(str(f"{self.hero.health} hp"), True, "#ffffff")
                self.screen.blit(health_text, (100, 650))# display health

                

class Menu():
    def __init__(self, name, bg_color):
        self.name = name
        self.bg_color = bg_color
        self.elements = []

    def add_text(self, text, font, size, color = "ffffff", pos = (0,0)):
        pygame_font = pygame.font.Font(font, size)
        text = pygame_font.render(text, True, color)
        elePos = [text, pos]

        self.elements.append(elePos)

    def add_button(self, text, font, size, color = "ffffff", pos = (0,0)):
        pygame_font = pygame.font.Font(font, size)
        btn_text = pygame_font.render(text, True, color)
        btn_rect = btn_text.get_rect(topleft = pos)

        elePos = [btn_text, btn_rect]
        self.elements.append(elePos)

    def draw (self, screen, background):
        background.fill(self.bg_color)
        for ele in self.elements:
            screen.blit(ele[0], ele[1])      











       