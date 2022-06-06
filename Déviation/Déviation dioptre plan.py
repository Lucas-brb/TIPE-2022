import matplotlib.pyplot as plt
import numpy as np


N=0.7


x=np.linspace(-np.pi/2,np.pi/2,1000)
## Double dioptre concave vers la droite

for i in range(1,10,2):
    R=i*10**(-1)
    y=(np.arcsin(N*np.sin(x))+np.arcsin(R*np.sin(x))-np.arcsin(N*R*np.sin(x))-x)*(180/np.pi)
    plt.plot(x*180/np.pi,y,label = f'R = {R:.2}')
    plt.legend()
## Double dioptre vers la gauche


# for i in range(1,10,2):
#     R=i*10**(-1)
#     R1=1/R
#     y=(-np.arcsin(R1*np.sin(x))+np.arcsin(N*R1*np.sin(x))-np.arcsin(N*np.sin(x))+x)*(180/np.pi)
#     plt.plot(x*(180/np.pi),y)


plt.title("Déviation à l'entrée de la lentille (en °)")
plt.xlabel("Angle d'incidence (en °)")
plt.show()

