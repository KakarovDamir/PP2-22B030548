import pygame


pygame.init()

songs = ["Naruto.mp3", "JCole.mp3", "LilUziVert.mp3"]
index_num = 0
volume = 0.5
st = pygame.mixer.Sound(songs[index_num])


pygame.display.set_caption('DAMIRFY')
screen = pygame.display.set_mode((500,300))
mp3 = pygame.image.load(r"mp3files\haha.jpg")
mp3 = pygame.transform.scale(mp3,(500,300))
ps = pygame.image.load(r"mp3files\fff.jpg")
ps = pygame.transform.scale(ps,(40,40))


font = pygame.font.Font(None,30)
font2 = pygame.font.Font(None,20)
txt = font.render(f'{songs[index_num]}',True,(0,0,0))
txt_rect = txt.get_rect()
txt_rect.x = 200
txt_rect.y = 220


trt = font2.render("stop(play): SPACE, next: RIGHT, previous: LEFT", True, (0,0,0))
trt_rect = trt.get_rect()
trt_rect.x = 0
trt_rect.y = 0

st.play()
pygame.mixer.music.set_volume(volume)
pause = False
status = True
while status:
    screen.fill((255,255,255))
    screen.blit(mp3,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause = not pause

    pressed = pygame.key.get_pressed()
    if pause: 
        pygame.mixer.pause()
        screen.blit(ps,(230,85))
            

    else: pygame.mixer.unpause()

    if pressed[pygame.K_RIGHT]:
        st.stop()
        index_num = (index_num + 1) % len(songs)
        st = pygame.mixer.Sound(songs[index_num])
        st.play()

        txt = font.render(f'{songs[index_num]}',True,(0,0,0))
        txt_rect = txt.get_rect()
        txt_rect.x = 200
        txt_rect.y = 220

    elif pressed[pygame.K_LEFT]:
        st.stop()
        index_num = (index_num - 1) % len(songs)
        st = pygame.mixer.Sound(songs[index_num])
        st.play()
        txt = font.render(f'{songs[index_num]}',True,(0,0,0))
        txt_rect = txt.get_rect()
        txt_rect.x = 200
        txt_rect.y = 220

    elif pressed[pygame.K_UP]:
        volume = volume + 1
        st.set_volume(volume)

    elif pressed[pygame.K_DOWN]:
        volume = volume - 1
        st.set_volume(volume)

    screen.blit(txt, txt_rect)
    screen.blit(trt,trt_rect)
    pygame.display.update()