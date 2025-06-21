# Audio Modem System – Transmit Text via Sound

This project implements a simple **audio modem** in Python that allows you to send short text messages (8–32 bytes) using sound. The message is encoded into an audio waveform, transmitted over speakers, received by a microphone on another computer, and decoded back into the original text.

---

## Features

- Converts text (8–32 bytes) into audio using **AFSK (Audio Frequency-Shift Keying)**
- Plays the audio on one computer (or speaker)
- Records the audio on another computer (or microphone)
- Decodes the audio waveform back into the original text
- Based on open-source modem logic from [`lavajuno/afskmodem`](https://github.com/lavajuno/afskmodem)

---

## Project Structure

```
.
├── afskmodem/               # Local copy of AFSK modem code (from lavajuno/afskmodem)
├── tx_text_to_wav.py        # Translates input text to audio file
├── play_audio.py            # Plays audio file via speaker
├── record_audio.py          # Records audio via mic to a file
├── rx_wav_to_text.py        # Decodes audio file to text
├── requirements.txt
└── README.md
```

---

## How It Works

1. The user enters a short message (8–32 bytes).
2. The `tx_text_to_wav.py` script uses **AFSK modulation** to save the message as an audio file.
3. The `play_audio.py` script plays the waveform via speaker.
4. On the receiving computer, `record_audio.py` records the sound to a WAV file.
5. Finally, `rx_wav_to_text.py` decodes the audio file and prints the original message.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/audio-modem.git
cd audio-modem
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install numpy scipy sounddevice soundfile
```

---

## 🛠 Setup of `afskmodem`

This project uses a local version of [`lavajuno/afskmodem`](https://github.com/lavajuno/afskmodem) because it is **not pip-installable**.

### To use it:
1. Clone it:
   ```bash
   git clone https://github.com/lavajuno/afskmodem.git
   ```
2. Copy the folder into this project:
   ```bash
   cp -r afskmodem ./audio-modem/
   ```

Now the structure should look like:

```
audio-modem/
├── afskmodem/
├── tx_text_to_wav.py
├── ...
```

### In your scripts, make sure you import like this:

```python
from afskmodem.transmit import Transmitter
from afskmodem.receive import Receiver
```

---

## How to Use

### ▶Transmit Side (Computer A)

1. Encode the message to audio:
   ```bash
   python tx_text_to_wav.py
   ```
   _(Enter a short message when prompted)_

2. Play it:
   ```bash
   python play_audio.py
   ```

### 🎙 Receive Side (Computer B)

1. Record audio:
   ```bash
   python record_audio.py
   ```

2. Decode it:
   ```bash
   python rx_wav_to_text.py
   ```

---

## requirements.txt

```
numpy
scipy
sounddevice
soundfile
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## Credits

- AFSK modem logic by [lavajuno/afskmodem](https://github.com/lavajuno/afskmodem)
---

## 📄 License

This project is released under the **MIT License** and includes source code adapted from `afskmodem`, which is also MIT-licensed.
