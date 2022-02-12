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

def h(m, mass_list, height_list):
    xy = []  #multiply data
    xy = list(map(lambda x,y: x*y ,mass_list, height_list))

    n = len(mass_list)                        #number of data points 

    a = (n*sum(xy) - sum(mass_list)*sum(height_list)) / (n*sum(mass_list**2) - sum(mass_list)**2)
    b = (sum(mass_list**2)*sum(height_list) - sum(mass_list)*sum(xy)) / (n*sum(mass_list**2) - (sum(mass_list))**2)
    
    height = a*m + b
    return height



print(h(1.0000000e-01, mass, swing))