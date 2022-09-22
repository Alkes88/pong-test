import turtle

wn = turtle.Screen()
wn.title("Pong by Alkes")
wn.bgcolor("black")
wn.setup(width=800, height= 600)
wn.tracer(0)

score_a = 0
score_b = 0

player_left = turtle.Turtle()
player_left.speed(0)
player_left.shape("square")
player_left.color("white")
player_left.shapesize(stretch_wid=5, stretch_len=1)
player_left.penup()
player_left.goto(-350, 0)

player_right = turtle.Turtle()
player_right.speed(0)
player_right.shape("square")
player_right.color("white")
player_right.shapesize(stretch_wid=5, stretch_len=1)
player_right.penup()
player_right.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Left: 0        Player Right: 0", align="center", font=("Courier", 24, "normal"))

def player_left_up():
    y = player_left.ycor()
    y += 20
    player_left.sety(y)

def player_left_down():
    y = player_left.ycor()
    y -= 20
    player_left.sety(y)

def player_right_up():
    y = player_right.ycor()
    y += 20
    player_right.sety(y)

def player_right_down():
    y = player_right.ycor()
    y -= 20
    player_right.sety(y)

wn.listen()
wn.onkeypress(player_left_up, "w")
wn.onkeypress(player_left_down, "s")
wn.onkeypress(player_right_up, "Up")
wn.onkeypress(player_right_down, "Down")

while True:
    wn.update() 

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player Left: {}        Player Right: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player Left: {}        Player Right: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_right.ycor() + 40 and ball.ycor() > player_right.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_left.ycor() + 40 and ball.ycor() > player_left.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 