# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:40:27 2019
Python 3.7.3

@author: ElisFIVE
based on  Python Game Programming Tutorial: Python Game Programming Tutorial: Pong for Beginners
https://www.youtube.com/watch?v=LH8WgrUWG_I

Changelog:
- added visual horizontal border
- paddle vertical movement is limited now
- added pause game
- added start new game with score reset
- added acceleration coefficient for every round

"""

import turtle

# Control settings and presets
a_up_key = "w"
a_down_key = "s"
b_up_key = "Up"
b_down_key = "Down"
pause_key = "p"
start_key = "g"
initial_speed = 0.1
acceleration = 1.1

wn = turtle.Screen()
wn.title("Pong by SkinnyCat (based on freeCodeCamp.org tutorial)")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Borders
border = turtle.Turtle()
border.shape("square")
border.color("white")
border.penup()
border.goto(400,250)
border.pendown()
border.goto(-400,250)
border.penup()
border.goto(400,-250)
border.pendown()
border.goto(-400,-250)
border.hideturtle()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

def paddle_a_up():
    y = paddle_a.ycor()
    if y < 200:
        y+= 20
    else:
        y = 200
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -200:
        y-= 20
    else:
        y = -200
    paddle_a.sety(y)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 200:
        y+= 20
    else:
        y = 200
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -200:
        y-= 20
    else:
        y = -200
    paddle_b.sety(y)

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0
ball.dy = 0

# Ball start/stop control
trigger = -1 # -1 - stand still; 1 - run
def ball_pause ():
    global trigger
    trigger *= -1

# Pen
score_a = 0
score_b = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()

def score():
    score_pen.clear()
    score_pen.goto(0,260)
    score_pen.write("Left player: {} Right player: {}".format(score_a,score_b), 
              align="center", 
              font=("Courier", 20, "normal"))
    score_pen.goto(0,-280)
    score_pen.write("Start new game: {} Pause: {}".format(start_key,pause_key), 
              align="center", 
              font=("Courier", 20, "normal"))

def initial():
    score_pen.goto(0,40)
    score_pen.write("Start new game: {} Pause: {}".format(start_key,pause_key), 
                align="center", 
                font=("Courier", 20, "normal"))
    
def start():
    global trigger
    trigger = 1
    ball.dx = initial_speed
    ball.dy = initial_speed
    ball.goto(0,0)
    global score_a
    score_a = 0
    global score_b
    score_b = 0
    score()
    
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, a_up_key)
wn.onkeypress(paddle_a_down, a_down_key)
wn.onkeypress(paddle_b_up, b_up_key)
wn.onkeypress(paddle_b_down, b_down_key)
wn.onkeypress(ball_pause, pause_key)
wn.onkeypress(start, start_key)
    
# Main game loop
initial()
while True:
    wn.update()
    # score() # greatly slows down the game, 
              # it is better to update the score only when it changes
    
    # Move the ball
    if trigger > 0:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
   
    # Border chaking
    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1

    if ball.ycor() < -240:
        ball.sety(-240)
        ball.dy *= -1
    
    if ball.xcor() > paddle_b.xcor()+50:
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1
        ball.dx *= acceleration
        ball.dy *= acceleration
        score()

    if ball.xcor() < paddle_a.xcor()-50:
        ball.goto(0,0)
        ball.dx *=-1
        score_b += 1
        ball.dx *= acceleration
        ball.dy *= acceleration
        score()
     
        
  
    #Collisions
    if ((ball.xcor () > paddle_b.xcor() - 20
        and ball.xcor () < paddle_b.xcor()
        and ball.ycor() < paddle_b.ycor() + 50 
        and ball.ycor() > paddle_b.ycor() - 50)
        or (ball.xcor () < paddle_a.xcor() + 20
        and ball.xcor () > paddle_a.xcor()
        and ball.ycor() < paddle_a.ycor() + 50 
        and ball.ycor() > paddle_a.ycor() - 50)):
        ball.dx *= -1   
