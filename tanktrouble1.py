#import libraries
import pygame
#initilize pygame
pygame.init()
#define sprite images
right = pygame.image.load('right.png')
left = pygame.image.load('left.png')
up = pygame.image.load('up.png')
down = pygame.image.load('down.png')
direction = "right"
#set game window size and title
screen_width = 1500
screen_height = 800
win = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("TT1")
#tank class object seup
class tank(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
#redraw function for orienting sprites and redrawing
def  redrawGameWindow():
    global direction
    win.fill((0, 0, 0,))
    if direction == "left":
        win.blit(left, (tank.x, tank.y))
    elif direction == "right":
        win.blit(right, (tank.x, tank.y))
    elif direction == "up": 
        win.blit(up, (tank.x, tank.y))
    elif direction == "down":
        win.blit(down, (tank.x, tank.y))
    pygame.display.update()

#main loop
tank = tank(50, 50, 50, 50)
run = True
while run:
    pygame.time.delay(16)
    #quit upon x click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #checking for keypress
    keys = pygame.key.get_pressed()
    #moving tank and defining direction for orientation.
    if keys[pygame.K_LEFT] and tank.x > 0:
        tank.x -= tank.vel
        direction = "left"
    elif keys[pygame.K_RIGHT] and tank.x < screen_width - tank.width:
        tank.x += tank.vel
        direction = "right"
    elif keys[pygame.K_UP] and tank.y > 0:
        tank.y -= tank.vel
        direction = "up"
    elif keys[pygame.K_DOWN] and tank.y < screen_height - tank.height:
        tank.y += tank.vel
        direction = "down"
        
    redrawGameWindow()

pygame.quit()
