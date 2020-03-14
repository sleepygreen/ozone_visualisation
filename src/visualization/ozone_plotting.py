# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:20:11 2020

@author: Harry
"""

import h5py
import numpy as np
import numpy.ma as ma
import pandas as pd
import os
from matplotlib.pyplot import *
from matplotlib import cm
from polar_plot_noframe import plot_polar_contour
from contextlib import contextmanager

cmaps= [
        'viridis', 'plasma', 'inferno', 'magma', 'cividis',
        'Greys', 'Purples', 'Blues',
        'spring', 'summer', 'autumn', 'winter','coolwarm',
        'PiYG', 'PRGn', 'BrBG', 'PuOr',
        'twilight']

#function to import from a directory (newdir) before reverting to cwd
@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

#set parameters for which files to import
o3_list = []

with cd(os.getcwd()+'\\Ozone Data'):
    filenames = [f for f in os.walk(".")][0][2]
    for f in filenames:
        he5_file = h5py.File(f,'r')
        #pull out just the O3 data
        o3_data_v0 = np.asarray(he5_file['HDFEOS/GRIDS/OMI Column Amount O3/Data Fields/ColumnAmountO3'])
        #add in replicate of the first column after the final column to avoid a gap in the final plot
        o3_data_v1 = np.concatenate((o3_data_v0,o3_data_v0[:,0:1]),axis=1)
        o3_data_v2 = ma.masked_values(o3_data_v1,-1.2676506e+30)
        o3_list.append(o3_data_v2)

#save means of 7 days worth of data at a time
#chosen seven days as need to cover areas where satellite doesn't track 
#increased number of days per plot to reduce the visibility of the line
#between 360 degrees and 0 degrees
o3_means = []
months = [31,28,31]
day = 0
for month in months:
    month_data = np.ma.array(o3_list[day:day+month]).mean(axis=0)
    day += month
    o3_means.append(month_data)

#plot a month of data with a colormap from the list of colormaps
with cd(os.getcwd()+'\\Plots'):
    #zip the three o3 mean arrays repeated enough times to have one each for the 
    for o3_mean, cmap, month in zip(o3_means*(int(len(cmaps)/len(o3_means))),cmaps,['Jan','Feb','Mar']*6):
        plot_polar_contour(o3_mean[0:45,:], np.arange(-180,181),np.arange(0,45),cmap=cmap,levels=200)
        savefig(month+' '+cmap+'.png')
        
#this code creates test arrays that are easily visualised to check that the mean
#code above works
#uniform_grid = np.asarray([[y for x in range(361)] for y in range(0,180)])
#test_list = [uniform_grid for x in range(21)]
#
#o3_means = []
#for i in range(weeks):
#    week = np.ma.array(test_list[i*7:(i+1)*7]).mean(axis=0)
#    o3_means.append(week)
#
#for i in range(weeks):
#    plot_polar_contour(o3_means[i][0:90,:], np.arange(-180,181),np.arange(0,90))
        