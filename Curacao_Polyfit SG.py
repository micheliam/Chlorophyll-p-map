import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal

Path = "/home/michelia.wibowo/labspaces/curacao-reef-mapping/misc/"
crc = xr.open_dataset(Path + "transectCuracao_129.nc")

wc = crc.W;
wc
cc = crc.cube;
cc

# chosing 5 different object Curacao, cut into 30 nm important wavelength (660-690nm)
wc[130]  # 660nm
wc[145]  # 690nm

# Y axis
wc1 = wc[130:145]

# pixel 1 diploria strigosa
C1 = cc.data[8157, 181, 130:145]
C1All = cc.data[8157, 181, :]
# pixel 2 Madracis aurentera
C2 = cc.data[10765, 339, 130:145]
C2All = cc.data[10765, 339, :]
# pixel 3 Millepora
C3 = cc.data[10138, 323, 130:145]
C3All = cc.data[10138, 323, :]
# pixel 4 Orbicella annularis
C4 = cc.data[8407, 45, 130:145]
C4All = cc.data[8407, 45, :]
# pixel 5 Coralinales
C5 = cc.data[8578, 492, 130:145]
C5All = cc.data[8578, 492, :]
# pixel 6 Dendrogyra cilindrus
C6 = cc.data[5260, 264, 130:145]
C6All = cc.data[5260, 264, :]
# pixel 7 Dictyota
C7 = cc.data[8291,431,130:145]
C7All = cc.data[8291,431, :]



# SG filter 1st smoothing
SGC1 = savgol_filter(C1All, window_length=31, polyorder=2, deriv=0)
SGC2 = savgol_filter(C2All, window_length=31, polyorder=2, deriv=0)
SGC3 = savgol_filter(C3All, window_length=31, polyorder=2, deriv=0)
SGC4 = savgol_filter(C4All, window_length=31, polyorder=2, deriv=0)
SGC5 = savgol_filter(C5All, window_length=31, polyorder=2, deriv=0)
SGC6 = savgol_filter(C6All, window_length=31, polyorder=2, deriv=0)
SGC7 = savgol_filter(C7All, window_length=31, polyorder=2, deriv=0)
SGC7x = savgol_filter(C7All, window_length=31, polyorder=3, deriv=0)

SGC7[137]
SGC7x[137]

# SG filter smoothed twice
SGC1s = savgol_filter(SGC1, window_length=21, polyorder=2, deriv=0)
SGC2s = savgol_filter(SGC2, window_length=21, polyorder=2, deriv=0)
SGC3s = savgol_filter(SGC3, window_length=21, polyorder=2, deriv=0)
SGC4s = savgol_filter(SGC4, window_length=21, polyorder=2, deriv=0)
SGC5s = savgol_filter(SGC5, window_length=21, polyorder=2, deriv=0)
SGC6s = savgol_filter(SGC6, window_length=21, polyorder=2, deriv=0)
SGC7s = savgol_filter(SGC7, window_length=21, polyorder=3, deriv=0)
SGC7xs = savgol_filter(SGC7x, window_length=7, polyorder=2, deriv=0)
SGC7s[137]
SGC7xs[137]


# SG filter 2der
SGC1d = savgol_filter(SGC1, window_length=31, polyorder=2, deriv=2)
SGC2d = savgol_filter(SGC2, window_length=31, polyorder=2, deriv=2)
SGC3d = savgol_filter(SGC3, window_length=31, polyorder=2, deriv=2)
SGC4d = savgol_filter(SGC4, window_length=31, polyorder=2, deriv=2)
SGC5d = savgol_filter(SGC5, window_length=31, polyorder=2, deriv=2)
SGC6d = savgol_filter(SGC6, window_length=13, polyorder=2, deriv=2)
SGC7d = savgol_filter(SGC7, window_length=31, polyorder=2, deriv=2)

#   EXPERIMENT
SGC6ds13 = savgol_filter(SGC6, window_length=13, polyorder=2, deriv=2)
SGC6ds15 = savgol_filter(SGC6, window_length=15, polyorder=2, deriv=2)
SGC6ds17 = savgol_filter(SGC6, window_length=17, polyorder=2, deriv=2)
#Pixel 6 coral
plt.title("D=0 Wl=31, D=2 Wl=3 ")
#plt.plot(wc, C6All, 'r', label='Raw')
#plt.plot(wc, SGC6, 'k', label='SG Smooth')
plt.plot(wc, SGC6ds13, 'r', label='13')
plt.plot(wc, SGC6ds15, 'g', label='15')
plt.plot(wc, SGC6ds17, 'b', label='17')
#plt.plot(wc, SGC6ds, 'y', label='SG Der-2 smooth')
plt.legend()
plt.show()

