import random
import cv2
# i love peanuts
# screen 33*33


def ran():
  return random.randint(1,5000)


# Generates cells in square area offset by player position
# This could be improved by generating only cells that are needed offset by player position when missing. 
def generateCells(screenx,screeny):
  map = [] # Start with blank map
  for x in range(32):
    for y in range(32):
      random.seed(x+screenx+((y+screeny)*32)) # Get seed for cell in a real game might want to pass the number output as an md5 hash to make it more unpredictable.
      randnum = ran() # generate cell number based off seed used

      if x+screenx > 168 or y+screeny > 168:
        map.append("^")
      elif randnum < 3750:
        map.append(" ")
      elif randnum < 4982:
        map.append("^")
      elif randnum < 5001:
        map.append("T")
      else:
        map.append("~")
  return map # Returns generated map as output


print("starting infinite world of AIDSrpg!")


camx = 128
camy = 128
pindex = 256
pcollide = ["^", "T"] # If terrain character is in this array the player cannot move onto it.

while True:
  map = generateCells(camy,camx)
  map[pindex] = "A"
  for y in range(32):
    print(str(map[0+(y*32):32+(y*32)]).replace("\'", "", 99999).replace(",", "", 99999).replace("[", "1").replace("]", "1"))
  pinput = input() + "m"
  pinput = pinput[0]
  if pinput == "q":
    exit("game over!")
  if pinput == "d" and not map[pindex+1] in pcollide[0:len(pcollide)]:
    camx += 1
  if pinput == "a" and not map[pindex-1] in pcollide[0:len(pcollide)]:
    camx -= 1
  if pinput == "w" and not map[pindex-32] in pcollide[0:len(pcollide)]:
    camy -= 1
  if pinput == "s" and not map[pindex+32] in pcollide[0:len(pcollide)]:
    camy += 1
