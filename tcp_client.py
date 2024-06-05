import socket 

TCP_IP = "127.0.0.1"
TCP_PORT = 5007

# UDP socket client
MESSAGE = "Hello, TCP server!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode("utf-8"), (TCP_IP, TCP_PORT))

data, server = sock.recvfrom(1024)
print("received message from server, your original message was:", data.decode("utf-8"))


