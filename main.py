import pygame
from constans import game
from snake import Snake
print(game.get("width"))
pygame.init()

screen = pygame.display.set_mode((game.get("width"), game.get("height")))

pygame.display.set_caption("Snake")

run = True
snake = Snake()
width = 20
print(snake.body[0])
height = 20


while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            snake.move()
        
    screen.fill((255, 255, 255))
    for body in snake.body:
        # print("{} - {}".format(body.pos[0], body.pos[1]))
        pygame.draw.rect(screen, (255, 200, 100), (body.pos[0], body.pos[1], width, height))

    snake.constantMove()
    
    # for i in range(len(snake.body)):
    #     pygame.draw.rect(screen, (255, 200, 100), (snake.position_x - i * width, snake.position_y, width, height))
    pygame.display.update()
pygame.quit()
    