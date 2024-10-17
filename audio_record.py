import sounddevice as sd
import numpy as np
import scipy.io.wavfile

# Parameters
duration = 10  # seconds
fs = 44100    # sample rate
channels = 1  # mono recording

# Record audio
print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
sd.wait()  # Wait until recording is finished
print("Recording complete!")

# Save the audio as a .wav file
scipy.io.wavfile.write("output.wav", fs, audio)
