from turtle import Turtle

FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)


    def move(self):
        self.fd(10)

    def player_return(self):
        self.goto(0, -280)


    def player_reached(self):
        if self.ycor() > FINISH_LINE:
           return  True
        else:
            return False
