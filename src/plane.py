#This program displays the resonator modes of a
#simple plane wave two-mirror optical cavity

import matplotlib.pyplot as plt
import numpy as np
import math
import mirror as m

#some constants
d=0.05 #distance between two mirrors (meters)
I0 = 1.0 #initial intensity of laser
c=299792458.0 #speed of light (m/s)

#setup the mirrors, M1 is input mirror
M1 = m.Mirror(0.995, 0.005)
M2 = m.Mirror(0.995, 0.005)

#FSR, frequency spacing between resonances
FSR = c/(2.0*d)
print("FSR = " + str(FSR) + "Hz")

f=np.arange(0.5*FSR,4.5*FSR,1000) #sweep range of frequency

# I is internal intensity, assuming phase=0
r = M1.R*M2.R
real=(1.0-2.0*np.sqrt(r)*np.cos(4.0*d*np.pi*f/c))
I=(M1.T*I0)/(real + r)

# IR is the reflected intensity, assuming phase = 0
A = 1.0 + (M1.T/M1.R)*np.sqrt(r)
num = 1.0 + A*A -2.0*np.cos(4.0*d*np.pi*f/c)
B = np.sqrt(r)
den = B*B+1.0-2.0*B*np.cos(4.0*d*np.pi*f/c)
IR = I0 - ((num/den) * M1.R * I0)

#Bounce number, the effective number of round trips
#a photon makes before it has 1/e probability of
#escaping resonator by some form of loss
Losses = 2.0-M1.R-M2.R
b = 1.0/Losses
print("Bounce No. = " + str(b))

#Cavity decay time, aka photon lifetime
tc = b/FSR
print("Photon Lifetime = " + str(tc))

#Full width half maximum
df = FSR/(2.0*np.pi*b)
print("FWHM = " + str(df))

#Finesse, indicator of quality of mirrorsself.
#Higher finesse is desired
finesse = (np.pi*math.pow(r,(0.25)))/(1.0-math.pow(r,(0.5)))
print("Finesse = " + str(finesse))

#Intensity inside the resonator with low Loss
IB = b*I0
print("Intensity buildup = " + str(IB))

#Impedance matching -> no light reflected from resonator
# T1 = Losses
if(M1.T==Losses): print("Matched")
else: print("Not Matched")

#plot intensity vs. frequency
plt.plot(f,I)
plt.plot(f,IR)
plt.grid(True)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Intensity')
plt.suptitle('Two Mirror cavity intensity')
plt.show()
