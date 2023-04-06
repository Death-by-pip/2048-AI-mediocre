from random import choice

grid = [[0 for x in range(0,4)] for y in range(0,4)]
score = 0

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
      while 0 <= x1+i <= 3 and 0 <= y1+j <= 3 and grid[x1+i][y1+j] == 0:
        grid[x1+i][y1+j] = grid[x1][y1]
        grid[x1][y1] = 0
        x1 += i
        y1 += j
  # if not (can_go_down() or can_go_left() or can_go_right() or can_go_up()):
  #   print("A test has ended.", score())

def get(x, y):
  return grid[x][y]

def get_score():
  # sum = 0
  # for x in range(0,4):
  #   for y in range(0,4):
  #     sum += get(x,y)*(4*x+2*y-9)
  # return sum
  return score

def can_go_down():
  for x in range(0,4):
    for y1 in range(0,4):
      for y2 in range(y1-1,-1,-1):
        if grid[x][y1] != 0 and grid[x][y2] == 0:
          return True
  return vertical_merges()

def can_go_up():
  for x in range(0,4):
    for y1 in range(3,-1,-1):
      for y2 in range(y1+1,4):
        if grid[x][y1] != 0 and grid[x][y2] == 0:
          return True
  return vertical_merges()

def can_go_left():
  for y in range(0,4):
    for x1 in range(0,4):
      for x2 in range(x1-1,-1,-1):
        if grid[x1][y] != 0 and grid[x2][y] == 0:
          return True
  return horizontal_merges()
  
def can_go_right():
  for y in range(0,4):
    for x1 in range(3,-1,-1):
      for x2 in range(x1+1,4):
        if grid[x1][y] != 0 and grid[x2][y] == 0:
          return True
  return horizontal_merges()

def vertical_merges():
  for x in range(0,4):
    for y in range(1,4):
      if grid[x][y] != 0 and grid[x][y-1] != 0 and grid[x][y] == grid[x][y-1]:
        return True
  return False

def horizontal_merges():
  for x in range(1,4):
    for y in range(0,4):
      if grid[x][y] != 0 and grid[x-1][y] != 0 and grid[x][y] == grid[x-1][y]:
        return True
  return False

def add_tile(x, y):
  if grid[x][y] == 0:
    # num = choice([1,1,1,1,2,1,1,1,1,1])
    num = 1
    grid[x][y] = num
  
def add_random_tile():
  options = []
  for x in range(0,4):
    for y in range(0,4):
      if grid[x][y] == 0:
        options.append((x,y))
        
  x,y = choice(options)
  add_tile(x,y)

def down():
  if not can_go_down():
    return
  shift(0,-1)
  merge(0,-1)
  shift(0,-1)
  add_random_tile()

def up():
  if not can_go_up():
    return
  shift(0,1)
  merge(0,1)
  shift(0,1)
  add_random_tile()
  
def right():
  if not can_go_right():
    return
  shift(1,0)
  merge(1,0)
  shift(1,0)
  add_random_tile()
  
def left():
  if not can_go_left():
    return
  shift(-1,0)
  merge(-1,0)
  shift(-1,0)
  add_random_tile()

def merge(i, j):
  if i + j < 0:
    xrange = range(-i,4)
    yrange = range(-j,4)
  else:
    xrange = range(3-i,-1,-1)
    yrange = range(3-j,-1,-1)

  for x in xrange:
    global score
    for y in yrange:
      if grid[x][y] != 0 and grid[x+i][y+j] != 0 and grid[x+i][y+j]==grid[x][y]:
        grid[x+i][y+j] += 2
        grid[x][y] = 0
        score += 2*grid[x+i][y+j]

def clear_board():
  global score
  global grid
  grid = [[0 for x in range(0,4)] for y in range(0,4)]
  score=0
