import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
import numpy as np
from numpy import append

#introduce transect
transect_3m=['006','031','054','081','091','102','118','134']
transect_6m=['005', '026', '044', '080','086','097','130']
transect_9m=['019', '024','043','084','085','095','114','129']
All_transect=['006','031','054','081','091','102','118','134','005', '026', '044', '080','086','097','130','019', '024','043','084','085','095','114','129']
transect_high=['005','006','019','085','086','091']
transect_med= ['095','097','102','114','118']
transect_low=['024','026','031','043','044','054','080','081','084','129','130','134']


#define LABEL_IDS
Path1 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_'
Path2 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/transects/transect_'
habs = xr.open_dataarray(Path1 + transect + '/classmap-crf.nc')
LABEL_IDS= {label: label_id for label, label_id in zip (habs.attrs['label'],habs.attrs['label_id'])}
LABEL_IDS

def select_chl (label,transect):
    Path1 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_'
    Path2 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/transects/transect_'
    habs = xr.open_dataarray(Path1 + transect + '/classmap-crf.nc')
    hd = habs.data
    chl = xr.open_dataarray(Path2 + transect + '/chl_dermap2.nc')
    chd = chl.data
    class_mask = hd == label
    class_chl = chd[class_mask]
    return class_chl[class_chl > 0].flatten()

#3 METERS

