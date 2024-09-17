import numpy as np

def get_loudness(audio_data, sample_rate):
    rms = np.sqrt(np.mean(np.array(audio_data)**2))
    loudness = min(1, rms * 15)
    # loudness = 20 * np.log10(rms)

    return loudness

# Example usage
audio_data = np.random.randn(44100)  # Replace with your actual audio data
sample_rate = 44100  # Replace with your actual sample rate

loudness = get_loudness(audio_data, sample_rate)
print(f"Loudness of the audio: {loudness} dB")
