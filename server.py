import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 5000


def threaded(connection, address):
    print(f"Connected by: {address}")
    while data := connection.recv(1024):
        connection.send(data)
    print(f"{address} is ending the connection.")
    connection.close()


def server_init():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(4)
    return server


def main():
    server = server_init()
    print("Wait for a client attempt to connect...")

    while True:
        connection, address = server.accept()
        Thread(target=threaded, args=(connection, address)).start()

    server.close()


main()
