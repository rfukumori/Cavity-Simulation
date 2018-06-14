import numpy as np
import math

#mirrors with reflectivity, trasmisstivity,
class Mirror:
    def __init__(self, R, T):
        self.R = R
        self.T = T
        self.L = 1.0-R-T


def main():
    m1 = Mirror(0.9, 0.05)
    print(m1.R)
    print(m1.T)
    print(m1.L)

if __name__ == "__main__": main()
