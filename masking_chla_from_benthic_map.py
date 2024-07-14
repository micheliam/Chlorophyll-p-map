import numpy
import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

Path = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/'
transect='transect_005/'
hab = mpimg.imread('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_005/classmap-crf.jpg')

classmap=xr.open_dataarray(Path + transect + "classmap-crf.nc")
cd=classmap.data
cd.shape
reflect = xr.open_dataarray(Path + transect + "boardreflect_nonorm.nc")
rd = reflect.data
rd.shape
W= reflect.W
#check if cd.shape = rd.shape
cd.shape
rd.shape
#checking dimension
cdim= 35235*640
cdim #17500800 total pixel in transect 006

#getting the all reflectance data in transect
spectrum=rd
spectrum.shape

#create boolean mask from benthic habitat map
obj = cd== 18 #Siderastrea siderea
mask= obj*1
np.sum(mask) #this should be the same with pixels number of the certain object
mask.shape
np.sum(mask)
#getting chl-a number
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

SELECTIONS = {
    'refboard': [1056, 1095, 207, 220],
    'porites aster': [1272, 1300, 81, 100],
    'halimeda': [1000, 1043, 95, 151],
    'diploria': [531, 573, 145, 200],
    'turf': [1465, 1552, 285, 412]
}


fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)

for name, coords in SELECTIONS.items():
    print(f'Processing {name}: {coords}')
    r1, r2, c1, c2 = coords
    pixels = reflect.sel(Y=slice(r1, r2),
                         X=slice(c1, c2),
                         W=slice(600, 750)
                         )

    pmean = pixels.mean(dim='W')
    pstd = pixels.std(dim='W')#.clip(1e-4)
    # print(pmean)
    # print(pstd)
    pmean = 0
    pstd = 1

    pixels: xr.DataArray = (pixels - pmean )/ pstd
    pixels = pixels.interpolate_na('W', method='slinear')
    X1 = savgol_filter(pixels.data, window_length=13, polyorder=2)
    X2 = savgol_filter(X1, window_length=9, polyorder=2)
    smoothed = pixels.copy(data=X2)
    smoothed.name = name

    smder = savgol_filter(X2, window_length=13, polyorder=2, deriv=2)
    smder = pixels.copy(data=smder)

    ax1.plot(smoothed.W, smoothed.mean(['Y', 'X']), label=name)
    ax2.plot(smder.W, smder.mean(['Y', 'X']), label=name)

    dermap = smder.sel(W=slice(655, 685)).max('W')

ax1.legend()
plt.show()

## TEST MAPPING
Rstart=0
Rstop=-1
pixels = reflect.sel(
    Y=slice(Rstart, Rstop),
    W=slice(600, 750)
            )


pmean = pixels.mean(dim='W')
pstd = pixels.std(dim='W')  # .clip(1e-4)

pixels: xr.DataArray = (pixels - pmean) / pstd
#pixels = pixels.interpolate_na('W', method='slinear')

X1 = savgol_filter(pixels.data, window_length=13, polyorder=2)
X1.shape
X2 = savgol_filter(X1, window_length=9, polyorder=2)

smoothed = pixels.copy(data=X2)
smoothed.name = name

smder = savgol_filter(X2, window_length=13, polyorder=2, deriv=2)
smder = pixels.copy(data=smder)


dermap = smder.sel(W=slice(655, 685)).max('W').clip(0)


from scipy.ndimage import median_filter

dermap_median = dermap.copy(
    data=median_filter(dermap, size=9, mode='reflect')
)


fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, sharex=True, sharey=True)
ax1.imshow(hab[Rstart: Rstop])
ax2.imshow(dermap_median, cmap='Greens', vmax=dermap.quantile(0.99, dim=('X', 'Y')))

nat = mpimg.imread('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_005/natural.jpg')
ncrop=nat[Rstart: Rstop,:,:]
ax3.imshow(ncrop)
plt.show()

dermap_median.shape
#####

#overlay the mask to tomask_chla
tomask_chla=chla(spectrum)
np.sum(tomask_chla)
#check if shape of  tomask_chla = mask
tomask_chla.shape
mask.shape

finalmask= tomask_chla*mask
finalmask=finalmask.clip(0)
np.sum(finalmask) #37.06131539570437

