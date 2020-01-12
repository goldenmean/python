import socket
import sys

#https://pymotw.com/2/socket/udp.html
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message from client.  It will be repeated.'

try:

    # Send data
    print('sending "%s"' % message)
    sent = sock.sendto(bytes(message,'utf-8'), server_address)

    # Receive response
    print ('waiting to receive')
    data, server = sock.recvfrom(4096)
    print ( 'received "%s"' % data)

finally:
    print ('closing socket')
    sock.close()