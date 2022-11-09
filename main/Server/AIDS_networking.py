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
    print("---You are running a modified version of Decentranet---")
    print("Never share your private key doing so will compromise the security of your server")
    print("You may share your public key freely to invite people to connect to your private server")

    # Read old pair if one does exist
    if os.path.exists("private.pem") and os.path.exists("public.pem"):
        with open("private.pem", "rt") as f:
            private_key = f.read()
            f.close()
        with open("public.pem", "rt") as f:
            public_key = f.read()
            f.close()
        print("Using old key delete private.pem or public.pem and run this program again to generate a new pair")
        print("Do not delete private.pem or public.pem unless required")
    else:  # Generate new pair if one doesn't exist
        key_pair = generate_eth_key()
        public_key = key_pair.public_key.to_hex()  # hex string
        private_key = key_pair.to_hex()  # hex string

        with open("private.pem", "wt") as f:
            f.write(private_key)
            f.close()

        with open("public.pem", "wt") as f:
            f.write(public_key)
            f.close()

        print("Created new key you now have a new identity")
    # print(f"{private_key}\n{public_key}")
    return private_key, public_key

#review time: 1668128107.0732753
#def client(ip, port, public_key, message):
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#       sock.connect((ip, port))
#       sock.send(encrypt(public_key, json.dumps(message).encode()))

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
       
        time.sleep(3600) # Run the server for 1 hour then shut the server down when there are no requests left
        
        print("Server shutting down")

        server.shutdown()
