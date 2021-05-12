import socket

HOST = "127.0.0.1"
PORT = 5000


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while message := input("Insert your message here: "):
        client.send(message.encode("ascii"))

        data = client.recv(1024)

        print("Message received from the server: ", str(data.decode("ascii")))

        continueLoop = input("Continue loop (Y/N): ")

        if continueLoop.lower() == "n":
            break

    client.close()


main()
