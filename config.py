MONTHS = ['01','02','03','04','05','06','07','08','09','10','11','12']
MISSING_YEARS = [2001,2010]
YEARS = [str(x) for x in range(1979, 2019) if x not in MISSING_YEARS]
COP_MONTH = '01'

he5_root = 'https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMTO3d.003/2019'
he5_ext = 'he5'

MAX_RETRIES = 20

NASA_PATH = 'data/raw/nasa/'
NASA_PROC_PATH = 'data/processed/nasa/'
NASA_PLOT_PATH = 'reports/figures/nasa/'
COP_PATH = 'data/raw/copernicus/'
COP_PROC_PATH = 'data/processed/copernicus/'
COP_PLOT_PATH = 'reports/figures/copernicus/'

DL_NASA = False
DL_COPERNICUS = False

NASA_DATES = ['2019-01-01', '2019-01-02', '2019-01-03']


