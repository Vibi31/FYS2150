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
    
    y_avg = np.mean(height_list)
    x_avg = np.mean(mass_list)

    m = E/D
    c = y_avg - m*x_avg
    height = m*mass + c

    print('stigningstall = ', m)
    print('usikkerheten til stigningstall =',)


    return height



print(h(0.2, mass, swing))

