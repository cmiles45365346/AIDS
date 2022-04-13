import random

# screen 21*8


def ran():
  return random.randint(1,5000)


def screen(screenx,screeny):
  map = []
  for x in range(21):
    for y in range(21):
      random.seed(x+screenx+((screeny + y)*21))
      randnum = ran()
      if randnum < 3750:
        map.append(" ")
      elif randnum < 4982:
        map.append("^")
      elif randnum < 5001:
        map.append("T")
      else:
        map.append("~")
  return map

print("starting infinite world!")

camx = 128
camy = 128
pindex = 367
pcollide = ["^"]

while True:
  map = screen(camx,camy)
  map[pindex] = "A"
  for y in range(21):
    print(map[0+(y*21)]+map[1+(y*21)]+map[2+(y*21)]+map[3+(y*21)]+map[4+(y*21)]+map[5+(y*21)]+map[6+(y*21)]+map[7+(y*21)]+
  map[8+(y*21)]+map[9+(y*21)]+map[10+(y*21)]+map[11+(y*21)]+map[12+y*21]+map[13+(y*21)]+map[14+(y*21)]+map[15+(y*21)]+
  map[16+(y*21)]+map[17+(y*21)]+map[18+(y*21)]+map[19+(y*21)]+map[20+(y*21)])
  pinput = input() + "m"
  pinput = pinput[0]
  if pinput == "q":
    exit("game over!")
  if pinput == "d" and not map[pindex+1] in pcollide[0:1]:
    camy += 1
  if pinput == "a" and not map[pindex-1] in pcollide[0:1]:
    camy -= 1
  if pinput == "w" and not map[pindex-21] in pcollide[0:1]:
    camx -= 1
  if pinput == "s" and not map[pindex+21] in pcollide[0:1]:
    camx += 1    
 
