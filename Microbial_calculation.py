
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal

transect='transect_129/'

print(f'Processing {transect}')

Path1 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/'
Path2 =  '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/transects/'
habs = xr.open_dataarray(Path1 + transect + 'classmap-crf.nc')
hd=habs.data
hd.shape
chl= xr.open_dataarray(Path2 + transect + 'chl_dermap2.nc')
chd=chl.data

#CALCULATING TURF
#create boolean mask from habitat map
#Turf Algae =40
turf_mask = hd== 40
turf_mask.shape
turf_mask= turf_mask*1
sum_turf_mask = np.sum(turf_mask)


#getting chl-a number
chd= chl.data
#masking the chl a to turf label
turf_chl= turf_mask*chd
turf_chl.shape
sum_turf_chl= np.sum(turf_chl)

chd.shape
np.sum(chd)
np.max(chd)
plt.imshow(chd, cmap='Greens')
plt.legend()
#CALCULATING CHL IN ALL
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
    finalmask37 = tomask_chla * mask37
    finalmask36 = tomask_chla * mask36
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

chlmask = chlamask(1,2,20,3,27,28,25,29,30,22,4,36,41,5,31,6,37,32,7,8,9,23,39,33,34,38,10,11,21,12,35,13,14,15,24,16,17,42,43,18,19,40,26,44,45,46,47,48)




#DOUBLE CHECK COVERAGE
def coverage (l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,l40,l41,l42,l43,l44,l45,l46,l47):
    cd = hd
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
    objc0 = np.sum(obj0)
    objc1 = np.sum(obj1)
    objc2 = np.sum(obj2)
    objc3 = np.sum(obj3)
    objc4 = np.sum(obj4)
    objc5 = np.sum(obj5)
    objc6 = np.sum(obj6)
    objc7 = np.sum(obj7)
    objc8 = np.sum(obj8)
    objc9 = np.sum(obj9)
    objc10 = np.sum(obj10)
    objc11 = np.sum(obj11)
    objc12 = np.sum(obj12)
    objc13 = np.sum(obj13)
    objc14 = np.sum(obj14)
    objc15 = np.sum(obj15)
    objc16 = np.sum(obj16)
    objc17 = np.sum(obj17)
    objc18 = np.sum(obj18)
    objc19 = np.sum(obj19)
    objc20 = np.sum(obj20)
    objc21 = np.sum(obj21)
    objc22 = np.sum(obj22)
    objc23 = np.sum(obj23)
    objc24 = np.sum(obj24)
    objc25 = np.sum(obj25)
    objc26 = np.sum(obj26)
    objc27 = np.sum(obj27)
    objc28 = np.sum(obj28)
    objc29 = np.sum(obj29)
    objc30 = np.sum(obj30)
    objc31 = np.sum(obj31)
    objc32 = np.sum(obj32)
    objc33 = np.sum(obj33)
    objc34 = np.sum(obj34)
    objc35 = np.sum(obj35)
    objc36 = np.sum(obj36)
    objc37 = np.sum(obj37)
    objc38 = np.sum(obj38)
    objc39 = np.sum(obj39)
    objc40 = np.sum(obj40)
    objc41 = np.sum(obj41)
    objc42 = np.sum(obj42)
    objc43 = np.sum(obj43)
    objc44 = np.sum(obj44)
    objc45 = np.sum(obj45)
    objc46 = np.sum(obj46)
    objc47 = np.sum(obj47)
    return objc0,objc1,objc2,objc3,objc4,objc5,objc6,objc7,objc8,objc9,objc10,objc11,objc12,objc13,objc14,objc15,objc16,objc17,objc18,objc19,objc20,objc21,objc22,objc23,objc24,objc25,objc26,objc27,objc28,objc29,objc30,objc31,objc32,objc33,objc34,objc35,objc36,objc37,objc38,objc39,objc40,objc41,objc42,objc43,objc44,objc45,objc46,objc47


coverage= coverage(1,2,20,3,27,28,25,29,30,22,4,36,41,5,31,6,37,32,7,8,9,23,39,33,34,38,10,11,21,12,35,13,14,15,24,16,17,42,43,18,19,40,26,44,45,46,47,48)

#Printing the information
#1      make sure the shape is the same
print(f'The shape of chl and habitat map is the same, {chd.shape}={hd.shape}')
#2      checking the pixels in turf algae
#this should be the same with pixels number of the turf
print(f'the pixels of turf algae in {transect} is {sum_turf_mask}')

#3      checking chl-a only in turf algae
print(f'concentration of chl-a of turf algae in {transect} is {sum_turf_chl}')

#4     chl-a in each 47 labels
#print(f'The chl in each 47 labels of {transect} is ')
print(f'({chlmask}')

#5       re-checking coverage in habitat map
#print(f'The chl in each 47 labels of {transect} is ')
print(f'({coverage}')