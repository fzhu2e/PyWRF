#!/usr/bin/env python3

import subprocess
import datetime
import os


class Public:
    log_file = None


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
    Public.log_file.write('# run_wps\n')
    Public.log_file.write('\n'.join(tmp_cmds))
    Public.log_file.write('\n')

    for tmp_cmd in tmp_cmds:
        subprocess.call(tmp_cmd, shell=True)


def run_real(run_name, start, run_hours, interval, input_out_interval):
    print('====================')
    print(' Run WRF-real...    ')
    print('====================')

    tmp_cmds = [
        './pywrf.py wrf -t make_new_run -o ' + run_name,
        './pywrf.py wrf -t make_namelist -s ' + start + ' -r ' + run_hours + ' -i ' + interval + ' -o ' + run_name + ' --inputout_interval ' + input_out_interval,
        './pywrf.py wrf -t make_real_srun -o ' + run_name,
        './pywrf.py wrf -t real -o ' + run_name
    ]
    Public.log_file.write('# run_real\n')
    Public.log_file.write('\n'.join(tmp_cmds))
    Public.log_file.write('\n')

    for tmp_cmd in tmp_cmds:
        subprocess.call(tmp_cmd, shell=True)


def run_wrf(run_name, start, run_hours, interval, inputout_interval, history_interval, inputout_begin_h):
    print('====================')
    print(' Run WRF-wrf...     ')
    print('====================')

    tmp_cmds = [
        './pywrf.py wrf -t make_namelist -s ' + start + ' -r ' + run_hours + ' -i ' + interval + ' -o ' + run_name + ' --history_interval ' + history_interval + ' --inputout_interval ' + inputout_interval + ' --inputout_begin_h ' + inputout_begin_h,
        './pywrf.py wrf -t make_wrf_srun -o ' + run_name,
        './pywrf.py wrf -t wrf -o ' + run_name
    ]
    Public.log_file.write('# run_wrf\n')
    Public.log_file.write('\n'.join(tmp_cmds))
    Public.log_file.write('\n')

    for tmp_cmd in tmp_cmds:
        subprocess.call(tmp_cmd, shell=True)


def run_gsi(run_name, ana_time, window):

    tmp_cmds = [
        './pywrf.py gsi -t make_new_run -o ' + run_name,
        './pywrf.py gsi -t make_script -a ' + ana_time + ' -o ' + run_name + ' -w ' + window,
        './pywrf.py gsi -t gsi -o ' + run_name
    ]
    Public.log_file.write('# run_gsi\n')
    Public.log_file.write('\n'.join(tmp_cmds))
    Public.log_file.write('\n')

    for tmp_cmd in tmp_cmds:
        subprocess.call(tmp_cmd, shell=True)


def run_da_update_bc(run_name, ana_time):

    tmp_cmds = [
        './pywrf.py wrfda -t make_new_run -o ' + run_name,
        './pywrf.py wrfda -t make_parame -o ' + run_name,
        './pywrf.py wrfda -t da_update_bc -a ' + ana_time + ' -o ' + run_name
    ]
    Public.log_file.write('# run_da_update_bc\n')
    Public.log_file.write('\n'.join(tmp_cmds))
    Public.log_file.write('\n')

    for tmp_cmd in tmp_cmds:
        subprocess.call(tmp_cmd, shell=True)


