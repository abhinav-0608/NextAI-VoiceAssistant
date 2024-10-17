import sounddevice as sd
import numpy as np

# Parameters
duration = 10  # seconds
fs = 44100    # sample rate
device = 0    # MacBook Pro Microphone (Device index 0)
channels = 1  # Set to 1 for mono recording

# Record audio
print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=channels, device=device)
sd.wait()  # Wait until recording is finished
print("Recording complete!")

# Play back the recorded audio
print("Playing back the audio...")
sd.play(audio, fs)
sd.wait()  # Wait until playback is finished
print("Playback complete!")
