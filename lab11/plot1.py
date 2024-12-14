import matplotlib.pyplot as plt
import numpy as np
# Given constants (you can adjust these)
Vd = 0.6  # Drain-source voltage in V
Vt = 1.22  # Threshold voltage in V

# Data for Vgs and Id at different angles
Vgs = [1.47, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.5, 5, 6, 7, 8]
Id_30deg = [10.4, 13.3, 26.3, 45.3, 69.4, 94.9, 117.1, 144.3, 156.7, 163.8, 168.2, 171.7, 174.8, 176.6, 178.8, 180.6, 182, 184.7, 185.4, 188.8, 191.5, 193.1]
Id_50deg = [14.6, 18, 32.9, 53.3, 77.1, 100.5, 119.3, 140.9, 151.4, 154.2, 158.4, 161.5, 164.5, 166.7, 168.7, 170, 171.3, 174, 176.1, 178.9, 180.9, 182.4]
Id_70deg = [16.9, 22.3, 38.6, 59.6, 82.3, 102.7, 117.4, 134.1, 142.3, 148.3, 152.4, 155.4, 157.9, 160, 161.5, 163, 164.3, 166.8, 168.9, 171.1, 173.1, 174.5]
VT = Vt*np.ones(22)
VDS = Vd*np.ones(22)
# Function to calculate beta
def calculate_beta(Id, Vgs, VDS, VT):
    return (Id / (VDS * (Vgs - VT - 0.5 * VDS)))

# Calculate beta for each temperature
beta_30deg = calculate_beta(Id_30deg, Vgs, VDS, VT)
beta_50deg = calculate_beta(Id_50deg, Vgs, VDS, VT)
beta_70deg = calculate_beta(Id_70deg, Vgs, VDS, VT)

# Plotting the beta vs Vgs
plt.figure(figsize=(8,6))

plt.plot(Vgs[1:], beta_30deg[1:], marker='o', label=r'$\beta$ (30°)')
plt.plot(Vgs[1:], beta_50deg[1:], marker='s', label=r'$\beta$ (50°)')
plt.plot(Vgs[1:], beta_70deg[1:], marker='^', label=r'$\beta$ (70°)')

# Adding labels, title, and legend
plt.xlabel('Vgs (V)', fontsize=12)
plt.ylabel(r'$\beta$ (mA/V²)', fontsize=12)
plt.title(r'$\beta$ vs Vgs at different temperatures', fontsize=14)
plt.legend()

# Adding grid
plt.grid(True)

# Show the plot
plt.show()
