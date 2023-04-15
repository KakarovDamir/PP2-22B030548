#Импортирование нужных библиотек
import pygame
import random

#Инициализация пайгейм
pygame.init()

#Даем значения высоты и ширины окна и обозначаем максимальный и текущий уровень
height = 400
width = 400
MAX_LEVEL = 3
level = 0

#Создаем окно с выше оказыннами знаечениями и даем название игры
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

#Эта функция нам понадобится позже для устоновки скорости
fps = pygame.time.Clock()

#Даем значение одного блока и скорости змеи
snake_block = 20
snake_speed = 5

#Устанавливем шрифт и размер текстов
font = pygame.font.Font(None,30)

#Cоздаем класс пойнт для дальнейшего удобства загружение координат
class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

#Этот класс будет отвечать за генерацию стен в игре по уровню
class Wall:
    #Эта функция инициялизирует уровень и открывет нам нужный файл, а так же все координаты стен закидывает в лист
    def __init__(self, level):
        self.level = level
        self.body = []
        f = open(f"level{self.level}.txt", "r")

        for y in range(0, height // snake_block + 1):
            for x in range(0, width // snake_block + 1):

                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    #Рисует стены по координатам
    def draw(self):
        for point in self.body:
            rect = pygame.Rect(snake_block * point.x, snake_block * point.y, snake_block, snake_block)
            pygame.draw.rect(screen, (226,135,67), rect)

#Эта функция отвечает за отоброжения текущего уровня и счета
def Score(score,level):
    value = font.render(f"SCORE: {score}",True,(255,255,255))
    screen.blit(value, (0,0))
    uroven = font.render(f'LEVEL: {level}', True,(255,255,255))
    screen.blit(uroven, (0,40))

#Эта функция отрисовывает змею на экране
def Snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0,255,0),(x[0], x[1], snake_block-1, snake_block-1))

#Эта функция выводит на экран текст который получает по указанным координатам 
def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [10, height // 3])

#Основная функция игры
def main():
    #Устанавливаем глобальные перемнные для дальнешего изменения или использования
    # переменная статус будет отвечать за цикл игры, клоус за рестарт, уолл генерацию стен
    global level , snake_speed
    status = True
    close = False
    wall = Wall(level)
    
    #устанавливаем центр координат(по этим координатам змея будет отображаться в начале игры)
    x1 = width // 2
    y1 = height // 2
    
    #эти переменные бедет отвечать за что как будет двигаться змея
    dx = 0
    dy = 0

    #Создаем лист для координат змеи и устанавливаем начальную длинну (ее будем исп. как счет в дальнешем)
    snake_list = []
    snake_length = 1

    #Даем координаты еды и проверяем ее на что не оказалось ли она в стене
    foodx = round(random.randrange(0, width - snake_block)/ 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block)/ 20.0) * 20.0
    for point in wall.body:
        if foodx == snake_block * point.x and foody == snake_block * point.y:
            foodx = round(random.randrange(0, width - snake_block)/ 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block)/ 20.0) * 20.0
        else:
            continue
    
    #Вот и цикл самой игры
    while status:
        #Если мы проиграли то блогодаря этому циклу можно заново начать играть
        while close == True:
            screen.fill((0,0,0))
            message("You Lost! Press C-Play Again or Q-Quit", (255,255,255))
            Score(snake_length - 1, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        status = False
                        close = False
                    if event.key == pygame.K_c:
                        main()
        
        #Цикл будет проверять на какую клавишу мы нажали и через условия она дает координаты как двигаться
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                status = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
            
                elif event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0

                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -snake_block
            
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = snake_block
        
        #условие проверяет не перешли ли мы границу
        if  x1 > width or x1 < 0 or y1 > height or y1 < 0:
            close = True

        #Ранее мы дали координаты как будет двигаться змея и сечас мы даем координаты для головы что бы она двигалась
        x1 += dx
        y1 += dy
        #Залеваем экран черным что бы у нас не остался след
        screen.fill((0,0,0))
        #Рисуем еду
        pygame.draw.rect(screen, (255,0,0), (foodx, foody, snake_block, snake_block))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        #Дали листу который будет отвечать за рисование тела змеи
        snake_list.append(snake_head)

        #Эта функция проверяет, если длина snake_list(текущая длина змеи) больше snake_length (желаемая длина змеи)
        #то функция del удаляет первый элемент из списка snake_list. Это что бы всегдаа сохр желаемою длинну змеи
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        #Проверяет коснулась ли она саму себя
        for x in snake_list[:-1]:
            if x == snake_head:
                close = True

        #через это условие меняем уровень и даем новую скорость
        if  (snake_length - 1) == 4:
            level = (level + 1) % MAX_LEVEL
            wall.__init__(level)
            wall.draw()
            snake_length = 1
            snake_list = []
            x1 = width // 2
            y1 = height // 2
            Snake(snake_block,snake_list)
            snake_speed += 2

        #вызываем все функции и обнавляем
        Snake(snake_block, snake_list)
        Grid()
        wall.draw()
        Score(snake_length - 1, level)

        pygame.display.update()

        #Проверяем сьела ли наша змея еди и если да то даем ей новую координату
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

            for point in wall.body:
                if foodx == snake_block * point.x and foody == snake_block * point.y:
                    foodx = round(random.randrange(0, width - snake_block)/ 20.0) * 20.0
                    foody = round(random.randrange(0, height - snake_block)/ 20.0) * 20.0
                else:
                    continue
            #Каждая сьетая еда +1 к счету
            snake_length += 1

        #Проверяем коснулась ли наша змея стен
        for point in wall.body:
            if x1 == snake_block * point.x and y1 == snake_block * point.y:
                close = True 

        if level == 0:
            snake_speed = 5

        #Скорость обнавления и скорость змеи
        fps.tick(snake_speed)
    
    #для завершения работы Pygame,
    pygame.quit()
    quit()

#рисуем сетку для удобства
def Grid():
    for x in range(0, width, snake_block):
        for y in range(0, height, snake_block):
            rect = pygame.Rect(x, y, snake_block, snake_block)
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)

#Вызываем функцию игры
main()