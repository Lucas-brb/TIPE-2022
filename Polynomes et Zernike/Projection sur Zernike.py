from scipy.integrate import dblquad
from Zernike import *
from Représentation_plan import *


def a(x):
    return x*a.n

def ps(f,g,domaine_x,domaine_y):
    return dblquad(lambda x, y : g(x,y) * f(x,y), domaine_y[0], domaine_y[1], domaine_x[0], domaine_x[1],epsabs=1e-2,epsrel=1e-4)

plan_z1=calc_z_centre(t,200,5,5)
lx=[i*0.5 for i in range (m1)]
ly=[j*0.5 for j in range (n1)]

z1=interpole2v(lx,ly,plan_z1)
projection_zernike = []
for n in range(6):
    pr = []
    for m in range(n+1):
        Zernike_xy(0,0,m,n)
        prod = ps(Zernike_xy,plan1,[1,4],[1,4])
        pr.append(prod)
        print(n, m, pr)
    projection_zernike.append(pr)
print (projection_zernike)
