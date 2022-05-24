from scipy.integrate import dblquad
from Zernike import *
from Représentation_plan import *


def ps(f,g,domaine_x,domaine_y):
    return dblquad(lambda rho, phi : 1/(math.pi)*f(rho,phi)*g(rho,phi), domaine_y[0], domaine_y[1], domaine_x[0], domaine_x[1],epsabs=1e-1,epsrel=1e-3)[0]

plan_z1=calc_z_centre(t,200,5,5)
lx=[i*0.5 for i in range (m1)]
ly=[j*0.5 for j in range (n1)]



z1=interpole2v(lx,ly,plan_z1)
projection_zernike = []
for n in range(6):
    pr = []
    for m in range(-n,n+1,2):
        Zernike_xy(0,0,m,n)
        prod = ps(Zernike,plan1_polaire_decale,[0,1.5],[0,2*math.pi])
        pr.append(prod)
    projection_zernike.append(pr)

print (np.array(projection_zernike))



def resultat(x,y):
    res = 0
    for n in range(6):
        k = 0
        for m in range(-n,n+1,2):
            Zernike(0,0,m,n)
            res += (projection_zernike[n][k])*Zernike_xy(x,y)
            k += 1
    return res

ax = Axes3D(plt.figure())
R = np.arange(0,1.5,0.1)
Phi = np.arange(0,2*math.pi+0.1,0.1)
R,P = np.meshgrid(R, Phi)
X , Y = R*np.cos(P) , R*np.sin(P)
resultat = np.vectorize(resultat)
Z = resultat(X,Y)
X, Y = 1.5*X+2.5, 1.5*Y+2.5
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
plt.xlabel('x', color = 'red')
plt.ylabel('y', color = 'red')
plt.show()
