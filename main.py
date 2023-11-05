import time
import turtle
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car = CarManager()
score = Scoreboard()
increment = 0

turtle.listen()
turtle.onkey(tim.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move(increment)

    # collision with cars
    for lil_car in car.all_cars:
        if lil_car.distance(tim) < 10:
            game_is_on = False
            score.game_over()

    # reach at top
    if tim.ycor() > 280:
        increment += 5
        score.add_up()
        tim.refresh()


screen.exitonclick()