tomask_chla
#plotting the mask and the habitat map
fig, (ax1, ax2 = plt.subplots(1,2)
fig.suptitle('Benthic vs Chl-a ')
ax1.set_title('Habitat Map')
ax1.imshow(hab[1200:2000])
ax2.set_title('Chl-a Map')
chls= ax2.imshow(tomask_chla.clip(0)[600:1400,:], cmap='Greens', interpolation='nearest')
fig.colorbar(chls, ax=ax2)
plt.show()

############# END ############

obj18 = cd == 18
np.sum(obj18)

#Extra:
#Calculation for all labels at whole transect


cd=hd
tomask_chla=chd
def chlamask (l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,l40,l41,l42,l43,l44,l45,l46,l47):
    obj0 = cd== l0
    obj1 = cd== l1
    obj2 = cd== l2
    obj3 = cd== l3
    obj4 = cd== l4
    obj5 = cd== l5
    obj6 = cd== l6
    obj7 = cd== l7
    obj8 = cd== l8
    obj9 = cd== l9
    obj10 = cd== l10
    obj11 = cd== l11
    obj12 = cd== l12
    obj13 = cd == l13
    obj14 = cd == l14
    obj15 = cd == l15
    obj16 = cd == l16
    obj17 = cd == l17
    obj18 = cd == l18
    obj19 = cd == l19
    obj20 = cd == l20
    obj21 = cd == l21
    obj22 = cd == l22
    obj23 = cd == l23
    obj24 = cd == l24
    obj25 = cd == l25
    obj26 = cd == l26
    obj27 = cd == l27
    obj28 = cd == l28
    obj29 = cd == l29
    obj30 = cd == l30
    obj31 = cd == l31
    obj32 = cd == l32
    obj33 = cd == l33
    obj34 = cd == l34
    obj35 = cd == l35
    obj36 = cd == l36
    obj37 = cd == l37
    obj38 = cd == l38
    obj39 = cd == l39
    obj40 = cd == l40
    obj41 = cd == l41
    obj42 = cd == l42
    obj43 = cd == l43
    obj44 = cd == l44
    obj45 = cd == l45
    obj46 = cd == l46
    obj47 = cd == l47
    mask0 = obj0 * 1
    mask1 = obj1 * 1
    mask2 = obj2 * 1
    mask3 = obj3 * 1
    mask4 = obj4 * 1
    mask5 = obj5 * 1
    mask6 = obj6 * 1
    mask7 = obj7 * 1
    mask8 = obj8 * 1
    mask9 = obj9 * 1
    mask10 = obj10 * 1
    mask11 = obj11 * 1
    mask12 = obj12 * 1
    mask13 = obj13 * 1
    mask14 = obj14 * 1
    mask15 = obj15 * 1
    mask16 = obj16 * 1
    mask17 = obj17 * 1
    mask18 = obj18 * 1
    mask19 = obj19 * 1
    mask20 = obj20 * 1
    mask21 = obj21 * 1
    mask22 = obj22 * 1
    mask23 = obj23 * 1
    mask24 = obj24 * 1
    mask25 = obj25 * 1
    mask26 = obj26 * 1
    mask27 = obj27 * 1
    mask28 = obj28 * 1
    mask29 = obj29 * 1
    mask30 = obj30 * 1
    mask31 = obj31 * 1
    mask32 = obj32 * 1
    mask33 = obj33 * 1
    mask34 = obj34 * 1
    mask35 = obj35 * 1
    mask36 = obj36 * 1
    mask37 = obj37 * 1
    mask38 = obj38 * 1
    mask39 = obj39 * 1
    mask40 = obj40 * 1
    mask41 = obj41 * 1
    mask42 = obj42 * 1
    mask43 = obj43 * 1
    mask44 = obj44 * 1
    mask45 = obj45 * 1
    mask46 = obj46 * 1
    mask47 = obj47 * 1
    finalmask0 = tomask_chla * mask0
    finalmask1 = tomask_chla * mask1
    finalmask2 = tomask_chla * mask2
    finalmask3 = tomask_chla * mask3
    finalmask4 = tomask_chla * mask4
    finalmask5 = tomask_chla * mask5
    finalmask6 = tomask_chla * mask6
    finalmask7 = tomask_chla * mask7
    finalmask8 = tomask_chla * mask8
    finalmask9 = tomask_chla * mask9
    finalmask10 = tomask_chla * mask10
    finalmask11 = tomask_chla * mask11
    finalmask12 = tomask_chla * mask12
    finalmask13 = tomask_chla * mask13
    finalmask14 = tomask_chla * mask14
    finalmask15 = tomask_chla * mask15
    finalmask16 = tomask_chla * mask16
    finalmask17 = tomask_chla * mask17
    finalmask18 = tomask_chla * mask18
    finalmask19 = tomask_chla * mask19
    finalmask20 = tomask_chla * mask20
    finalmask21 = tomask_chla * mask21
    finalmask22 = tomask_chla * mask22
    finalmask23 = tomask_chla * mask23
    finalmask24 = tomask_chla * mask24
    finalmask25 = tomask_chla * mask25
    finalmask26 = tomask_chla * mask26
    finalmask27 = tomask_chla * mask27
    finalmask28 = tomask_chla * mask28
    finalmask29 = tomask_chla * mask29
    finalmask30 = tomask_chla * mask30
    finalmask31 = tomask_chla * mask31
    finalmask32 = tomask_chla * mask32
    finalmask33 = tomask_chla * mask33
    finalmask34 = tomask_chla * mask34
    finalmask35 = tomask_chla * mask35
    finalmask36 = tomask_chla * mask36
    finalmask37 = tomask_chla * mask37
    finalmask38 = tomask_chla * mask38
    finalmask39 = tomask_chla * mask39
    finalmask40 = tomask_chla * mask40
    finalmask41 = tomask_chla * mask41
    finalmask42 = tomask_chla * mask42
    finalmask43 = tomask_chla * mask43
    finalmask44 = tomask_chla * mask44
    finalmask45 = tomask_chla * mask45
    finalmask46 = tomask_chla * mask46
    finalmask47 = tomask_chla * mask47
    count0 = np.sum(finalmask0)
    count1 = np.sum(finalmask1)
    count2 = np.sum(finalmask2)
    count3 = np.sum(finalmask3)
    count4 = np.sum(finalmask4)
    count5 = np.sum(finalmask5)
    count6 = np.sum(finalmask6)
    count7 = np.sum(finalmask7)
    count8 = np.sum(finalmask8)
    count9 = np.sum(finalmask9)
    count10 = np.sum(finalmask10)
    count11 = np.sum(finalmask11)
    count12 = np.sum(finalmask12)
    count13 = np.sum(finalmask13)
    count14 = np.sum(finalmask14)
    count15 = np.sum(finalmask15)
    count16 = np.sum(finalmask16)
    count17 = np.sum(finalmask17)
    count18 = np.sum(finalmask18)
    count19 = np.sum(finalmask19)
    count20 = np.sum(finalmask20)
    count21 = np.sum(finalmask21)
    count22 = np.sum(finalmask22)
    count23 = np.sum(finalmask23)
    count24 = np.sum(finalmask24)
    count25 = np.sum(finalmask25)
    count26 = np.sum(finalmask26)
    count27 = np.sum(finalmask27)
    count28 = np.sum(finalmask28)
    count29 = np.sum(finalmask29)
    count30 = np.sum(finalmask30)
    count31 = np.sum(finalmask31)
    count32 = np.sum(finalmask32)
    count33 = np.sum(finalmask33)
    count34 = np.sum(finalmask34)
    count35 = np.sum(finalmask35)
    count36 = np.sum(finalmask36)
    count37 = np.sum(finalmask37)
    count38 = np.sum(finalmask38)
    count39 = np.sum(finalmask39)
    count40 = np.sum(finalmask40)
    count41 = np.sum(finalmask41)
    count42 = np.sum(finalmask42)
    count43 = np.sum(finalmask43)
    count44 = np.sum(finalmask44)
    count45 = np.sum(finalmask45)
    count46 = np.sum(finalmask46)
    count47 = np.sum(finalmask47)
    return count0,count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,count13,count14,count15,count16,count17,count18,count19,count20,count21,count22,count23,count24,count25,count26,count27,count28,count29,count30,count31,count32,count33,count34,count35,count36,count37,count38,count39,count40,count41,count42,count43,count44,count45,count46,count47
chlamask(1,2,20,3,27,28,25,29,30,22,4,36,41,5,31,6,37,32,7,8,9,23,39,33,34,38,10,11,21,12,35,13,14,15,24,16,17,42,43,18,19,40,26,44,45,46,47,48)
cdim
np.sum(tomask_chla)
tomask_chla.shape