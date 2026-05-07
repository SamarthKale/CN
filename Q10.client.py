import socket

s = socket.socket()
s.connect(('localhost', 5000))

while True:
    msg = input("Client: ")
    s.send(msg.encode())
    print("Server:", s.recv(1024).decode())


# Socket Programming using TCP

# What is Socket Programming?
# Socket programming is a way to establish communication between two computers over a network using sockets.

# What is a Socket?
# A socket is a combination of:
# - IP Address
# - Port Number

# Example:
# 192.168.1.10 : 8080


# Steps in Socket Programming

# Server Side
# 1. Create socket
# 2. Bind IP address and port
# 3. Listen for connection
# 4. Accept client connection
# 5. Send/Receive data
# 6. Close connection

# Client Side
# 1. Create socket
# 2. Connect to server
# 3. Send/Receive data
# 4. Close connection


# TCP Three-Way Handshake

# The TCP three-way handshake is used to establish a reliable connection between client and server before data transfer.

# Steps:
# 1. Client sends SYN
# 2. Server replies with SYN-ACK
# 3. Client sends ACK

# After this, the connection is established and data transfer begins.
