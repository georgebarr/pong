from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong")
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_running = True
while game_running:
    screen.update()

screen.exitonclick()
