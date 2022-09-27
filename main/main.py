import terrainGeneration.generalTerrain as terrain
import inputController.inputManager as playerInput
import inventory.inventoryManager as inventory
from ecies.utils import generate_eth_key
import display.screenManager as screen
from ecies import encrypt
import socket
import time
import json
import os


def send_data(ip, port, receivers_public_key, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        address = (ip, port)
        sock.sendto(encrypt(receivers_public_key, json.dumps(message).encode()), address)


def generate_keys():
    print("---You are running a modified version of Decentranet---")
    print("Never share your private key doing so will compromise the security of your server")
    print("You may share your public key freely to invite people to connect to your private server")

    # Read old pair if one does exist
    if os.path.exists("private.pem") and os.path.exists("public.pem"):
        with open("private.pem", "rt") as f:
            priv_key = f.read()
            f.close()
        with open("public.pem", "rt") as f:
            pub_key = f.read()
            f.close()
        print("Using old key delete private.pem or public.pem and run this program again to generate a new pair")
        print("Do not delete private.pem or public.pem unless required")
    else:  # Generate new pair if one doesn't exist
        key_pair = generate_eth_key()
        pub_key = key_pair.public_key.to_hex()  # hex string
        priv_key = key_pair.to_hex()  # hex string

        with open("private.pem", "wt") as f:
            f.write(priv_key)
            f.close()

        with open("public.pem", "wt") as f:
            f.write(pub_key)
            f.close()

        print("Created new key you now have a new identity")
    # print(f"{private_key}\n{public_key}")
    return priv_key, pub_key


if __name__ == '__main__':
    print("Finished imports")
    print("starting infinite world of AIDSrpg!")

    # Server stuff
    server_ip = '127.0.0.1'
    server_port = 5000
    with open("server_public.pem", "rt") as f:
        server_public_key = f.read()
    private_key, public_key = generate_keys()

    screenDimensions = 32  # cells rendered in X and Y directions
    player_x = 0
    player_y = 0
    pindex = (screenDimensions ** 2 // 2) - screenDimensions // 2
    pcollide = ["∧", "a", "E"]  # If terrain character is in this array the player cannot move onto it.

    while True:
        currentTime = time.time()
        gameMap = terrain.generateCells(player_y, player_x, screenDimensions)
        gameMap[pindex] = "A"
        image = screen.createBlank(512, 512)
        image = screen.renderScreen(image, gameMap, screenDimensions)
        screen.displayScreen(image)
        player_x, player_y = playerInput.inputController(gameMap, screenDimensions, pcollide, pindex, player_x, player_y)
        send_data(server_ip, server_port, server_public_key, ["set_player_pos", player_x, player_y, public_key])
        # Upload player_x and player_y to server
        # print(time.time() - currentTime)
        # time.sleep(0.05) # forcefully sets max fps to 20 fps with no consideration of how much time passed
        # we decided combat will be turned based nad the game will run at 30 fps.
else:
    exit("You cannot use main as an import as it is not a library")