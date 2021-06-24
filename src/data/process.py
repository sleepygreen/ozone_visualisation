import numpy as np
import pandas as pd


def process_cop(cop_data):
    """

    Args:
        cop_data: list

    Returns: cop_proc: list

    """
    cop_proc = []
    for data in cop_data:
        # TODO gets around 0.5 degree latitude res of copernicus data by taking first 90 rows
        # Refactor to resample at 1 degree resolution
        o3_datav0 = pd.DataFrame(data[0:90, :].copy().byteswap().newbyteorder())
        with_plot_col = pd.concat((o3_datav0, o3_datav0.iloc[:, 0]), axis=1)
        # TODO add processed data export functions
        #o3_datav0.to_csv(export_path+year+month+'.csv')
        cop_proc.append(with_plot_col)

    return cop_proc


def process_nasa(omi_data):
    """

    Args:
        omi_data: list

    Returns: omi_proc: list

    """
    omi_proc = []
    for data in omi_data:
        with_plot_col = np.concatenate((data, data[:, 0:1]), axis=1)
        masked = np.ma.masked_values(with_plot_col, -1.2676506e+30)
        omi_proc.append(masked)

    return omi_proc


# TODO extract cop resampling code from here to seperate function
# for month in months:
#     # Open file in a netCDF reader
#     directory = 'data\\copernicus\\raw\\'
#     wrf_file_name = 'C3S_OZONE-L4-TC-ASSIM_MSR-1989'+month+'-fv0021.nc'
#     with cd(directory):
#         nc = netcdf.netcdf_file(wrf_file_name, 'r')
#         data = nc.variables['total_ozone_column'][0][
#                :].copy()  # copy to variable as .netcdf_file gives direct view to memory
#
#     # data in netcdf is bigendian so swap byte order in dataframe constructor
#     o3_datav0 = pd.DataFrame(data[0:90, :].copy().byteswap().newbyteorder())
#
#     # add col at end with [0,0,1,1,2,2,3...89,89] list for grouping pairs of latitudes
#     red_lat = pd.Series([int(np.floor(x / 2)) for x in range(90)])
#     o3_datav0['red_lat'] = pd.Series(red_lat)
#
#     # groupby pairing col and take means
#     o3_datav1 = o3_datav0.groupby('red_lat').mean()
#     assert o3_datav1.shape == (45, 720), "shape is : %r" % str(o3_datav1.shape)
#
#     # transpose to do same operation on rows (longitudes)
#     o3_datav2 = o3_datav1.transpose()
#     # create longitude pairing col
#     red_long = pd.Series([int(np.floor(x / 2)) for x in range(720)])
#     o3_datav2['red_long'] = red_long
#
#     # reduce resolution along columns (longitudes) and transpose again
#     o3_datav2 = o3_datav2.groupby('red_long').mean().transpose()
#
#     # add a duplicate of the first column for neat plotting
#     o3_data = pd.concat((o3_datav2, o3_datav2.iloc[:, 0]), axis=1)
#     assert o3_data.shape == (45,361), "shape is: %r" % str(o3_data.shape)
#
#     export_dir = 'data\\processed\\'
#
#     with cd(export_dir):
#         o3_data.to_csv(year+'01.csv')


# TODO refactor into mean_fn
# o3_means = []
# months = [31,28,31]
# day = 0
# for month in months:
#     month_data = np.ma.array(o3_list[day:day+month]).mean(axis=0)
#     day += month
#     o3_means.append(month_data)

# this code creates test arrays that are easily visualised to check that the mean
# code above works
# uniform_grid = np.asarray([[y for x in range(361)] for y in range(0,180)])
# test_list = [uniform_grid for x in range(21)]
#
# o3_means = []
# for i in range(weeks):
#    week = np.ma.array(test_list[i*7:(i+1)*7]).mean(axis=0)
#    o3_means.append(week)
#
# for i in range(weeks):
#    plot_polar_contour(o3_means[i][0:90,:], np.arange(-180,181),np.arange(0,90))
