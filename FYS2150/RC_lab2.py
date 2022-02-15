"""
Code written by Synne Mo Sadnes and Vibishan Raveendrarajah
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
frekvens = [10,50,100,300,500,1*10**3,5*10**3,10*10**3,50*10**3,100*10**3,500*10**3,800*10**3,1*10**6]
v_inn = [1.998,1.985,1.966,1.903,1.897,1.88,1.872,1.857,1.874, 1.854,1.826,1.23,1.627]
v_ut = [1.974,1.880, 1.651, 890.710*10**(-3), 574.*10**(-3), 299*10**(-3), 62*10**(-3), 32*10**(-3), 7*10**(-3), 4*10**(-3), 24*10**(-3), 22*10**(-3), 26*10**(-3)]

V = np.log10(np.array(v_ut)/np.array(v_inn))

omega = np.log10(np.array(frekvens)*2*np.pi)
frek = np.array(frekvens)

# linregress

#plt.xscale('log')
#plt.yscale('log')
omega2 = np.array(frekvens)*2*np.pi
v2 = np.array(v_ut)/np.array(v_inn)
reg = stats.linregress(omega[3:8], V[3:8])
reg2 = stats.linregress(omega2[3:8], v2[3:8])
print(reg2.intercept)
print("usikker", (reg2.stderr) )
plt.plot(omega, V)
plt.plot(omega[3:8], reg.intercept + reg.slope * omega[3:8])
plt.savefig('linregress.png', dpi=300)

print(reg.intercept)
plt.title('Log graf')
plt.xlabel('Frekvens [Hz]')
plt.ylabel('Spenning [V]')
plt.show()

print('delta C', np.sqrt((3.64*0.2/10)**2 + (3.64*0.00000259/0.0275)**2))