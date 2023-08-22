import pygame
import csv



class Tile:

    TILE = "tile"
    WALL = "wall"
    FINISH = "finish"
    SPEED_BOOST = "speed_boost"

    def __init__(self, number, type, xPos, yPos):
        self.size = 50
        self.type = type
        self.number = number
        self.setTileInfo(number)
        self.rect = pygame.Rect((xPos, yPos, self.size, self.size))

    def setTileInfo(self, number):
        if number == 1:
            self.colour = (0, 0, 255)
        elif number == 2:
            self.colour = (0, 255, 0)
        elif number == 4:
            self.size = 10
            self.colour = (33, 33, 33)
        else:
            self.colour = (255, 255, 255)


class TileMap:
    def __init__(self, file_name):
        self.walls = []
        self.objects = []
        self.enemies = []
        self.file_path = "maps"
        self.tile_size = 50
        self.finished = False
        self.load(file_name)

    def load(self, file_name):
        with open(f"{self.file_path}/{file_name}", newline='') as csv_file:
            rows = csv.reader(csv_file, delimiter=',', quotechar='|')
            
            y_pos = 0
            for row in rows:
                x_pos = 0
                for col in row:
                    tile_number = int(col)
                    
                    if tile_number != 0:
                        tile_list, tile_text = self.getTileType(tile_number)
                        tile_list.append(Tile(tile_number, tile_text, x_pos, y_pos))

                    x_pos += self.tile_size
                y_pos += self.tile_size


    def getTileType(self, number):
        types = [
            (1, self.walls, "wall"),
            (2, self.objects, "finish"),
            (3, self.enemies, "enemy"),
            (4, self.objects, "speed_boost")]
        
        for type in types:
            num_tile, list_tile, text_tile = type

            if num_tile == number:
                return list_tile, text_tile

        return self.walls, "tile"


    def draw_walls(self, screen):
        for tile in self.walls:
            pygame.draw.rect(screen, tile.colour, tile.rect)


    def draw_objects(self, screen):
        for tile in self.objects:
            if tile.type != "finish" or self.objectiveFinished():
                pygame.draw.rect(screen, tile.colour, tile.rect)

    
    def draw(self, screen):
        self.draw_walls(screen)
        self.draw_objects(screen)
    

    def objectiveFinished(self):
        if self.finished:
            return True

        for object in self.objects:
            if object.type == "speed_boost":
                return False
        
        self.finished = True
        return True
