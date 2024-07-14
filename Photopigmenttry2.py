import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal
Path = "/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_129/"
file1 = xr.open_dataset(Path + "boardreflect_nonorm.nc")
# to see dimension
#num_pixel =file1.sizes["X"] * file1.sizes["Y"]; num_pixel

w= file1.W;w
c= file1.cube;c
#p= file1.par
c.W.shape
#checking dimension
c.shape
#result of transect 83 = (20145, 640, 400)
#result transect 129 = (29529, 640, 200)

#applying savgol filter
#Pders = np.zeros((29529, 640, 200))
#for y in range (0, 29529):
    #for x in range (0, 640):
        #Ps = c.data[y,x]
        #Pders[y ,x] = signal.savgol_filter(Ps, window_length=3, polyorder=2, deriv=2)

#Pders = Pders.clip(0); Pders

P = c.data[8157,181,122:152]; P.shape

Yex = np.linspace(644, 704, num=30);Yex.shape
Yex
plt.plot(Yex, P, '-k', label='raw data')
checkingspectra(P4)

def checkingspectra(n):
    #P = c.data[y, x]
    #Yex = np.linspace(644, 704, num=30)
    Yex = np.linspace(644, 704, num=30);
    #print (P)
    plt.plot(Yex, n, '-k', label='raw data')
    SG1 = savgol_filter(n, window_length=9, polyorder=2, deriv=0)
    x = Yex
    t1 = 8.33296095e-04 * x * x + (-1.14801143e+00) * x + 3.97079780e+02
    #SG2 = savgol_filter(n, window_length= 7, polyorder=4, deriv=2)
    #SG3 = savgol_filter(n, window_length= 3*w+2, polyorder=3*p, deriv=2)
    plt.plot(Yex, SG1, '-b', label= 'savitzky-golay')
    plt.plot(Yex, t1, '-r', label='polyfit')
    #plt.plot(Yex, SG3, '-g', label='W=17 P-2 W/P=8.5')
    #print(SG1[138])
    #Pder2 = signal.savgol_filter(P, window_length=3, polyorder=1, deriv=2)
    #print(Pder2[275])
    #plt.plot(Pder2, '-g', label= 'WL=3 PO=2 der=2')
    ax = plt.gca()
    ax.set_xlabel("Wavelength, nm")
    ax.set_ylabel("Reflectance")
    plt.legend()


#checking with polyfit
f1 = np.polyfit(Yex, P1, 2)
#f1 array([ 8.33296095e-04, -1.14801143e+00,  3.97079780e+02])
x=Yex
t1=8.33296095e-04*x*x+(-1.14801143e+00)*x+3.97079780e+02
plt.plot(t1)
#pixel 1 diploria strigosa
P1=c.data[8157,181,122:152]; P1.shape
P1all=c.data[8157,181,:];
checkingspectra(P1)
#pixel 2 Madracis aurentera
P2=c.data[10765,339,122:152]
checkingspectra(P2)
#pixel 3 Millepora
P3=c.data[10138, 323,122:152]
checkingspectra(P3)
#pixel 4 Orbicella annularis
P4=c.data[8407,45,122:152]
checkingspectra(P4)
#pixel 5 Aplysyna archeri  (no chl-a peak)
checkingspectra(10770,164)
#pixel 6 Coralinales with a peak
checkingspectra(8578,492)
#pixel 7 tape
checkingspectra(7023,419)
# 8 Coralinales
checkingspectra(8592, 485)
#pixel 9 Turf algae with a peak
checkingspectra(6912, 47)
#pixel 10 Turf algae no peak
checkingspectra(6880,73)
# pixel 11 Orbicella Anularis in a very deep peak
checkingspectra(9006,518)

def photopigmentmap(n):
    #chl=252
    SG = savgol_filter(n, window_length=5, polyorder=3, deriv=2)
    SG2 = savgol_filter(n, window_length=7, polyorder=2, deriv=2)
    #SG3= savgol_filter(n, window_length=17, polyorder=2, deriv=0)
    SG = SG.clip(0)
    SG2 = SG2.clip(0)
    plt.imshow(SG, cmap='Greens_r', interpolation='nearest')
    #plt.imshow(SG2, cmap='Greens_r', interpolation='nearest')
    ax = plt.gca()
    shw = ax.imshow(SG)
    bar = plt.colorbar(shw)
    plt.xlabel('X')
    plt.ylabel('Y')
    bar.set_label('ColorBar')
    plt.show()
    return SG
