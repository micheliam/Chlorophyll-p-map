import xarray as xr
import scipy.signal
from scipy.signal import savgol_filter
import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

transect='transect_006/'


print(f'Processing {transect}')

infile_Path = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/'
hab = mpimg.imread(infile_Path + transect + 'classmap-crf.jpg')

output_file = f'{infile_Path.replace("/raw/", "/work/Michelia/")}/{transect}/chl_dermap2.nc'
from pathlib import Path
output_path = Path(output_file)
output_dir = output_path.parent
output_dir.mkdir(exist_ok=True, parents=True)

if not output_path.exists():

    print(f'Calculating chl for {transect}')
    tic = time.time()

    classmap=xr.open_dataarray(infile_Path + transect + "classmap-crf.nc")
    cd=classmap.data
    reflect = xr.open_dataarray(infile_Path + transect + "boardreflect_nonorm.nc")
    rd=reflect.data
W=reflect.W



    ## TEST MAPPING
    Rstart=-0
    Rstop=-1

    pixels = reflect#.sel(
        #Y=slice(Rstart, Rstop),
        W=slice(600, 750)
                )


    pmean = pixels.mean(dim='W')
    pstd = pixels.std(dim='W').clip(1e-6)
    #pstd.data[pstd.data==0]=1e-9
    pixels2: xr.DataArray = (pixels - pmean) / pstd
    pixels2= (pixels - pmean) / pstd
    #pixels = pixels.interpolate_na('W', method='slinear')


A=pixels[1,1,:]
B=pixels2[1,1,:]
C=pixels[3,3,:]
D=pixels2[3,3,:]
E=pixels[5,5,:]
F=pixels2[5,5,:]
G=pixels[9,9,:]
H=pixels2[9,9,:]
plt.plot(W,A, 'r')
plt.plot(W,B,'k')
plt.plot(W,C, 'r')
plt.plot(W,D, 'k')
plt.plot(W, E, 'r')
plt.plot(W, F, 'k')
plt.plot(W, G, 'r')
plt.plot(W, H, 'k')
plt.ylabel('Reflectance')
plt.xlabel('Wavelength (nm)')

    ##CHECK IF THERE IS NULL/INFINUTE
    # import pandas as pd
    # pixels.data.shape
    # #NULL
    # null= pd.notnull(pmean)
    # null.shape
    # unnull = np.unique(null, return_counts=True)
    # unnull
    # #infinite
    # inf=np.isfinite(pmean)
    # inf
    # uninf=np.unique(inf, return_counts=True)
    # uninf
    #
    # pmean.min()
    # pstd.min()

    ##
    X1 = savgol_filter(pixels.data, window_length=13, polyorder=2)
    X2 = savgol_filter(X1, window_length=13, polyorder=2)
    smoothed = pixels.copy(data=X2)

    smder = savgol_filter(X2, window_length=13, polyorder=3, deriv=2) * 1e4
    smder = pixels.copy(data=smder)

    dermap = smder.sel(W=slice(655, 685)).max('W').clip(0)

    from scipy.ndimage import median_filter

    dermap_median = dermap.copy(
        data=median_filter(dermap, size=9, mode='reflect')
    )

    dermap_median.shape




    dermap_median.name = 'chlA_dermap'

    print(dermap_median)
    print(dermap_median.sum())

    dermap_median.to_netcdf(output_path,
                            # encoding={
                            #     'chlA_dermap': dict(dtype='uint16', scale_factor=0.001)
                            # }
                            )
    print(f'Saved {output_file}')
    chl_map= output_dir / 'chl_dermap2.jpg'
    plt.imsave(chl_map, dermap_median, cmap='Greens', vmax=dermap_median.quantile(0.995, dim=('X', 'Y')))
    toc = time.time()

    print(f'Chl map done for {transect} in {toc-tic:.2f} s')


print(f'Creating montage')
montage_file = output_dir / 'montage_maps.jpg'
chl_map = output_dir / 'chl_dermap2.jpg'
natural_map = infile_Path + transect + 'natural.jpg'
habitat_map = infile_Path + transect + 'classmap-crf.jpg'

montage_command = f'montage {natural_map} {chl_map} {habitat_map} -tile 3x1 -geometry 640x+10 {montage_file}'

import subprocess, os

subpout = subprocess.check_call(montage_command.split(), env=dict(os.environ, MAGICK_CONFIGURE_PATH=f"{os.environ['HOME']}/.config/ImageMagick"))
print(f'Montage output: {subpout}')

#dermap_median.shape
#or
#loc_where_refboard = habitat_map.where(habitat_map=="refboard")
#vmin = dermap_median.where(loc_where_refboard).mean()
#plt.imsave(output_dir / 'chl_dermap.jpg', dermap_median, cmap='Greens', vmin=vmin, vmax=dermap_median.quantile(0.995, dim=('X', 'Y')))


# fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, sharex=True, sharey=True)
# ax1.imshow(hab[Rstart: Rstop])
# ax2.imshow(dermap_median, cmap='Greens', vmax=dermap_median.quantile(0.99, dim=('X', 'Y')))
#
# nat = mpimg.imread('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_006/natural.jpg')
# ncrop=nat[Rstart: Rstop,:,:]
# ax3.imshow(ncrop)
# plt.show()