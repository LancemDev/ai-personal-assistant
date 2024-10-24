import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
CHUNK = 1024  # Number of audio samples per frame
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sampling rate (samples per second)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Create a figure and axis for the plot
fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))

# Set plot parameters
ax.set_ylim(-2**15, 2**15)
ax.set_xlim(0, CHUNK)
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.title('Real-Time Audio Waveform')

# Update function for the animation
def update(frame):
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    line.set_ydata(data)
    return line,

# Create an animation
ani = animation.FuncAnimation(fig, update, blit=True)

# Show the plot
plt.show()

# Close the stream
stream.stop_stream()
stream.close()
p.terminate()