import sounddevice as sd
import soundfile as sf

def play_audio(filename='output.wav'):
    data, samplerate = sf.read(filename)
    sd.play(data, samplerate)
    sd.wait()
    print(f"[✓] Played {filename}")

if __name__ == "__main__":
    play_audio()
