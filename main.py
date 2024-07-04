# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=False)
    #server_socket.accept() # wait for client
    #server_socket.accept()[0].sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    
    client, addr = server_socket.accept()
    print(addr)
    data = client.recv(1024).decode()
    request_data: list[str] = data.split("\r\n")
    response: bytes = "HTTP/1.1 200 OK\r\n\r\n".encode()
    
    '''
    if request_data[0].split(" ")[1] != "/":
        response=bytes("HTTP/1.1 404 Not Found\r\n\r\n".encode())
    '''
    
    if request_data[0].split(" ")[1].startswith("/echo"):
        string=request_data[0].split(" ")[1][6:]
        response=bytes(f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(string)}\r\n\r\n{string}".encode())
        
    elif request_data[0].split(" ")[1] == "/":
        response: bytes = "HTTP/1.1 200 OK\r\n\r\n".encode()                    
    
    elif request_data[0].split(" ")[1] == "/user-agent":
        user_agent = request_data[2].split(": ")[1].strip()
        response = bytes(f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}".encode())
        
        #user_agent = next((line.split(": ")[1] for line in request_data if line.startswith("User-Agent:")), "")
        
    else:
        response=bytes("HTTP/1.1 404 Not Found\r\n\r\n".encode())
    
    client.sendall(response)
    server_socket.close()


if __name__ == "__main__":
    main()
