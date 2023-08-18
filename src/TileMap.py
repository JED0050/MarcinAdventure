import pygame
import csv



class Tile:
    def __init__(self, number, xPos, yPos):
        self.size = 50
        self.rect = pygame.Rect((xPos, yPos, self.size, self.size))

        self.setColour(number)

    def setColour(self, number):
        if number == 1:
            self.colour = (0, 0, 255)
        elif number == 2:
            self.colour = (0, 255, 0)
        else:
            self.colour = (255, 255, 255)


class TileMap:
    def __init__(self, file_name):
        self.walls = []
        self.objects = []
        self.file_path = "maps"
        self.tile_size = 50
        self.load(file_name)


    def load(self, file_name):
        with open(f"{self.file_path}/{file_name}", newline='') as csv_file:
            rows = csv.reader(csv_file, delimiter=',', quotechar='|')
            
            y_pos = 0
            for row in rows:
                x_pos = 0
                for col in row:
                    tile_number = int(col)
                    
                    
                    if tile_number == 1:
                        self.walls.append(Tile(tile_number, x_pos, y_pos))
                    elif tile_number == 2:
                        self.objects.append(Tile(tile_number, x_pos, y_pos))

                    x_pos += self.tile_size
                y_pos += self.tile_size


    def draw(self, screen):
        for tile in self.walls:
            pygame.draw.rect(screen, tile.colour, tile.rect)
        for tile in self.objects:
            pygame.draw.rect(screen, tile.colour, tile.rect)
