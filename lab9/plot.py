import matplotlib.pyplot as plt

# Given data
V_SB = [0, 1, 2, 3]  # V_SB values
V_T = [1.29, 2.36, 3.17, 3.85]  # V_T values

# Plotting V_T vs V_SB
plt.figure(figsize=(8, 6))
plt.plot(V_SB, V_T, marker='o', linestyle='-', color='b', label=r'$V_T$ vs $V_{SB}$')
plt.title(r'Plot of $V_T$ vs $V_{SB}$', fontsize=14)
plt.xlabel(r'$V_{SB}$ (V)', fontsize=12)
plt.ylabel(r'$V_T$ (V)', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()
