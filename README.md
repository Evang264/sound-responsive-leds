# Sound-Responsive LED Light Strip

This project controls an LED light strip connected to a Raspberry Pi Zero W in response to live sound input from a server (laptop). The system analyzes sound data for pitch and volume and sends control signals wirelessly to the Raspberry Pi to animate the LED strip accordingly.

## Features
- **Live sound processing**: Records sound, analyzes pitch and volume using Fast Fourier Transform (FFT), and sends control signals in real-time.
- **Wireless communication**: Python sockets are used to send processed sound data from the laptop to the Raspberry Pi.
- **LED animation**: The Raspberry Pi receives data and controls the LED light strip based on the pitch and volume of the sound.