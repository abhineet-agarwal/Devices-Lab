import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Data for illumination 1 (part 2)
Vd_I1_part2 = [0.085, 0.112, 0.138, 0.163, 0.188, 0.230, 0.257, 0.291, 0.345, 0.370, 
               0.387, 0.400, 0.411, 0.422, 0.436, 0.446, 0.452, 0.459, 0.461, 0.462]
Id_I1_part2 = [-7.98, -7.94, -7.9, -7.84, -7.76, -7.63, -7.5, -7.3, -6.75, -6.43, 
               -6.0, -5.59, -5.15, -4.69, -3.66, -2.77, -2.13, -1.22, -0.91, -0.7]

# Data for illumination 2 (part 2)
Vd_I2_part2 = [0.11, 0.18, 0.26, 0.33, 0.36, 0.41, 0.44, 0.46, 0.47, 0.475]
Id_I2_part2 = [-10.5, -10.32, -9.99, -9.4, -8.91, -7.27, -5.4, -2.77, -1.04, -0.87]

# Function to interpolate for Voc and Isc
def find_Isc(V, I):
    """Interpolate to find Isc (when V = 0)"""
    f = interpolate.interp1d(V, I, kind='linear', fill_value="extrapolate")
    return f(0)

def find_Voc(V, I):
    """Interpolate to find Voc (when I = 0)"""
    f = interpolate.interp1d(I, V, kind='linear', fill_value="extrapolate")
    return f(0)

# Finding Voc (open-circuit voltage) and Isc (short-circuit current) by interpolation
Isc_I1 = find_Isc(Vd_I1_part2, Id_I1_part2)
Voc_I1 = find_Voc(Vd_I1_part2, Id_I1_part2)

Isc_I2 = find_Isc(Vd_I2_part2, Id_I2_part2)
Voc_I2 = find_Voc(Vd_I2_part2, Id_I2_part2)

print(f"Isc (I1): {Isc_I1:.3f} A, Voc (I1): {Voc_I1:.3f} V")
print(f"Isc (I2): {Isc_I2:.3f} A, Voc (I2): {Voc_I2:.3f} V")

# Calculating power for both I1 and I2
Power_I1 = -np.array(Vd_I1_part2) * np.array(Id_I1_part2)
Power_I2 = -np.array(Vd_I2_part2) * np.array(Id_I2_part2)

# Plot power as a function of voltage on the same I-V plot for I1 and I2
plt.figure(figsize=(8, 6))

# I-V and Power plot for I1
plt.plot(Vd_I1_part2, Power_I1, linestyle='-', color='orange', label='I1 Power')
plt.xlabel('Voltage (V)')
plt.ylabel('Power (W)')
plt.title('Power Characteristics for I1')
plt.grid(True)
plt.legend()
plt.show()

# I-V and Power plot for I2
plt.figure(figsize=(8, 6))
plt.plot(Vd_I2_part2, Power_I2, linestyle='-', color='red', label='I2 Power')

plt.xlabel('Voltage (V)')
plt.ylabel('Power (W)')
plt.title('Power Characteristics for I2')
plt.grid(True)
plt.legend()
plt.show()

# Finding VMP and IMP for I1 and I2
VMP_I1 = Vd_I1_part2[np.argmax(Power_I1)]
IMP_I1 = Id_I1_part2[np.argmax(Power_I1)]

VMP_I2 = Vd_I2_part2[np.argmax(Power_I2)]
IMP_I2 = Id_I2_part2[np.argmax(Power_I2)]

print(f"VMP (I1): {VMP_I1} V, IMP (I1): {IMP_I1} A")
print(f"VMP (I2): {VMP_I2} V, IMP (I2): {IMP_I2} A")

# Calculating fill factor (FF)
FF_I1 = (IMP_I1 * VMP_I1) / (Isc_I1 * Voc_I1)
FF_I2 = (IMP_I2 * VMP_I2) / (Isc_I2 * Voc_I2)

print(f"Fill Factor (I1): {FF_I1:.3f}")
print(f"Fill Factor (I2): {FF_I2:.3f}")