class_chls_3m = {
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
class_chls_3m

for transect_num in transect_3m:
    for label in class_chls_3m:
        label_id = LABEL_IDS[label]
        chl_ = select_chl(label_id, transect_num)
        class_chls_3m[label].append(chl_)
for label in class_chls_3m:
    print(label, np.asarray(class_chls_3m[label]).shape)
for label in class_chls_3m:
    class_chls_3m[label] = np.concatenate(class_chls_3m[label])

madracis_3m=class_chls_3m['Madracis auretenra']
orbicella_3m= class_chls_3m['Orbicella annularis']
dstrigosa_3m= class_chls_3m['Diploria strigosa']
ofaveo_3m=class_chls_3m['Orbicella faveolata']
sidera_3m= class_chls_3m['Siderastrea siderea']

cyanos_3m= class_chls_3m['Cyanobacterial mat']
sediment_3m=class_chls_3m['Sediment']
turf_3m= class_chls_3m['Turf algae']
dicty_3m=class_chls_3m['Dictyota']
halim_3m=class_chls_3m['Halimeda opuntia']
lobo_3m=class_chls_3m['Lobophora variegata']
macroalgae_3m=np.concatenate((dicty_3m,halim_3m,lobo_3m))
cca_3m= class_chls_3m['Corallinales']

#6meters
class_chls_6m = {
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
for transect_num in transect_6m:
    for label in class_chls_6m:
        label_id = LABEL_IDS[label]
        chl_ = select_chl(label_id, transect_num)
        class_chls_6m[label].append(chl_)
for label in class_chls_6m:
    print(label, np.asarray(class_chls_6m[label]).shape)
for label in class_chls_6m:
    class_chls_6m[label] = np.concatenate(class_chls_6m[label])

madracis_6m=class_chls_6m['Madracis auretenra']
orbicella_6m= class_chls_6m['Orbicella annularis']
dstrigosa_6m= class_chls_6m['Diploria strigosa']
ofaveo_6m=class_chls_6m['Orbicella faveolata']
sidera_6m= class_chls_6m['Siderastrea siderea']


cyanos_6m= class_chls_6m['Cyanobacterial mat']
sediment_6m=class_chls_6m['Sediment']
turf_6m= class_chls_6m['Turf algae']
dicty_6m=class_chls_6m['Dictyota']
halim_6m=class_chls_6m['Halimeda opuntia']
lobo_6m=class_chls_6m['Lobophora variegata']
macroalgae_6m=np.concatenate((dicty_6m,halim_6m,lobo_6m))
cca_6m= class_chls_6m['Corallinales']


#9meters
class_chls_9m = {
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

for transect_num in transect_9m:
    for label in class_chls_9m:
        label_id = LABEL_IDS[label]
        chl_ = select_chl(label_id, transect_num)
        class_chls_9m[label].append(chl_)
for label in class_chls_9m:
    print(label, np.asarray(class_chls_9m[label]).shape)
for label in class_chls_9m:
    class_chls_9m[label] = np.concatenate(class_chls_9m[label])

madracis_9m=class_chls_9m['Madracis auretenra']
orbicella_9m= class_chls_9m['Orbicella annularis']
dstrigosa_9m= class_chls_9m['Diploria strigosa']
ofaveo_9m=class_chls_9m['Orbicella faveolata']
sidera_9m= class_chls_9m['Siderastrea siderea']

cyanos_9m= class_chls_9m['Cyanobacterial mat']
sediment_9m=class_chls_9m['Sediment']
turf_9m= class_chls_9m['Turf algae']
dicty_9m=class_chls_9m['Dictyota']
halim_9m=class_chls_9m['Halimeda opuntia']
lobo_9m=class_chls_9m['Lobophora variegata']
macroalgae_9m=np.concatenate((dicty_9m,halim_9m,lobo_9m))
cca_9m= class_chls_9m['Corallinales']


#INFRASTRUCTURE
#High
class_chls_high = {
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
class_chls_high

for transect_num in transect_high:
    for label in class_chls_high:
        label_id = LABEL_IDS[label]
        chl_ = select_chl(label_id, transect_num)
        class_chls_high[label].append(chl_)
for label in class_chls_high:
    print(label, np.asarray(class_chls_high[label]).shape)
for label in class_chls_high:
    class_chls_high[label] = np.concatenate(class_chls_high[label])

madracis_high=class_chls_high['Madracis auretenra']
orbicella_high= class_chls_high['Orbicella annularis']
dstrigosa_high= class_chls_high['Diploria strigosa']
ofaveo_high=class_chls_high['Orbicella faveolata']
sidera_high= class_chls_high['Siderastrea siderea']

cyanos_high= class_chls_high['Cyanobacterial mat']
sediment_high=class_chls_high['Sediment']
turf_high= class_chls_high['Turf algae']
dicty_high=class_chls_high['Dictyota']
halim_high=class_chls_high['Halimeda opuntia']
lobo_high=class_chls_high['Lobophora variegata']
macroalgae_high=np.concatenate((dicty_high,halim_high,lobo_high))
cca_high= class_chls_high['Corallinales']

#medium


class_chls_med = {
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
class_chls_med

for transect_num in transect_med:
    for label in class_chls_med:
        label_id = LABEL_IDS[label]
        chl_ = select_chl(label_id, transect_num)
        class_chls_med[label].append(chl_)
for label in class_chls_med:
    print(label, np.asarray(class_chls_med[label]).shape)
for label in class_chls_med:
    class_chls_med[label] = np.concatenate(class_chls_med[label])

madracis_med=class_chls_med['Madracis auretenra']
orbicella_med= class_chls_med['Orbicella annularis']
dstrigosa_med= class_chls_med['Diploria strigosa']
ofaveo_med=class_chls_med['Orbicella faveolata']
sidera_med= class_chls_med['Siderastrea siderea']

cyanos_med= class_chls_med['Cyanobacterial mat']
sediment_med=class_chls_med['Sediment']
turf_med= class_chls_med['Turf algae']
dicty_med=class_chls_med['Dictyota']
halim_med=class_chls_med['Halimeda opuntia']
lobo_med=class_chls_med['Lobophora variegata']
macroalgae_med=np.concatenate((dicty_med,halim_med,lobo_med))
cca_med= class_chls_med['Corallinales']

#low

class_chls_low = {
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
class_chls_low

for transect_num in transect_low:
    for label in class_chls_low:
        label_id = LABEL_IDS[label]
        chl_ = select_chl(label_id, transect_num)
        class_chls_low[label].append(chl_)
for label in class_chls_low:
    print(label, np.asarray(class_chls_low[label]).shape)
for label in class_chls_low:
    class_chls_low[label] = np.concatenate(class_chls_low[label])

madracis_low=class_chls_low['Madracis auretenra']
orbicella_low= class_chls_low['Orbicella annularis']
dstrigosa_low= class_chls_low['Diploria strigosa']
ofaveo_low=class_chls_low['Orbicella faveolata']
sidera_low= class_chls_low['Siderastrea siderea']

cyanos_low= class_chls_low['Cyanobacterial mat']
sediment_low=class_chls_low['Sediment']
turf_low= class_chls_low['Turf algae']
dicty_low=class_chls_low['Dictyota']
halim_low=class_chls_low['Halimeda opuntia']
lobo_low=class_chls_low['Lobophora variegata']
macroalgae_low=np.concatenate((dicty_low,halim_low,lobo_low))
cca_low= class_chls_low['Corallinales']



#Color Map
import yaml

with open('colormap.yml') as f:
    colormap = yaml.safe_load(f)



#Plot Depth
plt.figure()
ax= sns.boxplot(data=[madracis_3m, madracis_6m,madracis_9m,orbicella_3m,orbicella_6m, orbicella_9m, dstrigosa_3m, dstrigosa_6m,dstrigosa_9m,ofaveo_3m, ofaveo_6m,ofaveo_9m,sidera_3m,sidera_6m,sidera_9m], palette=[colormap['Madracis auretenra'],colormap['Madracis auretenra'],colormap['Madracis auretenra'], colormap['Orbicella annularis'],colormap['Orbicella annularis'],colormap['Orbicella annularis'],colormap['Diploria strigosa'],colormap['Diploria strigosa'],colormap['Diploria strigosa'],colormap['Orbicella faveolata'],colormap['Orbicella faveolata'],colormap['Orbicella faveolata'],colormap['Siderastrea siderea'],colormap['Siderastrea siderea'],colormap['Siderastrea siderea']],showfliers=False)
ax.set_xticklabels(['3m','6m','9m','3m','6m','9m','3m','6m','9m','3m','6m','9m','3m','6m','9m',])
#ax.set_xticklabels(['Madracis auretenra','Orbicella annularis','Diploria strigosa','Corallinales','Dictyota','Halimeda opuntia','Lobophora variegata'])
plt.ylabel("Chl-p Values")
ax.set_ylim(0,600)
ax.set_title('Top 5 Coral Coverage Across Depth')
#ax.legend([madracis_3m, madracis_6m,madracis_9m], ['Madracis auretenra')
#legend=plt.legend()
plt.show()

#Plot Infra
plt.figure()
ax= sns.boxplot(data=[madracis_high, madracis_med,madracis_low,orbicella_high,orbicella_med, orbicella_low, dstrigosa_high, dstrigosa_med,dstrigosa_low,ofaveo_high, ofaveo_med,ofaveo_low,sidera_high,sidera_med,sidera_low], palette=[colormap['Madracis auretenra'],colormap['Madracis auretenra'],colormap['Madracis auretenra'], colormap['Orbicella annularis'],colormap['Orbicella annularis'],colormap['Orbicella annularis'],colormap['Diploria strigosa'],colormap['Diploria strigosa'],colormap['Diploria strigosa'],colormap['Orbicella faveolata'],colormap['Orbicella faveolata'],colormap['Orbicella faveolata'],colormap['Siderastrea siderea'],colormap['Siderastrea siderea'],colormap['Siderastrea siderea']],showfliers=False)
ax.set_xticklabels(['high','med','low','high','med','low','high','med','low','high','med','low','high','med','low',])
#ax.set_xticklabels(['Madracis auretenra','Orbicella annularis','Diploria strigosa','Corallinales','Dictyota','Halimeda opuntia','Lobophora variegata'])
plt.ylabel("Chl-p Values")
ax.set_ylim(0,600)
ax.set_title('Top 5 Coral Coverage Across Different Infrastructure Level')
#ax.legend([madracis_high, madracis_med,madracis_low], ['Madracis auretenra')
#legend=plt.legend()
plt.show()
a

#####



plt.legend([colormap['Madracis auretenra']], ['Madracis auretenra])
colormap['Madracis auretenra']
    #,'Orbicella annularis','Diploria strigosa','Orbicella faveolata','Siderastrea siderea'])
a
g = sns.catplot(x="sex", y="total_bill",
                hue="smoker", col="time",

                data=tips, kind="box",

                height=4, aspect=.7);


###
# Create column names
depth = ['3' for i in [(madracis_3m),(orbicella_3m)]
depth.shape
classgroups = [f'obj_{i}' for i in range(n_objects)]
samples = [f'sample_{i}' for i in range(n_samples)]

df = pd.DataFrame({'': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})

#PLOT
#ax = sns.boxplot(data=iris, orient="h", palette="Set2")
#madracis_9m.shape
madracis=np.append(madracis_3m,madracis_6m, madracis_9m)
madracis_3m
madracis.shape
madracis_6m.shape