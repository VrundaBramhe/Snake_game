import turtle
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("black")
        self.goto(0,275)
        self.score=0
        self.wr()
    def wr(self):
       self.write(arg=f"SCORE = {self.score}",move=False,align="center",font=("Times New Roman",18,"italic"))

    def upd(self):
        self.score=self.score+1
        self.clear()
        self.wr()

    def gameover(self):
        self.goto(0,0)
        self.write(arg="GAME OVER !!", move=False, align="center", font=("Times New Roman", 30, "italic"))




