# Voici des données simulées

import numpy as np


def calc_z_coin (t,f, pasx,pasy) :
    m = len(t)
    n = len(t[0])
    Z = [[0 for _ in range (n)] for _ in range (m)]
    for i in range (1,n):
        X,Y = t[0][i-1]
        Z[0][i]=Z[0][i-1]-X/f*pasx
    for i in range (1,m):
        X,Y = t[i-1][0]
        Z[i][0]=Z[i-1][0]-Y/f*pasy
    for i in range (1,m):
        for j in range (1,n):
            X1 , Y1 = t[i][j-1]
            X2 , Y2 = t[i-1][j]
            Z[i][j] = 0.5*(Z[i][j-1]-X1/f*pasx + Z[i-1][j]-Y2/f*pasy)
    return Z




t=[[(0,0),(-1,-1),(0,1),(-1,1),(-1,0),(1,1),(-1,0),(-1,1),(-1,0),(-1,1),(-1,1),(-1,2),(0,0)],
   [(2,1),(1,1),(0,0),(-1,0),(-2,0),(-1,0),(0,0),(0,0),(0,-1),(-1,1),(-1,1),(-2,1),(-2,1)],
   [(1,0),(0,0),(0,1),(-2,0),(-2,-1),(-1,2),(0,1),(0,0),(-1,1),(0,-1),(0,1),(-1,1),(-1,3)],
   [(1,0),(0,0),(0,0),(-2,-1),(0,-1),(1,-1),(0,-1),(0,-1),(0,0),(0,-1),(-2,-1),(-1,0),(-1,0)],
   [(2,0),(0,-1),(0,0),(-2,0),(-1,0),(0,0),(1,0),(1,0),(-1,-2),(0,0),(0,0),(-1,-1),(-1,0)],
   [(1,0),(0,0),(1,0),(-1,0),(0,0),(0,0),(0,0),(0,-1),(0,0),(0,0),(2,0),(-1,1),(-1,-1)],
   [(1,0),(0,0),(2,0),(-1,0),(0,0),(0,0),(-2,2),(0,0),(0,0),(-1,0),(-1,1),(0,0),(-1,-1)],
   [(2,-2),(0,0),(1,-1),(0,-1),(0,0),(0,0),(0,0),(0,0),(-1,0),(0,0),(0,-1),(-2,0),(-1,-1)],
   [(1,-1),(-1,1),(1,0),(-1,0),(0,0),(0,0),(0,-1),(0,0),(0,0),(0,0),(-1,0),(-1,-1),(-2,-1)],
   [(0,0),(1,-1),(-1,0),(2,0),(0,0),(0,-1),(0,0),(0,0),(0,0),(0,0),(0,-1),(0,0),(0,0)],
   [(0,0),(1,-1),(-1,0),(1,-2),(0,-1),(1,-1),(0,0),(0,-1),(0,-1),(-1,-1),(0,0),(0,0),(0,0)]]

Z=calc_z_coin(t, 200, 5, 5)

x = [i for i in range(0,13)]
for j in range(0,10):
    x=x+[i for i in range(0,13)]

y= [0 for i in range (0,13)]
for j in range(1,11):
    y=y+[j for i in range(0,13)]

z=[]
for j in range(len(Z)):
    for i in range(len(Z[0])):
        z.append(-Z[j][i])
    


# Tracer le graphique

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

for i in range(0,360,10):
    fig = plt.figure()

    ax = fig.gca(projection='3d')

    ax.scatter(x,y,z, zdir='z',s=20,depthshade=True)

# Paramétrer le graphique

    ax.set_xlim3d([0.0,12]) ; ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 10]) ; ax.set_ylabel('Y')

    ax.set_zlim3d([-0.06, 0.06]) ; ax.set_zlabel('Z')

# Afficher

    ax.view_init(elev=10., azim=i)
    plt.show()