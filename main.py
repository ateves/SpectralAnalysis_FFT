import numpy as np
import matplotlib.pyplot as plt

# Generate a sample signal (sine wave)
t = np.arange(100) # Time vector
s = np.sin(0.15 * 2 * np.pi * t) # Signal

# Perform the FFT
S = np.fft.fft(s)

# Optional: shift the zero frequency component to the center
S_shifted = np.fft.fftshift(S)

# Plotting the magnitude (amplitude)
S_mag = np.abs(S_shifted)
plt.plot(t, S_mag, '.-')
plt.title("Frequency Domain Magnitude")
plt.show()
