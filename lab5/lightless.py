import numpy as np
import matplotlib.pyplot as plt

# Load the data files
data_35 = np.loadtxt('D:/Devices-Lab/lab5/Illumination_35')
data_45 = np.loadtxt('D:/Devices-Lab/lab5/Illumination_45')
data_55 = np.loadtxt('D:/Devices-Lab/lab5/Illumination_55')
data_65 = np.loadtxt('D:/Devices-Lab/lab5/Illumination_65')
data_75 = np.loadtxt('D:/Devices-Lab/lab5/Illumination_75')

# Extract voltage (V) and current (I) from each dataset
V_35, I_35 = data_35[:, 0], data_35[:, 3]
V_45, I_45 = data_45[:, 0], data_45[:, 3]
V_55, I_55 = data_55[:, 0], data_55[:, 3]
V_65, I_65 = data_45[:, 0], data_45[:, 3]
V_75, I_75 = data_75[:, 0], data_75[:, 3]

# Plotting the I-V characteristics for different temperatures
plt.figure(figsize=(10, 6))

plt.plot(V_35, I_35, label='Illumination at 35°C')
plt.plot(V_45, I_45, label='Illumination at 45°C')
plt.plot(V_55, I_55, label='Illumination at 55°C')
plt.plot(V_65, I_65, label='Illumination at 65°C')
plt.plot(V_75, I_75, label='Illumination at 75°C')

plt.xlabel('Voltage (V)')
plt.ylabel('Current (I)')
plt.title('I-V Characteristics of Solar Cell (Illumination) at Different Temperatures')
plt.legend()
plt.grid(True)
plt.show()

