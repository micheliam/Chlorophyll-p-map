import numpy
import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal

classmap = xr.open_dataarray('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_054/classmap-crf.nc')
cd=classmap.data
cd.shape

cdim= 27659* 640 #17701760 total pixel in transect 054
cdim

def name(no):
    name=classmap.label[no]
    id=classmap.label_id[no]
    return name, id

def coverage(name, label):
    cd = classmap.data
    obj = cd== label
    unique_array = np.unique(obj, return_counts=True)
    objcount = np.sum(obj)
    coverage = objcount / cdim * 100
    coverage1 = round(coverage, 2) #round off to 2 decimals
    #plt.figure()
    #plt.title(name+" Coverage: "+str(coverage1)+"%")
    #plt.imshow(obj, cmap='Greens')
    #plt.xlabel("X axis")
    #plt.ylabel("Y axis")
    return coverage,objcount,unique_array

name(1)

coverage    ('Dictyota', 37)


###

def coverage3(label):
    cd = classmap.data
    obj = cd== label
    unique_array = np.unique(obj, return_counts=True)
    objcount = np.sum(obj)
    coverage = objcount / cdim * 100
    coverage1 = round(coverage, 2) #round off to 2 decimals
    #plt.figure()
    #plt.title(name+" Coverage: "+str(coverage1)+"%")
    #plt.imshow(obj, cmap='Greens')
    #plt.xlabel("X axis")
    #plt.ylabel("Y axis")
    return objcount
coverage3(label)

label=[]

label = np.array([1,2,20])
label=[1,2,20,3,27,28,25,29,30,22,4,36,41,5,31,6,37,32,7,8,9,23,39,33,34,38,10,11,21,12,35,13,14,15,24,16,17,42,43,18,19,40,26,44,45,46,47,48]

cd.shape
for l in label:
    l = cd == label

l.shape


###
import numpy
import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal


classmap = xr.open_dataarray('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_129/classmap-crf.nc')
cd=classmap.data
cd.shape

cdim=cd.shape[0]*cd.shape[1]
cdim
def coverage1 (l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,l40,l41,l42,l43,l44,l45,l46,l47):
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


coverage1(1,2,20,3,27,28,25,29,30,22,4,36,41,5,31,6,37,32,7,8,9,23,39,33,34,38,10,11,21,12,35,13,14,15,24,16,17,42,43,18,19,40,26,44,45,46,47,48)