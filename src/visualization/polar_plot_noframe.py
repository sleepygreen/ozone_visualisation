# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:29:24 2020

@author: Harry
"""

import numpy as np
from matplotlib.pyplot import *
from matplotlib import cm

def plot_polar_contour(values, azimuths, zeniths, cmap, levels):
    """Plot a polar contour plot, with 0 degrees at the North.
 
    Arguments:
 
     * `values` -- A list (or other iterable - eg. a NumPy array) of the values to plot on the
     contour plot (the `z` values)
     * `azimuths` -- A list of azimuths (in degrees)
     * `zeniths` -- A list of zeniths (that is, radii)
 
    The shapes of these lists are important, and are designed for a particular
    use case (but should be more generally useful). The values list should be `len(azimuths) * len(zeniths)`
    long with data for the first azimuth for all the zeniths, then the second azimuth for all the zeniths etc.
 
    This is designed to work nicely with data that is produced using a loop as follows:
 
    values = []
    for azimuth in azimuths:
      for zenith in zeniths:
        # Do something and get a result
        values.append(result)
 
    After that code the azimuths, zeniths and values lists will be ready to be passed into this function.
 
    """
    theta = np.radians(azimuths)
    zeniths = np.array(zeniths)
 
    values = np.array(values)
    values = values.reshape(len(zeniths), len(azimuths))
 
    r, theta = zeniths, np.radians(azimuths)
    fig, ax = subplots(subplot_kw=dict(projection='polar',frameon=False),figsize=(9,9))
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_axis_off()
    cax = ax.contourf(theta, r, values,
                      np.arange(values.min(),values.max(),(values.max()-values.min())/levels),
                      cmap=matplotlib.pyplot.get_cmap(cmap),
                      extend='both')
    #autumn()
#    cb = fig.colorbar(cax)
#    cb.set_label("$Pixel  O_3/Dobsons$")

    return fig, ax, cax