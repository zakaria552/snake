import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame
from constans import game
pygame.init()
print(game.get("width"), game.get("height"))
screen = pygame.display.set_mode((game.get("width"), game.get("height")))