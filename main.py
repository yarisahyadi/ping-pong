from turtle import Screen
from bat import Bat
from ball import Ball
from score import Score
import time

TABLE_WIDTH = 600
TABLE_LENGTH = 1080

# setting up screen as the table
table = Screen()
table.bgcolor("black")
table.setup(TABLE_LENGTH, TABLE_WIDTH)
table.title("Ping Pong")
table.tracer(0)

# display the score
score = Score(TABLE_WIDTH)
score.line()

# initiate the bats
right_bat = Bat(color="yellow", bat_side="right")
left_bat = Bat(color="blue", bat_side="left")

table.listen()
table.onkeypress(key="Up", fun=right_bat.move_up)
table.onkeypress(key="Down", fun=right_bat.move_down)
table.onkeypress(key="w", fun=left_bat.move_up)
table.onkeypress(key="s", fun=left_bat.move_down)

# ball
ball = Ball()
is_game_over = False
table_edge = TABLE_WIDTH / 2

while not is_game_over:
    # time.sleep(0.1)
    ball.move()

    if ball.collide(table_edge):
        ball.bounce_side()

    if ((ball.distance(right_bat) < right_bat.width * 10 and ball.xcor() > right_bat.xcor() - right_bat.length * 20) or 
        (ball.distance(left_bat) < left_bat.width * 10 and ball.xcor() < left_bat.xcor() + left_bat.length * 20)):
        ball.bounce_bat()

    if ball.xcor() > TABLE_LENGTH / 2 + 20 or ball.xcor() < -TABLE_LENGTH / 2 - 20:
        ball.goto(0,0)
        # ball.restart()

    table.update()

table.exitonclick()
