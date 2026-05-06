import socket

s = socket.socket()

s.connect(("localhost", 12345))

# send custom message
msg = input("Enter message for server: ")
s.send(msg.encode())

# receive from server
reply = s.recv(1024).decode()
print("Server:", reply)

s.close()