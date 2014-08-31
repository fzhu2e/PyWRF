#!/usr/bin/env python3
import datetime

# Path
WPS_ROOT = "/data/fzhu/Tools/WRF-3.2.1/WPS"
WRF_ROOT = "/data/fzhu/Tools/WRF-3.2.1/WRFV3"
WRFDA_ROOT = "/data/fzhu/Tools/WRF-3.2.1/WRFDA"
GSI_ROOT = "/data/fzhu/Tools/GSI/comGSI_v3"

# Time
START_TIME = datetime.datetime(2012, 10, 25, 18)
END_TIME = datetime.datetime(2012, 10, 26, 00)
RUNNING_HOURS = END_TIME - START_TIME

# Case
PROJECT_NAME = "OSSE"
CASE_NAME = str(START_TIME.year) + str(START_TIME.month) + str(START_TIME.day) + str(START_TIME.hour)
RUN_NAME = PROJECT_NAME + "." + CASE_NAME


# Domain
