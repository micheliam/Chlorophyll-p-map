import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
import numpy as np

transect='transect_129/'

Path1 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/'
Path2 =  '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/transects/'

habs = xr.open_dataarray(Path1 + transect + 'classmap-crf.nc')
hd=habs.data
chl= xr.open_dataarray(Path2 + transect + 'chl_dermap2.nc')
chd=chl.data

def select_chl (label):
    obj= hd== label
    obj=obj*chd
    obj=obj.flatten()
    obj = obj[obj != 0]
    return(obj)

turf= select_chl(40)
cyan= select_chl(41)
sed= select_chl(42)

ax= sns.violinplot(data=[turf, cyan, sed])
ax.set_xticklabels(['Turf Algae','Cyanobacterial Mat','Sediment'])
ax.set_title('Transect 129')

########

#3 meters
transect_3m=['006','031','054','081','091','102','118','134']
#sites_3m=['Carmabi','Kokomo','Playa_Kalki','Habitat','Water_Factory','Mary_Pompoen','Sea_Aquarium','East_Point']
#for i, j in zip(transect_3m, sites_3m):
    #print(i, j)


h={}
c={}
for i in transect_3m:
    #hab= xr.open_dataarray(Path1 + i + '/classmap-crf.nc')
    #chl= xr.open_dataarray(Path2 + i + '/chl_dermap2.nc')
    h['hab' + (i)] = [xr.open_dataarray(Path1 +'transect_' + i + '/classmap-crf.nc')]
    c['chl' + (i)] = [xr.open_dataarray(Path2 +'transect_' + i + '/chl_dermap2.nc')]

def functc (tr):
    x=c['chl'+(tr)+'']
    x=np.asarray(x)
    return x

functc('006').shape
chd.shape
def functh (tr):
    x=h['hab'+(tr)+'']
    x=np.asarray(x)
    return x

functh('006').shape

def select_chl (transect,label):
    hd=functh(transect)
    cd=functc(transect)
    obj= hd = label
    obj=obj*cd
    obj=obj.flatten()
    obj = obj[obj != 0]
    return(obj)

t006='006'
turf= select_chl(t006,40)

cyan= select_chl(t006,41)

sed= select_chl(t006,42)


ax= sns.violinplot(data=[turf, cyan, sed])
ax.set_xticklabels(['Turf Algae','Cyanobacterial Mat','Sediment'])
ax.set_title('Transect'+t006)


funct_c ('006').shape
def funct2 ():
    a = funct(transect_3m[0])
    b = funct(transect_3m[1])
    c = funct(transect_3m[2])
    d = funct(transect_3m[3])
    e = funct(transect_3m[4])
    f = funct(transect_3m[5])
    g = funct(transect_3m[6])
    h = funct(transect_3m[7])
    all= np.concatenate((a,b,c,d,e,f,g,h))
    return all

violin_3m= funct2()

def select_chl (label):
    obj= hd== label
    obj=obj*chd
    obj=obj.flatten()
    obj = obj[obj != 0]
    return(obj)

turf= select_chl(40)
cyan= select_chl(41)
sed= select_chl(42)

ax= sns.violinplot(data=[turf, cyan, sed])
ax.set_xticklabels(['Turf Algae','Cyanobacterial Mat','Sediment'])
ax.set_title('Transect 129')


a=funct(transect_3m[0])
b=funct(transect_3m[1])
x= np.concatenate((a,b))
x.shape
type(a)
np.concatenate(funct(transect_3m[0]),transect_3m[1]),funct(transect_3m[2]),funct(transect_3m[3]),funct(transect_3m[4]),funct(transect_3m[05))
rep= [0,1,2,3,4,5,6,7]
transect_3m[1]
for i in rep:
    funct(transect_3m[i])
    print a


for i in transect_3m:
    b = funct(i)


b
    h['hab' + (i)] = [xr.open_dataarray(Path1 + i + '/classmap-crf.nc')]


namain('031')




c54=c['chl054']
type(c54)
c54x=np.asarray(c54)
c54x.shape
c54dim=27659*640

h
habs006
habs
chl
for i in
transect='134/'

Path1 = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_'
Path2 =  '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/transects/transect_'

habs = xr.open_dataarray(Path1 + transect + 'classmap-crf.nc')
hd=habs.data
hd.shape
chl= xr.open_dataarray(Path2 + transect + 'chl_dermap2.nc')
chd=chl.data


#6 meters
005	Carmabi
026	Kokomo
044	Playa Kalki
080	Habitat
086	Water Factory
097	Mary Pompoen
130	East Point

#9 meters

019	Carmabi
024	Kokomo
043	Playa Kalki
084	Habitat
085	Water Factory
095	Mary Pompoen
114	Sea Aquarium
129	East Point











######
turf_class = hd== 40
turf=turf_class*chd
cyan_class = hd== 41
cyan=cyan_class*chd
sed_class = hd== 42
sed=sed_class*chd

a= turf.flatten()
b=cyan.flatten()
c=sed.flatten()

ax=a
ax=ax[ax !=0]
bx=b
bx=bx[bx !=0]
bx.shape
cx=c
cx= cx[cx !=0]



sns.violinplot(data=[ax, bx, cx])

# Create a plot
sns.kdeplot(a, shade = True , color = "Green")
a.shape
turf.shape
sns.violinplot(y=a, showmedians=True)

fig, (ax1, ax2,ax3) = plt.subplots(nrows=1, ncols=3, figsize=(9, 4), sharey=True)
ax1.violinplot(y=turf, showmedians=True)
ax2.violinplot(cyan, showmedians=True)
ax3.violinplot(sed, showmedians=True)

fig, (ax1, ax2,ax3) = plt.subplots(nrows=1, ncols=3, figsize=(9, 4), sharey=True)
ax1.set_title('Turf Algae')
ax1.violinplot(a, showmedians=True)
ax2.set_title('Cyanobacterial Mat')



plt.ylabel("1= ")
plt.violinplot(dataset=[a, b, c])


sns.violinplot(y=bx, showmedians=True)
ax3.set_title('Sediment')
ax3.violinplot(y=c, showmedians=True)
chl
ax1.set_ylabel('Observed values')

np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
data
d=np.asarray(data)
d.shape
# Add title

plt.title('Violin Plot on Turf')
plt.show()

# Create a plot
plt.violinplot([turf, cyan, sed])

# Add title
plt.xlabel('(1) Turf Algae (2) Cyanobacterial Mat (3) Sediment')
plt.ylabel('Chl-a Value')
plt.title('Violin Plot')
plt.show()













######
a=xr.open_dataarray("/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/chl.csv",)

df = pd.read_csv("/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/chl.csv", error_bad_lines=False, encoding="ISO-8859-1")
print(df.head())
print(df.isnull().values.any())

chl=df.Chl_a_Value
chl



df.to_netcdf('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/chla.nc')
type(chl)
# Extract Figure and Axes instance
fig, ax = plt.subplots()
ax=sns.violinplot(chl)
chl.shape
plt.violinplot(chl)
sns.violinplot(chl)
chl.dtypes
chl.shape
c=np.asarray(c,dtype='float64')
c.shape
1105/3
# Create a plot
plt.violinplot(c, showmedians=True)
c
# Add title
ax.set_title('Violin Plot')
plt.show()