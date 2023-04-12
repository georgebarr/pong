from turtle import Turtle, Screen

screen = Screen()
screen.title("Pong")
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = Turtle('square')
paddle.color("White")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() + -20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_running = True
while game_running:
    screen.update()

screen.exitonclick()
