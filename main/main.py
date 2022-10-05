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
        data = json.loads(decrypt(server.private_key, data))
        # print("Recieved:", data)
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
    
    server_ip = '10.0.2.15'
    server_port = 28015
    with open("server_public.pem", "rt") as f:
        server.server_public_key = f.read()
    server.private_key, server.public_key = generate_keys()
    
    while True:
        try:
            server.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.sock.connect((server_ip, server_port))
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
        player_x, player_y = playerInput.input_controller(terrain, screen_dimensions, player_collides_with,  player_position, player_x,
                                                         player_y)
        server.send_stack.append(["set_player_pos", server.public_key, player_x, player_y])
        # Upload player_x and player_y to server
        # print("Ran loop in: {:.3f} seconds".format(time.time() - current_time))
        time.sleep(0.05)
else:
    server = ServerData # Give server to external python files