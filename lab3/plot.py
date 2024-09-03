import matplotlib.pyplot as plt
import numpy as np

# Data
voltage = np.array([-4.55, -3.58, -3.08, -2.03, -1.29, -0.6, 0,  0.28, 0.38, 0.45, 0.5, 
                    0.52, 0.54, 0.58, 0.6, 0.63, 0.66, 0.71, 0.76, 0.78])
current = np.array([-60e-6, -50e-6, -40e-6, -30e-6, -20e-6, -10e-6, 0, 20e-3, 120e-3, 460e-3,  1.23,
                    1.68, 2.06, 3.26, 4, 5.49, 7.19, 11.06, 15.71, 18.84])
log_abs_Id = np.array([-2.81, -2.99, -3.22, -3.51, -3.91, -4.61, -3.91, -2.12, -0.78, 0, 
                       0.21, 0.52, 0.72, 1.18, 1.39, 1.70, 1.97, 2.40, 2.75, 2.94])

# Plot reverse-biased I-V
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(voltage[voltage <= 0], current[voltage <= 0] * 1e6, 'bo-')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (µA)')
plt.title('Reverse-Biased I-V Characteristics')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(-70, 0)  # Set y-limits to focus on the reverse bias current

# Plot forward-biased I-V
plt.subplot(1, 2, 2)
plt.plot(voltage[voltage >= 0], current[voltage >= 0] * 1e3, 'ro-')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('Forward-Biased I-V Characteristics')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(0, 20000)  # Set y-limits to focus on the forward bias current

plt.tight_layout()
plt.show()


# Plot log(abs(Id)) vs V
plt.subplot(1, 2, 2)
plt.plot(voltage, log_abs_Id, 'go-')
plt.xlabel('Voltage (V)')
plt.ylabel('log(abs(I))')
plt.title('log(abs(I)) vs V')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.show()
