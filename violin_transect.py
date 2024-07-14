
# import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
import numpy as np
from numpy import append


transect_3m=['006','031','054','081','091','102','118','134']
transect_6m=['005', '026', '044', '080','086','097','130']
transect_9m=['019', '024','043','084','085','095','114','129']
All_transect=['006','031','054','081','091','102','118','134','005', '026', '044', '080','086','097','130','019', '024','043','084','085','095','114','129']
green_area= ['134','130','129','031','026','024','054','044','043']
yellow_area=[]
Carmabi=['006','005','019']
#A=[*Carmabi,*green_area]
#len(A)

transect='005'
Path1 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_'
Path2 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/transects/transect_'
habs = xr.open_dataarray(Path1 + transect + '/classmap-crf.nc')
LABEL_IDS= {label: label_id for label, label_id in zip (habs.attrs['label'],habs.attrs['label_id'])}
LABEL_IDS
#hd=habs.data
#plt.imshow(hd)
def select_chl2 (label,transect):
    Path1 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_'
    Path2 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/transects/transect_'
    habs = xr.open_dataarray(Path1 + transect + '/classmap-crf.nc')
    hd = habs.data
    chl = xr.open_dataarray(Path2 + transect + '/chl_dermap2.nc')
    chd = chl.data
    class_mask = hd == label
    class_chl = chd[class_mask]
    return class_chl[class_chl > 0].flatten()


class_chls = {
    'Acropora cervicornis': [],
    'Acropora palmata': [],
    'Actiniaria': [],
    'Agaricia': [],
    'Agelas conifera': [],
    'Aiolochroia crassa': [],
    'Antipathes caribbeana': [],
    'Aplysina archeri': [],
    'Aplysina cauliformis': [],
    'Briareum asbestinum': [],
    'Colpophyllia natans': [],
    'Corallinales': [],
    'Cyanobacterial mat': [],
    'Dendrogyra cylindrus': [],
    'Desmapsamma anchorata': [],
    'Dichocoenia stokesii': [],
    'Dictyota': [],
    'Diplastrella': [],
    'Diploria labyrinthiformis': [],
    'Diploria strigosa': [],
    'Eusmilia fastigiata': [],
    'Gorgoniidae': [],
    'Halimeda opuntia': [],
    'Hyrtios': [],
    'Ircinia campana': [],
    'Lobophora variegata': [],
    'Madracis auretenra': [],
    'Meandrina meandrites': [],
    'Millepora': [],
    'Montastrea cavernosa': [],
    'Neofibularia nolitangere': [],
    'Orbicella annularis': [],
    'Orbicella faveolata': [],
    'Orbicella franksi': [],
    'Plexauridae': [],
    'Porites asteroides': [],
    'Porites furcata': [],
    'Sediment': [],
    'Shadow': [],
    'Siderastrea siderea': [],
    'Solenastrea bournoni': [],
    'Turf algae': [],
    'Zoanthid': [],
    'float': [],
    'material': [],
    'reel': [],
    'refboard': [],
    'tape': [],
}
class_chls
#coral grouping (reefgroups)
Coral=[]
coral_species = [
    'Orbicella annularis', 'Acropora cervicornis','Acropora palmata'
]

for x in class_chls:
    if x in coral_species:
        Coral.append(class_chls[x])

Coral=np.concatenate(Coral)
Coral.shape
LABEL_IDS

###

chl_pixels=[]
depth_pixels = []
for transect_num in All_transect:
    if transect_num in transect_3m:
        depth = 3
    elif transect_num in transect_6m:
        depth = 6
    elif transect_num in transect_9m:
        depth = 9
    else:
        raise ValueError()

    # for label in class_chls:
    label = 'Cyanobacterial mat'
    label_id = LABEL_IDS[label]
    chl_ = select_chl2(label_id, transect_num)
    chl_pixels.append(chl_)
    depths_ = np.ones_like(chl_) * depth
    depth_pixels.append(depths_)
    #    class_chls[label].append(chl_)

CHL = np.concatenate(chl_pixels)
DEPTHS = np.concatenate(depth_pixels)


