import matplotlib.pyplot as plt
import numpy as np

from face_data import Face1, edges

def plot_face(plt,X,edges,color='b'):
    "plots a face"
    plt.plot(X[:,0], X[:,1], 'o', color=color)

    for i,j in edges:
        xi,yi = X[i]
        xj,yj = X[j]
        
        plt.plot((xi,xj), (yi,yj), '-', color=color)
        
        plt.axis('square')
        plt.xlim(-100,100)
        plt.ylim(-100,100)

####     A   
# a = np.linspace(0, 2*np.pi, 50)
# for alpha in a:
#     plt.cla()

#     A = np.array([[np.cos(alpha), np.sin(alpha)],
#                 [-np.sin(alpha), np.cos(alpha)]])
        
#     X = (A @ Face1.T).T
#     plot_face(plt, X, edges, color='b')

#     plt.pause(0.05)
#     plt.draw()

# plt.show()


####     B
# a = np.linspace(-3/4, 4/3, 20)
# for alpha in a:
#     plt.cla()

#     A = np.array([[alpha, 0],
#                 [0, alpha]])
        
#     X = (A @ Face1.T).T
#     plot_face(plt, X, edges, color='b')

#     plt.pause(0.05)
#     plt.draw()

# plt.show()


####    C
# a = np.linspace(3/4, 4/3, 20)
# for alpha in a:
#     plt.cla()

#     A = np.array([[alpha, 0],
#                 [0, 1/alpha]])
        
#     X = (A @ Face1.T).T
#     plot_face(plt, X, edges, color='b')

#     plt.pause(0.05)
#     plt.draw()

# plt.show()


# ####    D
a = np.linspace(-1, 1, 20)
for alpha in a:
    plt.cla()
    A = np.array([[1, 0],
                [alpha, 1]])
        
    X = (A @ Face1.T).T
    plot_face(plt, X, edges, color='b')

    plt.pause(0.05)
    plt.draw()

plt.show()
