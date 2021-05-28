import matplotlib.pyplot as plt
import src.data.download as dl
import src.data.ingest as ing
import src.data.process as ps
import src.visualization.visualization as vis
import config

# Download functions
if config.DL_NASA:
    print("Downloading Nasa data")
    filenames, urls = dl.gen_filenames(config.he5_root, config.he5_ext)
    dl.dl_nasa_he5_ozone(path=config.NASA_PATH, urls=urls[0:3], filenames=filenames[0:3],
                         max_retries=config.MAX_RETRIES)

if config.DL_COPERNICUS:
    print("Downloading Copernicus data")
    dl.dl_copernicus_data(years=config.YEARS, month=config.COP_MONTH, path=config.COP_PATH)
    dl.extract_copernicus(zip_folder=config.COP_PATH + 'download.zip', extract_path=config.COP_PATH)

# Data ingestion functions
cop_data = ing.ingest_cop(years=config.YEARS, month=config.COP_MONTH)
omi_data = ing.ingest_omi(config.NASA_PATH, dates=config.NASA_DATES)
print("Copernicus and Nasa data ingested")

# Data Processing functions
cop_proc = ps.process_cop(cop_data)
omi_proc = ps.process_omi(omi_data)
print("Copernicus and Nasa data ingested")

# Data plotting functions

cop_fig, cop_ax, cop_cax = vis.plot_polar_contour(cop_proc[0], cmap='spring', levels=200)
cop_fig.suptitle(config.YEARS[0] + '-' + config.COP_MONTH, x=0.515)
# fig.savefig(config.COP_PLOT_PATH + year + '-' + config.COP_MONTH + '.png', dpi=150, bbox_inches=0, pad_inches=0)

omi_fig, omi_ax, omi_cax = vis.plot_polar_contour(
    omi_proc[0],
    cmap='spring',
    levels=500,
    default_min=0,
    default_max=250
)

omi_fig.suptitle(config.NASA_DATES[0], x=0.515)
plt.show()
