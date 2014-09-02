#!/usr/bin/env python3
import datetime
import env_vars
import os

def init(args):
    # path
    env_vars.PYWRF_ROOT = os.getcwd()

    #=================== configuration-s ===================
    # Project
    env_vars.PROJECT_NAME = 'OSSE'
    env_vars.RESULTS_ROOT = '/data/fzhu/Results'

    env_vars.RESULTS = os.path.join(env_vars.RESULTS_ROOT, env_vars.PROJECT_NAME)
    env_vars.RESULTS_WPS = os.path.join(env_vars.RESULTS, 'wps')
    env_vars.RESULTS_REAL = os.path.join(env_vars.RESULTS, 'real')
    env_vars.RESULTS_WRF = os.path.join(env_vars.RESULTS, 'wrf')
    env_vars.RESULTS_DA_UPDATE_BC = os.path.join(env_vars.RESULTS, 'da_update_bc')
    env_vars.RESULTS_GSI = os.path.join(env_vars.RESULTS, 'gsi')

    tmp_dirs = [
            env_vars.RESULTS_ROOT,
            env_vars.RESULTS,
            env_vars.RESULTS_WPS,
            env_vars.RESULTS_REAL,
            env_vars.RESULTS_WRF,
            env_vars.RESULTS_DA_UPDATE_BC,
            env_vars.RESULTS_GSI,
            ]
    for tmp_dir in tmp_dirs:
        if not os.path.exists(tmp_dir):
            os.mkdir(tmp_dir)

    # data path
    env_vars.GEOG_DATA_PATH = '/data/fzhu/Data/ForWPS/geog_data_pwang/geog'
    env_vars.FNL_DATA_PATH = '/data/fzhu/Data/ForSDAT/ncep'
    env_vars.CRTM_PATH = '/data/fzhu/Data/ForGSI/CRTM_Coefficients'

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

    # time
    env_vars.HISTROY_INTERVAL = [180, 0, 0]
    env_vars.INPUTOUT_INTERVAL = 180
    env_vars.INPUTOUT_BEGIN_H = 3
    env_vars.INPUTOUT_END_H = 6

    # domain
    env_vars.TIME_STEP = 50
    env_vars.MAX_DOM = 1
    env_vars.E_WE = [500, 0, 0]
    env_vars.E_SN = [240, 0, 0]
    env_vars.E_VERT = [72, 0, 0]
    env_vars.DX = [16000, 0, 0]
    env_vars.DY = [16000, 0, 0]
    env_vars.I_PARENT_START = [1, 0, 0]
    env_vars.J_PARENT_START = [1, 0, 0]

    env_vars.REF_LAT = 33
    env_vars.REF_LON = -76
    env_vars.TRUELAT1 = 20
    env_vars.TRUELAT2 = 40
    env_vars.STAND_LON = -70

    # time
    env_vars.P_TOP_REQUESTED = 5000
    #=================== configuration-e ===================

    # time
    if hasattr(args, 'start'):
        if args.start is not None:
            yyyy = args.start[0:4]
            mm = args.start[4:6]
            dd = args.start[6:8]
            hh = args.start[8:10]
            env_vars.START_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))

    if hasattr(args, 'end'):
        if args.end is not None:
            yyyy = args.end[0:4]
            mm = args.end[4:6]
            dd = args.end[6:8]
            hh = args.end[8:10]
            env_vars.END_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))
            env_vars.RUNNING_HOURS = env_vars.END_TIME - env_vars.START_TIME

    if hasattr(args, 'run'):
        if args.run is not None:
            rh = args.run
            env_vars.RUNNING_HOURS = datetime.timedelta(hours=int(rh))
            env_vars.END_TIME = env_vars.START_TIME + env_vars.RUNNING_HOURS

    if hasattr(args, 'interval_seconds'):
        if args.interval_seconds is not None:
            env_vars.INTERVAL_SECONDS = args.interval_seconds

    if hasattr(args, 'ana'):
        if args.ana is not None:
            yyyy = args.ana[0:4]
            mm = args.ana[4:6]
            dd = args.ana[6:8]
            hh = args.ana[8:10]
            env_vars.ANA_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))

    if hasattr(args, 'window'):
        if args.window is not None:
            ww = args.window
            env_vars.WINDOW = datetime.timedelta(hours=int(ww))
        else:
            env_vars.WINDOW = datetime.timedelta(hours=1.5)

    if hasattr(args, 'cold'):
        if args.cold is not None:
            env_vars.COLD = True
        else:
            env_vars.COLD = False


    # run_name
    if args.workdir is not None:
        env_vars.RUN_NAME = args.workdir
    else:
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
    #print('----------------------------------')
    #print('TIME:')
    #print('Start time:', env_vars.START_TIME)
    #print('End time:', env_vars.END_TIME)
    #print('Running hours:', env_vars.RUNNING_HOURS)
    print('==================================')
