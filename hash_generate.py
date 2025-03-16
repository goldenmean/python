

import hashlib

def generate_secure_hash(data):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # If the input is a string, encode it to bytes
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Update the hash object with the bytes-like object
    sha256_hash.update(data)

    # Get the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    # Example with a string
    input_string = "Hello, World!"
    hash_result = generate_secure_hash(input_string)
    print(f"SHA-256 hash of '{input_string}': {hash_result}")

    # Example with bytes
    input_bytes = b"Hello,  World!"
    hash_result = generate_secure_hash(input_bytes)
    print(f"SHA-256 hash of {input_bytes}: {hash_result}")


