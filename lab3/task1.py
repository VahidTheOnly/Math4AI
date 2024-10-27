import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


A = np.array([[1, 2],
              [3, 4],
              [-2,1]])

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1, projection='3d')
ax1.set_title('column space')

u = np.random.randn(2,200)
v = A @ u

ax1.scatter(v[0,:], v[1,:], v[2,:], color='b')
    

ax2 = fig.add_subplot(1,2,2)
ax2.set_title('row space')

u = np.random.randn(200,3)
v = u @ A

ax2.plot(v[:,0], v[:,1], 'ro')

plt.show()
