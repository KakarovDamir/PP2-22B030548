import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("PAINT")
bet = pygame.Surface((600,600))

prevx = -1
prevy = -1
currentx = -1
currenty = -1

color = (255,255,255)

Pen = 'pen'
rec = 'rec'
eraser = 'eraser'
circle = 'circle'

kol = 'rec'
fps = pygame.time.Clock()
font = pygame.font.Font(None,20)

def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculateCircle(x1,y1,x2,y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

screen.fill((0,0,0))
mouse = False
status = True
while status:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_1]:
        kol = Pen

    elif pressed[pygame.K_2]:
        kol = rec

    elif pressed[pygame.K_3]:
        kol = eraser

    elif pressed[pygame.K_c]:
        screen.fill((0,0,0))
        bet.fill((0,0,0))

    elif pressed[pygame.K_4]:
        kol = circle

    elif pressed[pygame.K_r]:
        color = (255,0,0)

    elif pressed[pygame.K_g]:
        color = (0,255,0)

    elif pressed[pygame.K_b]:
        color = (0,0,255)

    elif pressed[pygame.K_w]:
        color = (255,255,255)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mouse = True
                currentx =  event.pos[0]
                currenty =  event.pos[1]    
                prevx =  event.pos[0]
                prevy=  event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP:
            mouse = False
            bet.blit(screen, (0, 0))

        if event.type == pygame.MOUSEMOTION:
            if mouse:
                currentx = event.pos[0]
                currenty = event.pos[1]
        
        if kol == rec:
            if mouse and prevx != -1 and prevy != -1 and currentx != -1 and currenty != -1:
                screen.blit(bet, (0, 0))
                r = calculateRect(prevx, prevy, currentx, currenty)
                pygame.draw.rect(screen, color,pygame.Rect(r), 1)

        if kol == Pen:
            if mouse:
                pygame.draw.line(screen, color, (prevx, prevy), (currentx, currenty), 10)
            prevx = currentx
            prevy = currenty

        if kol == circle:
            if mouse:
                screen.blit(bet,(0,0))
                r = calculateRect(prevx, prevy, currentx, currenty)
                pygame.draw.circle(screen,color,(prevx,prevy), (abs(prevx - currentx))/2,1)

        if kol == eraser:
            if mouse:
                pygame.draw.circle(screen,(0,0,0), (currentx,currenty), 25)

        txt = font.render(kol,True,(255,255,255))
        screen.blit(txt,(0,0))

        pygame.display.flip()
        fps.tick(60)