import sounddevice as sd
import soundfile as sf

def record_audio(filename='recorded.wav', duration=5, samplerate=44100):
    print(f"[⏺] Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, recording, samplerate)
    print(f"[✓] Recording saved to {filename}")

if __name__ == "__main__":
    record_audio()
