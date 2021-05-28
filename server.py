import socket
import json
from threading import Thread
from server.player import Player
from server.map import Map

HOST = "127.0.0.1"
PORT = 5000


def threaded(connection, address, map, id):
    print(f"Connected by: {address}")

    username = f"Player {id}"
    player = Player(0, 0, username)
    map.players.append(player)

    while data := connection.recv(1024):
        player.move(data.decode("ascii"), map)
        json_data = json.dumps(
            {
                "player": {
                    "username": player.username,
                    "life": player.life,
                    "position": (player.x, player.y),
                },
                "map": json.dumps(map.path),
            }
        ).encode("ascii")
        connection.send(json_data)

    print(f"{address} is closing connection.")
    connection.close()


def server_init():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
    except Exception:
        print("Could not bind the server to {}:{}".format(HOST, PORT))
        return None
    try:
        server.listen(4)
    except Exception:
        print("Could not put the server into listening mode.")
        return None

    return server


def main():
    count = 1
    server = server_init()
    if not server:
        return
    map = Map()
    print("Wait for a client attempt to connect...")

    while True:
        connection, address = server.accept()
        Thread(target=threaded, args=(connection, address, map, count)).start()
        count += 1

    close()


main()
