from ecies.utils import generate_eth_key
from ecies import decrypt
import AIDSServer
import socketserver
import socket
import threading
import json
import os


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


if __name__ == "__main__":
    print(socket.gethostbyname(socket.gethostname()))
    HOST, PORT = socket.gethostbyname(socket.gethostname()), 28015

    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)
    server.private_key, server.public_key = generate_keys()
    with server:
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()

        print("Server loop running in thread:", server_thread.name)

        AIDSServer.start(server.data_stack)

        print("Data stack at shutdown: {}".format(server.data_stack))

        server.shutdown()
