#!/usr/bin/env python3
import os
import subprocess
import re

import env_vars
import tools

def run(args):
    print('Start running WRFDA...')
    print('Task:', args.task)

    env_vars.WORK_ROOT = os.path.join(env_vars.WRFDA_ROOT, env_vars.RUN_NAME)
    print('WORK_ROOT:', env_vars.WORK_ROOT)

    os.chdir(env_vars.WRFDA_ROOT)

    if not os.path.exists(env_vars.WORK_ROOT):
        os.mkdir(env_vars.WORK_ROOT)

    os.chdir(env_vars.WORK_ROOT)

    if args.task == 'make_new_run':
        make_new_run()

    elif args.task == 'make_parame':
        make_namelist()

    elif args.task == 'da_update_bc':
        run_da_update_bc()

def make_new_run():
    subprocess.call('cp ../var/test/update_bc/* .', shell=True)

#def make_parame():
    #pass

def run_da_update_bc():

    subprocess.call('ln -sf ' + env_vars.RESULTS_WPS + '/met_em* .', shell=True)

    if env_vars.MPI_WRF == False:
        subprocess.call('./real.exe', shell=True)

    else:
        subprocess.call('qsub -sync y real.job', shell=True)

    yyyy = tools.pick_value('namelist.input', 'start_year')
    mm = tools.pick_value('namelist.input', 'start_month')
    dd = tools.pick_value('namelist.input', 'start_day')
    hh = tools.pick_value('namelist.input', 'start_hour')

    datehour = yyyy + mm + dd + hh

    #subprocess.call('ln -sf ' + os.path.join(env_vars.RESULTS_REAL, datehour, 'wrf* .'), shell=True)
