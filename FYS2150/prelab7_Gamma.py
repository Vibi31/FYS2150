import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from numpy import log, sqrt

#oppgave 2 + 3

pois = []                                   #verdier fra datasett

with open('poisson.csv', 'r') as file:
    for numbers in file:                        #read every line and append each values
        pois.append(numbers)              

poissons = np.array(pois).astype(np.int)

print('middelverdien = ', np.average(poissons))
print('standardavvik = ', np.std(poissons))

#oppgave 4


