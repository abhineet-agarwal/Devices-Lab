import matplotlib.pyplot as plt
import numpy as np

# Forward bias data (Voltage in V, Current in mA)
voltage_forward = np.array([0.0, 0.1, 0.11, 0.12, 0.13,
                             0.14, 0.15, 0.16, 0.17, 0.18,
                             0.19, 0.20, 0.21, 0.22, 0.23,
                             0.24, 0.25])
current_forward = np.array([0.00, 0.09, 0.14, 0.19, 0.31,
                             0.48, 0.74, 0.97, 1.33, 1.99,
                             2.88, 4.09, 5.78, 7.85, 10.63,
                             14.52, 19.18])

# Reverse bias data (Voltage in V, Current in μA)
voltage_reverse = np.array([-4.0, -3.5, -3.0, -2.5, -2.0,
                             -1.5, -1.0, -0.5, -0.2, -0.1,
                             -0.04, -0.01, 0])
current_reverse = np.array([-40, -39, -36, -34, -32,
                             -30, -27, -24, -22, -21,
                             -16, -7 , 0]) # Current in μA

# Plotting
plt.figure(figsize=(12,5))

# Forward Bias Plot
plt.subplot(1,2,1) # Change to horizontal layout
plt.plot(voltage_forward, current_forward) # Current in mA
plt.title('Voltage vs Current for Forward Bias')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.grid()
plt.axhline(0,color='black', lw=1) # Add horizontal line at y=0

# Reverse Bias Plot
plt.subplot(1,2,2) # Change to horizontal layout
plt.plot(voltage_reverse,current_reverse) # Current in μA
plt.title('Voltage vs Current for Reverse Bias')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (μA)')
plt.grid()
plt.axhline(0,color='black', lw=1) # Add horizontal line at y=0

# Show plots
plt.tight_layout()
plt.show()