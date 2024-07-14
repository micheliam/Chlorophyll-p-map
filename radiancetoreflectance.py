import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal

#Converting Radiance to Reflectance

#Open radiance files
Path = "/home/michelia.wibowo/labspaces/curacao-reef-mapping/misc/png_data/divescan_644/"
rad = xr.open_dataset(Path + "transect.nc", decode_times=False)
rad


w= rad.W;w
c= rad.cube;c

#checking dimension
c.shape
#result: Y= 8960  X= 640 Wl=480nm

#Pixels from ref board
rb= c.data[1205:1318,196:310,:]
rb.shape
#rb.shape is (113, 114, 480)
#w[268] = 675.4
#rbchl=c.data[1205:1318,196:310,268]



plt.imshow(rbchl, cmap='Greens_r', interpolation='nearest')
ax = plt.gca()
shw = ax.imshow(rbchl)
bar = plt.colorbar(shw)
plt.xlabel('X')
plt.ylabel('Y')
bar.set_label('ColorBar')
plt.show()


refspec = np.average(rb, axis=(0,1))
refspec.shape
plt.plot(refspec)


All=c.data
ref=All/refspec
ref.shape

np.max(c.data)
np.max(ref)
All.shape
ref.shape
w[282]
#Crop to wavelength 660-690nm
#w[254]=660.3nm
#w[282]=690.6nm
#try it out on porites pixel
#pixel 1 Porites
P1rad= All[1888,108,254:282]
P1ref= ref[1888,108,254:282]
#pixel 2 Scleractinia stony coral
P2rad= All[6505,306,254:282]
P2ref= ref[6505,306,254:282]
#pixel 3 Acropora
P3rad= All[5283, 403,254:282]
P3ref= ref[5283, 403,254:282]
#pixel 4 Sea anemone actiniaria (chl-a detected)
P4rad= All[2667,521,254:282]
P4ref= ref[2667,521,254:282]
#w[13]= 400nm
#w[384]=800.7 nm
P4refA= ref[2667,521,13:384]
#plot a whole transect
YexA=np.linspace(400,800.7,num=290)
plt.plot(YexA,P4refA)
#Plot different method
Yex = np.linspace(660.3, 690.56, num=28)
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Radiance")
plt.plot(Yex,P1ref,'-k', label= 'Raw reflectance')
#method 1
SGref1 = savgol_filter(P1ref, window_length=9, polyorder=2, deriv=0)
plt.plot(Yex,SGref1, '--r', label='SG wl=9, po=2, d=0')
plt.legend()
#method 2
PF1= np.polyfit(Yex,P1ref,2); PF1
#result F(x)= (1.49239741e-05*x*x)+(-1.61192981e-02*x)+4.90326683e+00
x = Yex
PFref1=(1.49239741e-05*x*x)+(-1.61192981e-02*x)+4.90326683e+00
plt.plot(Yex, PFref1, '--g', label='Polyfit')

plt.legend()
#method 1
SGref1der2 = savgol_filter(P1ref, window_length=9, polyorder=2, deriv=1)
plt.plot(Yex,SGref1der2, '--c', label='SG wl=9, po=2, d=1')
plt.legend()
#method 2
x=Yex
PFref1der1=(2.98479482e-05*x)+(-1.61192981e-02)
PFref1der1.shape
plt.plot(Yex, PFref1der1, '--m', label='Polyfit 1st derivative')
plt.legend()

#(1.49239741e-05*x*x)+(-1.61192981e-02*x)+4.90326683e+00
plt.plot(Yex, PFref1, '--g', label='Polyfit')
plt.legend()

p = np.poly1d([1.49239741e-05,-1.61192981e-02,4.90326683e+00])
p1 = np.polyder(p)
p1
plt.plot(Yex,)
p2=np.polyder(p1)
p2
poly1d([3, 2, 1])




plt.plot(Yex, P1ref,'-r',label='Porites')
plt.plot(Yex, P2ref,'-g',label='Stony coral')
plt.plot(Yex, P3ref,'-b',label='Acropora')
plt.plot(Yex, P4ref,'-c',label='Sea anemone')
plt.legend()
ax.legend()
plt.plot(Yex, P1ref)



#pixel 5 nephtheidae soft coral
P5=c.data[4489,262,:]
#pixel 6 Sinularia soft coral
P6=c.data[3832,325,:]
#pixel 7 Diploastrea heliopora brain coral
P7=c.data[1195,21,:]
# 8 Sediment
P8=c.data[1757, 303,:]
#pixel 9 Thorectidae sponges
P9=c.data[911,145,:]
#pixel 10 Merulinidae
P10=c.data[824,143,:]
# pixel 11 Ref board
P11= c.data[603,124,:]
np.max(P11)
#ans=  2759
np.average(P11)
#ans=718.8791666666667


plt.plot(Prefx)
Pref2= Prad/refspec
plt.plot(Pref2)
plt.plot(Prad)
plt.plot(Pref,'--r')

# create figure and axis objects with subplots()
fig,ax = plt.subplots()
Yex = np.linspace(386, 903.3, num=480)
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Radiance")
ax.plot(Yex, Prad,'-k',label='Radiance')
ax.legend(loc='upper right')
ax.legend()
ax2=ax.twinx()
ax2.set_xlabel("Wavelength (nm)")
ax2.set_ylabel("Reflectance")
ax2.plot(Yex, Prefx,'--r',label='Reflectance with average axis(0,1,2)')
ax2.legend(loc='lower right')
plt.show()


#checking on other coral

#pixel 1 Porites
P1= c.data[1888,108,250:280]
P1.shape
P1all= c.data[1888,108,:]
P1allref= div[1888,108,:]
plt.plot(P1all)
plt.plot(P1allref)



#applying savgol filter
Chla = ref[:, :, 268];
ref.shape
w[268]=675.4



#to map using SG filter
def photopigmentmap(n):
    #chl=252
    SG = savgol_filter(n, window_length=9, polyorder=2, deriv=2)
    SG2 = savgol_filter(n, window_length=17, polyorder=2, deriv=1)
    SG3= savgol_filter(n, window_length=17, polyorder=2, deriv=0)
    SG = SG.clip(0)
    plt.imshow(SG, cmap='Greens_r', interpolation='nearest')
    ax = plt.gca()
    shw = ax.imshow(SG)
    bar = plt.colorbar(shw)
    plt.xlabel('X')
    plt.ylabel('Y')
    bar.set_label('ColorBar')
    plt.show()
    return SG

photopigmentmap(Chla)
