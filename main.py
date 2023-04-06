#!/bin/python3

train = False

if not train:
  from Game import *
import random, math
mode = "normal"
# import Game_hidden as game
# import keras

network_layers=[16]

# model = keras.models.Sequential()



def num_mergers(line):
  # skip=False
  count=0
  n=-1
  while n<4:
    n+=1
    # if skip:
    #   skip = False
    #   continue
    for i in range(1,4-n):
      if line[n]==line[n+i]:
        count+=1
        n=n+i+1
        break
      elif line[n+i]!=0:
        break
        # skip=True
  return count

def total_horizontal_mergers():
  count=0
  for i in range(4):
    L=[]
    for n in range(4):
      L.append(get(n,i))
    count+=num_mergers(L)
  return count
  
def total_vertical_mergers():
  count=0
  for i in range(4):
    L=[]
    for n in range(4):
      L.append(get(i,n))
    count+=num_mergers(L)
  return count

def get_grid():
  one_d_grid=[]
  for x in range(4):
    for y in range(4):
      if not train:
        value=get(x,y)
        if value==0:
          value=1
        value = math.log2(value)
      else:
        value=game.get(x,y)
      #   one_d_grid.append(0)
      # else:
      #   one_d_grid.append(math.log2(value)+1)
      for i in range(18):
        if value==i:
          one_d_grid.append(1)
        else:
          one_d_grid.append(0)
  return one_d_grid

def create_network(layers):
  f=open("networks.txt","r")
  new_line=True
  if f.read()=="":
    new_line=False
  f.close()
  f=open("networks.txt","a")
  if new_line:
    f.write("\n")
  previous=288
  for i in layers:
    for n in range(previous*i):
      if n!=0:
        f.write(",")
      f.write(str(random.uniform(-1,1)))
    f.write(";")
    previous=i
  for i in range(previous*4):
    if i!=0:
      f.write(",")
    f.write(str(random.uniform(-1,1)))
  f.close()
  print("Network Created.")

def update_mode():
  global mode
  greatest=(0,0,0)
  for x in range(4):
    for y in range(4):
      if get(x,y)>greatest[2]:
        greatest = (x,y,get(x,y))
  if not greatest[2]==get(3,0):
    if greatest[2]==get(2,0):
      mode="right"
    elif greatest[2]==get(3,1):
      mode="down"
    elif not greatest[2] in ([get(2,0),get(3,0),get(3,1)]):
      mode="panic"
      # mode="normal"
  else:
    mode="normal"

def calculate_move(num,data):
  # f=open("networks.txt","r")
  # networks=f.read().split("\n")
  # f.close()
  # if len(networks)<=num and num>=0:
  #   for i in range(num-len(networks)+1):
  #     create_network(network_layers)
  #   f=open("networks.txt","r")
  #   networks=f.read().split("\n")
  #   f.close()
  # if num>=0:
  #   network = networks[num]
  #   network=network.split(";")
  #   for i in range(len(network)):
  #     network[i]=network[i].split(",")
  #     for n in range(len(network[i])):
  #       network[i][n]=float(network[i][n])

  #   D_old=data
  #   D=[]
  #   for l in range(len(network)-1):
  #     D=[]
  #     W=network[l]
  #     for n in range(int(len(W)/len(D_old))):
  #       x=0
  #       for wn in range(len(D_old)):
  #         x+=W[n*len(D_old)+wn]*D_old[wn]
  #       D.append(x)
  #     D_old=D

  #   L=D
  #   L.sort()
  #   if not train:
  #     if can_go_down() or can_go_left() or can_go_up() or can_go_right():
  #       for i in L:
  #         value = D.index(i)
  #         if value==0 and can_go_up():
  #           up()
  #         elif value==1 and can_go_left():
  #           left()
  #         elif value==2 and can_go_down():
  #           down()
  #         elif value==3 and can_go_right():
  #           right()
  #       return True
  #   elif game.can_go_down() or game.can_go_left() or game.can_go_up() or game.can_go_right():
  #     for i in L:
  #       value = D.index(i)
  #       if value==0 and game.can_go_up():
  #         game.up()
  #       elif value==1 and game.can_go_left():
  #         game.left()
  #       elif value==2 and game.can_go_down():
  #         game.down()
  #       elif value==3 and game.can_go_right():
  #         game.right()
  #     return True
  #   return False

  global mode
  
  if mode=="normal":
    if total_vertical_mergers()>=total_horizontal_mergers() and total_horizontal_mergers()>0 and can_go_down():
      down()
    elif total_horizontal_mergers()>total_vertical_mergers() and total_vertical_mergers()>0 and can_go_right():
      right()
    elif can_go_down():
      down()
    elif can_go_right():
      right()
    elif can_go_left():
      left()
      update_mode()
    elif can_go_up():
      up()
      # if get(3,0)==0 and can_go_down():
      #   down()
      update_mode()
  elif mode=="right":
    if get(3,0)==0 and can_go_right():
      right()
      update_mode()
    elif len([get(2,y) for y in range(4) if get(2,y)!=0]) > len([get(3,y) for y in range(4) if get(3,y)!=0]) and can_go_up():
      up()
      right()
      down()
      update_mode()
    elif can_go_left():
      left()
    elif can_go_up():
      up()
      down()
      update_mode()
    elif can_go_down():
      down()
    elif can_go_right():
      right()
      update_mode()
  elif mode=="down":
    if get(3,0)==0 and can_go_down():
      down()
      update_mode()
    elif len([get(y,3) for y in range(4) if get(y,3)!=0]) > len([get(y,2) for y in range(4) if get(y,2)!=0]) and can_go_left():
      left()
      down()
      right()
      update_mode()
    elif can_go_up():
      up()
    elif can_go_left():
      left()
      right()
      update_mode()
    elif can_go_right():
      right()
    elif can_go_down():
      down()
      update_mode()
  else:
    if random.randint(1,4)==1 and can_go_down():
      down()
    elif random.randint(1,3)==1 and can_go_right():
      right()
    elif random.randint(1,2)==1 and can_go_left():
      left()
    elif can_go_up():
      up()
    else: return False
    update_mode()
      
  # greatest=(0,0,0)
  # for x in range(4):
  #   for y in range(4):
  #     if get(x,y)>greatest[2]:
  #       greatest = (x,y,get(x,y))
  # if not greatest[2]==get(3,0):
  #   if greatest[2]==get(2,0):
  #     mode="right"
  #   elif greatest[2]==get(3,1):
  #     mode="down"
  #   elif not greatest[2] in ([get(2,0),get(3,0),get(3,1)]):
  #     # mode="panic"
  #     mode="normal"
  # else:
  #   mode="normal"
      
  if can_go_down() or can_go_left() or can_go_up() or can_go_right():
    return True
  return False
  
  # down()
  # left()
  # up()
  # right()
  # if can_go_down() or can_go_left() or can_go_up() or can_go_right():
  #   return True
  # return False

