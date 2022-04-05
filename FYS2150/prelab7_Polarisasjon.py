import numpy as np
from numpy import sin, loadtxt, cos, pi, arctan
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


def malu(I0, theta1, theta2):  #regner intensitet ved malu's lov

    return(I0*cos(theta2-theta1))


def Brewsters(n1, n2):
    return arctan(n2/n1)

def vinkelfrekvensen(V):
    return 2*pi*V

def vinkel_tall(lambd):
    return 2*pi/lambd