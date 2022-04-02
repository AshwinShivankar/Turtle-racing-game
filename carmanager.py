import random
from turtle import Turtle
import random
COLOR = ["red", "yellow", "blue", "green", "orange", "violet"]
CAR_MOVE = 5
INCREASE = 10
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_sp = CAR_MOVE


    def car_m(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
             car = Turtle("square")
             car.color(random.choice(COLOR))
             car.shapesize(stretch_len=2, stretch_wid=1)
             car.penup()
             random_y = random.randint(-250, 250)
             car.goto(300, random_y)
             self.all_cars.append(car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_sp)


    def car_speed(self):
        self.car_sp += INCREASE


