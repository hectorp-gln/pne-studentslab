import socket

class Client:

    def __init__(self, strIP = None, intport = None):
            self.ip = strIP
            self.port = intport

    def __str__(self):
        return "Connection to SERVER at" + str(self.ip) + ", PORT: " + str(self.port)

    def ping(self):
        print("OK")

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response



