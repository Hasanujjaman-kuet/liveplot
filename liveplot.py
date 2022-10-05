import numpy as np
import matplotlib.pyplot as plt

x, y = [], []

for idx in range(200):
    x.append(np.random.randint(1, 200))
    y.append(np.random.randint(1, 200))
    plt.scatter(x, y, color='lightgreen')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.grid(True)
    plt.pause(0.3)
plt.show()