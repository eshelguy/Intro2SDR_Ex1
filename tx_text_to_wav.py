from afskmodem import Transmitter

def text_to_wav(text, filename='output.wav', baud=1200):
    tx = Transmitter(baud)
    tx.save(text, filename)
    print(f"[✓] Saved audio to {filename}")

if __name__ == "__main__":
    text = input("Enter text (8–32 bytes): ").strip()
    if not (8 <= len(text.encode('utf-8')) <= 32):
        print("Error: Text must be 8–32 bytes")
    else:
        text_to_wav(text)
