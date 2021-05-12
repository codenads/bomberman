import socket

from _thread import *
import threading

HOST = "127.0.0.1"
PORT = 5000

lock = threading.Lock()


def threaded(connection, address):
    print("Connected by: ", address)
    while data := connection.recv(1024):
        connection.send(data)
    print("Ending connection.")
    connection.close()
    lock.release()


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
        lock.acquire()
        start_new_thread(threaded, (connection, address))

    server.close()


main()
