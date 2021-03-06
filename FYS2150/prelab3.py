import numpy as np 


#general line: y = mx + c, m = E/D, c = y_av - m*x_av
mass = []        #weight 'kg'
swing = []       #Pendulum swing 'mm'
#mass = E/D

with open('maalinger_deformasjon.dat', 'r') as file:
    for line in file:
        values = line.strip().split()
        mass.append(values[0])
        swing.append(values[1])

n = len(mass) #number of data points

import numpy as np 

#general line: y = mx + c, m = E/D, c = y_av - m*x_av
mass = []        #weight 'kg'
swing = []       #Pendulum swing 'mm'
#mass = E/D
file = np.loadtxt("maalinger_deformasjon.dat")
for line in file:
    mass.append(line[0])
    swing.append(line[1])

"""
#this doesnt work, IN1900 has not taught us well :')

with open('maalinger_deformasjon.dat', 'r') as file:
    for line in file:
        values = line.strip().split()
        mass.append(values[0])
        swing.append(values[1])
"""
#converting our lists to arrays
mass = np.array(mass)
swing = np.array(swing)

def h(mass, mass_list, height_list):
    n = len(mass_list)                        #number of data points 
    #mass_list is the x variable
    #height_list is our y output values

    #formulas from page 39. Practical Physics by G.L.Squires (2001 edition)
    D = np.sum(mass_list**2) - (1/n)*(np.sum(mass_list)**2)
    E = np.sum(mass_list*height_list) - (1/n)*np.sum(mass_list)*np.sum(height_list)
    F = np.sum(height_list**2) -(1/n)*(np.sum(height_list)**2)
    print('D =', D)
    print('E =', E)
    print('F =', F)
    
    y_avg = np.mean(height_list)
    x_avg = np.mean(mass_list)

    #linear values
    m = E/D
    c = y_avg - m*x_avg
    height = m*mass + c

    #usikkerhet
    di = (height_list -m*mass_list) - c

    #delta_m2 = (1/(n-2))*np.sum(di)/D
    delta_m2 = (1/(n-2))*((D*F-E**2)/D**2)

    #printing our values
    print('stigningstall = ', m)
    print('usikkerheten til stigningstall =', np.sqrt(delta_m2))

    return height



print('testing estimate with m=0.2kg:',h(0.2, mass, swing))

#task 4
tau = [4.12, 4.04, 4.16, 4.02, 4.03, 4.04, 3.89, 4.2, 4.12, 4.05]
m = 2.0
Tau_avg = np.average(tau)
t2pi = (Tau_avg/(2*np.pi))**2 / m
k = 1/t2pi

print('spring constant (k) =', k) 

#task 5
print('length of tau =', len(tau))
Delta_tau = np.std(tau)/np.sqrt(len(tau))
print('usikkerheten til massen =', (2*Delta_tau/np.average(tau)))
