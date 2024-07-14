import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal

#chla map
crc =xr.open_dataset('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_006/boardreflect_nonorm.nc')
cc = crc.cube
wc=crc.W
refboard=cc.data[1000:1500,:,:]
cc.data.shape
def chla (spectrum):
    #plt.plot(wc,spectrum[1, 1, :], 'k', label='Raw signal')
    Csmooth= signal.savgol_filter(spectrum, window_length= 13, polyorder=2, deriv=0)
    #plt.plot(wc,Csmooth[1,1,:], 'r',label='1st smoothing')
    Csmooth2 = signal.savgol_filter(Csmooth, window_length=9, polyorder=2, deriv=0)
    #plt.plot(wc,Csmooth2[1,1,:], 'g', label='2nd smoothing')
    Cder= signal.savgol_filter(Csmooth2, window_length=15, polyorder=2, deriv=2)
    #plt.plot(wc,Cder[1,1,:], 'b', label='Second Derivative')
    #plt.ylabel("Reflectance")
    #plt.xlabel("Wavelength (nm)")
    #plt.legend()
    chlvalue135= Cder[:,:,135] #absorption at 670nm
    chlvalue130 = Cder[:, :, 130] #absorption at 660nm
    return chlvalue135

refboards= chla(refboard)
refboards.shape


#habitat map
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
hab = mpimg.imread('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_006/classmap-crf.jpg')
hcrop=hab[1000:1500,:,:]
hcrop.shape


#natural
nat = mpimg.imread('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_006/natural.jpg')
ncrop=nat[1000:1500,:,:]


#plot
fig, (ax1, ax2,ax3) = plt.subplots(1,2,3)

fig, axs = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle('Transect 006 Y=1000:1500')
axs[0].set_title('Chl-A')
chls= axs[0].imshow(refboards.clip(0), cmap='Greens', interpolation='nearest')
#axs[0].set(xlabel='X', ylabel='Y')
axs[1].set_title('Habitat Map')
habs=axs[1].imshow(hcrop)
#axs[1].set(xlabel='X', ylabel='Y')
axs[2].set_title('Natural View')
nabs=axs[2].imshow(ncrop)
#axs[2].set(xlabel='X', ylabel='Y')
#fig.colorbar(chls)
fig.colorbar(chls, ax=axs[0])
plt.show()


fig.suptitle('Transect 006 Y=1000:1500')
#fig 1
ax1.set_title('Chl-a Map')
chls= ax1.imshow(refboards.clip(0), cmap='Greens', interpolation='nearest')
ax1.set(xlabel='X', ylabel='Y')
#ax1.colorbar()
#fig 2
ax2.set_title('Habitat Map')
habs=ax2.
ax2.set(xlabel='X', ylabel='Y')
#fig 3
ax2.set_title('Natural View')
nats=ax2.imshow(ncrop)
ax2.set(xlabel='X', ylabel='Y')

fig.colorbar(chls, ax=ax1)
plt.show()