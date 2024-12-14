import matplotlib.pyplot as plt
import numpy as np

# Data for illumination 1 (part 2)
Vd_I1_part2 = [0.085, 0.112, 0.138, 0.163, 0.188, 0.230, 0.257, 0.291, 0.345, 0.370, 
               0.387, 0.400, 0.411, 0.422, 0.436, 0.446, 0.452, 0.459, 0.461, 0.462]
Id_I1_part2 = [-7.98, -7.94, -7.9, -7.84, -7.76, -7.63, -7.5, -7.3, -6.75, -6.43, 
 -6.0, -5.59, -5.15, -4.69, -3.66, -2.77, -2.13, -1.22, -0.91, -0.7]


# Data for illumination 2 (part 2)
Vd_I2_part2 = [0.11, 0.18, 0.26, 0.33, 0.36, 0.41, 0.44, 0.46, 0.47, 0.475]
Id_I2_part2 = [-10.5, -10.32, -9.99, -9.4, -8.91, -7.27, -5.4, -2.77, -1.04, -0.87]


# Plot I-V characteristic for I1 and I2
plt.figure(figsize=(8, 6))

# I1 I-V plot (part 2)
plt.plot(Vd_I1_part2, Id_I1_part2, linestyle='-', color='green', label='I1 (Part 2)')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('I-V Characteristics for Illumination I1')
plt.grid(True)
plt.legend()
plt.show()
# I2 I-V plot (part 2)
plt.figure(figsize=(8, 6))
plt.plot(Vd_I2_part2, Id_I2_part2, linestyle='-', color='blue', label='I2 (Part 2)')

plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('I-V Characteristics for Illumination I2 (Part 2)')
plt.grid(True)
plt.legend()
plt.show()

# Finding Voc (open-circuit voltage) and Isc (short-circuit current)
Isc_I1 = Id_I1_part2[0]  # Isc is the current when voltage is 0 (approx)
Voc_I1 = Vd_I1_part2[-1]  # Voc is the voltage when current is 0 (approx)

Isc_I2 = Id_I2_part2[0]
Voc_I2 = Vd_I2_part2[-1]

print(f"Isc (I1): {Isc_I1} A, Voc (I1): {Voc_I1} V")
print(f"Isc (I2): {Isc_I2} A, Voc (I2): {Voc_I2} V")

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

print(f"Fill Factor (I1): {FF_I1}")
print(f"Fill Factor (I2): {FF_I2}")

# Superimposing I-V readings from part 1B and part 2
# Data for I1 (part 1B)
Vd_I1_part1 = [0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.4, 0.34, 0.22, 
               0.07, -0.11, -0.31, -0.5, -0.7, -0.89, -1.08]
Id_I1_part1 = [11.96, 6.53, 2.94, 1.17, -0.59, -2.32, -3.17, -4.02, -4.82, -5.58, 
               -6.89, -7.69, -8.08, -8.19, -8.26, -8.3, -8.35, -8.43, -8.51]

# Data for I2 (part 1B)
Vd_I2_part1 = [-0.8, -0.61, -0.42, -0.23, -0.04, 0.13, 0.27, 0.36, 0.43, 0.45, 0.46, 
               0.47, 0.48, 0.49, 0.5, 0.51]
Id_I2_part1 = [-11.09, -11, -10.93, -10.87, -10.76, -10.54, -10.07, -9, -5.94, -4.25, 
               -2.46, -0.7, 1.98, 5.57, 8.29, 15.58]

# Superimpose I1 readings
plt.figure(figsize=(8, 6))
plt.plot(Vd_I1_part1, Id_I1_part1, linestyle='-', color='green', label='I1 (Part 1B)')
plt.plot(Vd_I1_part2, Id_I1_part2, linestyle='--', color='lightgreen', label='I1 (Part 2)')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('Superimposed I-V Characteristics for I1 (Part 1B and Part 2)')
plt.grid(True)
plt.legend()
plt.show()

# Superimpose I2 readings
plt.figure(figsize=(8, 6))
plt.plot(Vd_I2_part1, Id_I2_part1, linestyle='-', color='blue', label='I2 (Part 1B)')
plt.plot(Vd_I2_part2, Id_I2_part2, linestyle='--', color='lightblue', label='I2 (Part 2)')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('Superimposed I-V Characteristics for I2 (Part 1B and Part 2)')
plt.grid(True)
plt.legend()
plt.show()
