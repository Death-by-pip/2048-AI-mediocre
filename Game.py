#!/bin/python3

from Helpers import *


turtle.speed(0)
turtle.tracer(1) #Change tracer value to increase speed of game. DO NOT RAISE ABOVE 10
for i in range(-2,2):
  for j in range(-2,2):
    draw_box(i, j)
turtle.hideturtle()

#add_random_tile()
#add_random_tile()

# setup()
screen.listen()
screen.delay(7)
# unsetup()
