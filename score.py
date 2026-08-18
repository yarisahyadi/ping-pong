from turtle import Turtle

FONT = ('Courier', 22, 'normal')
ALIGNMENT = "center"

class Score(Turtle):
    def __init__(self, table_width):
        super().__init__()
        self.length = table_width
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()

    def line(self):
        self.pencolor("white")
        self.penup()
        self.goto(0, self.length / 2 * -1)
        self.seth(90)
        for _ in range(self.length // 40):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def scoreboard(self, left_side=0, right_side=0):
        self.goto(0, self.length - 50)
        self.left_score += left_side
        self.right_score += right_side
        self._update_score()

    def _update_score(self):
        self.clear()
        self.write(f"Score:\n {self.left_score} {self.right_score}", align=ALIGNMENT, font=FONT)
