import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

x = [0, 5, 10, 15, 30, 35, 40, 50, 55, 60]
y = [100, 90, 65, 85, 70, 30, 40, 45, 20, 0]

fig, ax = plt.subplots(1, 1, figsize=(8, 4))

ax.plot(x, y, "o")

data = np.array((x, y))

spl = interpolate.splrep(x, y, s=0)
x_new = np.linspace(0, 60, 100)

out = interpolate.splev(x_new, spl)

ax.plot(x_new, out, "ob")
plt.show()
