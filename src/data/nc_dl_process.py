# -*- coding: utf-8 -*-
import sys,getopt
from scipy.io import netcdf
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src.data.context_management import cd
from src.visualization.polar_plot_noframe import plot_polar_contour
import matplotlib.pyplot as plt
import cdsapi

c = cdsapi.Client()

years = [str(x) for x in range(1989,2019)]

c.retrieve(
    'satellite-ozone',
    {
        'processing_level': 'level_4',
        'variable': 'ozone_mole_content',
        'vertical_aggregation': 'total_column',
        'sensor': 'combination_of_15_sensors_using_gap_filling_assimilation_methods',
        'year': years,
        'month': '01',
        'version': '0021',
        'format': 'zip',
    },
    'download.zip')

#months = ['01','02','03','04','05','06','07','08','09','10','11','12']

fig, ax = plt.subplots(3, 4)

for year in years:
    # Open file in a netCDF reader
    directory = 'data\\raw\\Copernicus\\'
    wrf_file_name = 'C3S_OZONE-L4-TC-ASSIM_MSR-1989'+'01'+'-fv0021.nc'
    with cd(directory):
        nc = netcdf.netcdf_file(wrf_file_name, 'r')
        data = nc.variables['total_ozone_column'][0][:].copy()  # copy to variable as .netcdf_file gives direct view to memory

    # data in netcdf is bigendian so swap byte order in dataframe constructor
    o3_datav0 = pd.DataFrame(data[0:90, :].copy().byteswap().newbyteorder())

    # add col at end with [0,0,1,1,2,2,3...89,89] list for grouping pairs of latitudes
    red_lat = pd.Series([int(np.floor(x / 2)) for x in range(90)])
    o3_datav0['red_lat'] = pd.Series(red_lat)

    # groupby pairing col and take means
    o3_datav1 = o3_datav0.groupby('red_lat').mean()
    assert o3_datav1.shape == (45, 720), "shape is : %r" % str(o3_datav1.shape)

    # transpose to do same operation on rows (longitudes)
    o3_datav2 = o3_datav1.transpose()
    # create longitude pairing col
    red_long = pd.Series([int(np.floor(x / 2)) for x in range(720)])
    o3_datav2['red_long'] = red_long

    # reduce resolution along columns (longitudes) and transpose again
    o3_datav2 = o3_datav2.groupby('red_long').mean().transpose()

    # add a duplicate of the first column for neat plotting
    o3_data = pd.concat((o3_datav2, o3_datav2.iloc[:, 0]), axis=1)
    assert o3_data.shape == (45,361), "shape is: %r" % str(o3_data.shape)

    plot_polar_contour(o3_data,np.arange(-180,181),np.arange(0,45),cmap='spring',levels=200)
    plt.show()