import socket
import sys

# Create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print ( 'starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    print( '\nwaiting to receive message' )
    data, address = sock.recvfrom(4096)
    
    print ('received %s bytes from %s' % (len(data), address) )
    print (data )
    
    if data:
       datastr = str(data,'utf-8')
       datastr = datastr + "I got your message, client..."
       data = bytes(datastr,'utf-8')
       sent = sock.sendto(data, address)
       print ('sent %s bytes back to %s' % (sent, address) )