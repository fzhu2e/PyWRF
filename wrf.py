#!/usr/bin/env python3
import os
import subprocess

import env_vars

def run(args):
    print('Start running WRF...')
    print('Task:', args.task)

    env_vars.WORK_ROOT = os.path.join(env_vars.WRF_ROOT, env_vars.RUN_NAME)
    print('WORK_ROOT:', env_vars.WORK_ROOT)

    os.chdir(env_vars.WRF_ROOT)

    if not os.path.exists(env_vars.WORK_ROOT):
        os.mkdir(env_vars.WORK_ROOT)

    os.chdir(env_vars.WORK_ROOT)

    if args.task == 'make_new_run':
        make_new_run()

    elif args.task == 'make_namelist':
        make_namelist(args)

    elif args.task == 'real':
        run_real()

    elif args.task == 'wrf':
        run_wrf()


def make_new_run():

    tmp_dirs = [
            'geogrid',
            'metgrid',
            ]
    for tmp_dir in tmp_dirs:
        if not os.path.lexists(tmp_dir):
            os.mkdir(tmp_dir)

    tmp_cmds = [
    'ln -sf ' + env_vars.WPS_ROOT + '/geogrid/src/geogrid.exe .',
    'ln -sf ' + env_vars.WPS_ROOT + '/geogrid/GEOGRID.TBL.ARW ./geogrid/GEOGRID.TBL',
    'ln -sf ' + env_vars.WPS_ROOT + '/link_grib.csh .',
    'ln -sf ' + env_vars.WPS_ROOT + '/ungrib/src/ungrib.exe .',
    'ln -sf ' + env_vars.WPS_ROOT + '/ungrib/Variable_Tables/Vtable.GFS Vtable',
    'ln -sf ' + env_vars.WPS_ROOT + '/metgrid/METGRID.TBL.ARW ./metgrid/METGRID.TBL',
    'ln -sf ' + env_vars.WPS_ROOT + '/metgrid/src/metgrid.exe .',
    ]
    for tmp_cmd in tmp_cmds:
        subprocess.call(tmp_cmd, shell=True)

def make_namelist(args):
    start_time = str(env_vars.START_TIME).replace(' ', '_')
    end_time = str(env_vars.END_TIME).replace(' ', '_')

    namelist = open('namelist.wrf', 'w')
    #=================== configuration-s ===================
    namelist.write("""
    &share
     wrf_core = 'ARW',
     max_dom = 1,
     start_date = '""" + start_time + """','""" + start_time + """',
     end_date   = '""" + end_time + """',''""" + end_time + """',
     interval_seconds = 21600,
     io_form_geogrid = 2,
     debug_level=10
    /

    &geogrid
     parent_id         =   1,   1,
     parent_grid_ratio =   1,   3,
     i_parent_start    =   1,  31,
     j_parent_start    =   1,  17,
     e_we              =  400, 112,
     e_sn              =  350,  97,
     geog_data_res     = '10m','30s',
     dx = 12000,
     dy = 12000,
     map_proj = 'lambert',
     ref_lat   = 27,
     ref_lon   = -70,
     truelat1  = 20,
     truelat2  = 35,
     stand_lon = -70,
     geog_data_path = '""" + env_vars.GEOG_DATA_PATH + """'
    /

    &ungrib
     out_format = 'WPS',
     prefix = 'FILE',
    /

    &metgrid
     fg_name = 'FILE',
     io_form_metgrid = 2
    /
    """)
    #=================== configuration-e ===================

def run_real():

    if env_vars.MPI_WRF == False:
        subprocess.call('./real.exe', shell=True)

    else:
        subprocess.call('qsub -sync y real.job', shell=True)

def run_wrf():

    if env_vars.MPI_WRF == False:
        subprocess.call('./wrf.exe', shell=True)

    else:
        subprocess.call('qsub -sync y wrf.job', shell=True)
