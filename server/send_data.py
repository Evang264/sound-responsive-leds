import socket

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(('192.168.12.2', 12233))  # Replace with your Raspberry Pi's IP address

    # Send a message
    while True:
        msg = int(input("Enter your int: "))
        if not msg:
            break
        client_socket.send(msg.encode())

finally:
    # Close the connection and socket in the finally block to ensure it happens even if an exception occurs
    client_socket.close()
