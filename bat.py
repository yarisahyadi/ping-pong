from turtle import Turtle

BAT_LENGTH = 1
BAT_WIDTH = 5
BAT_SHAPE = "square"
STEP = 50

class Bat(Turtle):
    def __init__(self, color="white", bat_side="right", table_length=1080):
        super().__init__()
        self.shape(BAT_SHAPE)
        self.color(color)
        self.length = BAT_LENGTH
        self.width = BAT_WIDTH
        self.side = bat_side.lower()
        self.bat_xcor = table_length / 2 - 40
        self.bat_ycor = 0
        self._make_bat()

    def _make_bat(self):
        if self.side == "left":
            self.bat_xcor *= -1
        self.shapesize(stretch_wid=BAT_WIDTH, stretch_len=BAT_LENGTH)
        self.penup()
        self.speed("fastest")
        self.goto(self.bat_xcor,self.bat_ycor)

    def move_up(self):
        new_y = self.ycor() + STEP
        self.goto(self.bat_xcor, new_y)

    def move_down(self):
        new_y = self.ycor() - STEP
        self.goto(self.bat_xcor, new_y)
