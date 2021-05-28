# Bomberman
## A bomberman socket application
### Bomberman implementation using a threaded client - server socket, supporting up to a maximum of 4 connections.

Created by: Kelly Bianca Araujo Silva (@kellybianca) and Luis Antônio da Silva Nascimento (@codenads)

To execute this project you have to follow this eteps:

1. Install [Python3](https://www.python.org/downloads/) in your computer

2. Clone this repository
```
git clone https://github.com/codenads/bomberman.git
```
```
cd bomberman
```
2. Execute the server
```
python3 server.py 
```
or 
```
python server.py 
```
3. Execute the client
```
python3 client.py
```
or
```
python client.py
```
To start this game, you have to input this commands:
moviment | description
---------|-----------
up | move to up
down | move to down
left | move to left
right | move to right
bomb | throw a bomb

One of the features that could be implemented would be the integration with pygames.

The difficulties faced were sending all data to all server connections.

We use the socket functions in our application:
* socket() -> receive a host and a door
* close() -> Mark the socket closed
* listen() -> Enable a server to accept connections
* accept() -> Accept a connection
* bind() -> Bind the socket to address
* recv() -> Receive data from the socket
* connect() -> Connect to a remote socket at address

Here is the [documentation](https://docs.python.org/3/library/socket.html) about python3 with socket
