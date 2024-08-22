import pygame, time, math, os

pygame.init() #초기화

SCREEN_HIGH = 800
SCREEN_WIDTH =700
Screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGH))

pygame.display.set_caption("볼")
Clock = pygame.time.Clock()

BLUE = (0,0,255)
WHITE = (0,0,0)

ball_x = int(SCREEN_WIDTH/2)
ball_y = int(SCREEN_HIGH/2)
ball_dx=4
ball_dy=4
ball_size = 40

running = True
#Update


while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_dx
    ball_y += ball_dy

    if (ball_y - ball_size)<=0 or (ball_y+ball_size) >= SCREEN_HIGH:
        ball_dy = ball_dy*-1

    if (ball_x - ball_size)<=0 or (ball_x+ball_size) >= SCREEN_WIDTH:
        ball_dx = ball_dx*-1

    Screen.fill(WHITE)

    pygame.draw.circle(Screen,BLUE,[ball_x,ball_y],ball_size,0)

    pygame.display.flip()
    Clock.tick(60)
        
pygame.quit()