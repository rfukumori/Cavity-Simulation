import numpy as np
import math

class Medium:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.mat = np.matrix([[1.0, d/n], [0.0, 1.0]])

#R is positive if the center of curvature lies in the positive
#direction of ray propogation
class Refraction:
    def __init__(self, n1, n2, R):
        self.n1 = n1
        self.n2 = n2
        self.R = R
        n3 = (n1-n2)/(n2*R)
        n4 = n1/n2
        self.mat = np.matrix([[1.0, 0.0], [n3, n4]])

class Transmission:
    def __init__(self, f):
        self.f = f
        self.mat = np.matrix([[1.0, 0.0], [-1.0/f, 1.0]])

#R>0 for concave mirror looking into it from prop. direction
class Reflection:
    def __init__(self, R):
        self.R = R
        self.mat = np.matrix([[1.0, 0.0], [-2.0/R, 1.0]])

def main():
    e1 = Refraction(0.9, 0.8, 0.7)
    print(e1.n1)
    print(e1.n2)
    print(e1.R)
    print(e1.mat)

if __name__ == "__main__": main()
