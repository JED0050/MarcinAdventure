import pygame



def move_player(player_rect, walls, move_step):
    key_input = pygame.key.get_pressed()   
    if not ((key_input[pygame.K_a] or key_input[pygame.K_LEFT]) and (key_input[pygame.K_d] or key_input[pygame.K_RIGHT])):
        if key_input[pygame.K_a] or key_input[pygame.K_LEFT]:
            player_rect.move_ip(-move_step, 0)
            fix_wall_hits(player_rect, walls, "L")
        elif key_input[pygame.K_d] or key_input[pygame.K_RIGHT]:
            player_rect.move_ip(move_step, 0)
            fix_wall_hits(player_rect, walls, "R")
    if not ((key_input[pygame.K_w] or key_input[pygame.K_UP]) and (key_input[pygame.K_s] or key_input[pygame.K_DOWN])):
        if key_input[pygame.K_w] or key_input[pygame.K_UP]:
            player_rect.move_ip(0, -move_step)
            fix_wall_hits(player_rect, walls, "U")
        if key_input[pygame.K_s] or key_input[pygame.K_DOWN]:
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
