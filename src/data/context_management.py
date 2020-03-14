# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:09:13 2020

@author: User
"""
import os
from contextlib import contextmanager

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)