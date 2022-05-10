import numpy as np 
import matplotlib.pyplot as plt

#constants of dispersjon formula:

def disp(lambd, B, C):
    B1, B2, B3 = B[0], B[1], B[2] 
    C1, C2, C3 = C[0], C[1], C[2]
    dispersion = np.sqrt((B1*lambd**2)/(lambd**2 - C1) +
                        (B2*lambd**2)/(lambd**2 - C2) +
                        (B3*lambd**2)/(lambd**2 - C3) + 1)
    print('diseprsion =', dispersion)
    return dispersion

B = [1.03961212, 0.23179234, 1.01046945]
C = [0.00600069867, 0.0200179144, 103.560653]
disp(520, B, C)

