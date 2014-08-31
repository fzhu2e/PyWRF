#!/usr/bin/env python3
import datetime
import env_vars
import os

def init(args):
    # path
    env_vars.PYWRF_ROOT = os.getcwd()
    env_vars.WPS_ROOT = "/data/fzhu/Tools/WRF-3.2.1/WPS"
    env_vars.WRF_ROOT = "/data/fzhu/Tools/WRF-3.2.1/WRFV3"
    env_vars.WRFDA_ROOT = "/data/fzhu/Tools/WRF-3.2.1/WRFDA"
    env_vars.GSI_ROOT = "/data/fzhu/Tools/GSI/comGSI_v3"

    # time
    yyyy = args.start[0:4]
    mm = args.start[4:6]
    dd = args.start[6:8]
    hh = args.start[8:10]
    env_vars.START_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))

    if type(args.end) is not None:
        yyyy = args.end[0:4]
        mm = args.end[4:6]
        dd = args.end[6:8]
        hh = args.end[8:10]
        env_vars.END_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))
        env_vars.RUNNING_HOURS = env_vars.END_TIME - env_vars.START_TIME

    else:
        rh = args.run
        env_vars.RUNNING_HOURS = datetime.timedelta(hours=int(rh))
        env_vars.END_TIME = env_vars.START_TIME + env_vars.RUNNING_HOURS

    # project
    env_vars.PROJECT_NAME = "OSSE"
    env_vars.CASE_NAME = str(env_vars.START_TIME.year) + str(env_vars.START_TIME.month) + str(env_vars.START_TIME.day) + str(env_vars.START_TIME.hour)
    env_vars.RUN_NAME = env_vars.PROJECT_NAME + "." + env_vars.CASE_NAME

    # domain

    # print
    print("==================================")
    print("Start running PyWRF...")
    print("----------------------------------")
    print("Arguments:", args)
    print("Running mode:", args.mode)
    print("Running task:", args.task)
    print("----------------------------------")
    print("RUN_NAME:", env_vars.RUN_NAME)
    print("----------------------------------")
    print("PATH:")
    print("PYWRF_ROOT:", env_vars.PYWRF_ROOT)
    print("WPS_ROOT:", env_vars.WPS_ROOT)
    print("WRF_ROOT:", env_vars.WRF_ROOT)
    print("WRFDA_ROOT:", env_vars.WRFDA_ROOT)
    print("GSI_ROOT:", env_vars.GSI_ROOT)
    print("----------------------------------")
    print("TIME:")
    print("Start time:", env_vars.START_TIME)
    print("End time:", env_vars.END_TIME)
    print("Running hours:", env_vars.RUNNING_HOURS)
    print("==================================")
