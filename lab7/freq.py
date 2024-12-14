import numpy as np
import matplotlib.pyplot as plt

# Data from the table
frequency = np.array([1e3, 5e3, 10e3, 50e3, 100e3, 150e3, 200e3, 250e3, 300e3, 350e3, 400e3, 450e3, 500e3, 550e3, 600e3])  # Frequency in Hz
V_out = np.array([1.1, 1.46, 1.5, 1.36, 1.34, 1.32, 1.26, 1.24, 1.22, 1.18, 1.14, 1.06, 1.02, 0.98, 0.96])  # V_out in V
gain = np.array([2.08, 2.92, 3.00, 2.72, 2.60, 2.64, 2.52, 2.68, 2.44, 2.36, 2.28, 2.12, 2.04, 1.96, 1.92])  # Gain

# Plotting the frequency response
plt.figure(figsize=(10, 6))
plt.plot(frequency, gain, marker='o', linestyle='-', color='b')
plt.xscale('log')  # Logarithmic scale for frequency
plt.xlabel('Frequency (Hz)', fontsize=14)
plt.ylabel('Gain', fontsize=14)
plt.title('Frequency Response', fontsize=16)
plt.grid(True)
plt.axhline(y=max(gain) / np.sqrt(2), color='r', linestyle='--', label='3dB Cutoff Level')
plt.legend()

# Finding the 3dB cutoff frequency
max_gain = max(gain)
cutoff_level = max_gain / np.sqrt(2)
cutoff_freq = frequency[np.where(gain <= cutoff_level)[0][0]]  # First frequency where gain is below cutoff level

# Display the plot
plt.tight_layout()
plt.show()

# Output the cutoff frequency
cutoff_freq_khz = cutoff_freq / 1e3  # Convert Hz to kHz
print(f'The 3dB cutoff frequency is approximately {cutoff_freq_khz:.2f} kHz.')
