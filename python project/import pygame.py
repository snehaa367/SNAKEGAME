import pygame
import random
from pygame.locals import *

pygame.init() 
 
width , height = 700,700
WIN = pygame.display.set_mode((width , height)) 
pygame.display.set_caption("First Game") 
 
#colours 
green = (0,66,37) 
white = (255, 255 , 255) 
red = (255 , 0 , 0) 
blue =(0,0,255)

#scoring
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
state = False
run=True
 
#snake variables  
snake_size = 20 
snake_speed = 15 
snake = [(height//2,width//2),(height//2 +20,height//2 + 20)] 
snake_direction = (0,0) 
 
# food variables 
food_size = 20 
food =[random.randrange(0, width - food_size, food_size), random.randrange(0, height - food_size, food_size)]

def renderScore():
    global score,font
    text = font.render(str(score), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (300, 30)
    WIN.blit(text,textRect)

def changeFood():
    global food
    food[0] = random.randrange(0, width - food_size, food_size)
    food[1] = random.randrange(0, height - food_size, food_size)

def appendSnake():
    global snake
    snake.append((snake[-1][0]+20,snake[-1][1]+20))

def snakeColide(appleRect,snakeRect): 
    global score, snake,run,state
    if (((snake[0] in snake[1::]) or (snake[0][0] not in range(0,width) ) or (snake[0][0] not in range(0,height))) and state):
        run=False
        
    elif pygame.Rect.colliderect(appleRect,snakeRect):
        appendSnake()
        score+=1
        changeFood()
def spawnApple(): 
    global food , food_size 
    pygame.draw.rect(WIN,red,(food[0],food[1],food_size,food_size)) 
    foodRect = Rect(food[0],food[1],food_size,food_size)
    return foodRect
 
def positionSnake(snake_direction): 
    global snake,snake_size 
    snake=snake[::-1] 
    for i in range(len(snake)-1): 
        snake[i]=snake[i+1] 
    snake=snake[::-1] 
    snake[0] = (snake[0][0]+snake_direction[0]*snake_size,snake[0][1]+snake_direction[1]*snake_size) 
    return snake
     
def createSnake(snake_direction): 
    snakeCord = positionSnake(snake_direction) 
    for segment in snake: 
        pygame.draw.rect(WIN,white,(segment[0],segment[1],snake_size,snake_size))
    snakeRect = Rect(snakeCord[0][0],snakeCord[0][1],snake_size,snake_size)
    return snakeRect
    
    
def displayScreen(snake_direction): 
    global WIN 
    WIN.fill(green)
    snake = createSnake(snake_direction)
    apple = spawnApple()
    snakeColide(apple,snake)
    renderScore()
    pygame.display.flip()
 
def main(): 
    global snake_direction ,run,state
 
    while run: 
        pygame.time.Clock().tick(snake_speed) 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP and snake_direction != (0,1): 
                    snake_direction = (0,-1) 
                    state=True
                elif event.key == pygame.K_DOWN and snake_direction != (0,-1): 
                    snake_direction = (0,1)
                    state=True
                elif event.key == pygame.K_LEFT and snake_direction != (1,0): 
                    snake_direction = (-1,0)
                    state=True
                elif event.key == pygame.K_RIGHT and snake_direction != (-1,0): 
                 snake_direction = (1,0)
                 state=True
    
        displayScreen(snake_direction)
        
main()