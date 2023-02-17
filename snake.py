import pygame
from constans import game
print(game.get("width"))
pygame.init()

screen = pygame.display.set_mode((game.get("width"), game.get("height")))