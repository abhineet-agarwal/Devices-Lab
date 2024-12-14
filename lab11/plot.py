import numpy as np
import matplotlib.pyplot as plt

# Data for Vgs and Id
Vgs = [0, 0.86, 0.87, 0.89, 0.92, 0.96, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2]
Id = [0, 0, 0.001, 0.002, 0.004, 0.009, 0.02, 0.047, 0.11, 0.243, 0.516, 1.047, 1.9, 3.57, 6, 9.51, 14.38, 20.8, 28.9, 38.8, 50.7, 65.2, 81.6, 100.1, 120.3, 142.6, 166.1]

# Calculate sqrt(Id)
sqrt_Id = np.sqrt(Id)
print(sqrt_Id)

# Plot sqrt(Id) vs Vgs
plt.figure(figsize=(8,6))
plt.plot(Vgs, sqrt_Id, marker='o', linestyle='-', color='g')

# Adding labels and title
plt.xlabel('Vgs (V)', fontsize=12)
plt.ylabel('sqrt(Id) (mA^0.5)', fontsize=12)
plt.title('sqrt(Id) vs Vgs', fontsize=14)

# Adding grid
plt.grid(True)

# Show plot
plt.show()
