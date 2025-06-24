
# Audio Modem – Ex1 Assignment

## Overview

This project is a simple **audio modem system** that transmits text messages using sound. It is designed as part of a computer science assignment to demonstrate digital communication via audio signals using Frequency Shift Keying (FSK).

Using this system, you can:
- Enter a short text message (8–32 characters)
- Convert the message to an audio signal (modulation)
- Transmit the audio via speakers
- Record and decode the message on another computer via microphone (demodulation)

## Features

- Binary data encoded as audio (0 → 18000 Hz, 1 → 20000 Hz)
- Transmission includes a synchronization header (`10101010`)
- Console-based interaction
- Clean and readable Python code
- Based on the open-source project by [sunw4r](https://github.com/sunw4r/audio_modem)

## 🛠Installation

### Requirements
Install Python dependencies:

```bash
pip install numpy sounddevice scipy
```

### Files
- `transmitter.py`: Sends a text message as an audio signal.
- `receiver.py`: Listens, records, and decodes an incoming audio signal into text.

## Usage

### 1. Transmitting a Message

```bash
python transmitter.py
```

You’ll be asked to input a message between 8 and 32 characters. The program will then play it through your speaker.

### 2. Receiving a Message

On a second computer (or the same one with a mic), run:

```bash
python receiver.py
```

Keep the microphone close to the speaker. The program will listen for the header and decode the message.

## How It Works

1. **Encoding:**
   - Converts each character into its ASCII binary (8 bits).
   - Each bit is mapped to a frequency:  
     `0` → 18000 Hz  
     `1` → 20000 Hz
   - Each bit is played for 0.1 seconds.

2. **Transmission:**
   - A sync header `10101010` is sent before the actual message.
   - The message is played as an audio waveform.

3. **Decoding:**
   - The receiver records audio for up to 20 seconds.
   - It detects the synchronization header.
   - Then it decodes the remaining signal bit-by-bit and converts it back to text.

## Notes

- Works best in a quiet environment.
- High-frequency tones may be filtered by some speakers or microphones.
- Message length is limited to 8–32 characters for reliability.

## Based On

This system is adapted from the original FSK audio modem implementation by [sunw4r](https://github.com/sunw4r/audio_modem).

