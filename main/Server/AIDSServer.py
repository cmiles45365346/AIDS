from ecies import encrypt
import socket
import json
import time


def send_data(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        address = (ip, port)
        with open("public.pem", "rt") as f:
            public_key = f.read()
        sock.sendto(encrypt(public_key, bytes(json.dumps(message).encode())), address)


def handle_request(request):
    if request[0] == "set_player_pos":
        pass


def start(stack):
    while True:
        while len(stack) > 0:
            start_time = time.time()
            print('Processing request: {}'.format(stack[0]))
            handle_request(stack[0])
            print('Processed request: {} in {} seconds'.format(stack[0], time.time() - start_time))
            stack.pop(0)
        time.sleep(0.1)
