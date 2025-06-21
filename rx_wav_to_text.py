from afskmodem import Receiver

def wav_to_text(filename='output.wav', baud=1200):
    rx = Receiver(baud)
    result = rx.load(filename, string=True)
    print(f"[✓] Decoded message: {result}")

if __name__ == "__main__":
    wav_to_text()
