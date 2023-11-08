import pygame
from pytmx.util_pygame import load_pygame
from modules.hero import Hero


class Tile(pygame.sprite.Sprite): #Cretes the tiles
	def __init__(self,pos,surf,groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)

        

class Level():
    def __init__(self, name, stage_nr, bg_color, hero_spawn = 0):
        self.str_name = name
        self.int_stage_nr = stage_nr
        self.lvlData = self.get_lvl_data(self.int_stage_nr)
        self.bg_color = bg_color
        self.hero_spawn = hero_spawn

        

        #Monsters in room


        
    def get_lvl_walls (self):
         return self.lvlData[1]

    def get_lvl_floor(self):
         return self.lvlData[0]  

    def get_lvl_data(self, lvl): #Determins what level to import
        
        path = f"lvlData/lvl_{lvl}.tmx"
        return self.create_lvl(path)


    def create_lvl(self, lvlData): # Creates the level from the level data and textures
        tmx_data = load_pygame(lvlData)
        lvl_walls_sprite_group = pygame.sprite.Group()
        lvl_floor_sprite_group = pygame.sprite.Group()

        tile_size = 64

        for layer in tmx_data.visible_layers:
            if hasattr(layer, "data"):
                for x,y,surf in layer.tiles():
                        surf2 = pygame.transform.scale(surf, (tile_size, tile_size))
                        pos = (x * tile_size, y * tile_size)
                        if layer.name in ('Floor'):
                            Tile(pos = pos, surf = surf2, groups = lvl_floor_sprite_group)
                        elif layer.name in ('Walls'):
                            Tile(pos = pos, surf = surf2, groups = lvl_walls_sprite_group)

        return lvl_floor_sprite_group, lvl_walls_sprite_group





