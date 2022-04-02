from turtle import Turtle, Screen
from player import Player
from carmanager import CarManager
import time

# create screen
# create player and move
# create car random color and move
# create collision with car
# set finish line

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross")
screen.tracer(0)


player = Player()
carmanager = CarManager()


screen.listen()
screen.onkey(player.move, "Up")



game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    carmanager.car_m()
    carmanager.move_car()

    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_on = False

    if player.player_reached():
        player.player_return()
        carmanager.car_speed()




screen.exitonclick()
