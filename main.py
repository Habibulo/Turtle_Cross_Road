"""Documentation for turtle_cross_road project"""
# 1. TODO create a main.py including screen of width 800, height 800
#       make a turtle, while loop and screen tracer with update.
# 2. TODO create cars as a car_manager.py and Car class which can move
# 3. TODO create a turtle player
# 4. TODO create a scoreboard that tracks the user core


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("gainsboro")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.point()

screen.exitonclick()
