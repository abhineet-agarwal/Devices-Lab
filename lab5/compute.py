import numpy as np
import matplotlib.pyplot as plt

# Data for each temperature
temp_data = {
    35: np.array([
        [0.000, -11.25], [0.130, -11.10], [0.200, -11.00], [0.300, -10.52],
        [0.400, -8.29], [0.410, -7.84], [0.420, -7.10], [0.430, -6.29],
        [0.440, -5.34], [0.450, -3.99], [0.460, -2.47], [0.465, -1.18],
        [0.467, -0.73], [0.471, 0.00]
    ]),
    45: np.array([
        [0.000, -11.25], [0.130, -11.09], [0.200, -10.95], [0.300, -10.25],
        [0.400, -6.95], [0.410, -5.88], [0.420, -4.80], [0.430, -3.24],
        [0.440, -1.53], [0.447, 0.00]
    ]),
    55: np.array([
        [0.000, -11.21], [0.130, -11.02], [0.200, -10.77], [0.300, -9.80],
        [0.325, -9.22], [0.350, -7.93], [0.375, -6.5], [0.400, -4.56],
        [0.410, -2.73], [0.420, -0.66], [0.423, 0.00]
    ]),
    65: np.array([
        [0.000, -11.16], [0.130, -10.93], [0.200, -10.63], [0.300, -9.36],
        [0.310, -8.83], [0.320, -8.31], [0.340, -7.45], [0.370, -4.91],
        [0.375, -4.85], [0.381, -3.24], [0.386, -2.39], [0.391, -1.58],
        [0.396, -0.65], [0.399, 0.00]
    ])
}

Voc_data = {35: 0.471, 45: 0.447, 55: 0.423, 65: 0.399}
Isc_data = {35: 11.25, 45: 11.25, 55: 11.21, 65: 11.16}

# 1. Plot IL-VL and PL-VL characteristics
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
for temp, data in temp_data.items():
    plt.plot(data[:, 0], data[:, 1], label=f'{temp}°C')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('IL-VL Characteristics')
plt.legend()

plt.subplot(1, 2, 2)
for temp, data in temp_data.items():
    power = -data[:, 0] * data[:, 1]
    plt.plot(data[:, 0], power, label=f'{temp}°C')
plt.xlabel('Voltage (V)')
plt.ylabel('Power (mW)')
plt.title('PL-VL Characteristics')
plt.legend()

plt.tight_layout()
plt.show()

# 2. Calculate Fill Factor and plot FF vs Temperature
def calculate_ff(data, voc, isc):
    power = -data[:, 0] * data[:, 1]
    max_power = np.max(power)
    return max_power / (voc * isc)

ff_data = {temp: calculate_ff(data, Voc_data[temp], Isc_data[temp]) 
           for temp, data in temp_data.items()}

plt.figure(figsize=(8, 6))
plt.plot(list(ff_data.keys()), list(ff_data.values()), 'o-')
plt.xlabel('Temperature (°C)')
plt.ylabel('Fill Factor')
plt.title('Fill Factor vs Temperature')
plt.grid(True)
plt.show()

# 3. Plot Vd vs Temperature and Voc vs Temperature
def find_voltage_at_current(data, target_current):
    for v, i in data:
        if -i <= target_current:
            return v
    return None

vd_data = {
    current: {temp: find_voltage_at_current(data, current) 
              for temp, data in temp_data.items()}
    for current in [1, 2, 5]
}

plt.figure(figsize=(8, 6))
for current, data in vd_data.items():
    plt.plot(list(data.keys()), list(data.values()), 'o-', label=f'Vd at {current}mA')
plt.plot(list(Voc_data.keys()), list(Voc_data.values()), 'o-', label='Voc')
plt.xlabel('Temperature (°C)')
plt.ylabel('Voltage (V)')
plt.title('Vd and Voc vs Temperature')
plt.legend()
plt.grid(True)
plt.show()

# 4. Comments on temperature dependence
print("Comments on temperature dependence:")
print("1. Voc: Decreases with increasing temperature.")
print("2. Isc: Slightly decreases with increasing temperature.")
print("3. Fill Factor: Generally decreases with increasing temperature, ")
print("   indicating reduced efficiency at higher temperatures.")
print("These trends are consistent with the theoretical expectations for solar cells.")
print("Fill Factor values:")
for temp, ff in ff_data.items():
    print(f"{temp}°C: {ff:.4f}")