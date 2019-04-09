from scipy.interpolate import BSpline
import matplotlib.pyplot as plt
import numpy as np

point = np.array([[108.1, 234],
                  [76, 228.3],
                  [48.2, 210.5],
                  [45.2, 186.7],
                  [59.3, 171.2]])
k = 3  # degree
t = [0, 1, 2, 3, 4, 5, 6, 7]
# c = [-1, 2, 0, -1]
c = point
spl = BSpline(t, c, k)



fig, ax = plt.subplots()
xx = np.linspace(1.5, 4.5, 50)
# ax.plot(xx, [spl(2.5) for x in xx], 'r-', lw=3, label='naive')
ax.plot(xx, spl(xx), 'b-', lw=4, alpha=0.7, label='BSpline')
ax.grid(True)
ax.legend(loc='best')
plt.show()
