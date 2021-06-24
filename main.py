import matplotlib.pyplot as plt
import src.data.download as dl
import src.data.ingest as ing
import src.data.process as ps
import src.visualization.visualization as vis
import config

# Download data
if config.DL_NASA:
    print("Downloading Nasa data")
    filenames, urls = dl.gen_nasa_filenames(config.he5_root, config.he5_ext)
    dl.dl_nasa_ozone(path=config.NASA_PATH, urls=urls[0:3], filenames=filenames[0:3], max_retries=config.MAX_RETRIES)

if config.DL_COPERNICUS:
    print("Downloading Copernicus data")
    dl.dl_copernicus_ozone(years=config.YEARS, month=config.COP_MONTH, path=config.COP_PATH)
    dl.extract_copernicus(zip_folder=config.COP_PATH + 'download.zip', extract_path=config.COP_PATH)

# Data ingestion functions
cop_data = ing.ingest_cop(years=config.YEARS, month=config.COP_MONTH)
nasa_data = ing.ingest_nasa(config.NASA_PATH, dates=config.NASA_DATES)
print("Copernicus and Nasa data ingested")

# Data processing
cop_proc = ps.process_cop(cop_data)
nasa_proc = ps.process_nasa(nasa_data)
print("Copernicus and Nasa data ingested")

# Data plotting
cop_fig, cop_ax, cop_cax = vis.plot_polar_contour(cop_proc[0], cmap='spring', levels=200)
cop_fig.suptitle(config.YEARS[0] + '-' + config.COP_MONTH, x=0.515)
cop_fig.savefig(config.COP_PLOT_PATH + config.YEARS[0] + '-' + config.COP_MONTH + '.png', dpi=150, bbox_inches=0,
                pad_inches=0)

nasa_fig, nasa_ax, nasa_cax = vis.plot_polar_contour(
    nasa_proc[0],
    cmap='spring', levels=500,
    default_min=0, default_max=250
)

nasa_fig.suptitle(config.NASA_DATES[0], x=0.515)
plt.show()
