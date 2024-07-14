#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:34:37 2022

@author: michelia.wibowo
"""
import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal

Path = "/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_129/"
crc129= xr.open_dataset(Path + "transect.nc")

wc= crc129.W;wc
wc
cc= crc129.cube;cc

cc.shape
#result Y=29529 X=640  WL=400


#convert rad to ref for PNG
#Pixels from ref board
rb= cc.data[536:607,81:170,:]
rb.shape
#rb.shape is (71,89, 400)

#check if rb is the refboard
#rbcrop=rb[:,:,275]
#rbcrop.shape
#plt.imshow(rbcrop)
#plt.legend()


refspec = np.average(rb, axis=(0,1))
plt.plot(refspec)
rad=cc.data
ref=rad/refspec
plt.plot(refspec)
ref.shape


#chosing 5 different object Curacao
#pixel 1 diploria strigosa
C1=rad[8157,181,:]
C1r=ref[8157,181,:]
C1r.shape
C1[390:400]
C1[300]
C1r[300]
refspec[300]
plt.plot(refspec)
plt.plot(wc,C1)
#pixel 2 Madracis aurentera
C2=rad[10765,339,:]
C2r=ref[10765,339,:]
#pixel 3 Millepora
C3=rad[10138, 323,:]
C3r=ref[10138, 323,:]
#pixel 4 Orbicella annularis
C4=rad[8407,45,:]
C4r=ref[8407,45,:]
#pixel 5 Coralinales
C5=rad[8578,492,:]
C5r=ref[8578,492,:]


C5rr=C5r[0:297]
plt.plot(C5r)

C1rr=C1r[0:250]
plt.plot(C1rr)
#rad
plt.plot(wc,C1)
#ref
plt.plot(C1r)
C1rr=C1r[0:260]
plt.plot(C1rr)

C1[275]
C1r[275]
refspec[275]

#plot without smoothing
fig, (ax1,ax2)=plt.subplots(1,2)
ax1.set_title('PNG divescan_644 raw')
ax1.plot(yp,P1, 'r', label='Porites')
ax1.plot(yp,P2, 'g', label='Scleractinia')
ax1.plot(yp,P3, 'b', label='Acropora')
ax1.plot(yp,P4, 'c', label='Anemone')
ax1.plot(yp,P5, 'y',label='Nephtheidae')
ax1.set(xlabel='wavelength', ylabel='reflectance')
ax1.legend()

ax2.set_title('Curacao Transect_129 raw')
ax2.plot(yc,C1, 'r', label='D. strigosa')
ax2.plot(yc,C2, 'g', label='M. aurentera')
ax2.plot(yc,C3, 'b', label='Millepora')
ax2.plot(yc,C4, 'c', label='O. anularis')
ax2.plot(yc,C5, 'y',label='Coralinales')
ax2.set(xlabel='wavelength', ylabel='reflectance')
ax2.legend()

# SG filter
SGP1 = savgol_filter(P1, window_length=23, polyorder=3, deriv=0)
SGP2 = savgol_filter(P2, window_length=23, polyorder=3, deriv=0)
SGP3 = savgol_filter(P3, window_length=23, polyorder=3, deriv=0)
SGP4 = savgol_filter(P4, window_length=23, polyorder=3, deriv=0)
SGP5 = savgol_filter(P5, window_length=23, polyorder=3, deriv=0)

SGC1 = savgol_filter(C1, window_length=9, polyorder=3, deriv=0)
SGC2 = savgol_filter(C2, window_length=9, polyorder=3, deriv=0)
SGC3 = savgol_filter(C3, window_length=9, polyorder=3, deriv=0)
SGC4 = savgol_filter(C4, window_length=9, polyorder=3, deriv=0)
SGC5 = savgol_filter(C5, window_length=9, polyorder=3, deriv=0)

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






#####what if crc is rad
#rbc= cc.data[536:607,81:170,:]
#refspecc = np.average(rbc, axis=(0,1))
#plt.plot(refspecc)
#Allc=cc.data
#Allc.shape
#refc=Allc/refspecc

#refc.shape
#pixel 1 diploria strigosa
#C1r=refc[8157,181,:]
#pixel 2 Madracis aurentera
#C2r=refc[10765,339,:]
#pixel 3 Millepora
#C3r=refc[10138, 323,:]
#pixel 4 Orbicella annularis
#C4r=refc[8407,45,:]
#pixel 5 Coralinales
#C5r=refc[8578,492,:]


#plt.plot(C1r)
#plt.plot(C2r)
#plt.plot(C3r)
#plt.plot(C4r)

