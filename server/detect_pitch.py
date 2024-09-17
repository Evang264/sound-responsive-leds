import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def detect_pitch(wav_data, sample_rate):
    # Perform FFT
    n = len(wav_data)
    frequencies = fftfreq(n, d=1/sample_rate)
    spectrum = fft(wav_data)

    # Get the magnitude spectrum (ignore negative frequencies)
    magnitude_spectrum = np.abs(spectrum[:n//2])

    # Find peaks in the magnitude spectrum
    peaks, _ = find_peaks(magnitude_spectrum, height=0.1)  # Adjust the height parameter as needed

    # Find the corresponding frequencies of the peaks
    pitch_frequencies = frequencies[peaks]

    # Select the dominant pitch frequency
    dominant_pitch_frequency = pitch_frequencies[np.argmax(magnitude_spectrum[peaks])]

    return dominant_pitch_frequency