import terrain_generation.general_terrain as terrain_generator
import input_controller.input_manager as playerInput
from ecies.utils import generate_eth_key
import display.screen_manager as screen
import combat.combat_manager as combat
from ecies import encrypt, decrypt
import threading
import socket
import time
import json
import os

class ServerData:
    public_key = b''
    server_public_key = b''
    private_key = b''
    players = []
    send_stack = []
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#review time: 1668128107.0732753
def generate_keys():
    def write_keys(public_key, private_key):
        with open("private.pem", "wt") as f:
            f.write(private_key)
            f.close()

        with open("public.pem", "wt") as f:
            f.write(public_key)
            f.close()

    def read_keys():
        with open("private.pem", "rt") as f:
            private_key = f.read()
            f.close()
        with open("public.pem", "rt") as f:
            public_key = f.read()
            f.close()
        return private_key, public_key

    # Read old pair if one does exist
    if os.path.exists("private.pem") and os.path.exists("public.pem"):
        print("Using old keys")
        return read_keys()
    else:  # Generate new pair if one doesn't exist
        key_pair = generate_eth_key()
        public_key = key_pair.public_key.to_hex()  # hex string
        private_key = key_pair.to_hex()  # hex string

        write_keys(public_key, private_key)

        print("Created new key you now have a new identity")
    return private_key, public_key

#review time: 1668128107.0732753
def reciever():
    while True:
        data = server.socket.recv(4096)
        data = json.loads(decrypt(server.private_key, data).decode())
        # print("Recieved:", data)
        handle_request(data)

def handle_request(request):
    if request[0] == "set_player_pos":
        server.players = request[1]

#review time: 1668128107.0732753
def sender():
    while True:
        try:
            while len(server.send_stack) > 0:
                server.socket.send(encrypt(server.server_public_key, json.dumps(server.send_stack[0]).encode()))
                server.send_stack.pop(0)
                print(server.send_stack)
        except Exception as e:
            pass
        time.sleep(0.1)

if __name__ == '__main__':
    server = ServerData
    
    print("Finished imports")
    print("starting infinite world of AIDSrpg!")
    
    server_ip = '192.168.1.17'
    server_port = 28015
    with open("server_public.pem", "rt") as f:
        server.server_public_key = f.read()
    server.private_key, server.public_key = generate_keys()
    
    while True:
        try:
            server.socket.connect((server_ip, server_port))
            break
        except Exception as e:
            print("Error occurred: {}".format(e))

    screen_dimensions = 32  # cells rendered in X and Y directions
    player_x = 0
    player_y = 0
    player_position = (screen_dimensions ** 2 // 2) - screen_dimensions // 2
    player_collides_with = ["∧", "a", "E"]  # If terrain character is in this array the player cannot move onto it.
    
    # Handle information coming in from the server
    reciever_thread = threading.Thread(target=reciever)
    reciever_thread.daemon = True
    reciever_thread.start()
    
    # Handle information going to the server
    sender_thread = threading.Thread(target=sender)
    sender_thread.daemon = True
    sender_thread.start()
    
    combat.enemies = combat.generate_enemy(player_x, player_y)
    while True:
        current_time = time.time()
        terrain = terrain_generator.generate_cells(player_y, player_x, screen_dimensions)
        terrain[player_position] = "A"
        terrain = combat.render_enemies(terrain, screen_dimensions, player_x, player_y)
        terrain = combat.render_players(terrain, screen_dimensions, player_x, player_y, server.players)
        image = screen.create_blank_image(512, 1024)
        image = screen.render_screen(image, terrain, screen_dimensions)
        image = screen.resize_screen(image)
        screen.display_screen(image)
        player_x, player_y, server.send_stack = playerInput.input_controller(terrain, screen_dimensions, player_collides_with,  player_position, player_x,
                                                         player_y, server.send_stack, server.public_key)
        server.send_stack.append(["set_player_pos", server.public_key, player_x, player_y])
        time.sleep(0.1)
        server.send_stack = [] # Prevents crash from too much data I'm bad programmer
