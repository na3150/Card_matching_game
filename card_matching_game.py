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
pos_x = [-210, -70,70, 210]
pos_y = [-250, -110, 30, 170]
