from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.current_heading = RIGHT  # Track the current heading
        self.key_pressed = False  # Flag to track if a key has been pressed

    def create_snake(self):
        for position in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("black")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def add_block(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.key_pressed = False  # Reset the flag after moving

    def up(self):
        if not self.key_pressed and self.current_heading != DOWN:
            self.head.setheading(UP)
            self.current_heading = UP
            self.key_pressed = True  # Set the flag when a key is pressed

    def down(self):
        if not self.key_pressed and self.current_heading != UP:
            self.head.setheading(DOWN)
            self.current_heading = DOWN
            self.key_pressed = True  # Set the flag when a key is pressed

    def left(self):
        if not self.key_pressed and self.current_heading != RIGHT:
            self.head.setheading(LEFT)
            self.current_heading = LEFT
            self.key_pressed = True  # Set the flag when a key is pressed

    def right(self):
        if not self.key_pressed and self.current_heading != LEFT:
            self.head.setheading(RIGHT)
            self.current_heading = RIGHT
            self.key_pressed = True  # Set the flag when a key is pressed
