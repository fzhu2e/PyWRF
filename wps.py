#!/usr/bin/env python3
import os
import subprocess
import re

import env_vars

def run(args):
    print('Start running WPS...')
    print('Task:', args.task)

    env_vars.WORK_ROOT = os.path.join(env_vars.WPS_ROOT, env_vars.RUN_NAME)
    print('WORK_ROOT:', env_vars.WORK_ROOT)

    os.chdir(env_vars.WPS_ROOT)

    if not os.path.exists(env_vars.WORK_ROOT):
        os.mkdir(env_vars.WORK_ROOT)

    os.chdir(env_vars.WORK_ROOT)

    if args.task == 'make_new_run':
        make_new_run()

    elif args.task == 'make_namelist':
        make_namelist()

    elif args.task == 'geogrid':
        run_geogrid()

    elif args.task == 'ungrib':
        run_ungrib()

    elif args.task == 'metgrid':
        run_metgrid()


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

def make_namelist():
    start_time = str(env_vars.START_TIME).replace(' ', '_')
    end_time = str(env_vars.END_TIME).replace(' ', '_')

    max_dom = str(env_vars.MAX_DOM)
    e_we = re.sub(r'\[|\]', '', str(env_vars.E_WE))
    e_sn = re.sub(r'\[|\]', '', str(env_vars.E_SN))
    e_vert = re.sub(r'\[|\]', '', str(env_vars.E_VERT))
    i_parent_start = re.sub(r'\[|\]', '', str(env_vars.I_PARENT_START))
    j_parent_start = re.sub(r'\[|\]', '', str(env_vars.J_PARENT_START))
    dx = str(env_vars.DX[0])
    dy = str(env_vars.DY[0])

    namelist = open('namelist.wps', 'w')
    #=================== configuration-s ===================
    namelist.write("""
    &share
     wrf_core = 'ARW',
     max_dom = """ + max_dom + """,
     start_date = '""" + start_time + """','""" + start_time + """',
     end_date   = '""" + end_time + """',''""" + end_time + """',
     interval_seconds = 21600,
     io_form_geogrid = 2,
     debug_level=10
    /

    &geogrid
     parent_id         =   1,   1,   1,
     parent_grid_ratio =   1,   3,   3,
     i_parent_start    =  """ + i_p_s + """,
     j_parent_start    =  """ + j_p_s + """,
     e_we              =  """ + e_we + """,
     e_sn              =  """ + e_sn + """
     geog_data_res     = '10m','30s',
     dx = """ + dx + """,
     dy = """ + dy + """,
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

def run_geogrid():
    if env_vars.MPI_WPS == False:
        subprocess.call('./geogrid.exe', shell=True)

    else:
        subprocess.call('qsub -sync y geogrid.job', shell=True)

def run_ungrib():
    subprocess.call('./link_grib.csh ' + env_vars.FNL_DATA_PATH + '/fnl*', shell=True)

    if env_vars.MPI_WPS == False:
        subprocess.call('./ungrib.exe', shell=True)

    else:
        subprocess.call('qsub -sync y ungrib.job', shell=True)

def run_metgrid():
    if env_vars.MPI_WPS == False:
        subprocess.call('./metgrid.exe', shell=True)

    else:
        subprocess.call('qsub -sync y metgrid.job', shell=True)
