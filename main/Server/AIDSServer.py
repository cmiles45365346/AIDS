from ecies import encrypt
import socket
import json
import time


class ServerData:
    players = []
    registered = []


def send_data(ip, port, public_key, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        address = (ip, port)
        sock.sendto(encrypt(public_key, json.dumps(message).encode()), address)


def verify_key(public_key):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(encrypt(public_key, json.dumps(public_key).encode()), ('localhost', 8642))
        return True
    except:
        return False


def handle_request(request, server_data):
    try:
        if request[0] == "set_player_pos":
            if verify_key(request[3]):
                print(server_data.registered)
                if server_data.registered.__contains__(request[3]):
                    for player in server_data.players:
                        if player[0] == request[3]:
                            player[1] = int(request[1])
                            player[2] = int(request[2])
                            send_out = []
                            for player2 in server_data.players:
                                if player2[0] != request[3]:
                                    send_out.append([player2[1], player2[2]])
                            send_data(request[4], request[5], request[3], ["set_player_pos", send_out])
                            print(["set_player_pos", send_out])
                else:
                    server_data.registered.append(request[3])
                    server_data.players.append([request[3], int(request[1]), int(request[2])])
    except Exception as error:
        print("An error occurred in the server: {}".format(error))


def start(stack):
    server_info = ServerData
    while True:
        while len(stack) > 0:
            start_time = time.time()
            print('Processing request: {}'.format(stack[0]))
            handle_request(stack[0], server_info)
            print('Processed request: {} in {} seconds'.format(stack[0], time.time() - start_time))
            stack.pop(0)
        time.sleep(0.05)
