import matplotlib.pyplot as plt

# Data for the plots (replace with your actual data)
# Data from Table 1: i_E = 3mA
ic_1 = [3.03, 3.04, 3.05, 3.06, 3.07, 3.08, 3.09]  # i_C values in mA
vcb_1 = [1.03, 5.07, 7.36, 8.96, 11.32, 11.60, 12.77]  # V_cb values in V

# Data from Table 2: i_E = 6mA
ic_2 = [5.19, 5.51, 6.00, 6.11, 6.16, 6.17, 6.18, 6.19]  # i_C values in mA
vcb_2 = [0.68, 0.67, 0.61, 0.53, 0.49, 0.45, 0.28, 0.02]  # V_cb values in V

# Data from Table 3: i_E = 9mA
ic_3 = [6.23, 6.92, 7.21, 7.84, 8.25, 8.61, 9.09, 9.11, 9.12]  # i_C values in mA
vcb_3 = [0.72, 0.71, 0.69, 0.68, 0.67, 0.64, 0.49, 0.26, 0.16]  # V_cb values in V

# Create Plot 1: i_E = 3mA
plt.figure(figsize=(6, 4))
plt.plot(ic_1, vcb_1, marker='o', color='b', label='$i_E = 3mA$')
plt.xlabel('$i_C$ (mA)')
plt.ylabel('$V_{cb}$ (V)')
plt.title('Plot 1: $i_E = 3mA$')
plt.grid(True)
plt.legend()
plt.show()

# Create Plot 2: i_E = 6mA
plt.figure(figsize=(6, 4))
plt.plot(ic_2, vcb_2, marker='o', color='g', label='$i_E = 6mA$')
plt.xlabel('$i_C$ (mA)')
plt.ylabel('$V_{cb}$ (V)')
plt.title('Plot 2: $i_E = 6mA$')
plt.grid(True)
plt.legend()
plt.show()

# Create Plot 3: i_E = 9mA
plt.figure(figsize=(6, 4))
plt.plot(ic_3, vcb_3, marker='o', color='r', label='$i_E = 9mA$')
plt.xlabel('$i_C$ (mA)')
plt.ylabel('$V_{cb}$ (V)')
plt.title('Plot 3: $i_E = 9mA$')
plt.grid(True)
plt.legend()
plt.show()
