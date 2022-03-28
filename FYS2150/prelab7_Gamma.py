import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from numpy import log, sqrt, arctan, pi

#oppgave 2 + 3

pois = []                                   #verdier fra datasett

with open('poisson.csv', 'r') as file:
    for numbers in file:                        #read every line and append each values
        pois.append(numbers)              

poissons = np.array(pois).astype(np.int)

print('middelverdien = ', np.average(poissons))
print('standardavvik = ', np.std(poissons))

"""
middelverdien =  30.53
standardavvik =  5.309340825375594
"""
#oppgave 4

r = 2       #vindu radius                   [cm]
d = 20      #distanse fra radiaktiv kilde   [cm]
A = 10e6    #aktivitet                      [Bq = 1/s]
Nb = 2      #bakgrunnstråling               [Bq = 1/s]
Nr = 23     #total gamma-kvant              [Bq = 1/s]

def GM_effectivity(radius, distans, Aktivitet, bakgrunn, total_kv):

    Omega = (pi*radius**2)/distans**2

    #ligning fra labtekst side 2, ligning (4)
    effectivity = (total_kv - bakgrunn)/(A*Omega/(4*pi))

    return effectivity

print('effectivity = ',GM_effectivity(r, d, A, Nb, Nr))

#oppgave 5

skjerming = [0, 4, 8, 12, 16, 20, 24]        #[mm]
n = [13.7, 12.4, 11.0, 9.7, 8.9, 7.9, 7.1]   #telleraten


X_vals = np.array(skjerming)      #fra [mm] til [m]
Y_vals = np.array(n)

reg = linregress(X_vals, Y_vals)

print('svekkingskoeffisient = ', reg.slope/1000)
print('usikkerheten i svekkingskoeffisient = ', reg.stderr/1000)


#oppgave 6 'hvor tykt Z trenger man for 95% absorpsjon'

mu = 100  #100 per m
I0 = Y_vals[0]
I = Y_vals[-1]
#bruker ligning (4) fra side 3 (labtekst)
print('hvor tykt (z) må være = ', abs((log(I0/I)/(-mu))*1000))
print('usikkerhet på z =', 0.09*abs((log(I0/I)/(-mu))*1000))


#oppgave 7 + 8 + 9
#bruker ligning (6), side 4
# E = delta_E * I + E0    mellom cesium og naturium
     
I_cs, I_na  = 410, 773 
E0_cs, E0_na = 662, 1275
E_cs, E_na = 512, 546
#delta_E = (E - E0)/I
def dispersjon(E, E0):
    return E-E0
#????????????????? 

print('cs', (662-512)/I_cs)
print('na', (511-1275)/I_na)


