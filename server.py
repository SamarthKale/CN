import socket

s = socket.socket()
s.bind(('localhost', 5000,))
s.listen(1)

c, addr = s.accept()

while True:
    print("Client:", c.recv(1024).decode())
    msg = input("You: ")
    c.send(msg.encode())
