from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=-250, y=250)
        self.refresh()

    def add_up(self):
        self.points += 1
        self.refresh()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over!", align="center", font=("Verdana", 24, "normal"))

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.points}", font=("Verdana", 24, "normal"))
