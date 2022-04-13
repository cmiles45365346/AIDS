import random
import cv2

# screen 33*33


def ran():
  return random.randint(1,5000)


# Generates cells in square area offset by player position
# This could be improved by generating only cells that are needed offset by player position when missing. 
def generateCells(screeny,screenx):
  map = [] # Start with blank map
  for x in range(33):
    for y in range(33):
      random.seed(x+screenx+((y+screeny)*33)) # Get seed for cell in a real game might want to pass the number output as an md5 hash to make it more unpredictable.
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


camy = 128
camx = 128
pindex = 256
pcollide = ["^", "T"] # If terrain character is in this array the player cannot move onto it.

while True:
  map = generateCells(camy,camx)
  map[pindex] = "A"
  for y in range(33):
    print(str(map[0+(y*33):33+(y*33)]).replace("\'", "", 99999).replace(",", "", 99999).replace("[", "1").replace("]", "1"))
  pinput = input() + "m"
  pinput = pinput[0]
  if pinput == "q":
    exit("game over!")
  if pinput == "d" and not map[pindex+1] in pcollide[0:len(pcollide)]:
    camy += 1
  if pinput == "a" and not map[pindex-1] in pcollide[0:len(pcollide)]:
    camy -= 1
  if pinput == "w" and not map[pindex-33] in pcollide[0:len(pcollide)]:
    camx -= 1
  if pinput == "s" and not map[pindex+33] in pcollide[0:len(pcollide)]:
    camx += 1
