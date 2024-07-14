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
c= file1.cube
w= file1.W


#pixel 1 diploria strigosa
P1=c[8157,181,:]
#pixel 2 Madracis aurentera
P2=c[10765,339,:]
#pixel 3 Millepora
P3=c[10138, 323,:]
#pixel 4 Orbicella annularis
P4=c[8407,45,:]
#pixel 5 Aplysyna archeri  (no chl-a peak)
P5=c[10770,164,:]
#pixel 6 Coralinales with a peak
P6=c[8578,492,:]
#pixel 7 tape
P7=c[7023,419,:]
# 8 Coralinales
P8=c[8592, 485,:]
#pixel 9 Turf algae with a peak
P9=c[6912, 47,:]
#pixel 10 Turf algae no peak
P10=c[6880,73,:]
# pixel 11 Orbicella Anularis in a very deep peak
P11=c[9006,518,:]

#function
def derivative (s):
    d=[]
    for i, a in enumerate(s):
        if i+1==len (s):
            diff= a
        else:
            diff= s[i+1]-a
        d.append (diff)
    return d

#calculating derivative
def plottingder (k):
    first_derivative= derivative(k)
    second_derivative= derivative(first_derivative)
    SGx = signal.savgol_filter(k, window_length=3, polyorder=2, deriv=2)
    Yex = np.linspace(400, 800, num=200);
    plt.plot(Yex, second_derivative, 'g', label="Mathematical calculation SDER")
    plt.plot(Yex,SGx, 'r', label= "Savitzky Golay SDER")
    plt.plot(Yex,k, 'b', label="Raw data")
    ax = plt.gca()
    ax.set_xlabel("Wavelength, nm")
    ax.set_ylabel("Reflectance")
    plt.legend()
    plt.show()
    return second_derivative[137]

plottingder(P2)
plt.plot(SGx)
SGx[137]
import numpy as np
import matplotlib.pyplot as plt

from detecta import detect_peaks
index = detect_peaks(SGx)
print(index)