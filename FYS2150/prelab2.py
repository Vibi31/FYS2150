import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

file = open('RC_data.csv', 'r')
data = file.read()
#data = np.loadtxt('RC_data.csv')   """this method did not work"""

print(data)  #testing

frekvens = []
vu_vi = []

with open('RC_data.csv', 'r') as file:
    firstline = next(file)
    for line in file:
        values = line.split(',')
        frekvens.append(values[0])
        vu_vi.append(values[1])


"""
for line in data:
    values = line.split(',')
    print(values)
    frekvens.append(values[0])
    vu_vi.append(values[1])
    #frekven =
"""
#last 9 values:
nine_frekvens = np.array(frekvens[-9:])
nine_vuvi = np.array(vu_vi[-9:])

print(linregress(nine_vuvi))





