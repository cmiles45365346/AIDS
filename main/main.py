import terrainGeneration.generalTerrain as terrain
import inputController.inputManager as playerInput
import inventory.inventoryManager as inventory
from ecies.utils import generate_eth_key
import display.screenManager as screen
import combat.combatManager as combat
from ecies import encrypt, decrypt
import socketserver
import threading
import socket
import time
import json
import os


def handle_request(request):
    if request[0] == "set_player_pos":
        server.players = request[1]


class ServerData:
    public_key = b''
    server_public_key = b''
    private_key = b''
    players = []
    send_stack = []
    sock = b''

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

def reciever():
    while True:
        data = server.sock.recv(4096)
        data = json.loads(decrypt(private_key, data))
        print("Recieved:", data)
        handle_request(data)

def sender():
    while True:
        while len(server.send_stack) > 0:
            server.sock.send(encrypt(server.server_public_key, json.dumps(server.send_stack[0]).encode()))
            server.send_stack.pop(0)
        time.sleep(0.1)

if __name__ == '__main__':
    server = ServerData
    
    print("Finished imports")
    print("starting infinite world of AIDSrpg!")
    #server_ip = '121.98.62.177'
    server_ip = '10.0.2.15'
    server_port = 28015
    with open("server_public.pem", "rt") as f:
        server.server_public_key = f.read()
    private_key, public_key = generate_keys()

    screenDimensions = 32  # cells rendered in X and Y directions
    player_x = 0
    player_y = 0
    pindex = (screenDimensions ** 2 // 2) - screenDimensions // 2
    pcollide = ["∧", "a", "E"]  # If terrain character is in this array the player cannot move onto it.
    private_key, public_key = generate_keys()
    while True:
        try:
            server.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.sock.connect((server_ip, server_port))
            break
        except Exception as e:
            print("Error occurred: {}".format(e))
    # Start a thread with the server -- that thread will then start one more thread for each request
    server_thread = threading.Thread(target=reciever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    
    server_thread = threading.Thread(target=sender)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    while True:
        currentTime = time.time()
        gameMap = terrain.generateCells(player_y, player_x, screenDimensions)
        gameMap[pindex] = "A"
        gameMap = combat.render_enemy(gameMap, screenDimensions, player_x, player_y)
        gameMap = combat.render_players(gameMap, screenDimensions, player_x, player_y, server.players)
        image = screen.createBlank(512, 1024)
        image = screen.renderScreen(image, gameMap, screenDimensions)
        image = screen.resizeScreen(image)
        screen.displayScreen(image)
        player_x, player_y = playerInput.inputController(gameMap, screenDimensions, pcollide, pindex, player_x,
                                                         player_y)
        server.send_stack.append(["set_player_pos", player_x, player_y, public_key])
        # Upload player_x and player_y to server
        # print(time.time() - currentTime)
        # time.sleep(0.05)  # forcefully sets max fps to 20 fps with no consideration of how much time passed
        # we decided combat will be turned based nad the game will run at 30 fps.
        #while len(server.data_stack) > 0:
        #    start_time = time.time()
        #    print('Processing request: {}'.format(server.data_stack[0]))
        #    handle_request(server.data_stack[0], server)
        #    print('Processed request: {} in {} seconds'.format(server.data_stack[0], time.time() - start_time))
        #    server.data_stack.pop(0)
        #    print(server.players)
        #data = server.sock.recv(1024)
        #print(data)
        time.sleep(0.05)
else:
    exit("You cannot use main as an import as it is not a library")
