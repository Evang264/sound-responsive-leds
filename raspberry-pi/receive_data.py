import socket
import colorsys
from control_led import *

def pitch_to_rgb(pitch):
    # Map pitch to hue value (assuming pitch is in a specific range, adjust as needed)
    hue = (pitch % 1000) / 1000.0  # Adjust 1000 as needed based on your pitch range

    # Convert hue to RGB
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

    # Scale RGB values to the range [0, 255]
    scaled_rgb = [int(val * 255) for val in rgb]

    return scaled_rgb

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
colors = [(0, 0, 0)] * 60

try:
    set_color(0, 100, 100, 100)
    strip.show()

    server_socket.bind(('0.0.0.0', 12233))  # Replace with your desired port
    server_socket.listen(1)

    print("Waiting for connection...")
    connection, address = server_socket.accept()
    print("Connected by", address)

    while True:
        # Receive and print the data
        data = connection.recv(1024)
        if data:
            print(data.decode())
            try:
                pitch, loudness = data.decode().split(' ')
            except:
                continue
            pitch = int(pitch)
            loudness = float(loudness)
            # print("Received:", data)
            rgb = pitch_to_rgb(pitch)
            rgb[0] = int(rgb[0] * loudness)
            rgb[1] = int(rgb[1] * loudness)
            rgb[2] = int(rgb[2] * loudness)
            colors.pop()
            colors.insert(0, rgb)
            
            for i in range(0, 60):
                set_color(i, colors[i][0], colors[i][1], colors[i][2])
                # strip.setPixelColor(i, Color(rgb[0], rgb[1], rgb[2]))

            strip.show()

finally:
    # Close the connection and socket in the finally block to ensure it happens even if an exception occurs
    connection.close()
    server_socket.close()
    colorWipe()
