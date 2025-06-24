import numpy as np
import sounddevice as sd

# General settings
sample_rate = 48000  # Sample rate
duration = 0.1       # Duration of each bit in seconds
freq_0 = 18000       # Frequency for bit 0 (Hz)
freq_1 = 20000       # Frequency for bit 1 (Hz)
header = '10101010'  # Synchronization pattern (8-bit alternating sequence)

# Generate a sine wave tone for a specific bit
def generate_tone(bit):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    if bit == '1':
        return np.sin(2 * np.pi * freq_1 * t)
    else:
        return np.sin(2 * np.pi * freq_0 * t)

# Convert string to audio signal (bit by bit)
def string_to_signal(data):
    signal = np.concatenate([generate_tone(bit) for byte in data for bit in format(ord(byte), '08b')])
    return signal

# Transmit the signal via speaker
def transmit(data):
    print("[Transmitting...]")
    header_signal = np.concatenate([generate_tone(bit) for bit in header])
    data_signal = string_to_signal(data)
    full_signal = np.concatenate((header_signal, data_signal))
    sd.play(full_signal, samplerate=sample_rate)
    sd.wait()
    print("[Transmission complete]")

if __name__ == "__main__":
    text = input("Enter the message to transmit (8–32 characters): ")
    if 8 <= len(text) <= 32:
        transmit(text)
    else:
        print("Message must be between 8 and 32 characters.")
