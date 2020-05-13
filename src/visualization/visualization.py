import numpy as np
import matplotlib.pyplot as plt

cmaps= [
        'viridis', 'plasma', 'inferno', 'magma', 'cividis',
        'Greys', 'Purples', 'Blues',
        'spring', 'summer', 'autumn', 'winter','coolwarm',
        'PiYG', 'PRGn', 'BrBG', 'PuOr',
        'twilight']

def plot_polar_contour(values, cmap, levels,default_min=True,default_max=True):
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
    lat_res, long_res = values.shape
    long_step = 360/(long_res-1)
    azimuths = np.arange(-180, 180 + long_step, long_step)
    zeniths = np.arange(0, lat_res)

    values = np.array(values)
    values = values.reshape(len(zeniths), len(azimuths))

    if default_min:
        val_min = values.min()
    else:
        val_min = default_min

    if default_max:
        val_max = values.max()
    else:
        val_max = default_max

    r, theta = zeniths, np.radians(azimuths)
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar', frameon=True), figsize=(15, 15))
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    cax = ax.contourf(theta, r, values,
                      np.arange(val_min, val_max, (val_max - val_min) / levels),
                      cmap=plt.get_cmap(cmap),
                      extend='both')

    return fig, ax, cax

# TODO add saving fn
# fig.savefig('w_to_b_'+file[0:-4]+'.png',dpi=300, bbox_inches=0, pad_inches=0)

def plot_polar_contour_frame(values, azimuths, zeniths, cmap):
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
    fig, ax = subplots(subplot_kw=dict(projection='polar'))
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    cax = ax.contourf(theta, r, values,
                      np.arange(values.min(), values.max(), (values.max() - values.min()) / 200),
                      cmap=matplotlib.pyplot.get_cmap(cmap),
                      extend='both')
    # autumn()
    cb = fig.colorbar(cax)
    cb.set_label("$Pixel  O_3/Dobsons$")

    return fig, ax, cax

# TODO add min plotting function
# min_vals = pd.Series([data.values.min() for data in ozone_data])
# avg_years = [3,5,7]
# year_datetime = pd.to_datetime(years)
#
# yr5_min_vals = min_vals.rolling(5, min_periods=1).mean()
# new_years = np.linspace(1979, 2019, 300)
#
# spl = make_interp_spline(years, yr5_min_vals, k=3)  # type: BSpline
# power_smooth = spl(new_years)
#
# fig, ax = plt.subplots()
# ax.plot(new_years, power_smooth,'black')
# ax.set_ylim((100,270))
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# plt.show()

# fig, ax = plt.subplots(2,1)
# ax[0].plot(year_datetime, min_vals, 'black')
# for yr in avg_years:
#     ax[0].plot(year_datetime, min_vals.rolling(yr, min_periods=1).mean())
# ax[1].plot(new_years, power_smooth)
# ax[1].set_ylim((100,270))
# ax[0].spines['top'].set_visible(False)
# ax[0].spines['right'].set_visible(False)
# plt.show()