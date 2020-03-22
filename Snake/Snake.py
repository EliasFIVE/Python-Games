# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:06:38 2019
Python 3.7.3

@author: ElisFIVE
based on  Python Game Programming Tutorial: Snake/Wormy Game by Christian Thompson
https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg

Changelog:

"""

import turtle
import time

delay = 0.2

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "left"

#F Functions
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_right():
    head.direction = "right"
def go_left():
    head.direction = "left"

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction =="down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction =="right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction =="left":
        x = head.xcor()
        head.setx(x - 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")  
wn.onkeypress(go_down, "s") 
wn.onkeypress(go_right, "d") 
wn.onkeypress(go_left, "a")       
wn.onkeypress(go_up, "Up")  
wn.onkeypress(go_down, "Down") 
wn.onkeypress(go_right, "Right") 
wn.onkeypress(go_left, "Left")   
#Main game loop

while True:
    wn.update()

    move()

    time.sleep(delay)

wn.mainloop()