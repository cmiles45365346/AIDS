from ecies.utils import generate_eth_key
from ecies import decrypt, encrypt
import AIDS_server
import socketserver
import socket
import threading
import time
import json
import os


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
#review time: 1668128107.0732753
    def handle(self):
        try:
            while True:
                data = self.request.recv(4096)
                data = json.loads(decrypt(server.private_key, data))
                AIDS_server.handle_request(self.request, data)
        except Exception as e:
            print("Failure occurred: {}".format(e))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):  # RW-perms from in and out of thread
    public_key = b''
    private_key = b''

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

if __name__ == "__main__":
    print(socket.gethostbyname(socket.gethostname()))
    HOST, PORT = socket.gethostbyname(socket.gethostname()), 28015

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server.private_key, server.public_key = generate_keys()
    with server:
        ip, port = server.server_address

        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        print("Server loop running in thread:", server_thread.name)

        tick_rate_ms = (1000 / 10)

        timer_start = time.time()
        next_frame = timer_start + 0.1
        while True:
            next_frame += 0.1
            # Main server loop
            if next_frame - time.time() > 0:
                time.sleep(next_frame - time.time()) # Pauses the server for time
        
        print("Server shutting down")

        server.shutdown()

'''
Make sure when launching you are launching main.py from main.py folder and AIDS_networking.py from AIDS_networking.py folder
or else Mac failure will be coming for you because you are using incorrect encryption keys.
'''