def run_ai(n):
  if not train:
    clear_board()
    add_random_tile()
    add_random_tile()
  else:
    game.clear_board()
    game.add_random_tile()
    game.add_random_tile()
  # i=1
  if not train:
    while True:
      if not calculate_move(n,get_grid()):
        return score()
  else:
    while True:
      if not calculate_move(n,get_grid()):
        return game.get_score()
      # print("AI made move",i)
      # i+=1

def test_ai(n,tests):
  # print("Testing")
  sum_of_scores=0
  for i in range(tests):
    sum_of_scores+=run_ai(n)
  return sum_of_scores/tests

def Key__(list):
  return list["average_score"]

def train_ai():
  f = open("networks.txt","r")
  networks = f.readlines()
  num_of_agents=50
  if len(networks)<num_of_agents:
    for i in range(num_of_agents-len(networks)):
      create_network(network_layers)
    networks=f.readlines()
  f.close()

  ai_scores=[]
  for i in range(len(networks)):
    ai_scores.append({"average_score":test_ai(i,3),"network":networks[i]})
    # print("Network",i+1,"has been tested.")
  # print("All networks have been tested.")
  ai_scores.sort(key=Key__,reverse=True)

  high_score = ai_scores[0]["average_score"]
  
  num_duplicate=5
  ai_scores = [ai_scores[int((abs(i-num_duplicate)+i-num_duplicate)/2)] for i in range(len(ai_scores))]
  # ai_scores = [ai_scores[math.floor(i/2)] for i in range(len(ai_scores))]
  ai_scores = [row["network"].split(";") for row in ai_scores]
  ai_scores = [[layer.split(",") for layer in row] for row in ai_scores]
  ai_scores = [[[str(float(weight)+random.uniform(0.005,-0.005)) for weight in layer] for layer in network] for network in ai_scores]
  ai_scores = "\n".join([";".join([",".join(layer) for layer in network]) for network in ai_scores])
  f = open("networks.txt","w")
  f.write(ai_scores)
  f.close()
  return high_score
  
playing=False
# screen.onkeyrelease(toggle_off,"space")
i=1
while train:
  print("Starting")
  print("Finished generation",i,"\nHighest score =",train_ai())
  i+=1

while True:
  if playing:
    input("")
    if not (can_go_down() or can_go_left() or can_go_right() or can_go_up()):
      playing = False
      unsetup()
  else:
    answer = input("Would you like to watch the AI play 2048, play 2048 yourself? Answer \"play\" to play and anything else to watch the AI play. ").lower()
    # if answer == "train":
    #   # screen.delay(0)
    #   # training=True
    #   i=1
    #   while True:
    #     print("Finished generation",i,"\nHighest score =",train_ai())
    #     i+=1
    if answer=="play":
      # training=False
      setup()
      playing=True
    else:
      # training=False
      run_ai(0)
