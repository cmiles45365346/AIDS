import terrainGeneration.generalTerrain as terrain
import inventoryManager.inventory as inventory
import displayController.screen as screen
import cv2

print("starting infinite world of AIDSrpg!")

camx = 0
camy = 0
pindex = 496
pcollide = ["∧", "🏠"]  # If terrain character is in this array the player cannot move onto it.

while True:
    map = terrain.generateCells(camy, camx)
    map[pindex] = "A"
    for y in range(32):
        print(str(map[0 + (y * 32):32 + (y * 32)]).replace("\'", "", 99999).replace(",", "", 99999).replace("[",
                                                                                                            "|").replace(
            "]", "|"))  # Displays map to console
    pinput = input() + "m"
    pinput = pinput[0].lower()
    if pinput == "q":
        exit("game shut down")
    if pinput == "d" and not map[pindex + 1] in pcollide[0:len(pcollide)]:
        camx += 1
    if pinput == "a" and not map[pindex - 1] in pcollide[0:len(pcollide)]:
        camx -= 1
    if pinput == "w" and not map[pindex - 32] in pcollide[0:len(pcollide)]:
        camy -= 1
    if pinput == "s" and not map[pindex + 32] in pcollide[0:len(pcollide)]:
        camy += 1
    if pinput == "e":
        pass
