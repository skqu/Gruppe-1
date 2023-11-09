import pygame


class Sprite(pygame.sprite.Sprite): 
	def __init__(self,pos,surf,groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)

        
        
class Hero(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image_width = 80 
        self.image_height = 80
        self.hero_image = pygame.image.load("./Graphics/characters/hero.png")
        self.resized_image = pygame.transform.scale(self.hero_image, (self.image_width, self.image_height))
        self.rect = self.resized_image.get_rect()
        self.rect.center = [pos_x, pos_y]


        self.movement_speed = 400
        self.health = 100
 

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

        
    
    def gui (self):
         pass

           
    def movement(self, key, walls_sprite_group, dt):
        


        if key[pygame.K_LEFT]:
            self.rect.move_ip(-self.movement_speed * dt, 0) 
            self.collision("left", walls_sprite_group)
        
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(self.movement_speed * dt, 0)
            self.collision("right", walls_sprite_group)

        if key[pygame.K_UP]:
            self.rect.move_ip(0, -self.movement_speed  * dt)
            self.collision("up", walls_sprite_group)

        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, self.movement_speed * dt) 
            self.collision("down", walls_sprite_group)

        
    def draw(self): 
        return self.resized_image, self.rect



 