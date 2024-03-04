from distutils.core import setup
import py2exe
from src.model.queue import Queue
from src.probability import *
from src.table import show_pn_table

setup(zipFile=None,
      options={'py2exe': {'bundle_files': 1}},
      console=["main.py"])
