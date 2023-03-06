import pygame
from constans import game
width = 20
height = 20
screen = pygame.display.set_mode((game.get("width"), game.get("height")))

class Cube:
    def __init__(self, pos):
        # self.dirx = dirx
        # self.diry = diry
        self.pos = pos
class Snake:
    body = []
    speed = 10
    turns = []
    def __init__(self):
        self.dirx = 1
        self.diry = 0
        self.head = Cube([50,50])
        self.body.append(self.head)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.turns.append(self.body[0].pos)
            self.dirx = -1
            self.diry = 0
        elif keys[pygame.K_RIGHT]:
            self.turns.append(self.body[0].pos)
            self.dirx = 1
            self.diry = 0
            # [x,y]
            print("x:{}, y:{}".format(self.body[-1].pos[0],self.body[-1].pos[1]))
            cube = Cube([self.body[-1].pos[0] - self.speed, self.body[-1].pos[1]])
            print(str(cube.pos))
            self.body.append(cube)
        elif keys[pygame.K_UP]:
            self.turns.append(self.body[0].pos)
            self.dirx = 0
            self.diry = -1
        elif keys[pygame.K_DOWN]:
            self.turns.append(self.body[0].pos)
            self.dirx = 0
            self.diry = 1
        print(self.body)
        for i, body in enumerate(self.body):
            if body.pos == self.turns[0]:
                # print("before {}".format(body.pos))
                body.pos[0] += self.dirx * self.speed
                body.pos[1] += self.diry * self.speed
                # print("after {}".format(body.pos))
            else:
                body.pos[0] += self.speed

                # self.body.diry[1] += self.diry * self.speed
            if i == len(self.body):
                self.body.remove(self.body[0])
    def constantMove(self):
        for i, body in enumerate(self.body):
            body.pos[0] += self.dirx * self.speed
            body.pos[1] += self.diry * self.speed

    


