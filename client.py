import socket
import json
from threading import Thread

HOST = "127.0.0.1"
PORT = 5000


def threaded(client):
    while data := client.recv(1024):
        json_data = json.loads(str(data.decode("ascii")))
        print("Message received from the server:", json_data)
        if json_data["player"]["life"] == False:
            print("Player died. Please type quit to exit the program.")
            print("Connection is being closed.")
            client.close()
            break


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    Thread(target=threaded, args=(client,)).start()

    while True:
        move = str(input("Insert your movement: ")).lower()
        if move in ["up", "down", "left", "right", "bomb"]:
            client.sendall(move.encode("ascii"))
        elif move == "quit":
            break

    print("Closing connection.")
    client.close()


main()
