import pygame
import random


class Monster:
    def __init__(self, pos_x, pos_y):
      
        self.image_width = 80 
        self.image_height = 80
        self.hero_image = pygame.image.load("./Graphics/characters/monster.png")
        self.resized_image = pygame.transform.scale(self.hero_image, (self.image_width, self.image_height))
        self.rect = self.resized_image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.movement_speed = 2000
        self.Health = 100
        self.health_gui = [0,0]

        self.ticks = pygame.time.get_ticks()
        self.movement_cooldown = 300
        


    def create_strenght(self, Name, Health, Defence, Strength):
        self.Name = Name
        self.Health = Health
        self.Defence = Defence
        self.Strength = Strength
       
    def take_dmg(self, dmg):
        BR = random.choice ([True, False])
        if BR == True:
                print(f"{self.Name} used defence, and blocked {self.Defence} of your damage!")
                self.Health -= (dmg - self.Defence)
                if self.Health < 0:
                    self.Health = 0
        else:  
            if dmg < self.Health:
                self.Health -= dmg
            else:
                self.Health = 0
                

    def Attack(self):
        return self.Strength
    
    def gui(self):
        font = pygame.font.Font(None, 20)
        health_text = font.render(str(f"{self.Health}"), True, "red")
        
        new_x = self.rect.x + self.rect.width / 2
        new_y = self.rect.y - 30
        self.health_gui[0] = (health_text)
        self.health_gui[1] = ((new_x, new_y))

        return self.health_gui

    def draw(self, walls, dt, screen):
        gui = self.gui()

        now = pygame.time.get_ticks()
        if now - self.ticks >= self.movement_cooldown:
            self.ticks  = now
            self.movement(walls, dt)


        screen.blit(self.resized_image, self.rect)      
        
        print(self.health_gui)
        screen.blit(gui[0], gui[1])
       


    def collision(self, direction, sprite_group): #Check if player is colliding with walls
        if pygame.sprite.spritecollide(self, sprite_group, False): 
            
            hits = pygame.sprite.spritecollide(self, sprite_group, False) #Get the sprites the player is colliding with
            match direction:
                case "left":
                    if hits:
                        self.rect.x = hits[0].rect.right 
                case "right":
                    if hits:
                        self.rect.x = hits[0].rect.left - self.rect.width
                
                case "up":
                    if hits:
                        self.rect.y = hits[0].rect.bottom        

                case "down":
                    if hits:
                        self.rect.y = hits[0].rect.top - self.rect.height  


    def movement(self, walls_sprite_group, dt):
       # Randomly select a direction
            
            direction = random.choice(['left', 'right', 'up', 'down'])
            
            # Update the monster's position based on the selected direction
            if direction == 'left':
                self.rect.move_ip(-self.movement_speed * dt, 0) 
                self.collision("left", walls_sprite_group)
                
            elif direction == 'right':
                self.rect.move_ip(self.movement_speed * dt, 0)
                self.collision("right", walls_sprite_group)


            elif direction == 'up':
                self.rect.move_ip(0, -self.movement_speed  * dt)
                self.collision("up", walls_sprite_group)

            elif direction == 'down':
                self.rect.move_ip(0, self.movement_speed * dt) 
                self.collision("down", walls_sprite_group)

        
if __name__ == "__main__":
    game = Monster()
    game.run_game()
 
