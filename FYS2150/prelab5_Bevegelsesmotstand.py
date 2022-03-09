import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


#terminal velocity, rayleigh
#turbulet flow
def rayleigh(Fg, Fd, velocity, rho, radius):
    Cr = Fd/(rho*(velocity**2)*(radius**2))       #rayleigh resistance coefficient
    Vr = np.sqrt(Fg/(Cr*rho*radius**2))           #terminal velocity by rayleigh 'Vr'
    return Vr

#terminal velocity, stokes
#laminar flow
def stokes(Fg, Fd, mass, velocity, radius,mu, rho):
    g = 9.81                                      #gravity constant
    Cs = Fd/(mu*velocity*radius)                  #dtokes resistance coefficient
    Vs = Fg/(Cs*mu*radius)
    return Vs

#importing data to plot
data = np.loadtxt("terminal_hastighet_rdata.dat")
 

plt.plot(data[0], data[1])
plt.plot(data[0], data[2])
plt.plot(data[0], data[3])

plt.legend(['Rayleigh', 'Other', 'Stoke'])
plt.xscale('log'), plt.yscale('log')

plt.show()

#finding gradient
def gradient(dat1, dat2):
    lin = linregress(dat1, dat2)
    grad = 10**lin.slope
    print('gradient =', grad)
    return grad

gradient(data[0], data[3])