def run_cyc_da_forecast(run_name, cold_start, spin_up_hours, cyc_da_every_hours, forecast_start, forecast_hours):
    '''
    cold_start --(spin_up_hours)--> warm_start --(cyc_da_every_hours)-->
    forcast_start --(forecast_hours)--> END
    '''

    print('PyWRF: start running cyc_da_forecast...')
    yyyy = cold_start[0:4]
    mm = cold_start[4:6]
    dd = cold_start[6:8]
    hh = cold_start[8:10]
    cold_start_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))
    cold_start = cold_start_TIME.strftime('%Y%m%d%H')

    warm_start_TIME = cold_start_TIME + datetime.timedelta(hours=spin_up_hours)
    warm_start = warm_start_TIME.strftime('%Y%m%d%H')

    yyyy = forecast_start[0:4]
    mm = forecast_start[4:6]
    dd = forecast_start[6:8]
    hh = forecast_start[8:10]
    forecast_start_TIME = datetime.datetime(int(yyyy), int(mm), int(dd), int(hh))
    forecast_end_TIME = forecast_start_TIME + datetime.timedelta(hours=forecast_hours)
    forecast_end = forecast_end_TIME.strftime('%Y%m%d%H')

    print('run_name:', run_name)
    print('cold_start:', cold_start)
    print('warm_start:', warm_start)
    print('forecast_start:', forecast_start)
    print('forecast_end:', forecast_end)
    print('spin_up_hours:', spin_up_hours)
    print('cyc_da_every_hours:', cyc_da_every_hours)

    #---------------------------------------------------------------------------
    # wps
    #---------------------------------------------------------------------------
    print('PyWRF: start running wps...')

    wps_interval = str(cyc_da_every_hours*3600)
    run_wps(run_name, cold_start, forecast_end, wps_interval)

    #---------------------------------------------------------------------------
    # real
    #---------------------------------------------------------------------------
    print('PyWRF: start running real...')

    real_interval = str(cyc_da_every_hours*3600)
    real_input_out_interval = str(cyc_da_every_hours*60)
    real_run_hours = str(cyc_da_every_hours)
    real_run_TIME = datetime.timedelta(hours=cyc_da_every_hours)

    # for cycling
    present_TIME = warm_start_TIME
    end_TIME = forecast_start_TIME

    while present_TIME < end_TIME:

        present = present_TIME.strftime('%Y%m%d%H')

        run_real(run_name, present, real_run_hours, real_interval, real_input_out_interval)

        present_TIME += real_run_TIME

    # for forecast
    real_run_hours = str(forecast_hours)
    real_input_out_interval = str(cyc_da_every_hours*180)
    run_real(run_name, forecast_start, real_run_hours, real_interval, real_input_out_interval)

    # for spin-up
    real_interval = str(cyc_da_every_hours*21600)
    real_run_hours = str(spin_up_hours)
    run_real(run_name, cold_start, real_run_hours, real_interval, real_input_out_interval)

    #---------------------------------------------------------------------------
    # wrf spin-up
    #---------------------------------------------------------------------------
    print('PyWRF: start running wrf for spin-up...')

    wrf_run_hours = str(spin_up_hours)
    wrf_interval = str(spin_up_hours*3600)
    wrf_inputout_interval = str(spin_up_hours*30)
    wrf_history_interval = str(spin_up_hours*30)
    wrf_inputout_begin_h = str(3)
    run_wrf(run_name, cold_start, wrf_run_hours, wrf_interval, wrf_inputout_interval, wrf_history_interval, wrf_inputout_begin_h)

    #---------------------------------------------------------------------------
    # gsi + da_update_bc
    #---------------------------------------------------------------------------
    print('PyWRF: start running gsi + da_update_bc...')
    ana_time = warm_start
    window = str(cyc_da_every_hours/2.)

    run_gsi(run_name, ana_time, window)
    run_da_update_bc(run_name, ana_time)

    #---------------------------------------------------------------------------
    # cycling: wrf + gsi + da_update_bc
    #---------------------------------------------------------------------------
    print('PyWRF: start running wrf + gsi + da_update_bc...')
    # for cycling
    present_TIME = warm_start_TIME
    end_TIME = forecast_start_TIME
    cyc_run_TIME = datetime.timedelta(hours=cyc_da_every_hours)

    wrf_run_hours = str(cyc_da_every_hours)
    wrf_interval = str(cyc_da_every_hours*3600)
    wrf_inputout_interval = str(cyc_da_every_hours*60)
    wrf_history_interval = str(cyc_da_every_hours*60)
    wrf_inputout_begin_h = str(cyc_da_every_hours)

    while present_TIME < end_TIME:

        present = present_TIME.strftime('%Y%m%d%H')

        run_wrf(run_name, present, wrf_run_hours, wrf_interval, wrf_inputout_interval, wrf_history_interval, wrf_inputout_begin_h)

        ana_time = present
        run_gsi(run_name, ana_time, window)
        run_da_update_bc(run_name, ana_time)

        present_TIME += cyc_run_TIME

    #---------------------------------------------------------------------------
    # wrf
    #---------------------------------------------------------------------------
    print('PyWRF: start running wrf for forecast...')
    wrf_run_hours = str(forecast_hours)
    wrf_interval = str(cyc_da_every_hours*10800)
    wrf_inputout_interval = str(cyc_da_every_hours*180)
    wrf_history_interval = str(cyc_da_every_hours*180)
    wrf_inputout_begin_h = str(cyc_da_every_hours*3)
    run_wrf(run_name, present, wrf_run_hours, wrf_interval, wrf_inputout_interval, wrf_history_interval, wrf_inputout_begin_h)


if __name__ == '__main__':

    log_file_name = 'running_script.sh'

    if os.path.exists(log_file_name):
        os.remove(log_file_name)

    Public.log_file = open(log_file_name, 'a')

    run_name = 'run_OSSE_6hcyc'
    cold_start = '2012102618'
    spin_up_hours = 6
    cyc_da_every_hours = 6
    forecast_start = '2012102706'
    forecast_hours = 48

    run_cyc_da_forecast(
        run_name,
        cold_start, spin_up_hours, cyc_da_every_hours,
        forecast_start, forecast_hours
    )

    Public.log_file.close()
