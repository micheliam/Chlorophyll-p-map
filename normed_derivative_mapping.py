import xarray as xr
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

infile_Path = '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/'
transect='transect_006/'
hab = mpimg.imread('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_006/classmap-crf.jpg')

classmap=xr.open_dataarray(infile_Path + transect + "classmap-crf.nc")
cd=classmap.data
cd.shape
reflect = xr.open_dataarray(infile_Path + transect + "boardreflect_nonorm.nc")

## TEST MAPPING
Rstart=-0
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
X2 = savgol_filter(X1, window_length=13, polyorder=2)
smoothed = pixels.copy(data=X2)

smder = savgol_filter(X2, window_length=13, polyorder=3, deriv=2) * 1e4
smder = pixels.copy(data=smder)

dermap = smder.sel(W=slice(655, 685)).max('W').clip(0)

from scipy.ndimage import median_filter

dermap_median = dermap.copy(
    data=median_filter(dermap, size=9, mode='reflect')
)


output_file = f'{infile_Path.replace("/raw/", "/work/")}/{transect}/chl_dermap.nc'
from pathlib import Path
output_path = Path(output_file)
output_dir = output_path.parent
output_dir.mkdir(exist_ok=True, parents=True)


dermap_median.name = 'chlA_dermap'

print(dermap_median)
print(dermap_median.sum())

dermap_median.to_netcdf(output_path,
                        # encoding={
                        #     'chlA_dermap': dict(dtype='uint16', scale_factor=0.001)
                        # }
                        )
print(f'Saved {output_file}')
loc_where_refboard = habitat_map.where(habitat_map=="refboard")
vmin = dermap_median.where(loc_where_refboard).mean()

plt.imsave(output_dir / 'chl_dermap.jpg', dermap_median, cmap='Greens', vmin=vmin, vmax=dermap_median.quantile(0.995, dim=('X', 'Y')))


# fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, sharex=True, sharey=True)
# ax1.imshow(hab[Rstart: Rstop])
# ax2.imshow(dermap_median, cmap='Greens', vmax=dermap_median.quantile(0.99, dim=('X', 'Y')))
#
# nat = mpimg.imread('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_006/natural.jpg')
# ncrop=nat[Rstart: Rstop,:,:]
# ax3.imshow(ncrop)
# plt.show()

