from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 5)
        if random_chance == 5:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1,2)
            # new_car.setheading(90)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            # new_car.speed = STARTING_SPEED
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            # new_x = car.xcor() - STARTING_MOVE_DISTANCE
            # car.goto(new_x, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT