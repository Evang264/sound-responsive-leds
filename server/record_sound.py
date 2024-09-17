import sounddevice as sd
# import matplotlib.pyplot as plt
import numpy as np
import socket
from detect_pitch import detect_pitch
from detect_loudness import get_loudness

SLEEP_TIME = 500 # ms
SAMPLE_RATE = 48_000
TIME = 48_000 // 20  # 50 ms

i = 0
tot = []

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(('192.168.12.18', 12233))  # Replace with your Raspberry Pi's IP address

    def callback(indata: np.ndarray, frames, time, status):
        if status:
            print(status)
        # print(indata.shape)
        # print(np.array(indata))

        avg = np.mean(indata, axis=1)

        global tot
        tot += list(avg)
        if TIME < len(tot):
            pitch = int(detect_pitch(tot[: TIME], SAMPLE_RATE))
            loudness = get_loudness(tot[: TIME], SAMPLE_RATE)
            print(loudness)
            client_socket.send(f"{pitch} {loudness}".encode())
            tot = tot[TIME:]


    stream = sd.InputStream(callback=callback, channels=2)
    with stream:
        input("press any key to stop.")
finally:
    client_socket.close()

# tot = np.array(tot)

# for i in range(0, tot.size - TIME, TIME):
#     print(detect_pitch(tot[i:min(i+TIME, tot.size)], SAMPLE_RATE))

# # plt.scatter(x=np.linspace(0, 1, tot.size), y=tot)
# # plt.show()