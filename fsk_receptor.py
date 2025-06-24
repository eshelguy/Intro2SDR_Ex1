import numpy as np
import sounddevice as sd
from scipy.fft import fft

# General settings
sample_rate = 48000
duration = 0.1
freq_0 = 18000
freq_1 = 20000
tolerance = 80
header = '10101010'

# Detect dominant frequency in signal chunk
def detect_frequency(signal):
    n = len(signal)
    freqs = np.fft.fftfreq(n, d=1 / sample_rate)
    fft_values = fft(signal)
    peak_freq = abs(freqs[np.argmax(np.abs(fft_values))])
    return peak_freq

# Convert frequency to binary bit
def frequency_to_bit(freq):
    if abs(freq - freq_0) < tolerance:
        return '0'
    elif abs(freq - freq_1) < tolerance:
        return '1'
    else:
        return None

# Detect header and return the remaining signal
def detect_header(signal):
    bits = []
    for i in range(0, len(signal), int(sample_rate * duration)):
        segment = signal[i:i + int(sample_rate * duration)]
        freq = detect_frequency(segment)
        bit = frequency_to_bit(freq)
        if bit is not None:
            bits.append(bit)
        if ''.join(bits[-8:]) == header:
            return True, signal[i + int(sample_rate * duration):]
    return False, None

# Convert the full signal into a string
def signal_to_string(signal):
    bits = []
    for i in range(0, len(signal), int(sample_rate * duration)):
        segment = signal[i:i + int(sample_rate * duration)]
        freq = detect_frequency(segment)
        bit = frequency_to_bit(freq)
        if bit is not None:
            bits.append(bit)
    byte_string = ''.join(bits)
    return ''.join([chr(int(byte_string[i:i + 8], 2)) for i in range(0, len(byte_string), 8)])

# Record and decode the audio signal
def receive():
    print("[Listening for audio signal...]")
    duration_seconds = 20
    recording = sd.rec(int(duration_seconds * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    recording = np.squeeze(recording)

    header_found, remaining_signal = detect_header(recording)
    if header_found:
        message = signal_to_string(remaining_signal)
        print(f"[Message received]: {message}")
    else:
        print("Header not detected. No message received.")

if __name__ == "__main__":
    receive()
