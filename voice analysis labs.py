import pyaudio
import wave
import speech_recognition as sr
import threading
import numpy as np
import matplotlib.pyplot as plt

rate = 16000
chunk = 1024
format = pyaudio.paInt16
channels = 1
filename = input("Enter desired file name: ")
filename = filename + ".wav"
print("Recording... Peress 'ENTER' to stop.")
p =  pyaudio.PyAudio()

stream = p.open(format=format,channels=channels,rate=rate,input=True,frames_per_buffer=chunk)
frames = []
stop = False
def stopRecording():
    global stop
    input()
    stop = True
threading. Thread(target=stopRecording).start()
while not stop:
    frames.append(stream.read(chunk, exception_on_overflow=False))
stream.stop_stream
stream.close()
sample_width = p.get_sample_size(format)
p.terminate()

print("Recording has Ended!")

with wave.open(filename, "wb") as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(sample_width)
    wf.setframerate(rate)
    wf.writeframes(b"".join(frames))
print("recording Saved: ", filename)
recogniser = sr.Recognizer()

with sr.AudioFile(filename) as src:
    audio = recogniser.record(src)
try:
    text = recogniser.recognize_google(audio)
    print("Transcription:", text)
except:
    print("Could not Transcribe!")

audio_data =b"".join(frames)
samples = np.frombuffer(audio_data,dtype=np.int16)
max_amplitude = np.max(samples)
min_amplitude = np.min(samples)
peak_amplitude = np.max(np.abs(samples))
average_amplitude = np.mean(np.abs(samples))
print("\nAudio Amplitude")
print("Maximum Amplitude :", max_amplitude)
print("Minimum Amplitude:", min_amplitude)
print("Peak Amplitude :", peak_amplitude)
print("Average Amplitude :", round(average_amplitude, 2))

time = np.arange(len(samples)) / rate
plt.figure(figsize=(12, 5))
plt.plot(time, samples)
plt.title("Voice Waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
