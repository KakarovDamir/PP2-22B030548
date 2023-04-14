import pygame

pygame.init()

w, h = 500, 500
pygame.display.set_caption('circle')
screen = pygame.display.set_mode((w, h))
x, y  = w // 2,h // 2
color = (255,0,0)
clock = pygame.time.Clock()

status = True
while status:
    
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y <= 30: continue
        else: y -= 20

    if pressed[pygame.K_DOWN]:
        if y >= h - 30: continue
        else: y += 20

    if pressed[pygame.K_RIGHT]:
        if x >= w - 30: continue
        else: x += 20
    
    if pressed[pygame.K_LEFT]:
        if x <= 30: continue
        else: x -= 20

    pygame.draw.circle(screen, color, (x, y), 25)
    pygame.display.flip()
    clock.tick(20)