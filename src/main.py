import pygame

from Player import Player

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
FPS = 60
fpsclock=pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(0,0)

run = True
while run:
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, player.colour, player.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:           
            if player.rect.collidepoint(pygame.mouse.get_pos()):
                player.changeColour()

    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_a]:
        player.rect.move_ip(-10,0)
    if key_input[pygame.K_d]:
        player.rect.move_ip(10,0)
    if key_input[pygame.K_w]:
        player.rect.move_ip(0,-10)
    if key_input[pygame.K_s]:
        player.rect.move_ip(0,10)

    pygame.display.update()
    fpsclock.tick(FPS)

pygame.quit()