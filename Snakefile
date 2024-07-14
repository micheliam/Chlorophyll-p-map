rule chl_smoothing:
    input:
        "../data/raw/transects/{transect}/boardreflect_nonorm.nc"
    output:
        "../data/raw/transects/{transect}/chlsmooth.nc"
    run:
        import xarray as xr
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy import signal

        crc = xr.open_dataset(input[0])
        wc = crc.W
        cc = crc.cube

        def calculation(y_spec, x_spec, lsmooth, wl1=0, wl2=200, po=2):
            spectrum = cc.data[y_spec, x_spec, wl1:wl2]
            Csmooth = signal.savgol_filter(spectrum, window_length=lsmooth, polyorder=po, deriv=0)
            return spectrum, Csmooth, wl1, wl2

        s, cl,wl1,wl2 = calculation(13453, 387, 7, 15, 20, 190, po=2)
        #fix this for loop for 1 pixel to be the whole transect (or 2000 pixels)
        #for y in range(0, Ylength):
            for x in range(0, 640):
                Cs = cropc[y, x]
                Chlvalues[y, x] = chlv(Cs)

         #from numpy array, you have to convert to dataarray to be able to save it to netcdf (read about the dimension and coordinates of .nc files)

         #to save into net cdf
         your_dataset.to_netcdf('/your_filepath/your_netcdf_filename.nc')



rule chl_value:
    input:
        "smoothed.nc"
    output:
        "sder.nc"
        "chl_value.nc"
    run:

        def obtainchl(Cder,wl1):
            chlvalue = Cder[130-wl1]
            return chlvalue

rule chl_map
    input
        "chl_value.nc"
    output
        "chl_map.fig"


rule chl_map
    input
        "chl_value.nc"
    output
        "chl_map.fig"

