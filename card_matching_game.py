import turtle as t
import random
import time

t.bgcolor("white")
t.setup(700,700)
t.up()
t.ht()
t.goto(0, 280)
t.write("카드 매칭 게임", False, "center", ("",30,"bold"))

turtles = []
pos_x = [-210, -70, 70, 210]
pos_y = [-250, -110, 30, 170]

#x좌표 값 마다 모든 y좌표값의 위치로 turtle 이동
#각각의 x좌표 값 마다 y가 한번 씩 돌도록
for x in range(4):
    for y in range(4):
        new_turtle = t.Turtle()
        new_turtle.up()
        new_turtle.speed(0)
        new_turtle.color("white") #배경색과 동일한 하얀색으로
        new_turtle.goto(pos_x[x], pos_y[y])
        turtles.append(new_turtle)

default_img = "images/default_img.gif"
t.addshape(default_img) #배경 설정

img_list = []
for i in range(8):
    img = f"images/img{i}.gif"
    t.addshape(img)
    img_list.append(img)
    img_list.append(img) #같은 사진이 2번 들어가도록

random.shuffle(img_list) #랜덤으로 이미지 섞기
for i in range(16):
    turtles[i].shape(img_list[i])

time.sleep(3)

for i in range(16): #3초 후 default 이미지로 변경
    turtles[i].shape(default_img)

