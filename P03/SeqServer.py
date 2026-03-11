import socket
from Seq1 import Seq
from Client0 import Client
import termcolor

IP = "127.0.0.1"
PORT = 8080

sequences_list = ["TGAGGACCGACGGTTAATAG","ACCGTGTGGGTCTATACAGT","CTGTAGAGAGCAGTGTTGGG","CAACACTGAGGCCAGTAATA","CCATTAATGGTCTGGAATTC"]

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #This line makes it so there is no issues with the port
ls.bind((IP,PORT))
ls.listen()
print("The server is running")

while True:
    print("Waiting for a client to connect...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        message_raw = cs.recv(2048)
        message = message_raw.decode()
        command = message.strip().split(" ",1)
        command_type = command[0]

        if len(command) > 1:
                argument = command[1]

        if command_type == "PING":
            message = "OK!"
        elif command_type == "GET":
            message = str(sequences_list[int(argument)])
        elif command_type == "INFO":
            s = Seq(argument)
            a_count = s.count_base("A")
            c_count = s.count_base("C")
            g_count = s.count_base("G")
            t_count = s.count_base("T")
            total_count = a_count + c_count + g_count + t_count

            message = "Sequence:" + argument + "\n" + "Total length:" + str(len(argument)) + "\n"
            message += "A: " + str(a_count) + " (" + str(round(a_count / total_count * 100,2)) + "%)" + "\n"
            message += "C: " + str(c_count) + " (" + str(round(c_count / total_count * 100,2)) + "%)" + "\n"
            message += "G: " + str(g_count) + " (" + str(round(g_count / total_count * 100,2)) + "%)" + "\n"
            message += "T: " + str(t_count) + " (" + str(round(t_count / total_count * 100,2)) + "%)" + "\n"

        elif command_type == "COMP":
            s = Seq(argument)
            message = str(s.complement())
        elif command_type == "REV":
            s = Seq(argument)
            message = str(s.reverse())
        elif command_type == "GENE":
            list_files = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
            if argument in list_files:
                s = Seq()
                message = s.read_fasta("sequences/" + argument + ".txt")
            else:
                message = "Gene not valid"
        else:
            message = "NOT A VALID COMMAND"

        message += "\n"
        termcolor.cprint(str(command_type) + " command!", "green")
        print(message)
        cs.send(message.encode())

        cs.close()