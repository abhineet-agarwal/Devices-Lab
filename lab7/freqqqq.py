import numpy as np
import matplotlib.pyplot as plt

# Data from the table
frequency = np.array([1e3, 5e3, 10e3, 50e3, 100e3, 150e3, 200e3, 250e3, 300e3, 
                      350e3, 400e3, 450e3, 500e3, 550e3, 600e3, 650e3, 700e3, 750e3, 800e3, 850e3, 900e3])  # Frequency in Hz
V_out = np.array([1.76, 1.84, 2.20, 4.64, 5.28, 5.44, 5.36, 5.36, 5.20, 5.04, 
                  4.80, 4.64, 4.40, 4.16, 4.00, 3.76, 3.60, 3.44, 3.28, 3.12, 2.96])  # V_out in V

# Plotting the frequency response
plt.figure(figsize=(10, 6))
plt.plot(frequency, V_out, marker='o', linestyle='-', color='b')
plt.xscale('log')  # Logarithmic scale for frequency
plt.xlabel('Frequency (Hz)', fontsize=14)
plt.ylabel('$V_{out}$ (pk-pk) (V)', fontsize=14)
plt.title('Frequency Response', fontsize=16)
plt.grid(True)

# Finding the 3dB cutoff frequency
max_V_out = max(V_out)
cutoff_level = max_V_out / np.sqrt(2)
cutoff_freq_index = np.where(V_out <= cutoff_level)[0][0]  # Find the first frequency below cutoff level
cutoff_freq = frequency[cutoff_freq_index]  # 3dB cutoff frequency

# Display the cutoff frequency on the plot
plt.axhline(y=cutoff_level, color='r', linestyle='--', label='3dB Cutoff Level')
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()

# Output the cutoff frequency
cutoff_freq_khz = cutoff_freq / 1e3  # Convert Hz to kHz
print(f'The 3dB cutoff frequency is approximately {cutoff_freq_khz:.2f} kHz.')
