import os
import requests
from bs4 import BeautifulSoup
from contextlib import contextmanager
import config
import cdsapi

# Set url and extenstion for OMI TO3d data retrieval
he5_root = 'https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMTO3d.003/2019'
he5_ext = 'he5'

# Set max get request retries
MAX_RETRIES = 20


# Function to retrieve file urls from root (e.g. 2019 url)
def list_web_directory_files(url, ext=''):
    """

    Args:
        url: str
        ext: str

    Returns: web_files: list

    """
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    web_files = [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    # only take the files with the right extension
    return web_files


def gen_filenames():
    """

    Returns: filenames, urls: list, list

    """
    urls_v0 = []
    for file in list_web_directory_files(he5_root, he5_ext):
        urls_v0.append(file)

    # De-duplicate list
    urls = urls_v0[::2]

    filenames = []
    for url in urls:
        filenames.append(url[95:99] + '-' + url[100:102] + '-' + url[102:104] + '.he5')

    return filenames, urls


# function to get data based on retrieved urls
def save_url(url, path, filename):
    """

    Args:
        url: str
        path: str
        filename: str

    Returns: None, file written to path+filename

    """
    result = session.get(url)
    try:
        result.raise_for_status()
        f = open(path+filename, 'wb')
        f.write(result.content)
        f.close()
        print('contents of URL written to ' + filename)
    except:
        print('requests.get() returned an error code ' + str(result.status_code))


def dl_nasa_he5_ozone(path, urls, filenames):
    """

    Args:
        path: str
        urls: list
        filenames: list

    Returns: Contents of url saved to path

    """
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
    session.mount('https://', adapter)
    for url, filename in zip(urls, filenames):
        save_url(url, path, filename)


def dl_copernicus_data(years, path):
    c = cdsapi.Client()
    c.retrieve(
        'satellite-ozone',
        {
            'processing_level': 'level_4',
            'variable': 'ozone_mole_content',
            'vertical_aggregation': 'total_column',
            'sensor': 'combination_of_15_sensors_using_gap_filling_assimilation_methods',
            'year': years,
            'month': '01',
            'version': '0021',
            'format': 'zip',
        },
        path + 'download.zip')
