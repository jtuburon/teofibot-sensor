#!/usr/bin/python
import os
# Change working directory so relative paths (and template lookup) work again
BASE_DIR= os.path.dirname(__file__)
os.chdir(BASE_DIR)

import sys
sys.path.append(BASE_DIR)

from main import app

application= app