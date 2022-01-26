import numpy as np

vals = np.loadtxt("data1.csv") #load our excel file

print('average value:', round(np.average(vals),3)) #round to 3 s.f
print('average:', np.sum(vals)/len(vals))

print('median value:', np.median(vals))
print('standard dev:', np.std(vals))


val = (5.601054380986817,
3.5382979635322767,
2.6898881592786963,
3.0683681157582705,
4.982580359019149,
0.27647776565732984,
4.958333715761938,
1.227417391438317,
2.287653599054308,
2.7143080867085936,
0.36692231913525264,
1.7793014217286385,
3.893626324558491,
-1.8237431058155291,
6.379018317177231,
1.0634799014781082,
5.977860018511146,
0.9667635643804684,
-1.3516075683699809,
1.852576387069702,
1.9016212618825805,
5.0027113589042855,
4.496323730893322,
4.4483703999062705,
4.403808195636768,
4.610645966607665,
2.6697325244754597,
0.9955619334340238,
4.163472920197233,
7.2226767575389825,
3.120241016708151,
3.1019810694464205,
4.420248631382169,
2.809477927407536,
0.59266256257686,
3.526664887518068,
2.6784386395600115,
2.6693506695601843,
5.205471522338398,
3.752421009634556,
-0.16187365836427992,
0.804332685300865,
3.420616155075538,
2.1087083551639365,
2.46111106900773,
0.655797863428627,
3.255327328308312,
5.082240135816427,
5.565491880440949,
3.697997567139881,
1.2251077006421285,
3.122902583923623,
-0.7803739998082837,
6.4102631083566735,
3.5810741620890854,
2.8801755256800106,
3.7211106450585416,
1.3824184870581808,
3.590702425895821,
3.8966388971347565,
7.486592407954864,
4.708642033728175,
1.135923017999935,
3.0005712172662204,
3.3951975266020327,
3.5819079143653867,
4.927299607061566,
3.403002032882012,
1.2758170016256143,
5.167198427039278,
4.823694468668578,
2.326481047685857,
5.75693810247718,
3.5907526434497763,
2.0216257003528524,
0.543112035924183,
4.446702606770636,
5.205796774913901,
-0.5644191455505894,
3.493268690212306,
5.119062315232831,
4.295463663727476,
5.821900137132186,
1.3337355001192404,
3.9540153065940165,
1.8270411247572138,
2.524654682558799,
3.035653673733958,
4.591739856475668,
4.601261517954404,
4.007812140493759,
4.069077394697087,
2.042516420690992,
3.1173046260227686,
3.556329713630681,
4.805094186304887,
4.877034551917558,
0.581539238539869,
3.653516366309168,
2.5382953904334355
)

print('average=', np.average(val))
print('standard deviation=', np.std(val))
print('std from average:', np.std(val)/np.sqrt(len(val)))

import numpy as np
import matplotlib.pyplot as plt
import random
def mean(data):
    """
    finner gjennomsnitt
    """
    f = 1/len(data)*np.sum(data)
    return f


def std(data):
    """
    Finner standardavvik
    """
    f = mean(data)
    s = np.sqrt(1/(len(data)-1)*np.sum((data-f)**2))
    return s

def mean_std(data):
    """
    Finner standardavviket i gjennomsnittet
    """
    return std(data)/np.sqrt(len(data))
n = np.array([2,20,40,60,80,100,150,250,500,1000])
a = 1
b = 2
xmid = np.zeros(len(n))
s = np.zeros(len(n))
sm = np.zeros(len(n))

random.seed(1)
for i in range(len(n)):
    x = a+b*np.random.randn(n[i],1)
    xmid[i] = mean(x)
    s[i] = std(x)
    sm[i] = mean_std(x)

plt.style.use("seaborn")
plt.plot(n,xmid,label="Gjennomsnitt")
plt.plot(n,s,label="Standardavvik")
plt.plot(n,sm,label="Standardavviket i gjennomsnittet")
plt.legend()
plt.show()

#finding number of values within 1 std of mean value

tot = 0
avg = np.average(val)
std = np.std(val)
for value in val:
    if value <= (avg + std) and value >= (avg-std):
        tot += 1
    else:
        pass
print('percent in +/- 1std =', tot*100/len(val))

tot2 = 0
avg = np.average(val)
std = np.std(val)
for value in val:
    if value <= (avg + 2*std) and value >= (avg - 2*std):
        tot2 += 1
    else:
        pass
print('percent in +/- 2std =', tot2*100/len(val))