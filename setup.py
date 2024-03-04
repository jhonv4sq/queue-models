from distutils.core import setup
import py2exe
from model.queue import Queue
from probability import *
from table import *

setup(zipFile=None,
      options={'py2exe': {'bundle_files': 1}},
      console=["main.py"])
