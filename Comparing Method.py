import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal

Path = "/home/michelia.wibowo/labspaces/curacao-reef-mapping/misc/"
#png = xr.open_dataset(Path + "transectPNG_divescan_644.nc", decode_times=False)
crc= xr.open_dataset(Path + "transectCuracao_129.nc")
#PNG
#wp= png.W;wp
#cp= png.cube;cp
#Curacao
wc= crc.W;wc
cc= crc.cube;cc

#convert rad to ref for PNG
#Pixels from ref board
rb= cp.data[1205:1318,196:310,:]
rb.shape
#rb.shape is (113, 114, 480)

refspec = np.average(rb, axis=(0,1))
All=cp.data
ref=All/refspec

#chosing 5 different object on PNG
#pixel 1 Porites
P1= ref[1888,108,13:280]
#pixel 2 Scleractinia stony coral
P2= ref[6505,306,13:280]
#pixel 3 Acropora
P3= ref[5283, 403,13:280]
#pixel 4 Sea anemone actiniaria (chl-a detected)
P4= ref[2667,521,13:280]
#pixel 5 nephtheidae soft coral
P5=ref[4489,262,13:280]
wp[280]


#CURACAO
#chosing 5 different object Curacao
#pixel 1 diploria strigosa
C1=cc.data[8157,181,130:145]

#pixel 2 Madracis aurentera
C2=cc.data[10765,339,130:145]
C2.shape
wc[130]
wc[145]
#pixel 3 Millepora
C3=cc.data[10138, 323,130:145]
#pixel 4 Orbicella annularis
C4=cc.data[8407,45,130:145]
#pixel 5 Coralinales
C5=cc.data[8578,492,130:145]

wc1=wc[130:145]
C5.shape
wc1.shape


#plot without smoothing
fig, (ax1,ax2)=plt.subplots(1,2)
ax1.set_title('PNG divescan_644 raw')
ax1.plot(wp,P1, 'r', label='Porites')
ax1.plot(wp,P2, 'g', label='Scleractinia')
ax1.plot(wp,P3, 'b', label='Acropora')
ax1.plot(wp,P4, 'c', label='Anemone')
ax1.plot(wp,P5, 'y',label='Nephtheidae')
ax1.set(xlabel='wavelength', ylabel='reflectance')
ax1.legend()

ax2.set_title('Curacao Transect_129 raw')
ax2.plot(wc,C1, 'r', label='D. strigosa')
ax2.plot(wc,C2, 'g', label='M. aurentera')
ax2.plot(wc,C3, 'b', label='Millepora')
ax2.plot(wc,C4, 'c', label='O. anularis')
ax2.plot(wc,C5, 'y',label='Coralinales')
ax2.set(xlabel='wavelength', ylabel='reflectance')
ax2.legend()

#plt.set_title('Curacao Transect_129 raw')
plt.plot(wc1,C1, 'r', label='D. strigosa')
plt.plot(wc1,C2, 'g', label='M. aurentera')
plt.plot(wc1,C3, 'b', label='Millepora')
plt.plot(wc1,C4, 'c', label='O. anularis')
plt.plot(wc1,C5, 'y',label='Coralinales')
plt.set(xlabel='wavelength', ylabel='reflectance')
plt.legend()
C1.shape
# SG filter
#SGP1 = savgol_filter(P1, window_length=23, polyorder=3, deriv=0)
#SGP2 = savgol_filter(P2, window_length=23, polyorder=3, deriv=0)
#SGP3 = savgol_filter(P3, window_length=23, polyorder=3, deriv=0)
#SGP4 = savgol_filter(P4, window_length=23, polyorder=3, deriv=0)
#SGP5 = savgol_filter(P5, window_length=23, polyorder=3, deriv=0)

SGC1 = savgol_filter(C1, window_length=9, polyorder=2, deriv=0)
SGC2 = savgol_filter(C2, window_length=9, polyorder=2, deriv=0)
SGC3 = savgol_filter(C3, window_length=9, polyorder=2, deriv=0)
SGC4 = savgol_filter(C4, window_length=9, polyorder=2, deriv=0)
SGC5 = savgol_filter(C5, window_length=9, polyorder=2, deriv=0)

#plot sg

fig, (ax1,ax2)=plt.subplots(1,2)
ax1.set_title('SG - PNG divescan_644 SG')
ax1.plot(yp,SGP1, 'r', label='Porites')
ax1.plot(yp,SGP2, 'g', label='Scleractinia')
ax1.plot(yp,SGP3, 'b', label='Acropora')
ax1.plot(yp,SGP4, 'c', label='Anemone')
ax1.plot(yp,SGP5, 'y',label='Nephtheidae')
ax1.set(xlabel='wavelength', ylabel='reflectance')
ax1.legend()

ax2.set_title('SG - Curacao Transect_129 SG')
ax2.plot(yc,SGC1, 'r', label='D. strigosa')
ax2.plot(yc,SGC2, 'g', label='M. aurentera')
ax2.plot(yc,SGC3, 'b', label='Millepora')
ax2.plot(yc,SGC4, 'c', label='O. anularis')
ax2.plot(yc,SGC5, 'y',label='Coralinales')
ax2.set(xlabel='wavelength', ylabel='reflectance')
ax2.legend()

plt.set_title('SG - Curacao Transect_129 SG')
plt.plot(wc1,SGC1, 'r', label='D. strigosa')
plt.plot(wc1,SGC2, 'g', label='M. aurentera')
plt.plot(wc1,SGC3, 'b', label='Millepora')
plt.plot(wc1,SGC4, 'c', label='O. anularis')
plt.plot(wc1,SGC5, 'y',label='Coralinales')
plt.set(xlabel='wavelength', ylabel='reflectance')
plt.legend()


#polyfit

pfC1= np.polyfit(wc1,C1,2); pfC1
#RESULT:  array([1.617656e-04, -2.109100e-01,  7.058887e+01])
x = wc1
pfC1x=(1.617656e-04,*x*x)+(-2.109100e-0*x)+7.058887e+0
plt.plot(wc1, pfC1x, '-g', label='Polyfit')
plt.plot(wc1,SGC1, '-r', label='SG')
plt.plot(wc1,C1,'-b', label='Raw')
plt.legend()