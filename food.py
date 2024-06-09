from random import randint
#from snake import Snake
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.4,0.4)
        self.color("red")
        self.penup()
        self.speed("fastest")
        x=randint(-280,280)
        y=randint(-280,280)
        self.goto(x,y)


