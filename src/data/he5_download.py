# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:48:23 2019

@author: Harry
"""
import h5py
import numpy as np
import pandas as pd
import numpy.ma as ma
import os
import requests
from bs4 import BeautifulSoup
from contextlib import contextmanager

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

#set url and extenstion for OMI TO3d data retrieval
root = 'https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMTO3d.003/2019'
ext = 'he5'

#function to retrieve file urls from root (e.g. 2019 url)
def listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    #only take the files with the right extension
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

#populate list of file urls
url_list_v0 = []
for file in listFD(root, ext):
    url_list_v0.append(file)

#every url is duplicated for some reason (may be reading .xml files as well?)
#so take every second file name
url_list = url_list_v0[::2]

#read filenames out of url strings to save as
filenames = []
for url in url_list:
    filenames.append(url[95:99]+'-'+url[100:102]+'-'+url[102:104]+'.he5')

MAX_RETRIES = 20
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
session.mount('https://', adapter)

#function to get data based on retrieved urls
def save_url(url, filename):
    result = session.get(url)
    try:
        result.raise_for_status()
        f = open(filename,'wb')
        f.write(result.content)
        f.close()
        print('contents of URL written to '+filename)
    except:
        print('requests.get() returned an error code '+str(result.status_code))

#save selection from url_list based on parameters in range
with cd(os.getcwd()+'\\Ozone Data'):
    for url, filename in zip(url_list[30:], filenames[30:]):
        save_url(url, filename)
