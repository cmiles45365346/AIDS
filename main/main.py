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
        players = request[1]


def send_data(ip, port, receivers_public_key, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        address = (ip, port)
        sock.sendto(encrypt(receivers_public_key, json.dumps(message).encode()), address)


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            data = json.loads(decrypt(server.private_key, self.request[0]))
            server.data_stack.append(data)
            print(server.data_stack)
        except Exception as e:
            print("Failure occurred: {}".format(e))


class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):  # RW-perms from in and out of thread
    public_key = b''
    private_key = b''
    data_stack = []


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
    # server_ip = '121.98.62.177'
    # server_port = 28015
    server_ip = '10.0.2.15'
    server_port = 28015
    my_ip = 'profile-replication.at.playit.gg'
    my_port = 33653
    HOST = 'localhost'
    PORT = 5000
    with open("server_public.pem", "rt") as f:
        server_public_key = f.read()
    private_key, public_key = generate_keys()

    screenDimensions = 32  # cells rendered in X and Y directions
    player_x = 0
    player_y = 0
    pindex = (screenDimensions ** 2 // 2) - screenDimensions // 2
    pcollide = ["∧", "a", "E"]  # If terrain character is in this array the player cannot move onto it.
    players = []
    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)
    server.private_key, server.public_key = generate_keys()
    with server:
        # Start a thread with the server -- that thread will then start one more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()

        print("Server loop running in thread:", server_thread.name)

        while True:
            currentTime = time.time()
            gameMap = terrain.generateCells(player_y, player_x, screenDimensions)
            gameMap[pindex] = "A"
            gameMap = combat.render_enemy(gameMap, screenDimensions, player_x, player_y)
            gameMap = combat.render_players(gameMap, screenDimensions, player_x, player_y, players)
            image = screen.createBlank(512, 1024)
            image = screen.renderScreen(image, gameMap, screenDimensions, players)
            image = screen.resizeScreen(image)
            screen.displayScreen(image)
            player_x, player_y = playerInput.inputController(gameMap, screenDimensions, pcollide, pindex, player_x,
                                                             player_y)
            send_data(server_ip, server_port, server_public_key, ["set_player_pos", player_x, player_y, public_key, my_ip,
                                                                  my_port])
            # Upload player_x and player_y to server
            # print(time.time() - currentTime)
            time.sleep(0.05)  # forcefully sets max fps to 20 fps with no consideration of how much time passed
            # we decided combat will be turned based nad the game will run at 30 fps.
            while len(server.data_stack) > 0:
                start_time = time.time()
                print('Processing request: {}'.format(server.data_stack[0]))
                handle_request(server.data_stack[0])
                print('Processed request: {} in {} seconds'.format(server.data_stack[0], time.time() - start_time))
                server.data_stack.pop(0)
                print(players)
        server.shutdown()
else:
    exit("You cannot use main as an import as it is not a library")
