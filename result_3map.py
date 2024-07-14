chl = xr.open_dataarray('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/transects/transect_005/chl_dermap2.nc')

plt.imshow(chl.data, cmap='Greens',vmax=chl.quantile(0.995, dim=('X', 'Y')))
plt.colorbar()