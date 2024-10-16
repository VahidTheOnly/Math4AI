import matplotlib.pyplot as plt
import numpy as np

from face_data import *


def plot_face(plt, X, edges, k, color='b'):

    plt.plot(X[:,0], X[:,1], 'o', color=color)

    i,j = edges[k]  # edge from node i to node j
    xi = X[i,0]
    yi = X[i,1]

    xj = X[j,0]
    yj = X[j,1]
        
    # draw a line between X[i] and X[j]
    plt.plot((xi,xj), (yi,yj), '-', color=color)

    plt.axis('square')
    plt.xlim(-100,100)
    plt.ylim(-100,100)
    

# for k in range(len(edges)):     
#     plot_face(plt, Face1, edges, k, color='b')
#     plt.draw()
#     plt.pause(0.05)

def morph(plt, start, end, edges):
    a = np.linspace(0, 1, 20)
    for alpha in a:
        plt.clf()
        w1 = alpha*end + (1-alpha)*start
        plot_face(plt, w1, edges, 0, color='b')
        plt.draw()
        plt.pause(0.05)

morph(plt, Face1, Face2, edges)
morph(plt, Face2, Face3, edges)
morph(plt, Face3, Face1, edges)


plt.show()