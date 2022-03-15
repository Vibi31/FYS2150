import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from numpy import log

"""open excel file and append values into two lists"""

B = []                                       #magnetic flux list 
theta = []                                   #angle 

with open('RC_data.csv', 'r') as file:
    firstline = next(file)                   #first line is skipped (title: B, theta)
    for line in file:                        #read every line and append each values
        values = line.split(',')
        B.append(values[0])
        theta.append(values[1])

B, theta = np.array(B), np.array(theta)      #convert our lists to numpy array's

#oppgave 

def 
"""
#using equations from page 4 of the lab text, we get D-para, D-orto. 
#Parrallelt og ortogonalt paa rotasjons aksen, 'D' er avmagnetiseringsfaktoren (si det rask 3 ganger)
"""

#function takes in epsilon (eksentrisiteten)
#eksentrisiteten er et mål på hvor flattrykt ellipsoiden er
def avmagnet(epsilon):                              
    D_orto = (1-1/epsilon**2) * (1-(1/(2*epsilon))*log((1+epsilon)/(1-epsilon)))
    D_para = (1-D_orto)/2

