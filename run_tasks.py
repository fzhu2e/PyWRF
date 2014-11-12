#!/usr/bin/env python3

import os
import subprocess
import datetime
import re
import time

def run_wps(run_name, start_time, end_time, interval):
    print('====================')
    print(' Run WPS...         ')
    print('====================')

    tmp_cmds = [
	'./pywrf.py wps -t make_new_run -o ' + run_name,
    './pywrf.py wps -t make_namelist -s ' + start_time + ' -e ' + end_time + ' -i ' + interval + ' -o ' + run_name,
    './pywrf.py wps -t geogrid -o ' + run_name,
    './pywrf.py wps -t ungrib -o ' + run_name,
    './pywrf.py wps -t metgrid -o ' + run_name
    ]

    for tmp_cmd in tmp_cmds:
        subprocess.call(tmp_cmd, shell=True)

def run_real(run_name, start_time, end_time, run_time, interval, input_out_interval):
    print('====================')
    print(' Run WRF-real...    ')
    print('====================')

    yyyy = start_time[0:4]
    mm = start_time[4:6]
    dd = start_time[6:8]
    hh = start_time[8:10]
    start_time_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))
    yyyy = end_time[0:4]
    mm = end_time[4:6]
    dd = end_time[6:8]
    hh = end_time[8:10]
    end_time_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))

    run_time_TIME = datetime.timedelta(hours=int(run_time))

    time_TIME = start_time_TIME
    while time_TIME < end_time_TIME:
        time_STR = str(time_TIME.year) + str(time_TIME.month) + str(time_TIME.day) + str(time_TIME.hour).zfill(2)

        tmp_cmds = [
        './pywrf.py wrf -t make_new_run -o ' + run_name,
        './pywrf.py wrf -t make_namelist -s ' + time_STR + ' -r ' + run_time + ' -i ' + interval + ' -o ' + run_name + ' --inputout_interval ' + input_out_interval,
        './pywrf.py wrf -t make_real_srun -o ' + run_name,
        './pywrf.py wrf -t real -o ' + run_name
        ]

        for tmp_cmd in tmp_cmds:
            subprocess.call(tmp_cmd, shell=True)

        time_TIME += run_time_TIME

def run_wrf(run_name, start_time, run_time, interval,
        inputout_interval, history_interval, inputout_begin_h):
    print('====================')
    print(' Run WRF-wrf...     ')
    print('====================')

    tmp_cmds = [
    './pywrf.py wrf -t make_namelist -s ' + start_time + ' -r ' + run_time + ' -i ' + interval + ' -o ' + run_name + ' --history_interval ' + history_interval + ' --inputout_interval ' + inputout_interval + ' --inputout_begin_h ' + inputout_begin_h,
    './pywrf.py wrf -t make_wrf_srun -o ' + run_name,
    './pywrf.py wrf -t wrf -o ' + run_name
    ]

    for tmp_cmd in tmp_cmds:
        subprocess.call(tmp_cmd, shell=True)

def run_gsi(run_name, ana_time, window):

    tmp_cmds = [
	'./pywrf.py gsi -t make_new_run -o ' + run_name,
	'./pywrf.py gsi -t make_script -a ' + ana_time + ' -o ' + run_name + ' -w ' + window,
	'./pywrf.py gsi -t gsi -o ' + run_name
    ]

    for tmp_cmd in tmp_cmds:
        subprocess.call(tmp_cmd, shell=True)

def run_da_update_bc(run_name, ana_time):

    tmp_cmds = [
	'./pywrf.py wrfda -t make_new_run -o ' + run_name,
	'./pywrf.py wrfda -t make_parame -o ' + run_name,
	'./pywrf.py wrfda -t da_update_bc -a ' + ana_time + ' -o ' + run_name
    ]

    for tmp_cmd in tmp_cmds:
        subprocess.call(tmp_cmd, shell=True)

def run_osse_hourly():
    print('====================')
    print(' Run OSSE Hourly... ')
    print('====================')

    # Settings
    run_name = 'run_OSSE_hourly'

    start_time = '2012102518'
    warm_time = '2012102600'
    mid_time = '2012102612'
    end_time = '2012102818'
    run_time = '1'

    interval = '3600'
    input_out_interval = '60'
    history_interval = '60'
    inputout_begin_h = '1'

    window = '0.5'

    #=============================================================
    # running list
    #=============================================================

    #run_wps(run_name, start_time, end_time, interval)

    #run_real(run_name, warm_time, mid_time, run_time, interval, input_out_interval)
    #run_real(run_name, mid_time, end_time, '54', '10800', '180')
    #run_real(run_name, start_time, warm_time, '6', '21600', '360')

    #run_wrf(run_name, start_time, '6', '10800', '180', '180', '3')

    run_gsi(run_name, warm_time, window)
    run_da_update_bc(run_name, warm_time)

    # cycling assimilation
    time = warm_time
    yyyy = time[0:4]
    mm = time[4:6]
    dd = time[6:8]
    hh = time[8:10]
    time_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))
    run_time_TIME = datetime.timedelta(hours=int(run_time))

    yyyy = mid_time[0:4]
    mm = mid_time[4:6]
    dd = mid_time[6:8]
    hh = mid_time[8:10]
    mid_time_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))

    while time_TIME <= mid_time_TIME:

        time_STR = str(time_TIME.year) + str(time_TIME.month) + str(time_TIME.day) + str(time_TIME.hour)

        run_wrf(run_name, time_STR, run_time, interval, input_out_interval, history_interval, inputout_begin_h)

        time_TIME += run_time_TIME
        time_STR = str(time_TIME.year) + str(time_TIME.month) + str(time_TIME.day) + str(time_TIME.hour).zfill(2)

        print(time_STR)

        run_gsi(run_name, time_STR, window)
        run_da_update_bc(run_name, time_STR)

    run_wrf(run_name, mid_time, 54, 10800, 180, 180, 3)

if __name__ == '__main__':
    run_osse_hourly()
