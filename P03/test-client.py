from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP,PORT)

commands_list = ["PING", "GET", "INFO", "COMP", "REV", "GENE"]
GET_0 = "TGAGGACCGACGGTTAATAG"
for command in commands_list:
    print(command)
    if command == "GET":
        print(f"* Testing {command.split()[0]} . . .")
        for n in range(0,5):
            response = c.talk(command + " " + str(n))
            print(command + " " + str(n) + ":" + response)
    elif command == "INFO" or command == "COMP" or command == "REV":
        print(f"* Testing {command.split()[0]} . . .")
        print(command + ": "+ GET_0)
        response = c.talk(command + " " + GET_0)
        print(response)
    elif command == "GENE":
        list_files = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
        print(f"* Testing {command.split()[0]} . . .")
        for GENE_name in list_files:
            print(f"Testing {GENE_name} . . .")
            response = c.talk(command + " " + GENE_name)
            print(response)
    else:
        print(f"* Testing {command.split()[0]} . . .")
        response = c.talk(command)
        print(response)