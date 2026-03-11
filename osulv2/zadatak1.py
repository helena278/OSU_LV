import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 3, 1])
y = np.array([1, 2, 2, 1, 1])

plt.plot(
    x, y,
    linestyle='-',
    linewidth=1, 
    marker='o', 
    markersize=5,
    color='tab:red' 
)

plt.title("Primjer")
plt.xlabel("X os")
plt.ylabel("Y os")
plt.axis([0, 4, 0, 4]) 
plt.grid(False)
plt.show() 