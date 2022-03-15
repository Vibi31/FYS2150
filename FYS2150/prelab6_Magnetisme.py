import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from numpy import log, sqrt

"""open excel file and append values into two lists"""

B = []                                       #magnetic flux list 
theta = []                                   #angle 

with open('faraday.csv', 'r') as file:
    firstline = next(file)                   #first line is skipped (title: B, theta)
    for line in file:                        #read every line and append each values
        values = line.split(',')
        B.append(values[0])
        theta.append(values[1])


#convert our lists to numpy array's
B, theta = np.array(B).astype(np.float), np.array(theta).astype(np.float)      




"""
#using equations from page 4 of the lab text, we get D-para, D-orto. 
#Parrallelt og ortogonalt paa rotasjons aksen, 'D' er avmagnetiseringsfaktoren (si det rask 3 ganger)
#function takes in 2 values, axis length 
#eksentrisiteten er et mål på hvor flattrykt ellipsoiden er
"""

def avmagnet(a_para, a_orto):                 #avmagnetiseringsfaktor, tar in akselengder 

    f = a_para/a_orto                         #akselengde faktor?

    epsilon =   sqrt(1-1/(f**2))              #eksentrisiteten  

    D_orto = (1-1/epsilon**2) * (1-(1/(2*epsilon))*log((1+epsilon)/(1-epsilon)))
    D_para = (1-D_orto)/2

    print('parallel avmagnetiseringsfaktor', D_para)
    print('ortogonal avmagnetiseringsfaktor', D_orto)
    print()
    
    return D_orto, D_para

#prelab oppgave 6:
avmagnet(20, 2)




"""
Next function calculates verdet-constant (refer to page 6 of lab text)
#takes in magnetic flux (B), angle (theta), flintglass length (L), uncertainty (uncert)

Verdet-konstanten kan bestemmes fra linjens stigningstall
vi vet at: theta = VBL 
verdet konstant (V), lengde (L), magnetisk fluks (B), vinkel (theta)

V = theta/(B*L)
"""

def verdet(B, theta, L, uncert): #magnetisk-fluks, vinkel, flintglass lengde (mm), lengde usikkerhet
    lin = linregress(B*L, theta)   #theta som funksjon av magnetisk-fluks
    verdet_konstant = lin.slope 
    verdet_deviation = lin.stderr

    print('verdet konstant (Tm):', verdet_konstant*1000)
    print('verdet konstant usikkerhet (Tm):', verdet_deviation*1000)


#oppgave 7
verdet(B, theta, 30, 1)
