#!/bin/python3

from random import choice
from Tile import *

# store_data = False
screen = turtle.Screen()

i = 2
while i < 5000:
  screen.addshape(str(i)+".gif")
  i*=2

box_size = 64

grid = [[None for x in range(0,4)] for y in range(0,4)]

def get(x, y):
  if grid[x][y] == None:
    return 0
  return grid[x][y].value

def score():
  sum = 0
  for x in range(0,4):
    for y in range(0,4):
      sum += get(x,y)
  return sum

def can_go_down():
  for x in range(0,4):
    for y1 in range(0,4):
      for y2 in range(y1-1,-1,-1):
        if grid[x][y1] != None and grid[x][y2] == None:
          return True
  return vertical_merges()

def can_go_up():
  for x in range(0,4):
    for y1 in range(3,-1,-1):
      for y2 in range(y1+1,4):
        if grid[x][y1] != None and grid[x][y2] == None:
          return True
  return vertical_merges()

def can_go_left():
  for y in range(0,4):
    for x1 in range(0,4):
      for x2 in range(x1-1,-1,-1):
        if grid[x1][y] != None and grid[x2][y] == None:
          return True
  return horizontal_merges()
  
def can_go_right():
  for y in range(0,4):
    for x1 in range(3,-1,-1):
      for x2 in range(x1+1,4):
        if grid[x1][y] != None and grid[x2][y] == None:
          return True
  return horizontal_merges()

  
def vertical_merges():
  for x in range(0,4):
    for y in range(1,4):
      if grid[x][y] != None and grid[x][y-1] != None and grid[x][y].value == grid[x][y-1].value:
        return True
  return False

def horizontal_merges():
  for x in range(1,4):
    for y in range(0,4):
      if grid[x][y] != None and grid[x-1][y] != None and grid[x][y].value == grid[x-1][y].value:
        return True
  return False

def draw_box(x, y):
  turtle.penup()
  turtle.setposition(x*box_size, y*box_size)
  turtle.pendown()
  turtle.setposition((x+1)*box_size, y*box_size)
  turtle.setposition((x+1)*box_size, (y+1)*box_size)
  turtle.setposition(x*box_size, (y+1)*box_size)
  turtle.setposition(x*box_size, y*box_size)
  turtle.penup()
  
def add_tile(x, y):
  if grid[x][y] == None:
    # num = choice([2,2,2,2,4,2,2,2,2,2])
    num = 2
    grid[x][y] = Tile(x,y,num)
  return grid[x][y]
  
def add_random_tile():
  options = []
  for x in range(0,4):
    for y in range(0,4):
      if grid[x][y] == None:
        options.append((x,y))
  
  x,y = choice(options)
  add_tile(x,y)

def refresh():
  for x in range(0,4):
    for y in range(0,4):
      if grid[x][y] != None:
        grid[x][y].refresh(x,y)
        
  if not (can_go_down() or can_go_left() or can_go_right() or can_go_up()):
    print("Game Over! Score:", score())

# def store_data():
#   new_line=True
#   f = open("dataset.txt","r")
#   if f=="":
#     new_line=False
#   f.close()
#   f = open("dataset.txt","a")
#   if new_line==True:
#     f.write("\n")
  
def down():
  if not can_go_down():
    return
  shift(0,-1)
  merge(0,-1)
  shift(0,-1)
  add_random_tile()
  refresh()

def up():
  if not can_go_up():
    return
  shift(0,1)
  merge(0,1)
  shift(0,1)
  add_random_tile()
  refresh()
  
def right():
  if not can_go_right():
    return
  shift(1,0)
  merge(1,0)
  shift(1,0)
  add_random_tile()
  refresh()
  
def left():
  if not can_go_left():
    return
  shift(-1,0)
  merge(-1,0)
  shift(-1,0)
  add_random_tile()
  refresh()
  
def shift(i, j):
  if i + j < 0:
    xrange = range(-i,4)
    yrange = range(-j,4)
  else:
    xrange = range(3-i,-1,-1)
    yrange = range(3-j,-1,-1)
    
  for x in xrange:
    for y in yrange:
      x1 = x
      y1 = y
      while 0 <= x1+i <= 3 and 0 <= y1+j <= 3 and grid[x1+i][y1+j] == None:
        grid[x1+i][y1+j] = grid[x1][y1]
        grid[x1][y1] = None
        x1 += i
        y1 += j
        
def merge(i, j):
  if i + j < 0:
    xrange = range(-i,4)
    yrange = range(-j,4)
  else:
    xrange = range(3-i,-1,-1)
    yrange = range(3-j,-1,-1)
        
  for x in xrange:
    for y in yrange:
      if grid[x][y] != None and grid[x+i][y+j] != None and grid[x+i][y+j].merge(grid[x][y]):
        grid[x][y].turtle.ht()
        grid[x][y] = None
        
def setup():
  screen.onkey(up,"w")
  screen.onkey(left,"a")
  screen.onkey(down,"s")
  screen.onkey(right,"d")
  clear_board()
  add_random_tile()
  add_random_tile()
  screen.listen()
  screen.delay(7)
  

def unsetup():
  screen.onkey(None,"w")
  screen.onkey(None,"a")
  screen.onkey(None,"s")
  screen.onkey(None,"d")

def clear_board():
  for i in range(4):
    for n in range(4):
      if grid[i][n]!=None:
        grid[i][n].turtle.ht()
        grid[i][n] = None
