import pygame
import random

class Player:
    def __init__(self, xPos, yPos):
        self.rect = pygame.Rect((xPos,yPos,50,50))
        self.colour = (255, 0, 0)
    
    def changeColour(self):
        self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
