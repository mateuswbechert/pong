import turtle

window = turtle.Screen()
window.title("Pong by @matwolbec")
window.bgcolor("black")
window.setup(width=800, height=600)
#tracer set to 0 force to manually update the screen
#window.tracer(0)

# definitions
speed = 2
paddle_width = 5
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=paddle_width, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=paddle_width, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = speed
ball.dy = speed


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0  Player B:0", align="center", font=("Courier", 24, "normal"))


# Functions
# Paddle A moves
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if paddle_a.ycor() < 240:
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if paddle_a.ycor() > -240:
        paddle_a.sety(y)

# Paddle B moves
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if paddle_b.ycor() < 240:
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if paddle_b.ycor() > -240:
        paddle_b.sety(y)


window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down , "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down , "Down")

# main loop game
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) 

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle collision
    add_size = 52
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + add_size and ball.ycor() > paddle_b.ycor() - add_size):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + add_size and ball.ycor() > paddle_a.ycor() - add_size):
        ball.setx(-330)
        ball.dx *= -1
