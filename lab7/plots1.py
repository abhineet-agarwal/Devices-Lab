import matplotlib.pyplot as plt

# Data from the table
V_be = [0.63, 0.64, 0.66, 0.67, 0.70, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.80]  # V_be in V
I_C = [1.02, 1.69, 2.96, 4.88, 6.05, 6.71, 6.93, 7.31, 7.49, 8.23, 8.78, 9.63, 10.23]  # I_C in mA
I_B = [0.004, 0.007, 0.013, 0.022, 0.3, 1.0, 1.4, 2.2, 3.0, 4.4, 5.6, 7.1, 8.5]  # I_B in mA

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot I_C
plt.plot(V_be, I_C, marker='o', color='b', label='$I_C$ (mA)', linewidth=2)

# Plot I_B
plt.plot(V_be, I_B, marker='x', color='g', label='$I_B$ (mA)', linewidth=2)

# Adding labels and title
plt.xlabel('$V_{be}$ (V)', fontsize=14)
plt.ylabel('Current (mA)', fontsize=14)
plt.title('Plot of $I_C$ and $I_B$ against $V_{be}$', fontsize=16)
plt.grid(True)
plt.legend()
plt.ylim(0, max(I_C) + 2)  # Set y-limits for better visibility

# Show the plot
plt.tight_layout()
plt.show()
