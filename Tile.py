#!/bin/python3

import turtle

# training=False

class Tile():
  def __init__(self, x=0, y=0, value=2):
    self.value = value
    self.turtle = turtle.Turtle()
    self.turtle.hideturtle()
    self.turtle.penup()
    self.turtle.shape(str(self.value)+".gif")
    self.turtle.speed(0)
    self.turtle.seth(90)
    self.turtle.setposition((x-1.5)*64, (y-1.5)*64)
    self.turtle.showturtle()
    # if not training:
      # self.turtle.speed(6)
    
  def refresh(self, x, y):
    self.turtle.shape(str(self.value)+".gif")
    self.turtle.setposition((x-1.5)*64, (y-1.5)*64)
    
  def merge(self, other):
    if self.value == other.value:
      self.value *= 2
      other.turtle.ht()
      return True
    return False
