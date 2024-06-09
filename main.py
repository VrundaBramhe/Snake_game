from snake import Snake
from turtle import Screen
import time
from scoreboard import Scoreboard
from food import Food

screen=Screen()

screen.bgpic("snakebg.gif")
screen.setup(width=600,height=600)
#screen.bgcolor("black")
screen.title(titlestring="SNAKE GAME")
screen.tracer(0)

score=0

s=Snake()
f=Food()
sc = Scoreboard()

screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.down,"Down")
screen.onkey(s.left,"Left")
screen.onkey(s.right,"Right")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

    #food
    if s.head.distance(f) < 15:
        f.ht()
        s.add_block()
        sc.upd()
        f=Food()

    #collision with wall
    if s.head.xcor()>280 or s.head.xcor()<-280 or s.head.ycor()>280 or s.head.ycor()<-280:
        sc.gameover()
        game_is_on=False

    #collsion with tail
    for segment in s.segments[1:]:
        if s.head.distance(segment) ==0 :
            game_is_on = False
            sc.gameover()




screen.exitonclick()