import statsmodels.api as sm
import statsmodels.formula.api as smf
mod = sm.OLS(endog=CHL, exog=DEPTHS)
print('fitting linear model. hold on')
res = mod.fit()
print(res.summary())

exit()

#3 meters
for transect_num in transect_3m:
    for label in class_chls:
        label_id = LABEL_IDS[label]
        chl_ = select_chl2(label_id, transect_num)
        class_chls[label].append(chl_)


Sediment_3m=class_chls['Sediment']
Turf_3m= class_chls['Turf algae']
Cyanos_3m= class_chls['Cyanobacterial mat']
Madracis_3m=class_chls['Madracis auretenra']
Orbicella_3m= class_chls['Orbicella annularis']
Dstrigoas_3m= class_chls['Diploria strigosa']
Cca_3m= class_chls['Corallinales']
dicty_3m=class_chls['Dictyota']
halim_3m=class_chls['Halimeda opuntia']
lobo_3m=class_chls['Lobophora variegata']


#6meters
for transect_num in transect_6m:
    for label in class_chls:
        label_id = LABEL_IDS[label]
        chl_ = select_chl2(label_id, transect_num)
        class_chls[label].append(chl_)

Sediment_6m=class_chls['Sediment']
Turf_6m= class_chls['Turf algae']
Cyanos_6m= class_chls['Cyanobacterial mat']
Madracis_6m=class_chls['Madracis auretenra']
Orbicella_6m= class_chls['Orbicella annularis']
Dstrigoas_6m= class_chls['Diploria strigosa']
Cca_6m= class_chls['Corallinales']
dicty_6m=class_chls['Dictyota']
halim_6m=class_chls['Halimeda opuntia']
lobo_6m=class_chls['Lobophora variegata']

#9meters
for transect_num in transect_9m:
    for label in class_chls:
        label_id = LABEL_IDS[label]
        chl_ = select_chl2(label_id, transect_num)
        class_chls[label].append(chl_)

Sediment_9m=class_chls['Sediment']
Turf_9m= class_chls['Turf algae']
Cyanos_9m= class_chls['Cyanobacterial mat']
Madracis_9m=class_chls['Madracis auretenra']
Orbicella_9m= class_chls['Orbicella annularis']
Dstrigoas_9m= class_chls['Diploria strigosa']
Cca_9m= class_chls['Corallinales']
dicty_9m=class_chls['Dictyota']
halim_9m=class_chls['Halimeda opuntia']
lobo_9m=class_chls['Lobophora variegata']

#All sites all transects
for transect_num in All_transect:
    for label in class_chls:
        label_id = LABEL_IDS[label]
        chl_ = select_chl2(label_id, transect_num)
        class_chls[label].append(chl_)


Sediment_all=class_chls['Sediment']
Turf_all= class_chls['Turf algae']
Cyanos_all= class_chls['Cyanobacterial mat']
Madracis_all=class_chls['Madracis auretenra']
Orbicella_all= class_chls['Orbicella annularis']
Dstrigoas_all= class_chls['Diploria strigosa']
Cca_all= class_chls['Corallinales']
dicty_all=class_chls['Dictyota']
halim_all=class_chls['Halimeda opuntia']
lobo_all=class_chls['Lobophora variegata']


Sediment_all.shape
sedime
type(transect_3m)
A.shape
#CONTOH A
#All sites all transects
for transect_num in transect_9m:
    for label in class_chls:
        label_id = LABEL_IDS[label]
        chl_ = select_chl2(label_id, transect_num)
        class_chls[label].numpy.append(chl_)
for label in class_chls:
    print(label, np.asarray(class_chls[label]).shape)
for label in class_chls:
    class_chls[label] = np.concatenate(class_chls[label])

Sediment_Ax=class_chls['Sediment']
Turf_Ax= class_chls['Turf algae']
Cyanos_Ax= class_chls['Cyanobacterial mat']
Madracis_Ax=class_chls['Madracis auretenra']



#Checking the dimension
#this why i need to concatenate it
for label in class_chls:
    print(label, np.asarray(class_chls[label]).shape)

for label in class_chls:
    class_chls[label] = np.concatenate(class_chls[label])
