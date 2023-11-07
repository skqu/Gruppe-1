import pygame
from pytmx.util_pygame import load_pygame
from os.path import dirname, join



#from main import Game


class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,surf,groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)

        


class Level():
    def __init__(self):
        pass

    
    def lvl_manager(self, lvl):
        match lvl:
            case "1":
                return self.create_lvl('lvlData/test_Lvl.tmx')
            case "2":
                return self.create_lvl('lvlData/test_Lvl2.tmx')


    def create_lvl(self, lvlData):
        tmx_data = load_pygame(lvlData)
        lvl_sprite_group = pygame.sprite.Group()
    
        tile_size = 64

        for layer in tmx_data.visible_layers:
            if hasattr(layer, "data"):
                
                for x,y,surf in layer.tiles():
                        print(surf)
                        surf2 = pygame.transform.scale(surf, (tile_size, tile_size))
                        pos = (x * tile_size, y * tile_size)
                        Tile(pos = pos, surf = surf2, groups = lvl_sprite_group)
        
        return lvl_sprite_group







    















# tmx_data = load_pygame('Projeckt2/lvlData/test_Lvl.tmx')
# sprite_group = pygame.sprite.Group()

# for layer in tmx_data.visible_layers:
#      if hasattr(layer, "data"):
#           for x,y,surf in layer.tiles():
                
#                 surf2 = pygame.transform.scale(surf, (64, 64))


#                 pos = (x * 64, y * 64)
#                 tile = Tile(pos = pos, surf = surf2, groups = sprite_group)
                



 



# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

    


    
#     sprite_group.draw(screen)







#     pygame.display.update()
    








# class level():
#     def __init__(self):
#         pass


