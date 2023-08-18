import pygame



def move_player(player_rect, walls, move_step):
    key_input = pygame.key.get_pressed()   
    if not (key_input[pygame.K_a] and key_input[pygame.K_d]):
        if key_input[pygame.K_a]:
            player_rect.move_ip(-move_step, 0)
            fix_wall_hits(player_rect, walls, "L")
        if key_input[pygame.K_d]:
            player_rect.move_ip(move_step, 0)
            fix_wall_hits(player_rect, walls, "R")
    if not (key_input[pygame.K_w] and key_input[pygame.K_s]):
        if key_input[pygame.K_w]:
            player_rect.move_ip(0, -move_step)
            fix_wall_hits(player_rect, walls, "U")
        if key_input[pygame.K_s]:
            player_rect.move_ip(0, move_step)
            fix_wall_hits(player_rect, walls, "B")

def fix_wall_hits(player_rect, tiles, direction):
    for tile in tiles:
        tile_rect = tile.rect
        collide = pygame.Rect.colliderect(player_rect, tile_rect)

        if collide:
            if direction == "R":
                player_rect.right = tile_rect.left
            elif direction == "L":
                player_rect.left = tile_rect.right
            elif direction == "U":
                player_rect.top = tile_rect.bottom
            elif direction == "B":
                player_rect.bottom = tile_rect.top
            return
