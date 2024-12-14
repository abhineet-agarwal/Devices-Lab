import matplotlib.pyplot as plt
import numpy as np
# Given constants (adjust these if needed)
Vd = 0.6  # Drain-source voltage in V
Vt = 1.22  # Threshold voltage in V

# Temperatures corresponding to each Id column
temperatures = [30, 50, 70]  # in degrees Celsius

# Data for Id at different temperatures (for specific Vgs values)
Id_30deg = [69.4, 193.1]  # Id values at Vgs=1.8V and Vgs=8V for 30°
Id_50deg = [77.1, 182.4]  # Id values at Vgs=1.8V and Vgs=8V for 50°
Id_70deg = [82.3, 174.5]  # Id values at Vgs=1.8V and Vgs=8V for 70°

Vgs_values = [1.8, 8]  # Low Vgs = 1.8V, High Vgs = 8V
VT = Vt*np.ones(22)
VDS = Vd*np.ones(22)
# Function to calculate beta
def calculate_beta(Id, Vgs, VDS, VT):
    return (Id / (VDS * (Vgs - VT - 0.5 * VDS)))

# Calculate beta for low Vgs = 1.8V and high Vgs = 8V at different temperatures
beta_low_Vgs = [calculate_beta(Id_30deg[0], Vgs_values[0], VDS, VT), 
                calculate_beta(Id_50deg[0], Vgs_values[0], VDS, VT), 
                calculate_beta(Id_70deg[0], Vgs_values[0], VDS, VT)]

beta_high_Vgs = [calculate_beta(Id_30deg[1], Vgs_values[1], VDS, VT), 
                 calculate_beta(Id_50deg[1], Vgs_values[1], VDS, VT), 
                 calculate_beta(Id_70deg[1], Vgs_values[1], VDS, VT)]

print(beta_high_Vgs)
print(beta_low_Vgs)
# Plotting the beta vs Temperature for low Vgs (1.8V)
plt.figure(figsize=(8,6))
plt.plot(temperatures, beta_low_Vgs, marker='o')

# Adding labels and title (no legend)
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel(r'$\beta$ (mA/V²)', fontsize=12)
plt.title(r'$\beta$ vs Temperature at $V_{GS} = 1.8V$', fontsize=14)

# Adding grid
plt.grid(True)

# Show the first plot (low Vgs)
plt.show()

# Plotting the beta vs Temperature for high Vgs (8V)
plt.figure(figsize=(8,6))
plt.plot(temperatures, beta_high_Vgs, marker='s')

# Adding labels and title (no legend)
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel(r'$\beta$ (mA/V²)', fontsize=12)
plt.title(r'$\beta$ vs Temperature at $V_{GS} = 8V$', fontsize=14)

# Adding grid
plt.grid(True)

# Show the second plot (high Vgs)
plt.show()