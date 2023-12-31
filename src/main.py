import pygame

from Player import Player
from TileMap import TileMap
from Movement import *

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

fpsclock=pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_speed = 2
player = Player(100, 100)

file_name = "level_1.csv"
tile_map = TileMap(file_name)
#tile_map.draw_walls(screen)

run = True
while run:
    
    screen.fill((255,255,102))

    tile_map.draw(screen)

    pygame.draw.rect(screen, player.colour, player.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:           
            if player.rect.collidepoint(pygame.mouse.get_pos()):
                player.changeColour()

    move_player(player.rect, tile_map.walls, player_speed)

    for object in tile_map.objects:
        if pygame.Rect.colliderect(player.rect, object.rect):
            if object.type == "finish" and tile_map.objectiveFinished():
                run = False
                break
            elif object.type == "speed_boost":
                player_speed += 2
                tile_map.objects.remove(object)

    pygame.display.update()
    fpsclock.tick(FPS)

pygame.quit()