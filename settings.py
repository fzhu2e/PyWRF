#!/usr/bin/env python3
import datetime
import env_vars
import os

def init(args):
    # path
    env_vars.PYWRF_ROOT = os.getcwd()

    #=================== configuration-s ===================
    # data path
    env_vars.GEOG_DATA_PATH = '/data/fzhu/Data/ForWPS/geog_data_pwang/geog'
    env_vars.FNL_DATA_PATH = '/data/fzhu/Data/ForSDAT/ncep'

    # model root
    env_vars.WPS_ROOT = '/data/fzhu/Tools/WRF-3.2.1/WPS'
    env_vars.WRF_ROOT = '/data/fzhu/Tools/WRF-3.2.1/WRFV3'
    env_vars.WRFDA_ROOT = '/data/fzhu/Tools/WRF-3.2.1/WRFDA'
    env_vars.GSI_ROOT = '/data/fzhu/Tools/GSI/comGSI_v3'

    # model setting
    env_vars.MPI_WPS = False
    env_vars.MPI_WRF = True
    env_vars.MPI_WRFDA = False
    env_vars.MPI_GSI = True

    env_vars.TIME_STEP = 60
    env_vars.MAX_DOM = 1
    env_vars.E_WE = [400, 0, 0]
    env_vars.E_SN = [350, 0, 0]
    env_vars.E_VERT = [35, 0, 0]
    env_vars.DX = [16000, 0, 0]
    env_vars.DY = [16000, 0, 0]
    env_vars.I_PARENT_START = [1, 0, 0]
    env_vars.J_PARENT_START = [1, 0, 0]
    #=================== configuration-e ===================

    # time
    if args.start is not None:
        yyyy = args.start[0:4]
        mm = args.start[4:6]
        dd = args.start[6:8]
        hh = args.start[8:10]
        env_vars.START_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))

    if args.end is not None:
        yyyy = args.end[0:4]
        mm = args.end[4:6]
        dd = args.end[6:8]
        hh = args.end[8:10]
        env_vars.END_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))
        env_vars.RUNNING_HOURS = env_vars.END_TIME - env_vars.START_TIME

    if args.run is not None:
        rh = args.run
        env_vars.RUNNING_HOURS = datetime.timedelta(hours=int(rh))
        env_vars.END_TIME = env_vars.START_TIME + env_vars.RUNNING_HOURS

    # run_name
    if args.workdir is not None:
        env_vars.RUN_NAME = args.workdir
    else:
        env_vars.PROJECT_NAME = 'OSSE'
        env_vars.CASE_NAME = str(env_vars.START_TIME.year) + str(env_vars.START_TIME.month) + str(env_vars.START_TIME.day) + str(env_vars.START_TIME.hour)
        env_vars.RUN_NAME = env_vars.PROJECT_NAME + '.' + env_vars.CASE_NAME

    # domain

    # print
    print('==================================')
    print('Start running PyWRF...')
    print('----------------------------------')
    print('Arguments:', args)
    print('Running mode:', args.mode)
    print('Running task:', args.task)
    print('----------------------------------')
    print('RUN_NAME:', env_vars.RUN_NAME)
    print('----------------------------------')
    print('PATH:')
    print('PYWRF_ROOT:', env_vars.PYWRF_ROOT)
    print('WPS_ROOT:', env_vars.WPS_ROOT)
    print('WRF_ROOT:', env_vars.WRF_ROOT)
    print('WRFDA_ROOT:', env_vars.WRFDA_ROOT)
    print('GSI_ROOT:', env_vars.GSI_ROOT)
    print('----------------------------------')
    print('TIME:')
    print('Start time:', env_vars.START_TIME)
    print('End time:', env_vars.END_TIME)
    print('Running hours:', env_vars.RUNNING_HOURS)
    print('==================================')
