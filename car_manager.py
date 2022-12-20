import random
from turtle import Turtle
COLORS = ["pink", "purple", "orange", "blue", "yellow", "black"]
STARTING_MOVING_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVING_DISTANCE

        # to create a random car somewhere on the y axis
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
           new_car = Turtle("square")
           new_car.shapesize(stretch_wid=1, stretch_len=2)
           new_car.penup()
           new_car.color(random.choice(COLORS))
           random_y = random.randint(-300, 300)
           new_car.goto(300, random_y)
           self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def new_level(self):
        self.car_speed += MOVE_INCREMENT