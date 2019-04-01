import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# x = np.array(np.arange(-0.8, 0.8, 0.025))
# y = np.sin(x)
# z = np.array(np.arange(-0.8, 0.8, 0.025)) # np.array([0.025]*len(x))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(-0.8, 0.8, 0.025)
y = np.sin(x)
X, Y = np.meshgrid(x, y) # create matrix of pair x and y into greed

zs = np.array([np.sin(x) for x,y in zip(np.ravel(X), np.ravel(Y))])
print(zs)

# zs = np.sin(x)
Z = zs.reshape(X.shape)
ax.plot_surface(X, Y, Z)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot3D(x, y, z, 'gray')

# plt.show()
