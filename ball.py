from turtle import Turtle
import random

BALL_SIZE = 20
BALL_SHAPE = "circle"
STEP = 0.2

class Ball(Turtle):
    def __init__(self, ball_color="white"):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(ball_color)
        self.shapesize(BALL_SIZE / 20)
        self.penup()
        self.step_x = STEP
        self.step_y = STEP

    def start(self):
        self.starting_angle = random.randint(0, 360)
        self.seth(self.starting_angle)
        self.forward(STEP)
        
    def move(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)
        # self.speed("slowest")

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
