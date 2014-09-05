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
    yyyy = str(env_vars.ANA_TIME.year).zfill(4)
    mm = str(env_vars.ANA_TIME.month).zfill(2)
    dd = str(env_vars.ANA_TIME.day).zfill(2)
    hh = str(env_vars.ANA_TIME.hour).zfill(2)

    ana_time = yyyy + mm + dd + hh

    datehour = ana_time

    result_dir = os.path.join(env_vars.RESULTS_DA_UPDATE_BC, datehour)

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

    subprocess.call('cp ' + os.path.join(env_vars.RESULTS_REAL, datehour, 'wrfbdy_d01 .'), shell=True)
    subprocess.call('cp ' + os.path.join(env_vars.RESULTS_GSI, datehour, 'wrf_inout wrfvar_output'), shell=True)

    subprocess.call('./da_update_bc.exe', shell=True)

    subprocess.call('cp wrfbdy_d01 ' + result_dir, shell=True)

    subprocess.call('rm -f ' + os.path.join(env_vars.WRF_ROOT, env_vars.RUN_NAME, 'wrfbdy_d01'), shell=True)
    subprocess.call('cp wrfbdy_d01 ' + os.path.join(env_vars.WRF_ROOT, env_vars.RUN_NAME), shell=True)
