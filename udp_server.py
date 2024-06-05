## UDP Socket server 

import socket

# UDP socket server
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("UDP server up and listening")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Address of client is {addr}")
    message = data.decode("utf-8")
    print("Hey client your message was received ok!:", message)

    # send echo
    sock.sendto(data, addr)








   

