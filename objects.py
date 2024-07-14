
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal


Path = "/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_005/"
crc = xr.open_dataset(Path + "boardreflect_nonorm.nc")

wc = crc.W
cc = crc.cube
wc[130]

def objects (y,x,lsmooth,lder, wl1, wl2, name):
    obj= cc.data[y,x,wl1:wl2]
    SG = signal.savgol_filter(obj, window_length=lsmooth, polyorder=2, deriv=0)
    SDER= signal.savgol_filter(SG, window_length=lder, polyorder=2, deriv=2)
    wvl = wc[wl1:wl2]
    plt.figure()
    plt.title(name)
    plt.plot(wvl,obj,'r',label='Raw')
    plt.plot(wvl,SG,'g',label='SG smoothing')
    plt.plot(wvl,SDER,'b',label='Second Derivative')
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Reflectance")
    plt.legend()
    return obj

a= objects(15774,9,31,15,0,200,'Tape')
#b= objects(16197,90,31,15,110,150,'Rubble')
#c= objects(17566,431,31,15,110,150,'Sediment')
#d= objects(15676,96,31,15,110,150,'Meandrina')
#e= objects(17656,179,31,15,'Neofibularia')
#f= objects(13496,270,31,15,'Halimeda')

import sys
print (a)

