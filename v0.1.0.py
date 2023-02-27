import pygame

#语文1，数学2，英语3，科学4，社会5，音乐6，美术7，体育8
#y为横坐标,x为纵坐标
map=[
        [1,3,1,1,1,1,1,1,1,1,1,1,1,1,1],#
        [2,1,0,1,0,0,0,0,0,0,1,0,1,0,0],#
        [3,4,1,1,0,1,1,1,0,1,1,0,0,0,1],#
        [4,1,0,1,0,1,0,0,0,0,1,0,1,1,1],#
        [5,5,0,0,0,1,1,1,1,0,0,0,1,1,1],#
        [6,6,1,1,1,1,1,1,1,1,1,1,1,1,1],#
        [7,5,0,0,0,1,1,1,1,0,0,0,1,1,1],#
        [8,7,0,0,0,1,1,1,1,0,0,0,1,1,1] #
    ]
print("今日课程表如下:")
for i in range(6):
    print(map[i])
x=0
y=0#设置第一天的起始点
passMusic=None
knockMusic=None #加载变量
def move_s():#如果输入s，解析课程表
    global map,x,y,passMusic,knockMusic
    if map[x][y]==1:
        print("语文课")
        x+=1
        passMusic.play()
    elif map[x][y]==2:
        print("数学课")
        x+=1
        passMusic.play()
    elif map[x][y]==3:
        print("英语课")
        x+=1
        passMusic.play()
    elif map[x][y]==4:
        print("科学课")
        x+=1
        passMusic.play()
    elif map[x][y]==5:
        print("社会课")
        x+=1
        passMusic.play()
    elif map[x][y]==6:
        print("音乐课")
        x+=1
        passMusic.play()
    elif map[x][y]==7:
        print("美术课")
        x+=1
        passMusic.play()
    elif map[x][y]==8:
        print("体育课")
        x+=1
        passMusic.play()
    else:
        print("课程表数据错误，请检查课程表第",x+1,"行",y+1,"列",sep="")#系统报错
        knockMusic.play()
        x+=1
    print("x:",x,"y:",y)
    if x==6:
        print("恭喜，今天放学了")
        x=0
        y+=1#返回至下一天
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

def main(): #显示设置
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
                if event.key==pygame.K_s: 
                    move_s()
                print("x:",x,"y:",y)
        screen.blit(background,(0,0))
        if x==7:
            print("\n恭喜，放学了！！！！！")
            break
        # if pygame.mixer.music.get_busy()==False:
        #     pygame.mixer.music.play()
        pygame.display.update()
    pygame.quit()
if  __name__ == "__main__":
    main()