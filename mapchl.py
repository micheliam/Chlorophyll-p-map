import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Path = "/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_005/"
crc = xr.open_dataset(Path + "boardreflect_nonorm.nc")
wc = crc.W
cc = crc.cube


def calculation(y_spec, x_spec, lsmooth, lder, wl1=0, wl2=200, po=2):
    spectrum = cc.data[y_spec, x_spec, wl1:wl2]
    Csmooth = signal.savgol_filter(spectrum, window_length=lsmooth, polyorder=po, deriv=0)
    Cder = signal.savgol_filter(Csmooth, window_length=lder, polyorder=po, deriv=2)
    return spectrum, Csmooth, Cder, wl1, wl2


# Tape(15774,9)
# Rubble (16197, 90)
# Sediment(17566, 431)
# Meandrina(15676, 96)
# Neofibularia(17656, 179)
# Halimeda (13496, 270)
# Diploria (13453, 387)
wc[150]
s1, cs1, cd1,wl11,wl21 = calculation(13453, 387, 7, 15, 20, 190, po=2)
s2, cs2, cd2,wl12,wl22 = calculation(13453, 387, 7, 15, 110, 150, po=2)
wl=wc[wl1:wl2]
plt.plot (wl,cs1)
cs21 = signal.savgol_filter(cs1, window_length=13, polyorder=2, deriv=0)
plt.plot (wl,cs21)
cs31 = signal.savgol_filter(cs21, window_length=11, polyorder=2, deriv=0)
plt.title('Spectrum reflectance on Diploria coral')
plt.plot(wl,cs31)
plt.xlabel('Wavelength(nm)')
plt.ylabel('Reflectance')

wl=wc[wl1:wl2]

def visualisation(spectrum, Csmooth, Cder, name):
    wl = wc[wl1:wl2]
    plt.figure()
    plt.title(name)
    plt.plot(wl, spectrum, 'r', label='Raw spectrum')
    plt.plot(wl, Csmooth, 'g', label='SG Smooth')
    plt.plot(wl, Cder, 'b', label='Second Derivative')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Reflectance')
    plt.legend()
    plt.show()

visualisation(s, cs, cd, 'Tape') #to plot the spectrum

def obtainchl(Cder,wl1):
    chlvalue = Cder[130-wl1]
    return chlvalue

# the chl-a value on the chosen pixel
chlv = obtainchl(cd,wl1)



def mapchl(Y1, Y2):
    cropc = cc.data[Y1:Y2,:,:]
    Ylength = Y2 - Y1
    Chlvalues = np.zeros((Ylength, 640))
    for y in range(0, Ylength):
        for x in range(0, 640):
            Cs = cropc[y, x]
            Chlvalues[y, x] = chlv(Cs)
    plt.figure()
    plt.title("Chl-a at 660 absorptions")
    plt.imshow(Chlvalues.clip(0), cmap='Greens', interpolation='nearest')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    return Chlvalues


mapchl(13350, 13650)
