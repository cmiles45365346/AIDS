from ecies import encrypt
import socket
import json
import time


class ServerData:
    players = []
    registered = []


def send_data(sock, public_key, message):
    sock.sendall(encrypt(public_key, json.dumps(message).encode()))


def verify_key(public_key):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(encrypt(public_key, json.dumps(public_key).encode()), ('localhost', 8642))
        return True
    except:
        return False


def handle_request(sock, data):
    try:
        if verify_key(data[1]):
            if data[0] == "set_player_pos":
                    if server_info.registered.__contains__(data[1]):
                        for player in server_info.players:
                            if player[0] == data[1]:
                                player[1] = int(data[2]) + 16 # Player x
                                player[2] = int(data[3]) + 15 # Player y
                                send_out = []
                                for player2 in server_info.players:
                                    if player2[0] != data[1]:
                                        send_out.append([player2[1], player2[2]])
                                send_data(sock, data[1], ["set_player_pos", send_out])
                    else:
                        server_info.registered.append(data[1]) # Player public key
                        server_info.players.append([data[1], int(data[2]), int(data[3])])
            elif data[0] == "cast_fireball":
                print("Player casted fireball")
                pass
    except Exception as error:
        print("An error occurred in the server: {}".format(error))

if __name__ == '__main__':
    exit("Please run AIDSNetworking")
else:
    server_info = ServerData