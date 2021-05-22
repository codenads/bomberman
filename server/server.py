import socket
import uuid
from threading import Thread
from server.player import Player
from server.map import Map

HOST = "127.0.0.1"
PORT = 5000


def threaded(connection, address, map):
    print(f"Connected by: {address}")
    username = uuid.uuid4()
    player = Player(0, 0, username)
    while data := connection.recv(1024):
        player.move(data.decode("ascii"), map)
        connection.send(data)
    print(f"{address} is ending the connection.")
    connection.close()


def server_init():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
    except Exception:
        print("Could not bind the server to {}:{}".format(HOST, PORT))
        return -1
    try:
        server.listen(4)
    except Exception:
        print("Could not put the server into listening mode.")
        return -1

    return server


def main():
    server = server_init()
    if server == -1:
        return
    map = Map()
    print("Wait for a client attempt to connect...")

    while True:
        connection, address = server.accept()
        Thread(target=threaded, args=(connection, address, map)).start()

    close()


main()
