import os
import requests
from bs4 import BeautifulSoup
from contextlib import contextmanager
import config

# Set url and extenstion for OMI TO3d data retrieval
he5_root = 'https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMTO3d.003/2019'
he5_ext = 'he5'


# Function to retrieve file urls from root (e.g. 2019 url)
def listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    # only take the files with the right extension
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
