import pygame
import math
pygame.init()

wScreen = 1200
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))
pygame.display.set_caption("Projectile motion")


class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        def draw(self, win):
            pygame.draw.circle(win, (0,0,0), (self.x,self.y), self.radius)
            pygame.draw.circle(win, self.color, (self.x,self.y), self.radius-1)
        @staticmethod
        def ballpath(startx, starty, power, ang, time):
            pass

def redrawWindow():
    win.fill((64,64,64))
    golfBall.draw(win)
    pygame.display.update()



golfBall = ball(300, 494, 5, (255,255,255)) 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False

pygame.quit()