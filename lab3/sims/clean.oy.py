import numpy as np
import matplotlib.pyplot as plt

def clean_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    v_data = []
    i_data = []
    reading_data = False

    for line in lines:
        if line.startswith('Voltage (V), Current (A/cm2)'):
            reading_data = True
            continue
        if reading_data and line.strip() and not line.startswith('----'):
            v, i = map(float, line.strip().split(','))
            v_data.append(v)
            i_data.append(i)
        if line.startswith('----'):
            reading_data = False

    return np.array(v_data), np.array(i_data)

# Load and clean the data
V, I = clean_data("C:/Users/Admin/Downloads/current8.txt")

# Sort data and remove duplicates
sorted_indices = np.argsort(V)
V = V[sorted_indices]
I = I[sorted_indices]

# Remove duplicates
_, unique_indices = np.unique(V, return_index=True)
V = V[unique_indices]
I = I[unique_indices]

# Create I-V plot
plt.figure(figsize=(10, 6))
plt.plot(V, I)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A/cm²)')
plt.title('I-V Characteristic')
plt.grid(True)
plt.show()

# Create ln(I) vs V plot
# We'll use the absolute value of I to avoid issues with logarithms of negative numbers
plt.figure(figsize=(10, 6))
plt.plot(V, np.log(np.abs(I)))
plt.xlabel('Voltage (V)')
plt.ylabel('ln(|I|)')
plt.title('ln(I) vs V')
plt.grid(True)
plt.show()

# Optional: Print the number of data points before and after processing
print(f"Number of data points before processing: {len(sorted_indices)}")
print(f"Number of data points after removing duplicates: {len(unique_indices)}")