cc.shape
cropc=cc.data[400:700,:,:]
cropc.shape

def chla (spectrum):
    Csmooth= signal.savgol_filter(spectrum, window_length=31, polyorder=2, deriv=0)
    Cder= signal.savgol_filter(Csmooth, window_length=15, polyorder=2, deriv=2)
    chlvalue= Cder[130]
    return chlvalue

chla(C6All)


Chlvalues = np.zeros((300,640))

for y in range(0, 300):
    for x in range(0, 640):
        Cs = cropc[y,x]
        Chlvalues[y,x]= chla(Cs)

Chlvalues.shape
Chlvalues.clip(0)


plt.figure
plt.imshow(Chlvalues, cmap='Greens_r', interpolation='nearest')
plt.show()




    def derivative(s):
        d = []
        for i, a in enumerate(s):
            if i + 1 == len(s):
                diff = a
            else:
                diff = s[i + 1] - a
            d.append(diff)
        return d


#coba coba
#Pixel 7 Dictyota
plt.figure()
plt.title("Wl=7 to Wl=21(3)")
plt.plot(wc, C7All, 'r', label='Raw')
plt.plot(wc, SGC7, 'k', label='SG Smooth')
plt.plot(wc, SGC7s, 'b', label='SG Smooth-2')
# plt.plot(wc,SGC6d,'g', label='SG derivative')
plt.legend()
plt.show()

plt.figure()
plt.title("Wl=21(3) to Wl=7")
plt.plot(wc, C7All, 'r', label='Raw')
plt.plot(wc, SGC7x, 'k', label='SG Smooth')
plt.plot(wc, SGC7xs, 'b', label='SG Smooth-2')
# plt.plot(wc,SGC6d,'g', label='SG derivative')
plt.legend()
plt.show()


# polyfit
# Pixel 1
pfC1 = np.polyfit(wc1, C1, 2);
pfC1
pfC1.shape
# RESULT:  array([1.617656e-04, -2.109100e-01,  7.058887e+01])
x = wc1
pfC1x = (1.617656e-04 * x * x) + (-2.109100e-01 * x) + 7.058887e+01
# Pixel 2
pfC2 = np.polyfit(wc1, C2, 2);
pfC2
# RESULT:   array([-8.897107e-04,  1.202905e+00, -4.054511e+02])
x = wc1
pfC2x = (-8.897107e-04 * x * x) + (1.202905e+00 * x) + -4.054511e+02
# Pixel 3
pfC3 = np.polyfit(wc1, C3, 2);
pfC3
# RESULT:   array([ 1.090362e-03, -1.416259e+00,  4.619523e+02])
x = wc1
pfC3x = (1.090362e-03 * x * x) + (-1.416259e+00 * x) + 4.619523e+02
# Pixel4
pfC4 = np.polyfit(wc1, C4, 2);
pfC4
# RESULT:   array([3.998225e-03, -5.325339e+00,  1.779282e+03])
x = wc1
pfC4x = (3.998225e-03 * x * x) + (-5.325339e+00 * x) + 1.779282e+03
# Pixel5
pfC5 = np.polyfit(wc1, C5, 2);
pfC5
# RESULT:  array([ 2.062511e-03, -2.808865e+00,  9.572717e+02])
x = wc1
pfC5x = (2.062511e-03 * x * x) + (-2.808865e+00 * x) + 9.572717e+02

# plot
plt.plot(wc1, pfC1x, '-*r', label='Polyfit')
plt.plot(wc1, SGC1, '--r')
plt.plot(wc1, C1, '-r', label='D. strigosa')
plt.plot(wc1, pfC2x, '-*g', label='Polyfit')
plt.plot(wc1, SGC2, '--g')
plt.plot(wc1, C2, '-g', label='M. aurentera')
plt.plot(wc1, pfC3x, '-*b', label='Polyfit')
plt.plot(wc1, SGC3, '--b')
plt.plot(wc1, C3, '-b', label='Millepora')
plt.plot(wc1, pfC4x, '-*c', label='Polyfit')
plt.plot(wc1, SGC4, '--c')
plt.plot(wc1, C4, '-c', label='O. anularis')
plt.plot(wc1, pfC5x, '-*y', label='Polyfit')
plt.plot(wc1, SGC5, '--y')
plt.plot(wc1, C5, '-y', label='Coralinales')
plt.xlabel('Wavelength(nm')
plt.ylabel('Reflectance')
plt.legend()
plt.show()

plt.plot(wc, C2all)
