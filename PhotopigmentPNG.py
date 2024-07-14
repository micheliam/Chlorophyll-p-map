import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal

Path = "/home/michelia.wibowo/labspaces/curacao-reef-mapping/misc/png_data/divescan_644/"
file1 = xr.open_dataset(Path + "transect.nc", decode_times=False)
file1
# to see dimension
num_pixel =file1.sizes["X"] * file1.sizes["Y"]; num_pixel

w= file1.W;w
c= file1.cube;c
#p= file1.par
c.W.shape
#checking dimension
c.shape
#result: 8960x640x480
w



#pixel 1 Porites
P1= c.data[1888,108,250:280]
P1.shape
P1all= c.data[1888,108,:]
P1allref= div[1888,108,:]
plt.plot(P1all)
plt.plot(P1allref)
#pixel 2 Scleractinia stony coral
P2= c.data[6505,306,:]
#pixel 3 Acropora
P3=c.data[5283, 403,:]
#pixel 4 Sea anemone actiniaria (chl-a detected)
P4=c.data[2667,521,:];P4.shape
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

c.data.shape
All=c.data
All/718
All
c.data
All
x=[1,2,3,4]
x/4
All.shape
x = np.arange(5)
div=np.true_divide(All, 718.8791666666667)
div
div.shape
plt.plot(div)
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])


Yex = np.linspace(386, 903.3, num=480);Yex.shape
Yex1=Yex[250:280]
Yex1
#655.98956159 to 687.30835073
plt.plot(Yex,P1all)
plt.plot(Yex1, P1, '--k', label='raw data')
plt.plot(Yex,P1all, label='whole spectrum')
t1= np.polyfit(Yex1,P1,2)
t1
#result t1 2.52406891e-01, -3.40483363e+02,  1.15051216e+05])
P1all
P1.shape
P1all.shape
plt.plot(P1all)
#result t1= [ 1.68220920e-02, -2.29645149e+01,  8.09367983e+03])


def checkingspectra(n):
    #P = c.data[y, x]
    #Yex = np.linspace(644, 704, num=30)
    Yex = np.linspace(386, 903.3, num=480);
    Yex1= Yex[250:280]
    #print (P)
    plt.plot(Yex1, n, '--k', label='raw data')
    SG1 = savgol_filter(n, window_length=13, polyorder=2, deriv=0)
    SG2 = savgol_filter(SG1, window_length= 13, polyorder=2, deriv=0)
    SG3 = savgol_filter(SG2, window_length= 13, polyorder=2, deriv=0)
    SG4 = savgol_filter(SG3, window_length=13, polyorder=2, deriv=0)
    x = Yex1
    t1 = 2.52406891e-01*x*x+(-3.40483363e+02)*x+1.15051216e+05
    plt.plot(Yex1, SG4, '-g', label= 'savitzky-golay')
    plt.plot(Yex1, t1, '-r', label='polyfit')
    #plt.plot(Yex, SG3, '-g', label='W=17 P-2 W/P=8.5')
    #print(SG1[138])
    #Pder2 = signal.savgol_filter(P, window_length=3, polyorder=1, deriv=2)
    #print(Pder2[275])
    #plt.plot(Pder2, '-g', label= 'WL=3 PO=2 der=2')
    ax = plt.gca()
    ax.set_xlabel("Wavelength, nm")
    ax.set_ylabel("Reflectance")
    plt.legend()
checkingspectra(P1)



#applying savgol filter
Chla = c.data[:, :, 268]; Yex[268]
Chlc = c.data[:, :, 60]; Yex[60]

def photopigmentmap(n):
    #chl=252
    SG = savgol_filter(n, window_length=17, polyorder=2, deriv=1)
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

plt.plot(Yex, P4)
Yex[268]

Pders = np.zeros((8960, 640, 480))
for y in range(0, 8960):
    for x in range(0, 640):
        Ps = c.data[y, x]
        Pders[y, x] = signal.savgol_filter(Ps, window_length=11, polyorder=2, deriv=2)
        plt.show()

#filter to 675nm only
m = Pders[:,:,262]
#plot chl-a map
plt.imshow(m, cmap ='Greens_r', interpolation = 'nearest')
# show image
shw = ax.imshow(m)
# make bar
bar = plt.colorbar(shw)
# show plot with labels
plt.xlabel('X')
plt.ylabel('Y')
bar.set_label('ColorBar')
plt.show()

#available color :Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Grseens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r


#calculate powerspectrum
X=P5

# Calculate the power spectrum
ps = np.abs(np.fft.fftshift(np.fft.fft(X))) ** 2;ps.shape

# Define pixel in original signal and Fourier Transform
pix = np.arange(X.shape[0])
fpix = np.arange(ps.shape[0]) - ps.shape[0] // 2

with plt.style.context(('ggplot')):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    axes[0].plot(pix, X)
    axes[0].set_xlabel('pixel')
    axes[0].set_ylabel('irradiance spectrum')

    axes[1].semilogy(fpix, ps, 'b')
    axes[1].set_xlabel('pixel (Fourier space)')
    axes[1].set_ylabel('Power Spectrum')

