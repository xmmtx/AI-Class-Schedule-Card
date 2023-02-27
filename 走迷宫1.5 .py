import pygame

map=[
        [1,1,1,1,1,1,1,1,1,1,1],
        [1,2,0,1,0,0,0,0,0,0,1],
        [1,0,1,1,0,1,1,1,0,1,1],
        [1,0,0,1,0,1,0,0,0,0,1],
        [1,1,0,0,0,1,1,1,1,0,0],
        [1,1,1,1,1,1,1,1,1,1,1]
    ]
map2=[
        [1,1,1,1,1,1,1,0,1,1,1],
        [1,0,1,0,1,2,1,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,0,1],
        [1,1,0,1,1,1,1,0,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1]
    ]
map3=[
        [1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,1,0,1,0,1,1],
        [1,0,1,0,0,1,0,0,0,0,1],
        [1,0,0,1,0,0,0,1,0,1,1],
        [1,1,0,0,1,1,0,1,0,2,1],
        [1,1,1,0,1,1,1,1,1,1,1]
    ]
loc=[[1,1],[1,5],[4,9]]
guanka=[[4,10],[0,7],[5,3]]
m=len(map)
m1=len(map[0])
x=loc[0][0]
y=loc[0][1]
x2=guanka[0][0]
y2=guanka[0][1]
n=0
passMusic=None
knockMusic=None
def move_left():
    global map,x,y
    global passMusic,knockMusic
    if map[x][y-1]!=1:
        map[x][y]=0
        y-=1
        map[x][y]=2
        passMusic.play()
    else:
        knockMusic.play()
def move_right():
    global map,x,y
    if map[x][y+1]!=1:
        map[x][y]=0
        y+=1
        map[x][y]=2
        passMusic.play()
    else:
        knockMusic.play()
def move_up():
    global map,x,y
    if map[x-1][y]!=1:
        map[x][y]=0
        x-=1
        map[x][y]=2
        passMusic.play()
    else:
        knockMusic.play()
def move_down():
    global map,x,y
    if map[x+1][y]!=1:
        map[x][y]=0
        x+=1
        map[x][y]=2
        passMusic.play()
    else:
        knockMusic.play()
def gameOver(screen_temp,t):
    bgRedlmg=pygame.image.load("./images/指示墙2.png")   
    bgRedlmg=pygame.transform.scale(bgRedlmg,(320,350))
    screen_temp.blit(bgRedlmg,(360-160,100))
    successlmg=pygame.image.load("./images/恭喜通关1.png")   
    successlmg=pygame.transform.scale(successlmg,(172,78))
    screen_temp.blit(successlmg,(360-85,150))
    nextGuanKalmg=pygame.image.load("./images/下一关1.png")   
    nextGuanKalmg=pygame.transform.scale(nextGuanKalmg,(172,78))
    screen_temp.blit(nextGuanKalmg,(360-85,240))
    gameOverlmg=pygame.image.load("./images/游戏结束1.png")   
    gameOverlmg=pygame.transform.scale(gameOverlmg,(172,78))
    screen_temp.blit(gameOverlmg,(360-85,330))
    pygame.display.update()
    mousedown=False
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousedown=True
            if event.type==pygame.MOUSEBUTTONUP:
                mousedown=False
        if mousedown==True:
            spot=pygame.mouse.get_pos()
            x2=spot[0]
            y2=spot[1]
            if x2>=360-85 and x2<=360-85+172 and y2>=240 and y2<=240+78:
                t=t+1
                print('进入下一关！')
                return t
            if x2>=360-85 and x2<=360-85+172 and y2>=330 and y2<=330+78:
                print('游戏结束！')
                return -1
def main():
    global map,x,y
    global passMusic,knockMusic
    global m,m1,n
    global x2,y2
    pygame.init()
    screen = pygame.display.set_mode((720,500)) 
    background = pygame.image.load("./images/背景3.jpg") 
    w=50
    h=50
    background=pygame.transform.scale(background,(720,500))
    background = pygame.image.load("./images/背景3.jpg")  
    background=pygame.transform.scale(background,(720,500))
    bgmg = pygame.image.load("./images/墙4.jpg")   #可以1~5，建议4
    bgmg=pygame.transform.scale(bgmg,(w,h))
    td = pygame.image.load("./images/通道1.jpg")   
    td=pygame.transform.scale(td,(w,h))
    mouse = pygame.image.load("./images/人物2.jpg")    
    mouse=pygame.transform.scale(mouse,(w,h))
    passMusic=pygame.mixer.Sound('./music/正确1.wav')
    knockMusic=pygame.mixer.Sound('./music/错误1.wav')
    pygame.mixer.init()
    pygame.mixer.music.load('./music/迷宫配乐1.mp3') #可以1~5
    while True:
        for event in pygame.event.get():   
            if event.type==pygame.QUIT: 
                exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT: 
                    move_left()
                elif event.key==pygame.K_RIGHT: 
                    move_right()
                elif event.key==pygame.K_UP: 
                    move_up()
                elif event.key==pygame.K_DOWN: 
                    move_down()
                print("x:",x,"y:",y)
        screen.blit(background,(0,0))
        for x1 in range(m):
            for y1 in range(m1):
                if map[x1][y1]==1:
                    screen.blit(bgmg,(100+y1*w,100+x1*h))
                elif map[x1][y1]==0:
                    screen.blit(td,(100+y1*w,100+x1*h))
                else:
                    screen.blit(mouse,(100+y1*w,100+x1*h))
        if x==x2 and y==y2:
            n=gameOver(screen,n)
            if n==3:
                print('通关了！')
                break
            if n==-1:
                print('游戏结束了！')
                break
            if n==1:
                map=map2
            elif n==2:
                map=map3
            x=loc[n][0]
            y=loc[n][1]
            x2=guanka[n][0]
            y2=guanka[n][1]
            m=len(map)
            m1=len(map[0])     
        if x==4 and y==10:
            print("\n恭喜，你走出了迷宫")
            break
        if pygame.mixer.music.get_busy()==False:
            pygame.mixer.music.play()
        pygame.display.update()
    pygame.quit()
if  __name__ == "__main__":
    main()