import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 7805 #if the port is used by some other service or access to that is blocked python gives error
#OSError: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print("Received message: ", data)
    #print("received message:   From %s" %(data, addr) )
    #print("received message {} from {}".format(data, addr))
    print("received message", data, "from ",addr);