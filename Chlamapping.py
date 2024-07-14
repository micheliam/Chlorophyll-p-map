import xarray
import xarray as xr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.signal
from scipy.signal import savgol_filter
from scipy import signal

crc = xr.open_dataset('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/raw/transects/transect_006/transect.nc')
wc= crc.W
cc= crc.cube


