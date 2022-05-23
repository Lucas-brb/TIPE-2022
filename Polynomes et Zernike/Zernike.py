import math

def Rmn(m,n,rho):
    R = 0
    if (n-m) % 2 == 0:
        for k in range((n-m)//2+1):
            R += ((-1)**k*math.factorial(n-k)) / (math.factorial(k)*math.factorial((n+m)/2-k)*math.factorial((n-m)/2-k))*rho**(n-2*k)
    return R

def Zernike(m,n,rho,phi):
    if m > 0 :
        return Rmn(m,n,rho)*math.cos(m*phi)
    else:
        return Rmn(m,n,rho)*math.sin(m*phi)

def Zernike_xy(x,y,m=None,n=None):
    if m==None:
        m = Zernike_xy.m
    else:
        Zernike_xy.m = m

    if n==None:
        n = Zernike_xy.n
    else:
        Zernike_xy.n = n

    if x == 0 and y == 0:
        return 0
    elif x < 0 and y == 0 :
        return Zernike(Zernike_xy.m,Zernike_xy.n,math.sqrt(x*x+y*y),math.pi)
    else:
        return Zernike(Zernike_xy.m,Zernike_xy.n,math.sqrt(x*x+y*y),math.atan(y/(x+math.sqrt(x*x+y*y))))