import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from contextlib import contextmanager
from src.data.context_management import cd
from src.visualization.polar_plot_noframe import plot_polar_contour

ozone_data = list()

with cd(os.getcwd()+'\\data\\processed\\'):
    filenames = [f for f in os.walk(".")][0][2][0:2]
    for file in filenames:
        ozone_data.append(pd.read_csv(file,index_col='red_lat'))

print(filenames)

with cd(os.getcwd()+'\\reports\\figures\\'):
    for data, file in zip(ozone_data, filenames):
        fig, ax, cax = plot_polar_contour(data, np.arange(-180, 181), np.arange(0, 45), cmap='binary', levels=200)
        fig.savefig('w_to_b_'+file[0:-4]+'.png',dpi=300, bbox_inches=0, pad_inches=0)

plt.show()