photopigmentmap(P1all)




#checking derivative with another method
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import ndarray
from numpy.ndarray import derivative


def checkingder(y,x):
    P = c.data[y, x]
    P_2d = P.derivative(n=2)
    #plt.plot(x_range,y_spl_2d(x_range))
    plt.plot(P_2d, '-r', label='2der')
    ax = plt.gca()
    ax.set_xlabel("Wavelength, nm")
    ax.set_ylabel("Reflectance")
    plt.legend()
    plt.show()

from detecta import detect_peaks


checkingder(5000,100)


import numpy as np
import matplotlib.pyplot as plt


P=c.data
P.shape
Pex=P[8407,45,:]
Pex.shape

Yex=np.linspace(400, 800, num=200)
plt.plot(Yex,Pex)

SG10 = signal.savgol_filter(Pex, window_length=0, polyorder=0, deriv=2)
plt.plot(SG10)
#to plot it
plt.plot(Yex,Pex)
# calculate polynomial

z = np.polyfit(list(range(200)),Pex, 2); z
#2nd order polynomial z = array([-3.45434577e-04,  4.18584643e-01, -1.16608305e+02])
#array([-1.39566002e-03,  2.85903480e-01, -4.44398021e+00])
#3rd order polynomial z=  array([-9.61908865e-07,  1.38600138e-03, -5.96959878e-01,  7.71737777e+01])
#polynomial f(x)= (-3.45434577e-04)x^2 + (4.18584643e-01)x  - 1.16608305e+02


# get x and y vectors
x = Pex
y = [y for y in range(400, 800)]
y = np.linspace(400, 800, num=200, retstep=True)
y2=list(y)
(1:200)


#calculating derivative using gaussian
# importing the library
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np

# defining the function
def function(x):
    return(-1.39566002e-03*x*x+ 2.85903480e-01*x-4.44398021e+00)
#return (-3.45434577e-04)*x*x + (4.18584643e-01)*x  - 1.16608305e+02
#return ((-9.61908865e-07)*x***)+(1.38600138e-03)*x**+(-5.96959878e-01*x)+7.71737777e+01

# calculating its derivative
def deriv(x):
    return derivative(function, x)

import numpy as np
import matplotlib.pyplot as plt


# defininf x-axis intervals
#y = np.linspace(400, 800)
# plotting the function
plt.plot(Yex, function(Pex), color='purple', label='Function')
plt.plot(Yex, np.poly1d(z)(Yex), color='purple', label='Function')
plt.plot(Yex,Pex)

def derivative (s):
    d=[]
    for i, a in enumerate(s):
        if i+1==len (s):
            diff= a
        else:
            diff= s[i+1]-a
        d.append (diff)
    return d

def prevderivative (s):
    d=[]
    for i, a in enumerate(s):
        if i+1==len (s):
            diff= a
        else:
            diff= s[i+1]-a
        d.append (diff)
    return d

def derivative1 (s):
    d=np.diff(s, axis=0)
    return d
Pex.shape
first_derivative= derivative(Pex)
second_derivative= derivative(first_derivative)
second_derivative
first_derivative1= derivative1(Pex)
second_derivative1= derivative(first_derivative1)
second_derivative1
a=second_derivative1
b=second_derivative
SGx = signal.savgol_filter(Pex, window_length=3, polyorder=2, deriv=2)
plt.plot(a,'-r')
plt.plot(b,'--g')
plt.plot(second_derivative,'-g)
plt.plot(SGx)
plt.plot(Yex,Pex)
derivative
# plotting its derivative
plt.plot(Yex, deriv(Pex), color='green', label='Derivative')
# formatting
plt.legend(loc='upper left')
plt.grid(True)

#derivative with scipy misc
from scipy.misc import derivative
def f(x):
    return x**3 + x**2
derivative(f, 1.0, dx=1e-6)
4.9999999999217337

