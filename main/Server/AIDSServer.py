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
        if data[0] == "set_player_pos":
            if verify_key(data[3]):
                print(server_info.registered, 'a')
                if server_info.registered.__contains__(data[3]):
                    for player in server_info.players:
                        if player[0] == data[3]:
                            player[1] = int(data[1]) + 16 # Player x
                            player[2] = int(data[2]) + 15 # Player y
                            send_out = []
                            for player2 in server_info.players:
                                if player2[0] != data[3]:
                                    send_out.append([player2[1], player2[2]])
                            send_out.append([2+16, 2+15])
                            send_data(sock, data[3], ["set_player_pos", send_out])
                            print(["set_player_pos", send_out])
                else:
                    server_info.registered.append(data[3]) # Player public key
                    server_info.players.append([data[3], int(data[1]), int(data[2])])
    except Exception as error:
        print("An error occurred in the server: {}".format(error))

if __name__ == '__main__':
    exit("Please run AIDSNetworking")
else:
    server_info = ServerData