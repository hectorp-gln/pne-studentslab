import socket

class Client:

    def __init__(self, strIP = None, intport = None):
            self.ip = strIP
            self.port = intport

    def __str__(self):
        return "Connection to SERVER at", str(self.ip),", PORT: ", str(self.port)

    def ping(self):
        print("OK")

    def talk(self, msg):
        MAX_OPEN_REQUESTS = 5

        number_con = 0

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((self.ip, self.port))
            # become a server socket
            # MAX_OPEN_REQUESTS connect requests before refusing outside connections
            serversocket.listen(MAX_OPEN_REQUESTS)

            while True:
                print("Waiting for connections at {}, {} ".format(self.ip, self.port))
                (clientsocket, address) = serversocket.accept()

                number_con += 1

                print("CONNECTION: {}. From the IP: {}".format(number_con, address))

                msg = clientsocket.recv(2048).decode("utf-8")
                print("Message from client: {}".format(msg))

                message = "Hello from the teacher's server\n"
                send_bytes = str.encode(message)
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(self.ip, self.port))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()



