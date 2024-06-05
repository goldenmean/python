











import json

def parse_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


import socket

def establish_socket_connection(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock


def serialize_data(data):
    # Serialize the data to a JSON formatted string
    serialized_data = json.dumps(data)

# Example JSON data
#data = {"id": 2, "name": "abc"}


def send_data(sock, data):
    # Serialize data if needed
    serialized_data = serialize_data(data)
    sock.sendall(serialized_data.encode())


def deserialize_data(data):
    # Deserialize the data from a JSON formatted string
    deserialized_data = json.loads(data)
    return deserialized_data

def verify_response(data):
    # Verify the response
    if data["id"] == 2 and data["name"] == "abc":
        print("Response verified successfully")
    else:
        print("Response verification failed")


def receive_response(sock):
    data = b''
    while True:
        packet = sock.recv(4096)
        if not packet:
            break
        data += packet
    # Deserialize and verify response
    deserialized_data = deserialize_data(data.decode())
    verify_response(deserialized_data)   


def main():
    json_file_path = "path/to/your/json/file.json"
    host = "hardware_board_ip_address"
    port = 12345  # Assuming the radio software listens on port 12345

    # Parse JSON data
    iq_symbols = parse_json_data(json_file_path)

    # Establish socket connection
    sock = establish_socket_connection(host, port)

    try:
        # Send IQ symbols to the radio software
        for symbol in iq_symbols:
            send_data(sock, symbol)
            
            # Optionally, wait for a response after sending each symbol
            receive_response(sock)
    finally:
        sock.close()

if __name__ == "__main__":
    main()