import pygame


class Sprite(pygame.sprite.Sprite): 
	def __init__(self,pos,surf,groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)

        
        
class Monster(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image_width = 80 
        self.image_height = 80
        self.hero_image = pygame.image.load("./Graphics\characters\monster.png")
        self.resized_image = pygame.transform.scale(self.hero_image, (self.image_width, self.image_height))
        self.rect = self.resized_image.get_rect()
        self.rect.center = [pos_x, pos_y]


        self.movement_speed = 400

 

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

        
    
           
    def movement(self, key, walls_sprite_group, dt):
        pass
        
        
    def draw(self): 
        return self.resized_image, self.rect



 