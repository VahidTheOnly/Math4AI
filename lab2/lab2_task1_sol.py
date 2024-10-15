import numpy as np
import matplotlib.pyplot as plt

n = 11
S1 = np.vstack((-np.cos(np.linspace(0,np.pi,n)), -0.7+np.sin(np.linspace(0,np.pi,n)))).T
S2 = np.vstack((np.linspace(-1.2,1.2,n), np.zeros(n))).T

plt.plot(S1[:,0], S1[:,1], 'bo-')
plt.plot(S2[:,0], S2[:,1], 'ro-')

a = np.linspace(0, 1, 20)
for alpha in a:
    S3 = alpha * S1 + (1-alpha) * S2
    plt.plot(S3[:, 0], S3[:, 1], 'g-')
    plt.draw()
    plt.pause(0.2)

plt.xlim(-1.5,1.5)
plt.ylim(-1,0.5)
plt.show()