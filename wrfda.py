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
        make_parame()

    elif args.task == 'da_update_bc':
        run_da_update_bc()

def make_new_run():
    subprocess.call('rm -rf *', shell=True)
    subprocess.call('cp ../var/build/da_update_bc.exe .', shell=True)

def make_parame():

    print('Update lower boundary condition?', env_vars.LOWER)

    if env_vars.LOWER == True:
        parame = open('parame.in', 'w')
        #=================== configuration-s ===================
        parame.write("""&control_param
 da_file            =   './wrfvar_input'
 wrf_input          =   './wrfinput_d01'
 update_lateral_bdy =   .false.
 update_low_bdy     =   .true.
 iswater            =   16
/
""")
        #=================== configuration-e ===================
        parame.close()

    else:
        parame = open('parame.in', 'w')
        #=================== configuration-s ===================
        parame.write("""&control_param
 da_file            =   './wrf_inout'
 wrf_bdy_file       =   './wrfbdy_d01'
 debug              =   .true.
 domain_id          =   1
 update_lateral_bdy =   .true.
 update_low_bdy     =   .false.
 update_lsm         =   .false.
 var4d_lbc          =   .false.
/
""")
        #=================== configuration-e ===================
        parame.close()

def run_da_update_bc():
    yyyy = str(env_vars.ANA_TIME.year).zfill(4)
    mm = str(env_vars.ANA_TIME.month).zfill(2)
    dd = str(env_vars.ANA_TIME.day).zfill(2)
    hh = str(env_vars.ANA_TIME.hour).zfill(2)

    ana_time = yyyy + mm + dd + hh

    datehour = ana_time

    ana_datetime = str(env_vars.ANA_TIME).replace(' ', '_')

    result_dir = os.path.join(env_vars.RESULTS_DA_UPDATE_BC, datehour)

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

    if env_vars.LOWER == True:
        subprocess.call('cp ' + os.path.join(env_vars.RESULTS_REAL, datehour, 'wrfinput_d01 .'), shell=True)
        bk_file = os.path.join(env_vars.WRF_ROOT, env_vars.RUN_NAME, 'wrfvar_input_d01_'+ana_datetime)
        subprocess.call('cp ' + bk_file + ' wrfvar_input', shell=True)

        subprocess.call('./da_update_bc.exe', shell=True)

        subprocess.call('cp wrfvar_input ' + result_dir, shell=True)
        subprocess.call('rm -f ' + bk_file, shell=True)
        subprocess.call('cp wrfvar_input ' + bk_file, shell=True)

    else:
        subprocess.call('cp ' + os.path.join(env_vars.RESULTS_REAL, datehour, 'wrfbdy_d01 .'), shell=True)
        subprocess.call('cp ' + os.path.join(env_vars.RESULTS_GSI, datehour, 'wrf_inout .'), shell=True)

        subprocess.call('./da_update_bc.exe', shell=True)

        subprocess.call('cp wrfbdy_d01 ' + result_dir, shell=True)

        subprocess.call('rm -f ' + os.path.join(env_vars.WRF_ROOT, env_vars.RUN_NAME, 'wrfbdy_d01'), shell=True)
        subprocess.call('cp wrfbdy_d01 ' + os.path.join(env_vars.WRF_ROOT, env_vars.RUN_NAME), shell=True)
