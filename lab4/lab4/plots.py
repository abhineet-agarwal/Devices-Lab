import matplotlib.pyplot as plt

# Data for dark I-V characteristic (Part 1a)
Vd_dark = [-1.9, -1.72, -1.54, -1.35, -1.16, -0.97, -0.78, -0.58, -0.39, -0.24, -0.09, 0, 
           0.09, 0.17, 0.31, 0.38, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49]
Id_dark = [-1.08, -0.81, -0.63, -0.47, -0.35, -0.27, -0.21, -0.16, -0.13, -0.1, -0.06, 0, 
           0.05, 0.19, 0.79, 1.93, 3.44, 4.26, 4.67, 5.95, 7.25, 9.46, 11.68, 13.9]

# Data for I1 (Green LED) I-V characteristic (Part 1b)
Vd_I1 = [0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.4, 0.34, 0.22, 0.07, -0.11, -0.31, -0.5, -0.7, -0.89, -1.08]
Id_I1 = [11.96, 6.53, 2.94, 1.17, -0.59, -2.32, -3.17, -4.02, -4.82, -5.58, -6.89, -7.69, -8.08, -8.19, -8.26, -8.3, -8.35, -8.43, -8.51]

# Data for I2 (Blue LED) I-V characteristic (Part 1b)
Vd_I2 = [-0.8, -0.61, -0.42, -0.23, -0.04, 0.13, 0.27, 0.36, 0.43, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51]
Id_I2 = [-11.09, -11, -10.93, -10.87, -10.76, -10.54, -10.07, -9, -5.94, -4.25, -2.46, -0.7, 1.98, 5.57, 8.29, 15.58]

# Plotting Dark I-V characteristic
plt.figure(figsize=(6,4))
plt.plot(Vd_dark, Id_dark, linestyle='-', color='black', label='Dark')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('Dark I-V Characteristic')
plt.grid(True)
plt.legend()
plt.show()

# Plotting I1 (Green LED) I-V characteristic
plt.figure(figsize=(6,4))
plt.plot(Vd_I1, Id_I1, linestyle='-', color='green', label='I1 (Green LED)')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('I-V Characteristic for I1 (Green LED)')
plt.grid(True)
plt.legend()
plt.show()

# Plotting I2 (Blue LED) I-V characteristic
plt.figure(figsize=(6,4))
plt.plot(Vd_I2, Id_I2, linestyle='-', color='blue', label='I2 (Blue LED)')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('I-V Characteristic for I2 (Blue LED)')
plt.grid(True)
plt.legend()
plt.show()
