import socket

s = socket.socket()

s.bind(("localhost", 12345))

s.listen(1)

print("Waiting for client...")

c, addr = s.accept()

print("Connected with", addr)

# receive from client
msg = c.recv(1024).decode()
print("Client:", msg)

# send custom message
reply = input("Enter message for client: ")
c.send(reply.encode())

c.close()
s.close()