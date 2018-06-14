##This program will calculate stability of Cavity
import numpy as np

##Constants, mirrors
L = 0.5 #distance between mirrors in m
lam = lam = 0.00000000542 #wavelength of beam
#concave mirrors of + sign, vice versa
R1 = 0.2 #radius of curvature of mirror 1
R2 = 0.4 #radius of curvature of mirror 2

#g-params
g1 = 1.0 - (L/R1)
g2 = 1.0 - (L/R2)
G = g1*g2

def isStable(a, b):
    if(a*b>0 and a*b<1):
        return True
    else: return False

#now get mirror locations wrt z0, the minimum waist size position
p1 = g2*(1.0-g1)
p2 = g1*(1.0-g2)

z1 = -L*(p1)/(p1+p2)
z2 = L*(p2)/(p1+p2)

#beam waist
denom = np.power((g1+g2-2.0*G),2)
w0 = np.sqrt(lam*L/np.pi)*np.power(G*(1.0-G)/denom, 0.25)

print(str(z1))
print(str(z2))

print(str(w0))
