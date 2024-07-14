import xarray as xr
import scipy.signal
from scipy.signal import savgol_filter
import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

transect='transect_006/'
infile_Path = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/'
hab = mpimg.imread(infile_Path + transect + 'classmap-crf.jpg')


classmap=xr.open_dataarray(infile_Path + transect + "classmap-crf.nc")
cd=classmap.data
reflect = xr.open_dataarray(infile_Path + transect + "boardreflect_nonorm.nc")
rd=reflect.data

pixels = reflect.sel(
    # Y=slice(Rstart, Rstop),
    W=slice(600, 750)
)

rw = reflect.W.sel(
    # Y=slice(Rstart, Rstop),
    W=slice(600, 750)
)
rw.shape
pixels.shape
a= pixels[200,200,:]
b= pixels1[200,200,:]

#Plot Normalisation
plt.plot(rw,a,'r',label='raw spectral')
plt.plot(rw, b,'k',label='normalised')
plt.ylabel('Reflectance')
plt.xlabel('Wavelength (nm)')
plt.legend()

#Plot Smoothing




pixels1 = reflect.sel(
    # Y=slice(Rstart, Rstop),
    W=slice(600, 750)
)

pmean = pixels1.mean(dim='W')
pstd = pixels1.std(dim='W').clip(1e-6)
# pstd.data[pstd.data==0]=1e-9
pixels1: xr.DataArray = (pixels1 - pmean) / pstd
# pixels = pixels.interpolate_na('W', method='slinear')
pixels1.shape