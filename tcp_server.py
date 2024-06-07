## UDP Socket server 

import socket

# UDP socket server
TCP_IP = "127.0.0.1"
TCP_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))

print("TCP server up and listening")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Address of client is {addr}")
    message = data.decode("utf-8")
    print("Hey client your message was received ok!:", message)

    # send echo
    sock.sendto(data, addr)








   

