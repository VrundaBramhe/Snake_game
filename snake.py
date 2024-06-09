from turtle import Turtle
from food import Food
POSITION=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake(Food):
    def __init__(self):
        super().__init__
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in POSITION:
            self.create_block(position)

    def create_block(self,position):
        new_segment=Turtle()
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def add_block(self):
        self.create_block(self.segments[-1].position())


    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].fd(20)

    def new_block(self):
        new_segment1 = Turtle()
        new_segment1.shape("square")
        new_segment1.color("white")
        new_segment1.penup()
        p=self.segments[len(self.segments)].pos()
        new_segment1.goto(p)
        self.segments.append(new_segment1)



    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)


