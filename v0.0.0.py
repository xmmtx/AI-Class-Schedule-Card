#语文1，数学2，英语3，科学4，社会5，音乐6，美术7，体育8
#y为横坐标,x为纵坐标
map=[
        [1,3,1,1,1,1,1,1,1,1,1,1,1,1,1],#
        [0,1,0,1,0,0,0,0,0,0,1,0,1,0,0],#
        [3,4,1,1,0,1,1,1,0,1,1,0,0,0,1],#
        [4,1,0,1,0,1,0,0,0,0,1,0,1,1,1],#
        [5,5,0,0,0,1,1,1,1,0,0,0,1,1,1],#
        [6,9,1,1,1,1,1,1,1,1,1,1,1,1,1],#
        [7,5,0,0,0,1,1,1,1,0,0,0,1,1,1],#
        [8,7,0,0,0,1,1,1,1,0,0,0,1,1,1] #
    ]
print("今日课程表如下:")
for i in range(6):
    print(map[i])
x=0
y=0
while True:
    s=input("输入s以表示下节课：")
    if s=='s':#如果输入s，解析课程表
        if map[x][y]==1:
            print("语文课")
            x+=1
        elif map[x][y]==2:
            print("数学课")
            x+=1
        elif map[x][y]==3:
            print("英语课")
            x+=1
        elif map[x][y]==4:
            print("科学课")
            x+=1
        elif map[x][y]==5:
            print("社会课")
            x+=1
        elif map[x][y]==6:
            print("音乐课")
            x+=1
        elif map[x][y]==7:
            print("美术课")
            x+=1
        elif map[x][y]==8:
            print("体育课")
            x+=1
        else:
            print("课程表数据错误，请检查课程表第",x+1,"行",y+1,"列",sep="")#系统报错
    print("x:",x,"y:",y)
    if x==6:
        print("恭喜，今天放学了")
        x=0
        y+=1#返回至下一天