# Calculate the power spectrum
ps = np.abs(np.fft.fftshift(np.fft.fft(X[0:100]))) ** 2

# Define pixel in origina signal and Fourier Transform
pix = np.arange(X[0:100].shape[0])
fpix = np.arange(ps.shape[0]) - ps.shape[0] // 2
pix.shape
ps.shape
with plt.style.context(('ggplot')):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    axes[0].plot(pix, X[0:100])
    axes[0].set_xlabel('pixel')
    axes[0].set_ylabel('irradiance spectrum')

    axes[1].semilogy(fpix, ps, 'b')
    axes[1].set_xlabel('pixel (Fourier space)')
    axes[1].set_ylabel('power spectrum')


# Calculate three different smoothed spectra
X_smooth_1 = savgol_filter(X, 5, polyorder=2, deriv=0)
X_smooth_2 = savgol_filter(X, 11, polyorder=2, deriv=0)
X_smooth_3 = savgol_filter(X, 17, polyorder=2, deriv=0)

# Calculate the power spectra in a featureless region
ps = np.abs(np.fft.fftshift(np.fft.fft(X[0:100]))) ** 2
ps_1 = np.abs(np.fft.fftshift(np.fft.fft(X_smooth_1[0:100]))) ** 2
ps_2 = np.abs(np.fft.fftshift(np.fft.fft(X_smooth_2[0:100]))) ** 2
ps_3 = np.abs(np.fft.fftshift(np.fft.fft(X_smooth_3[0:100]))) ** 2

# Define pixel in Fourier space
fpix = np.arange(ps.shape[0]) - ps.shape[0] // 2

plt.figure(figsize=(10, 8))
with plt.style.context(('ggplot')):
    plt.semilogy(fpix, ps, 'b', label='No smoothing')
    plt.semilogy(fpix, ps_1, 'r', label='Smoothing: w/p = 2.5')
    plt.semilogy(fpix, ps_2, 'g', label='Smoothing: w/p = 5.5')
    plt.semilogy(fpix, ps_3, 'm', label='Smoothing: w/p = 7.5')
    plt.legend()
    plt.xlabel('pixel')

####

#checking der with function - Daniel's
def derivative (s):
    d=[]
    for i, a in enumerate(s):
        if i+1==len (s):
            diff= a
        else:
            diff= s[i+1]-a
        d.append (diff)
    return d

P4
new_array = np.array([1,4,6,100,2,4])
new_output=np.diff(new_array, axis=0);new_output
result = np.diff(new_array, axis=0);result
print("Difference along axis=0:",new_output)
print("Difference along axis=1:",result)

#derivative with function - Michel's
def derivative1 (s):
    d=np.diff(s, axis=0)
    return d
P4.shape


first_derivative1=derivative1(P4)
second_derivative1=derivative1(first_derivative1)
second_derivative1
plt.plot(second_derivative1)



first_derivative= derivative(P4)
second_derivative= derivative(first_derivative)
plt.plot(second_derivative, '--r')
plt.plot(second_derivative1, 'b')
SGx = signal.savgol_filter(P4, window_length=9, polyorder=2, deriv=0)


plt.plot(Yex,P4, '-r', label='raw data')
plt.plot(Yex,SGx, '--b', label='Savitzky Golay w=9 o=2 d=0')
plt.legend()
plt.show()
derivative
# plotting its derivative
plt.plot(Yex, deriv(Pex), color='green', label='Derivative')
# formatting
plt.legend(loc='upper left')
plt.grid(True)


#between 663,2-685,2 nm
Pchl=P[252:272]
Pchl
np.amin(Pchl)
#Yexc = np.linspace(387.1, 397, num=10)
#plt.plot(Yexc,Pchl, '-r', label='chl range raw data')

#function to check spectra
def checkingspectra(y,x):
    P = c.data[y, x]
    Yex = np.linspace(386, 903.3, num=480)
    w=5
    p=2
    plt.plot(Yex, P, '-k', label='raw data')
    SG1 = savgol_filter(P, window_length=w, polyorder=p, deriv=0)
    SG2 = savgol_filter(P, window_length= 2*w+1, polyorder=p, deriv=0)
    SG3 = savgol_filter(P, window_length= 4*w+1, polyorder=3*p, deriv=0)
    plt.plot(Yex, SG1, '-b', label= 'WL=w(5) PO=p(2) der=0')
    plt.plot(Yex, SG2, '-r', label='WL=2w+1 PO=p der=0')
    plt.plot(Yex, SG3, '-g', label='WL=4w+1 PO=3p der=0')
    #print(SG1[138])
    #Pder2 = signal.savgol_filter(P, window_length=3, polyorder=1, deriv=2)
    #print(Pder2[275])
    #plt.plot(Pder2, '-g', label= 'WL=3 PO=2 der=2')
    ax = plt.gca()
    ax.set_xlabel("Wavelength, nm")
    ax.set_ylabel("Reflectance")
    plt.legend()

