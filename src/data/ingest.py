from scipy.io import netcdf
import h5py
import numpy as np


def ingest_cop(years, month):
    """

    Args:
        years: list
        month: str

    Returns: list

    """
    cop_data = []
    for year in years:
        directory = 'data\\raw\\copernicus\\'
        wrf_file_name = 'C3S_OZONE-L4-TC-ASSIM_MSR-' + year + month + '-fv0021.nc'

        nc = netcdf.netcdf_file(directory + wrf_file_name, 'r')
        data = nc.variables['total_ozone_column'][0][:].copy()  # copy as .netcdf_file gives direct view to memory
        cop_data.append(data)

    return cop_data


def ingest_omi(path, dates):
    """

    Args:
        path: str
        dates: list

    Returns: list

    """
    omi_data = []
    for date in dates:
        he5_file = h5py.File(path + date + '.he5', 'r')

        o3_data_v0 = np.asarray(he5_file['HDFEOS/GRIDS/OMI Column Amount O3/Data Fields/ColumnAmountO3'])
        omi_data.append(o3_data_v0)

    return omi_data
