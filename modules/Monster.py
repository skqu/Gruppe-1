import pygame
import random

import time

class Monster:
    def __init__(self, screen, screen_x, screen_y):
      
        # Initialize Pygame
        pygame.init()


        # Screen dimensions
        self.screen_width = screen_x
        self.screen_height = screen_y

        # Create the screen
        #self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen = screen
        #pygame.display.set_caption("Monster Moving")

        # Load the original image
        original_image = pygame.image.load("Graphics\characters\monster.png")

        # Define the desired width and height for the resized image
        desired_width = 85
        desired_height = 55

        # Resize the image
        self.resized_image = pygame.transform.scale(original_image, (desired_width, desired_height))
        pygame.image.save(self.resized_image, "monster3.png")

        # Load the monster image
        self.monster_image = pygame.image.load("monster3.png")
        self.monster_rect = self.monster_image.get_rect()

 

        # Monster starting position
        self.monster_x = random.randint(0, self.screen_width - self.monster_rect.width)
        self.monster_y = random.randint(0, self.screen_height - self.monster_rect.height)

        #self.monster_x = 0
        #self.monster_y = 0

        # Set the maximum number of steps for each direction
        self.max_steps = 1  # Adjust this value as needed



        #self.rect = self.resized_image.get_rect()
        #self.rect.center = [self.monster_x, self.monster_y]


        # Initialize step counters
        self.left_steps = 0
        self.right_steps = 0
        self.up_steps = 0
        self.down_steps = 0

        # Create a clock to control the frame rate
        self.clock = pygame.time.Clock()


        #Movement speed
        self.movement_speed = 5000


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
    
    def draw(self):
         #self.movement()
         return self.resized_image, self.monster_rect


    def collision(self, direction, sprite_group): #Check if player is colliding with walls
        if pygame.sprite.spritecollide(self, sprite_group, False): 
            
            hits = pygame.sprite.spritecollide(self, sprite_group, False) #Get the sprites the player is colliding with
            match direction:
                case "left":
                        if hits:
                            self.monster_rect.x = hits[0].monster_rect.right 
                case "right":
                    if hits:
                        self.monster_rect.x = hits[0].rect.left - self.monster_rect.width
                
                case "up":
                    if hits:
                        self.monster_rect.y = hits[0].monster_rect.bottom        

                case "down":
                    if hits:
                        self.monster_rect.y = hits[0].monster_rect.top - self.monster_rect.height  



    def movement(self, walls_sprite_group, dt):
       # Randomly select a direction
            
            direction = random.choice(['left', 'right', 'up', 'down'])
            print(direction)
            # Update the monster's position based on the selected direction and step count
            if direction == 'left' and self.left_steps < self.max_steps:
                self.monster_x -= self.movement_speed * dt # Move left
                self.left_steps += 1
                #self.collision("left", walls_sprite_group)
                
            elif direction == 'right' and self.right_steps < self.max_steps:
                self.monster_x += self.movement_speed * dt # Move right
                self.right_steps += 1
               # self.collision("right", walls_sprite_group)

            elif direction == 'up' and self.up_steps < self.max_steps:
                self.monster_y -= self.movement_speed * dt # Move up
                self.up_steps += 1
                #self.collision("left", walls_sprite_group)

            elif direction == 'down' and self.down_steps < self.max_steps:
                self.monster_y += self.movement_speed * dt # Move down
                self.down_steps += 1
                #self.collision("left", walls_sprite_group)


            # Reset step counters when the maximum number of steps is reached
            if self.left_steps == self.max_steps:
                self.left_steps = 0
            if self.right_steps == self.max_steps:
                self.right_steps = 0
            if self.up_steps == self.max_steps:
                self.up_steps = 0
            if self.down_steps == self.max_steps:
                self.down_steps = 0

            # Ensure the monster stays within the screen boundaries
            self.monster_rect.x = max(0, min(self.screen_width - self.monster_rect.width, self.monster_x))
            self.monster_rect.y = max(0, min(self.screen_height - self.monster_rect.height, self.monster_y)) 

            

    
    # def run_game(self):
        
     
    #         self.screen.fill((0, 0, 0))
    #         self.screen.blit(self.monster_image, (self.monster_x, self.monster_y))
    #         pygame.display.update()

    #         self.clock.tick(2)  # Limit the frame rate per second

    #     pygame.quit()

if __name__ == "__main__":
    game = Monster()
    game.run_game()
 
