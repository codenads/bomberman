import sys, pygame

pygame.init()

size = width, height = 640, 480
dx = 1
dy = 1
x= 163
y = 120
aquamarine = (127,255,212)
black = (0,0,0)

screen = pygame.display.set_mode(size)


while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x += dx
    y += dy

    if x < 0 or x > width:   
        dx = -dx

    if y < 0 or y > height:
        dy = -dy

    screen.fill(aquamarine)

    pygame.draw.circle(screen, black, (x,y), 8)
    
    pygame.draw.line(screen, black, [2,0], [10, 2], width)

    pygame.display.flip()   