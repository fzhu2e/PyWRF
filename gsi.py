#!/usr/bin/env python3
import os
import subprocess
import datetime
import re

import env_vars

def run(args):
    print('Start running GSI...')
    print('Task:', args.task)

    env_vars.WORK_ROOT = os.path.join(env_vars.GSI_ROOT, env_vars.RUN_NAME)
    print('WORK_ROOT:', env_vars.WORK_ROOT)

    os.chdir(env_vars.GSI_ROOT)

    if not os.path.exists(env_vars.WORK_ROOT):
        os.mkdir(env_vars.WORK_ROOT)

    os.chdir(env_vars.WORK_ROOT)

    if args.task == 'make_new_run':
        make_new_run()

    elif args.task == 'make_script':
        make_script(args)

    elif args.task == 'gsi':
        run_gsi()

def make_new_run():
    subprocess.call('cp -r ../run/* .', shell=True)

def make_namelist(args):
    yyyy_s = str(env_vars.START_TIME.year)
    mm_s = str(env_vars.START_TIME.month)
    dd_s = str(env_vars.START_TIME.day)
    hh_s = str(env_vars.START_TIME.hour)

    yyyy_e = str(env_vars.END_TIME.year)
    mm_e = str(env_vars.END_TIME.month)
    dd_e = str(env_vars.END_TIME.day)
    hh_e = str(env_vars.END_TIME.hour)

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

    namelist = open('namelist.input', 'w')
    #=================== configuration-s ===================
    namelist.write("""
    &time_control
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
    interval_seconds                    = 21600
    input_from_file                     = .true.,.true.,.true.,
    history_interval                    = 360,  60,   60,
    frames_per_outfile                  = 1, 1000, 1000,
    restart                             = .false.,
    restart_interval                    = 5000,
    io_form_history                     = 2
    io_form_restart                     = 2
    io_form_input                       = 2
    io_form_boundary                    = 2
    debug_level                         = 1000
    write_input             = .true.,
    inputout_interval       = 360,
    inputout_begin_h        = 6,
    inputout_end_h          = 6,
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
    p_top_requested                     = 1000,
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
    smooth_option                       = 0
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
    w_damping                           = 0,
    diff_opt                            = 1,
    km_opt                              = 4,
    diff_6th_opt                        = 0,      0,      0,
    diff_6th_factor                     = 0.12,   0.12,   0.12,
    base_temp                           = 290.
    damp_opt                            = 0,
    zdamp                               = 5000.,  5000.,  5000.,
    dampcoef                            = 0.2,    0.2,    0.2
    khdif                               = 0,      0,      0,
    kvdif                               = 0,      0,      0,
    non_hydrostatic                     = .true., .true., .true.,
    moist_adv_opt                       = 1,      1,      1,
    scalar_adv_opt                      = 1,      1,      1,
    /

    &bdy_control
    spec_bdy_width                      = 15,
    spec_zone                           = 1,
    relax_zone                          = 14,
    specified                           = .true., .false.,.false.,
    nested                              = .false., .true., .true.,
    /

    &grib2
    /

    &namelist_quilt
    nio_tasks_per_group = 0,
    nio_groups = 1,
    /
    """)
    #=================== configuration-e ===================

def make_real_job(args):
    job = open('real.job', 'w')
    #=================== configuration-s ===================
    job.write("""#!/usr/bin/env bash

# Set job name
#$ -N real_arw

# Merge stdout stderr
#$ -j y

# Set the number of processors
#$ -pe mpi2_mpd 48

# Set output directory
#$ -o $HOME/output

# Source /etc/csh.cshrc for basic environment and modules
source /etc/bashrc
# Set up input, output and executable variables
# These often differ per job
INPUT=""" + env_vars.WORK_ROOT + """
RESULTS=$INPUT/$JOB_NAME.$JOB_ID
EXECUTABLE=$INPUT/real.exe

# Set up for MPI
export MPD_CON_EXT="sge_$JOB_ID.$SGE_TASK_ID"

# Load modules
module load bundle/basic-1
module load jobvars

WORK_DIR=/scratch4/fzhu/real
# Do our work in our scheduler-assigned temporary directory
cd $WORK_DIR
# Copy your input to your $TMPDIR
rsync -aL $INPUT/* $WORK_DIR
#mpiexec
mpiexec -machinefile $TMPDIR/machines -n $NSLOTS $EXECUTABLE
# Copy your results to a directory in /data/$USER
rsync -a ./rsl* $RESULTS
rsync -a ./wrfinput* $RESULTS
rsync -a ./wrfbdy* $RESULTS

exit 0""")
    #=================== configuration-e ===================

def make_wrf_job(args):
    job = open('wrf.job', 'w')
    #=================== configuration-s ===================
    job.write("""#!/usr/bin/env bash

# Set job name
#$ -N wrf_arw

# Merge stdout stderr
#$ -j y

# Set the number of processors
#$ -pe mpi2_mpd 192

# Set output directory
#$ -o $HOME/output

# Source /etc/csh.cshrc for basic environment and modules
source /etc/bashrc
# Set up input, output and executable variables
# These often differ per job
INPUT=""" + env_vars.WORK_ROOT + """
RESULTS=$INPUT/$JOB_NAME.$JOB_ID
EXECUTABLE=$INPUT/wrf.exe

# Set up for MPI
export MPD_CON_EXT="sge_$JOB_ID.$SGE_TASK_ID"

# Load modules
module load bundle/basic-1
module load jobvars

WORK_DIR=/scratch4/fzhu/wrf
# Do our work in our scheduler-assigned temporary directory
cd $WORK_DIR
# Copy your input to your $TMPDIR
rsync -aL $INPUT/* $WORK_DIR
#mpiexec
mpiexec -machinefile $TMPDIR/machines -n $NSLOTS $EXECUTABLE
# Copy your results to a directory in /data/$USER
rsync -a ./rsl* $RESULTS
rsync -a ./wrfout* $RESULTS
rsync -a ./wrfvar* $RESULTS

exit 0""")
    #=================== configuration-e ===================

def run_real():

    wps_work = os.path.join(env_vars.WPS_ROOT, env_vars.RUN_NAME)
    subprocess.call('ln -sf ' + wps_work + '/met_em* .', shell=True)

    if env_vars.MPI_WRF == False:
        subprocess.call('./real.exe', shell=True)

    else:
        subprocess.call('qsub -sync y real.job', shell=True)

def run_wrf():

    subprocess.call('ln -sf ./real_arw.*/wrf* .', shell=True)

    if env_vars.MPI_WRF == False:
        subprocess.call('./wrf.exe', shell=True)

    else:
        subprocess.call('qsub -sync y wrf.job', shell=True)
