import numpy as np
import mirror as m
import ABCD as abcd

#Open a file
dir = '/Users/rfukumori/Desktop/Code/CavitySimulation/output/'
outputW = open(dir + 'outputW.txt', "w")
outputR = open(dir + 'outputR.txt', "w")

#make some arrays for the data
WArray = []
RArray = []

#Some constants
lam = 0.00000000542 #place holder wavelength of incident monochromatic light (m)
d = 0.50 #distance between the two mirrors (m)
n = 0.9 #index of refraction of medium in mirror

#waist size as a function of z, propogation direction
def W(A, B, D):
    den = (1.0- (((A+D)/2.0)*((A+D)/2.0)))
    if den<0:
        denom = np.sqrt(-den)
    else:
        denom = np.sqrt(den)
    numer = B*lam/np.pi
    w = numer/denom
    return w

#radius of curvature
def R(A, B, D):
    return 2.0*B/(D-A)

#setup two mirrors below
m1 = abcd.Reflection(-0.5) #radius of curvature of 50cm
m2 = abcd.Reflection(-0.2) #radius of curvature of 20cm

#for no material between
#calculate z parameters dependent on R's and d
#num = d*(R1-d)*(R2-d)*(R1+R2-d)
#den = np.power(R1+R2-2.0*d,2.0)
#z0 = np.sqrt(num/den)
#z1 = -d*(R2-d)/(R1+R2-2.0*d)
#z2 = d*(R1-d)/(R1+R2-2.0*d)
#calculate beam waist
#w0 = np.sqrt(lam*z0/(np.pi))
#w1 = w0*np.sqrt(1.0+np.power(z1/z0,2))
#w2 = w0*np.sqrt(1.0+np.power(z2/z0,2))

#get the total M matrix of roundtrip, from any point z along central axis
#should go from z=0(m1) to z=d (m2)
def M(z):
    Air = abcd.Medium(n, d-z)
    return m1.mat * (Air.mat * (m2.mat * Air.mat))

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def get_params():
    for z in my_range(0.01, d-0.01, d/1000.0):
        temp=M(z)
        A = temp.item((0,0))
        B = temp.item((0,1))
        D = temp.item((1,1))
        WArray.append(W(A,B,D))
        RArray.append(R(A,B,D))

def main():
    get_params()
    for W in WArray:
        outputW.write(str(W) + '\n')
    for R in RArray:
        outputR.write(str(R) + '\n')

if __name__ == "__main__": main()
