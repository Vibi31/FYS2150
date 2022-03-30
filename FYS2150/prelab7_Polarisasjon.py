import numpy as np
from numpy import sin, loadtxt
import matplotlib.pyplot as plt

data_1 = loadtxt("polarisering1.dat")
data_2 = loadtxt("polarisering2.dat")
data_3 = loadtxt("polarisering3.dat")

plt.plot(data_1[0], data_1[1])
plt.plot(data_2[0], data_2[1])
plt.plot(data_3[0], data_3[1])

plt.show()

def refraction_index(theta_incident):
    
    return sin(theta_incident) / sin((180 - (theta_incident + 90)))

