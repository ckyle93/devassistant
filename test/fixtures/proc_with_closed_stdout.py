#!/usr/bin/python

import os
import sys
import time

os.close(1)
time.sleep(1) # one second should be enough for parent process to do iteration with readline()
sys.exit(1)
