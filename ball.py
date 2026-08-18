from turtle import Turtle
import random

BALL_SIZE = 20
BALL_SHAPE = "circle"
SPEED = 0.1

class Ball(Turtle):
    def __init__(self, ball_color="white"):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(ball_color)
        self.shapesize(BALL_SIZE / 20)
        self.penup()
        self.step_x = SPEED
        self.step_y = SPEED

    def restart(self):
        self.goto(0, 0)
        self.step_x *= -1
        
    def move(self):
        new_x = self.xcor() + random.randint(0, 1) * self.step_x
        new_y = self.ycor() + random.randint(0, 1) * self.step_y
        self.goto(new_x, new_y)

    def collide(self, table_side):
        self.table_side = table_side
        return (self.ycor() >= self.table_side - BALL_SIZE / 2 or
                self.ycor() <= self.table_side * -1 + BALL_SIZE / 2)

    def hit(self):
        pass

    def bounce_side(self):
        self.step_y *= -1
        self.move()

    def bounce_bat(self):
        self.step_x *= -1
        self.move()
