import matplotlib.pyplot as plt

# Data
temperatures = [250, 275, 300, 325, 350, 375, 400]
voltages = [0.671, 0.615, 0.537, 0.498, 0.439, 0.381, 0.322]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(temperatures, voltages, marker='o')

# Customize the plot
plt.title('Cut-in Voltage vs Temperature')
plt.xlabel('Temperature (K)')
plt.ylabel('Cut-in Voltage (V)')
plt.grid(True)

# Add data labels
for i, txt in enumerate(voltages):
    plt.annotate(f'{txt}V', (temperatures[i], voltages[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Show the plot
plt.tight_layout()
plt.show()