import numpy as np 
import matplotlib.pyplot as plt

#constants of dispersjon formula:

def disp(lambd, B, C): #sellemier equation
    lambd = lambd/1000 #konverterer fra nanometer til mikrometer
    B1, B2, B3 = B[0], B[1], B[2] 
    C1, C2, C3 = C[0], C[1], C[2]
    n = np.sqrt(( 1 + ((B1*lambd**2)/(lambd**2 - C1)) +
          ((B2*lambd**2)/(lambd**2 - C2)) +
          ((B3*lambd**2)/(lambd**2 - C3)) ))
    
    print('diseprsion =', n)
    return n

B = [1.03961212, 0.231792344, 1.01046945]
C = [0.00600069867, 0.0200179144, 103.560653]   #konverterer fra micro til nano ve *1000
disp(520, B, C)

def R(d_x, d): #finner krumningsradien R, d_x = dobbel x, d = forhøyningen
    x = d_x/2
    R = (x**2 + d**2)/(2*d)
    print('R =', R)
    return R

R = R(31, 0.4) #begge i mm


def fokallengde(R, lambd, dispersjon): #også kalles for brennvidde (krumningsradien R, lamda, dispersjon)
    #funker for bikonvekse linser der R2 = -R1 = R
    R1 = -R
    R2 = -R1
    disp = (dispersjon - 1)*(1/R1 - 1/R2)
    print(abs(disp))
    n = dispersjon
    fokallengde = R/(2*(n-1))
    print('fokallengde =',fokallengde)
    return fokallengde

fokallengde(270, 520, R)

def bilde_avstand(s, f):
    avstand = f*s/(s-f)
    print('s_merkert (avstand) =', avstand)
    return avstand
