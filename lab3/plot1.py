import matplotlib.pyplot as plt
import numpy as np

# Data
# Wavelengths in nm
wavelengths = {
    "blue": 450,
    "green": 530,
    "red": 630,
    "infrared": 850
}

# Vout (Voltage) and Intensity Data
data = {
    "blue": {
        "current": np.array([0.301, 0.416, 0.572]),
        "voltage": np.array([2.6, 4.3, 4.9]),
        "intensity": np.array([1000, 1500, 2000])
    },
    "green": {
        "current": np.array([0.188, 0.294, 0.371]),
        "voltage": np.array([3.0, 3.7, 4.5]),
        "intensity": np.array([1000, 1500, 2000])
    },
    "red": {
        "current": np.array([2.0, 3.0, 4.0]),
        "voltage": np.array([6.9, 10.3, 13.7]),
        "intensity": np.array([1000, 1500, 2000])
    },
    "infrared": {
        "current": np.array([4.51, 5.17, 6.28]),
        "voltage": np.array([55.2, 64.9, 81.5]),
        "intensity": np.array([1000, 1500, 2000])
    }
}

# Plot Vout vs Wavelength for each intensity
for color, values in data.items():
    plt.figure(figsize=(6, 4))
    plt.plot([wavelengths[color]] * len(values["voltage"]), values["voltage"], 'o-')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Vout (Voltage)')
    plt.title(f'Vout vs Wavelength ({color.capitalize()} LED)')
    plt.grid(True)
    plt.show()

# Plot Vout vs Intensity for each LED
for color, values in data.items():
    plt.figure(figsize=(6, 4))
    plt.plot(values["intensity"], values["voltage"], 'o-')
    plt.xlabel('Intensity (lm)')
    plt.ylabel('Vout (Voltage)')
    plt.title(f'Vout vs Intensity ({color.capitalize()} LED)')
    plt.grid(True)
    plt.show()