Turf_all
#Plot

ax= sns.violinplot(data=[Madracis_all, Orbicella_all, Dstrigoas_all,Cca_all,dicty_all,halim_all,lobo_all], palette=[colormap['Madracis auretenra'],colormap['Orbicella annularis'],colormap['Diploria strigosa'],colormap['Corallinales'],colormap['Dictyota'],colormap['Halimeda opuntia'],colormap['Lobophora variegata']])
ax.set_xticklabels(['Madracis auretenra','Orbicella annularis','Diploria strigosa','Corallinales','Dictyota','Halimeda opuntia','Lobophora variegata'])
ax.set_ylim(0,600)
ax.set_title('All Transect')



Sediment_all=class_chls['Sediment']
Turf_all= class_chls['Turf algae']
Cyanos_all= class_chls['Cyanobacterial mat']
Madracis_all=class_chls['Madracis auretenra']
Orbicella_all= class_chls['Orbicella annularis']
Dstrigoas_all= class_chls['Diploria strigosa']
Cca_all= class_chls['Corallinales']
dicty_all=class_chls['Dictyota']
halim_all=class_chls['Halimeda opuntia']
lobo_all=class_chls['Lobophora variegata']

import yaml

with open('colormap.yml') as f:
    colormap = yaml.safe_load(f)

colormap['Acropora cervicornis']

Turf_all.shape


c=1



###########
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
import numpy as np

transect_3m=['006','031','054','081','091','102','118','134']

def select_chl (label,transect):
    Path1 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_'
    Path2 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/transects/transect_'
    habs = xr.open_dataarray(Path1 + transect + '/classmap-crf.nc')
    hd = habs.data
    chl = xr.open_dataarray(Path2 + transect + '/chl_dermap2.nc')
    chd = chl.data
    obj= hd== label
    obj=obj*chd
    obj=obj.flatten()
    obj = obj[obj != 0]
    return(obj)


turf= np.concatenate((select_chl(40,transect_3m[0]),select_chl(40,transect_3m[1]),select_chl(40,transect_3m[2]),select_chl(40,transect_3m[3]),select_chl(40,transect_3m[4]),select_chl(40,transect_3m[5]),select_chl(40,transect_3m[6]),select_chl(40,transect_3m[7])), axis=None)
cyan= np.concatenate((select_chl(41,transect_3m[0]),select_chl(41,transect_3m[1]),select_chl(41,transect_3m[2]),select_chl(41,transect_3m[3]),select_chl(41,transect_3m[4]),select_chl(41,transect_3m[5]),select_chl(41,transect_3m[6]),select_chl(41,transect_3m[7])), axis=None)
sed= np.concatenate((select_chl(42,transect_3m[0]),select_chl(42,transect_3m[1]),select_chl(42,transect_3m[2]),select_chl(42,transect_3m[3]),select_chl(42,transect_3m[4]),select_chl(42,transect_3m[5]),select_chl(42,transect_3m[6]),select_chl(42,transect_3m[7])), axis=None)

ax= sns.violinplot(data=[turf, sed, cyan])
ax.set_xticklabels(['Turf Algae','Sediment','Cyanobacterial Mat'])
ax.set_title('3 Meter Depth')


###
# for i in transect_3m:
#     Turf1= select_chl(40,i)
#     np.concatenate(Turf1)
#     print Turf1.shape

a.shape
a=select_chl(40,'006')
b=select_chl(40,'031')
a.shape
b.shape
type(a)
#8996475+1454125=10450600



class_chls = {
    'Sediment': [],
    'Turf algae': [],
    'cyanos': [],
}



for transect_num in transect_3m:
    for label in class_chls:
        Turf = LABEL_IDS[label]
        chl_ = select_chl(40, transect_num)
        class_chls[label].append(chl_)

for label in class_chls:
    class_chls[label] = np.concatenate(class_chls[label]




##
for i in transect_3m:
    select_chl2(40, transect_3m[i])

select_chl(40,transect_3m[0])

    print(i)



turf006= select_chl(40,'006')
turf006.shape

for label in class_chls:
    class_chls[label'] = np.concatenate(class_chls[label]


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break