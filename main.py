from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# paddle = Turtle("square")
# paddle.color("white")
# #all turles start out 20 x 20 so if want 200 x 20 , would take times 5 and 1
# paddle.penup()
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.goto(350, 0)



#have to make the screen listen for key strokes first
screen.listen()
#when use functions as params omit the ()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

#need to manually update the screen because of tracer(0)
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()

#collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

#if r_padle misses
    if ball.xcor() > 380 or ball.xcor() < -300:
        ball.reset_position()
        scoreboard.l_point()

#if l_padle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()


