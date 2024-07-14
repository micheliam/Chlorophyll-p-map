import netCDF4
import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal

Path = "/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_006/"
crc = xr.open_dataset(Path + "boardreflect_nonorm.nc")
crc.cube
wc = crc.W
cc = crc.cube


#notes:
#wc[130] =660nm
#wc[145] =690nm
cc.shape
#crop area to map (because its not possible to map 29000*640 pixel at one time)
cropc=cc.data
#cropc=cc.data[0:1500,:,:]
#cropc=cc.data[13350:13650,:,:] #Where refboard is
cropc.shape
refboard=cc.data[1000:1500,:,:]

def chla (spectrum):
    plt.plot(wc,spectrum[1, 1, :], 'k', label='Raw signal')
    Csmooth= signal.savgol_filter(spectrum, window_length= 13, polyorder=2, deriv=0)
    plt.plot(wc,Csmooth[1,1,:], 'r',label='1st smoothing')
    Csmooth2 = signal.savgol_filter(Csmooth, window_length=9, polyorder=2, deriv=0)
    plt.plot(wc,Csmooth2[1,1,:], 'g', label='2nd smoothing')
    Cder= signal.savgol_filter(Csmooth2, window_length=15, polyorder=2, deriv=2)
    plt.plot(wc,Cder[1,1,:], 'b', label='Second Derivative')
    plt.ylabel("Reflectance")
    plt.xlabel("Wavelength (nm)")
    plt.legend()
    chlvalue135= Cder[:,:,135]
    chlvalue130 = Cder[:, :, 130]
    return chlvalue135

chlavalue= chla(cropc)
chlavalue.shape
refboards= chla(refboard)
refboards.shape

#plot
plt.figure()
plt.title("Transect 006 Chl-a at 670 absorptions")
#plt.imshow(chlavalue.clip(0), cmap='Greens', interpolation='nearest')
plt.imshow(refboards.clip(0), cmap='Greens', interpolation='nearest')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()
plt.show()