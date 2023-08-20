import turtle
import winsound

window = turtle.Screen()
window.title("Pong!")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

score1 = 0
score2 = 0

left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.color("red")
left_paddle.penup()
left_paddle.goto(-350, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.color("blue")
right_paddle.penup()
right_paddle.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 8, "normal"))


def left_paddle_up():
    if left_paddle.ycor() < 250:
        y = left_paddle.ycor()
        y += 20
        left_paddle.sety(y)


def left_paddle_down():
    if left_paddle.ycor() > -250:
        y = left_paddle.ycor()
        y -= 20
        left_paddle.sety(y)


def right_paddle_up():
    if right_paddle.ycor() < 250:
        y = right_paddle.ycor()
        y += 20
        right_paddle.sety(y)


def right_paddle_down():
    if right_paddle.ycor() > -250:
        y = right_paddle.ycor()
        y -= 20
        right_paddle.sety(y)


window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.dy *= -1
        winsound.PlaySound("click-button-menu-147349.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.dy *= -1
        winsound.PlaySound("click-button-menu-147349.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        winsound.PlaySound("high-zcore-96686.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 8, "normal"))
        if (score1 + score2) % 2 == 1:
            ball.dx = -0.1
        else:
            ball.dx = 0.1
        ball.dy = 0.1

    if ball.xcor() < -390:
        winsound.PlaySound("high-zcore-96686.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 8, "normal"))
        if (score1 + score2) % 2 == 1:
            ball.dx = -0.1
        else:
            ball.dx = 0.1
        ball.dy = 0.1

    if -350 < ball.xcor() < -340 and left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 40:
        ball.dx *= -1
        winsound.PlaySound("click-button-menu-147349.wav", winsound.SND_ASYNC)
    if 350 > ball.xcor() > 340 and right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 40:
        ball.dx *= -1
        winsound.PlaySound("click-button-menu-147349.wav", winsound.SND_ASYNC)

    ball.dx *= 1.0001
    ball.dy *= 1.0001

    if score1 > 4 or score2 > 4:
        winsound.PlaySound("tada-fanfare-a-6313.wav", winsound.SND_ASYNC)
        break
while True:
    window.update()
    if score1 > score2:
        pen.clear()
        pen.write("Player 1 wins!", align="center", font=("Courier", 8, "normal"))
    if score1 < score2:
        pen.clear()
        pen.write("Player 2 wins!", align="center", font=("Courier", 8, "normal"))
