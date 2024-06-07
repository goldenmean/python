import socket 

TCP_IP = "127.0.0.1"
TCP_PORT = 6000

# TCP socket client
MESSAGE = "Hello, TCP server!"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT)) #Establish a connection to server
sock.send(MESSAGE.encode("utf-8"))

data = sock.recv(1024)
print("received message from server, your original message was:", data.decode("utf-8"))





