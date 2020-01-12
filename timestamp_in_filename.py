#!/bin/python

import os
import time

fstr = time.strftime("%d%b%Y_%H%M%S")
logfile = "log_"+fstr+".txt"
rcmd = "dir /OD >"+logfile

os.system(rcmd)
