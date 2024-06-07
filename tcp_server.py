## TCP Socket server 

import socket
import sys
import signal 


def close_server(server_socket):
    """Close the server socket."""
    server_socket.shutdown(socket.SHUT_RDWR)
    server_socket.close()

#Signal Handler is not working as pressing CTRL-C/CTRL-D is not invoking this handler
def signal_handler(sig, frame):
    """Handle SIGINT signal."""
    print('\nClosing server...')
    close_server(sock)
    sys.exit(0)



# TCP socket server
TCP_IP = "127.0.0.1"
TCP_PORT = 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)  # Listen for incoming connections

print("TCP server up and listening")
# Register signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)


try: 
    while True:
        conn, addr = sock.accept()  # Accept incoming connection
        data = conn.recv(1024)
        message = data.decode("utf-8")
        print("Hey client your message was received ok!:", message)

        # send echo
        conn.sendall(data)
        conn.close()

except KeyboardInterrupt: # The KeyboardInterrupt exception is Not being raised on pressing CTRL-C/D
    print("Closing server")
    sock.close()
    sys.exit(0)










   

