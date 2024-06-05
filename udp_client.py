import socket 

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# UDP socket client
MESSAGE = "Hello, UDP server!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode("utf-8"), (UDP_IP, UDP_PORT))

data, server = sock.recvfrom(1024)
print("received message from server, your original message was:", data.decode("utf-8"))


