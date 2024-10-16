import matplotlib.pyplot as plt
import numpy as np

from face_data import Face1, Face2, Face3, TargetFace1, TargetFace2, edges

def plot_face(plt,X,edges,color='b'):    
    plt.plot(X[:,0], X[:,1], 'o', color=color)

    i,j = edges[0]  # edge from node i to node j
    xi = X[i,0]
    yi = X[i,1]

    xj = X[j,0]
    yj = X[j,1]
        
    plt.plot((xi,xj), (yi,yj), '-', color=color)

    plt.axis('square')
    plt.xlim(-100,100)
    plt.ylim(-100,100)
    

# # make a guess
# a = 0.3
# b = 0.3
# c = 0.4

# F = a * Face1 + b * Face2 + c * Face3
# plot_face(plt, TargetFace1, edges, color='r')
# plot_face(plt, F, edges, color='g')

faces = np.vstack([Face1.flatten(), Face2.flatten(), Face3.flatten()]).T
Target_1 = TargetFace1.flatten()
Target_2 = TargetFace2.flatten()

a, b, c = np.linalg.solve(faces.T @ faces, faces.T @ Target_2)

print(f'a = {a}, b = {b}, c = {c}')

F = a * Face1 + b * Face2 + c * Face3

plot_face(plt, TargetFace1, edges, color='r')
plot_face(plt, F, edges, color='g')

plt.show()