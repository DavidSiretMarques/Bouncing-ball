"""
Bouncing ball. Change the speed in line 12 to change its behaviour.
Use the keyboard keys + and - to speed up and down, and use the space key to stop the ball
"""
import sys, pygame


pygame.init()

#constants
width, height = pygame.display.get_desktop_sizes()[0]
speed = [1, 0]
eps = 1e-6
#set screen(window), load ball and put ball in screen
screen = pygame.display.set_mode()
ball = pygame.image.load("circle.png").convert_alpha()
ballrect = ball.get_rect()  #gets the measurements of the ball image
ballrect.center=(width/2,height/2)

#Put text
font = pygame.font.SysFont(None, 50)
while True:
    #Events for interacting with the game
    for event in pygame.event.get():
        #push the x or the esc button to exit
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] : sys.exit()
        #push buttons to do things
        if event.type == pygame.KEYDOWN:
           #plus to add speed 
           if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
               if speed[0]<0:
                   speed[0]-=0.1
               else:
                   speed[0]+=0.1
           #minus to substract it        
           if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
               if speed[0]<0:
                   speed[0]+=0.1
               else:
                   speed[0]-=0.1
            #space to pause
           if event.key == pygame.K_SPACE:
               if abs(speed[0])<eps:
                   speed[0]= v
               else:
                   v= speed[0]
                   speed[0]= 0
    #render text to show speed
    text = font.render(str(round(abs(speed[0]),2)),True,(0,0,0))
    #move the ball
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill((255,255,255))
    screen.blit(text,(10,10))
    screen.blit(ball, ballrect)
    pygame.display.flip()