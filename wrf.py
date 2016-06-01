#!/usr/bin/env python3
import os
import subprocess
import re
import time

import env_vars
import tools


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
        make_namelist()

    elif args.task == 'make_real_srun':
        make_real_srun()

    elif args.task == 'make_wrf_srun':
        make_wrf_srun()

    elif args.task == 'real':
        run_real()

    elif args.task == 'wrf':
        run_wrf()


def make_new_run():
    subprocess.call('cp ../run/* .', shell=True)
    subprocess.call('ln -sf ' + env_vars.WRF_ROOT + '/main/*.exe .', shell=True)
    subprocess.call('rm -f namelist.input', shell=True)


def make_namelist():
    yyyy_s = str(env_vars.START_TIME.year).zfill(4)
    mm_s = str(env_vars.START_TIME.month).zfill(2)
    dd_s = str(env_vars.START_TIME.day).zfill(2)
    hh_s = str(env_vars.START_TIME.hour).zfill(2)

    yyyy_e = str(env_vars.END_TIME.year).zfill(4)
    mm_e = str(env_vars.END_TIME.month).zfill(2)
    dd_e = str(env_vars.END_TIME.day).zfill(2)
    hh_e = str(env_vars.END_TIME.hour).zfill(2)

    run_days = str(env_vars.RUNNING_HOURS.days)
    run_hours = str(env_vars.RUNNING_HOURS.seconds//3600)

    time_step = str(env_vars.TIME_STEP)
    max_dom = str(env_vars.MAX_DOM)
    e_we = re.sub(r'\[|\]', '', str(env_vars.E_WE))
    e_sn = re.sub(r'\[|\]', '', str(env_vars.E_SN))
    e_vert = re.sub(r'\[|\]', '', str(env_vars.E_VERT))
    i_parent_start = re.sub(r'\[|\]', '', str(env_vars.I_PARENT_START))
    j_parent_start = re.sub(r'\[|\]', '', str(env_vars.J_PARENT_START))
    dx = re.sub(r'\[|\]', '', str(env_vars.DX))
    dy = re.sub(r'\[|\]', '', str(env_vars.DY))

    interval_seconds = str(env_vars.INTERVAL_SECONDS)
    history_interval = re.sub(r'\[|\]', '', str(env_vars.HISTORY_INTERVAL))
    inputout_interval = str(env_vars.INPUTOUT_INTERVAL)
    inputout_begin_h = str(env_vars.INPUTOUT_BEGIN_H)
    inputout_end_h = str(env_vars.INPUTOUT_END_H)

    p_top_requested = str(env_vars.P_TOP_REQUESTED)
    eta_levels = re.sub(r'\[|\]', '', str(env_vars.ETA_LEVELS))
    # print(eta_levels)

    # zap_close_levels                    = 1,
    # eta_levels                          = """ + eta_levels + """

    namelist = open('namelist.input', 'w')
    # =================== configuration-s ===================
    namelist.write("""&time_control
 run_days                            = """ + run_days + """,
 run_hours                           = """ + run_hours + """,
 run_minutes                         = 0,
 run_seconds                         = 0,
 start_year                          = """ + yyyy_s + """, """ + yyyy_s + """, """ + yyyy_s + """,
 start_month                         = """ + mm_s + """, """ + mm_s + """, """ + mm_s + """,
 start_day                           = """ + dd_s + """, """ + dd_s + """, """ + dd_s + """,
 start_hour                          = """ + hh_s + """, """ + hh_s + """, """ + hh_s + """,
 start_minute                        = 00,   00,   00,
 start_second                        = 00,   00,   00,
 end_year                            = """ + yyyy_e + """, """ + yyyy_e + """, """ + yyyy_e + """,
 end_month                           = """ + mm_e + """, """ + mm_e + """, """ + mm_e + """,
 end_day                             = """ + dd_e + """, """ + dd_e + """, """ + dd_e + """,
 end_hour                            = """ + hh_e + """, """ + hh_e + """, """ + hh_e + """,
 end_minute                          = 00,   00,   00,
 end_second                          = 00,   00,   00,
 interval_seconds                    = """ + interval_seconds + """,
 input_from_file                     = .true.,.true.,.true.,
 history_interval                    = """ + history_interval + """,
 frames_per_outfile                  = 1, 1000, 1000,
 restart                             = .false.,
 restart_interval                    = 5000,
 io_form_history                     = 2
 io_form_restart                     = 2
 io_form_input                       = 2
 io_form_boundary                    = 2
 debug_level                         = 1000
 write_input             = .true.,
 inputout_interval       = """ + inputout_interval + """,
 inputout_begin_h        = """ + inputout_begin_h + """,
 inputout_end_h          = """ + inputout_end_h + """,
 input_outname           = "wrfvar_input_d<domain>_<date>",
 /

 &domains
 time_step                           = """ + time_step + """,
 time_step_fract_num                 = 0,
 time_step_fract_den                 = 1,
 max_dom                             = """ + max_dom + """,
 e_we                                = """ + e_we + """,
 e_sn                                = """ + e_sn + """,
 e_vert                              = """ + e_vert + """,
 p_top_requested                     = """ + p_top_requested + """,
 num_metgrid_levels                  = 27,
 num_metgrid_soil_levels             = 4,
 dx                                  = """ + dx + """,
 dy                                  = """ + dy + """,
 grid_id                             = 1,     2,     3,
 parent_id                           = 0,     1,     2,
 i_parent_start                      = """ + i_parent_start + """,
 j_parent_start                      = """ + j_parent_start + """,
 parent_grid_ratio                   = 1,     3,     3,
 parent_time_step_ratio              = 1,     3,     3,
 feedback                            = 1,
 smooth_option                       = 0,
 /

 &physics
 mp_physics                          = 6,     3,     3,
 ra_lw_physics                       = 4,     1,     1,
 ra_sw_physics                       = 4,     1,     1,
 radt                                = 30,    30,    30,
 sf_sfclay_physics                   = 1,     1,     1,
 sf_surface_physics                  = 2,     2,     2,
 bl_pbl_physics                      = 1,     1,     1,
 bldt                                = 0,     0,     0,
 cu_physics                          = 1,     1,     0,
 cudt                                = 5,     5,     5,
 isfflx                              = 1,
 ifsnow                              = 0,
 icloud                              = 1,
 surface_input_source                = 1,
 num_soil_layers                     = 4,
 sf_urban_physics                    = 0,     0,     0,
 maxiens                             = 1,
 maxens                              = 3,
 maxens2                             = 3,
 maxens3                             = 16,
 ensdim                              = 144,
 /

 &fdda
 /

 &dynamics
 w_damping                           = 1,
 diff_opt                            = 1,
 km_opt                              = 4,
 diff_6th_opt                        = 0,      0,      0,
 diff_6th_factor                     = 0.12,   0.12,   0.12,
 base_temp                           = 290.
 damp_opt                            = """ + str(env_vars.DAMP_OPT) + """,
 zdamp                               = 5000.,  5000.,  5000.,
 dampcoef                            = 0.2,    0.2,    0.2
 khdif                               = 0,      0,      0,
 kvdif                               = 0,      0,      0,
 non_hydrostatic                     = .true., .true., .true.,
 moist_adv_opt                       = 1,      1,      1,
 scalar_adv_opt                      = 1,      1,      1,
 use_baseparam_fr_nml                = .true.
 /

 &bdy_control
 spec_bdy_width                      = """ + str(env_vars.SPEC_BDY_WIDTH) + """,
 spec_zone                           = 1,
 relax_zone                          = """ + str(env_vars.RELAX_ZONE) + """,
 specified                           = .true., .false., .false.,
 nested                              = .false., .true., .true.,
 /

 &grib2
 /

 &namelist_quilt
 nio_tasks_per_group = 0,
 nio_groups = 1,
 /""")
    # =================== configuration-e ===================
    namelist.close()


def make_real_srun():

    yyyy = tools.pick_value('namelist.input', 'start_year').zfill(4)
    mm = tools.pick_value('namelist.input', 'start_month').zfill(2)
    dd = tools.pick_value('namelist.input', 'start_day').zfill(2)
    hh = tools.pick_value('namelist.input', 'start_hour').zfill(2)

    datehour = yyyy + mm + dd + hh

    result_dir = os.path.join(env_vars.RESULTS_REAL, datehour)

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

    user_name = os.environ['USER']

    srun = open('real.srun', 'w')
    # =================== configuration-s ===================
    srun.write("""#!/usr/bin/env bash
#SBATCH --job-name=real_arw

#SBATCH --partition=s4
#SBATCH --export=ALL
#SBATCH --ntasks=""" + str(env_vars.REAL_PROC) + """
#SBATCH --mem-per-cpu=6000
#SBATCH --time=00:30:00
#SBATCH --output=/scratch/""" + user_name + """/tmp/real_arw-control.%j
source /etc/bashrc
module purge
module load license_intel intel/14.0-2
module load impi
module load hdf hdf5
module load netcdf4/4.1.3

# here you could call a script that creates your srun jobs and manages them
# or you could just run srun like this

INPUT=""" + env_vars.WORK_ROOT + """
RESULTS=""" + result_dir + """
EXECUTABLE=./real.exe

WORK_DIR=/scratch/$USER/real

cd $WORK_DIR
rm -rf ./*
#rsync -a $INPUT/* $WORK_DIR
cp $INPUT/* $WORK_DIR

srun --cpu_bind=core --distribution=block:block $EXECUTABLE

#rsync -a ./wrfbdy* $RESULTS
#rsync -a ./wrfinput* $RESULTS
cp ./wrfbdy* $RESULTS
cp ./wrfinput* $RESULTS

# rm -rf ./*

exit 0""")
    # =================== configuration-e ===================
    srun.close()


def make_wrf_srun():

    yyyy = tools.pick_value('namelist.input', 'start_year').zfill(4)
    mm = tools.pick_value('namelist.input', 'start_month').zfill(2)
    dd = tools.pick_value('namelist.input', 'start_day').zfill(2)
    hh = tools.pick_value('namelist.input', 'start_hour').zfill(2)

    datehour = yyyy + mm + dd + hh

    result_dir = os.path.join(env_vars.RESULTS_WRF, datehour)

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

    user_name = os.environ['USER']

    srun = open('wrf.srun', 'w')
    # =================== configuration-s ===================
    srun.write("""#!/usr/bin/env bash
#SBATCH --job-name=wrf_arw

#SBATCH --partition=s4
#SBATCH --export=ALL
#SBATCH --ntasks=""" + str(env_vars.WRF_PROC) + """
#SBATCH --mem-per-cpu=6000
#SBATCH --time=02:00:00
#SBATCH --output=/scratch/""" + user_name + """/tmp/wrf_arw-control.%j
source /etc/bashrc
module purge
module load license_intel intel/14.0-2
module load impi
module load hdf hdf5
module load netcdf4/4.1.3

# here you could call a script that creates your srun jobs and manages them
# or you could just run srun like this

INPUT=""" + env_vars.WORK_ROOT + """
RESULTS=""" + result_dir + """
EXECUTABLE=./wrf.exe

WORK_DIR=/scratch/$USER/wrf/

cd $WORK_DIR
rm -rf ./*
#rsync -a $INPUT/* $WORK_DIR
cp $INPUT/* $WORK_DIR

srun --cpu_bind=core --distribution=block:block $EXECUTABLE

# rsync -a ./wrfvar* $RESULTS
# rsync -a ./wrfout* $RESULTS
cp ./wrfvar* $RESULTS
cp ./wrfout* $RESULTS

#rm -rf ./*

exit 0""")
    # =================== configuration-e ===================
    srun.close()


def run_real():

    yyyy = tools.pick_value('namelist.input', 'start_year')
    mm = tools.pick_value('namelist.input', 'start_month')
    dd = tools.pick_value('namelist.input', 'start_day')
    hh = tools.pick_value('namelist.input', 'start_hour')

    datehour = yyyy + mm + dd + hh

    result_dir = os.path.join(env_vars.RESULTS_REAL, datehour)

    subprocess.call('ln -sf ' + env_vars.RESULTS_WPS + '/met_em* .', shell=True)

    if not env_vars.MPI_WRF:
        subprocess.call('./real.exe', shell=True)

    else:
        subprocess.call('sbatch real.srun', shell=True)

    while not tools.real_done(result_dir):
        print('real.exe is not done, sleep for a while...')
        time.sleep(30)

    print('real.exe is DONE!!!')
    subprocess.call('cp ' + os.path.join(result_dir, 'wrf* .'), shell=True)
    subprocess.call('cp namelist.input ' + result_dir, shell=True)


def run_wrf():

    yyyy = tools.pick_value('namelist.input', 'start_year')
    mm = tools.pick_value('namelist.input', 'start_month')
    dd = tools.pick_value('namelist.input', 'start_day')
    hh = tools.pick_value('namelist.input', 'start_hour')

    datehour = yyyy + mm + dd + hh

    yyyy = tools.pick_value('namelist.input', 'end_year')
    mm = tools.pick_value('namelist.input', 'end_month')
    dd = tools.pick_value('namelist.input', 'end_day')
    hh = tools.pick_value('namelist.input', 'end_hour')

    end_time = yyyy + '-' + mm + '-' + dd + '_' + hh + ':00:00'

    result_dir = os.path.join(env_vars.RESULTS_WRF, datehour)

    if not env_vars.MPI_WRF:
        subprocess.call('./wrf.exe', shell=True)

    else:
        subprocess.call('sbatch wrf.srun', shell=True)

    print(end_time)
    while not tools.wrf_done(result_dir, end_time):
        print('wrf.exe is not done, sleep for a while...')
        time.sleep(30)

    print('wrf.exe is DONE!!!')
    subprocess.call('cp ' + os.path.join(result_dir, 'wrfvar* .'), shell=True)
    subprocess.call('cp namelist.input ' + result_dir, shell=True)
