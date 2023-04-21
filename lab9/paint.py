import pygame,math
#инициализация, создаем полигон и окошко для игры
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("PAINT")
bet = pygame.Surface((600,600))
#начальная позиция мыши
prevx = -1
prevy = -1
currentx = -1
currenty = -1

color = (255,255,255)

#переменные для каждой фигуры
Pen = 'pen'
rec = 'rec'
eraser = 'eraser'
circle = 'circle'
square = 'square'
equilat = "equilit"
rhomb = "rhomb"
right = 'right'


kol = 'rec'
fps = pygame.time.Clock()
font = pygame.font.Font(None,20)
#для удобства создаем для каждой фигуры функций для расчета
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def squaree(x1,y1,x2,y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(x1 - x2))

def calculateCircle(x1,y1,x2,y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw(x1,y1,x2,y2):
        # calculating length of side
        side_len = math.pow((x2-x1)**2 + (y2-y1)**2, 0.5)
        
        # calculating vertices
        vertex_1 = (x1, y1)
        vertex_2 = (x2, y2)
        vertex_3 = (x2 + side_len, y2)
        vertex_4 = (x1 + side_len, y1)
        vertices = [vertex_1, vertex_2, vertex_3, vertex_4]

        # Drawing rhombus (square but corners are not only 90 degrees)
        pygame.draw.polygon(screen,color, vertices, width = 5)

def draw2(x1,y1,x2,y2):
        # calculating width(bottom side) of triangle
        w = (x2 - x1) *2

        # calculating vertices
        vertex_1 = (x1, y1)
        vertex_2 = (x2, y2)
        vertex_3 = (x2-w, y2)
        vertices = [vertex_1, vertex_2, vertex_3]

        # Drawing equilateral triangle
        pygame.draw.polygon(screen,color, vertices, width = 5)


def draw3(x1,y1,x2):

        side_len = x2-x1                      # calculating length of side
        h = math.pow(side_len**2 * 0.75, 0.5) # calculating height

        if side_len < 0: h *= -1              # to draw inverted triangle
        
        # calculating vertices
        vertex_1 = (x1, y1)
        vertex_2 = (x2, y1)
        vertex_3 = (x1 + side_len/2, y1 - h)
        vertices = [vertex_1, vertex_2, vertex_3]

        # Drawing right triangle
        pygame.draw.polygon(screen,color, vertices, width = 1)

screen.fill((0,0,0))
mouse = False
status = True
while status:
    #определяем какая переменная 
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

    elif pressed[pygame.K_5]:
        kol = square

    elif pressed[pygame.K_6]:
        kol = equilat

    elif pressed[pygame.K_7]:
        kol = rhomb

    elif pressed[pygame.K_8]:
        kol = right

    elif pressed[pygame.K_r]:
        color = (255,0,0)

    elif pressed[pygame.K_g]:
        color = (0,255,0)

    elif pressed[pygame.K_b]:
        color = (0,0,255)

    elif pressed[pygame.K_w]:
        color = (255,255,255)

    #Определение координат мыши
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
        
        #И рисуем фигуру которую выбрали
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

        if kol == square:
            if mouse:
                screen.blit(bet, (0, 0))
                r = squaree(prevx, prevy, currentx, currenty)
                pygame.draw.rect(screen, color,pygame.Rect(r), 1)

        if kol == rhomb:
            if mouse:
                screen.blit(bet,(0,0))
                draw(prevx, prevy, currentx, currenty)

        if kol == equilat:
            if mouse:
                screen.blit(bet,(0,0))
                draw2(prevx, prevy, currentx, currenty)

        if kol == right:
            if mouse:
                screen.blit(bet,(0,0))
                draw3(prevx, prevy, currentx)


        #вставляем текущий текст и обн экран
        txt = font.render(kol,True,(255,255,255))
        screen.blit(txt,(0,0))

        pygame.display.flip()
        fps.tick(60)