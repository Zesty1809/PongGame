# import libraries
import turtle

# create screen
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# left paddle
left_pad = turtle.Turtle()
left_pad.shape("square")
left_pad.speed(0)
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# right paddle
right_pad = turtle.Turtle()
right_pad.shape("square")
right_pad.speed(0)
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# ball of circle shape
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(40)
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# initialization of score
left_player = 0
right_player = 0

# display the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0, Right_player : 0", align="center", font=("Courier", 24, "normal"))


def paddle_a_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def paddle_a_down():
    y = left_pad.ycor()
    y += -20
    left_pad.sety(y)


def paddle_b_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def paddle_b_down():
    y = right_pad.ycor()
    y += -20
    right_pad.sety(y)


# keyboard bindings
sc.listen()
sc.onkeypress(paddle_a_up, "w")
sc.onkeypress(paddle_a_down, "s")
sc.onkeypress(paddle_b_up, "Up")
sc.onkeypress(paddle_b_down, "Down")

while True:
    sc.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # checking borders
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dx *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left player : {}, Right player : {}".format(left_player, right_player),
                     align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dx *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left player : {}, Right player : {}".format(left_player, right_player),
                     align="center", font=("Courier", 24, "normal"))

    # paddle ball collision
    if (360 < ball.xcor() < 370) and (right_pad.ycor() + 80 > ball.ycor() > right_pad.ycor() - 80):
        ball.setx(360)
        ball.dx *= -1

    if (-360 > ball.xcor() > -370) and (left_pad.ycor() + 80 > ball.ycor() > left_pad.ycor() - 80):
        ball.setx(-360)
        ball.dx *= -1
#
# turtle.Screen().exitonclick()
