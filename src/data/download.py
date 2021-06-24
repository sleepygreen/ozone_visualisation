import requests
from bs4 import BeautifulSoup
import cdsapi
import zipfile


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


def gen_nasa_filenames(he5_root, he5_ext):
    """

    Args:
        he5_root: str
        he5_ext: str

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
def save_url(url, path, filename, session):
    """

    Args:
        session: requests.Session()
        url: str
        path: str
        filename: str

    Returns: None, file written to path+filename

    """
    result = session.get(url)
    if result.status_code == 200:
        f = open(path + filename, 'wb')
        f.write(result.content)
        f.close()
        print('contents of URL written to ' + path + filename)
    else:
        print('requests.get() returned an error code ' + str(result.status_code))


def dl_nasa_ozone(path, urls, filenames, max_retries):
    """
    Saves contents of url to path with filename, retrying only max_retries number of times
    Args:
        max_retries: int
        path: str
        urls: list
        filenames: list

    Returns:

    """
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=max_retries)
    session.mount('https://', adapter)
    for url, filename in zip(urls, filenames):
        save_url(url, path, filename, session)


def dl_copernicus_ozone(years, month, path):
    """

    Args:
        years: list
        month: str
        path: str

    Returns:

    """
    c = cdsapi.Client()
    c.retrieve(
        'satellite-ozone-v1',
        {
            'format': 'zip',
            'processing_level': 'level_4',
            'variable': 'atmosphere_mole_content_of_ozone',
            'vertical_aggregation': 'total_column',
            'sensor': 'msr',
            'year': years,
            'month': month,
            'version': 'v0021',
        },
        path + 'download.zip')


def extract_copernicus(zip_folder, extract_path):
    """
    Extracts contents of zip_folder to extract_path
    Args:
        zip_folder: str
        extract_path: str

    Returns:

    """
    with zipfile.ZipFile(zip_folder, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
