#!/usr/bin/env python3
import os
import subprocess
import re

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

    elif args.task == 'make_jobs':
        make_real_job()
        make_wrf_job()

    elif args.task == 'real':
        run_real()

    elif args.task == 'wrf':
        run_wrf()

def make_new_run():
    subprocess.call('cp ../run/* .', shell=True)
    subprocess.call('ln -sf ' + env_vars.WRF_ROOT+ '/main/*.exe .', shell=True)
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
    histroy_interval = re.sub(r'\[|\]', '', str(env_vars.HISTROY_INTERVAL))
    inputout_interval = str(env_vars.INPUTOUT_INTERVAL)
    inputout_begin_h = str(env_vars.INPUTOUT_BEGIN_H)
    inputout_end_h = str(env_vars.INPUTOUT_END_H)

    p_top_requested = str(env_vars.P_TOP_REQUESTED)

    namelist = open('namelist.input', 'w')
    #=================== configuration-s ===================
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
 history_interval                    = """ + histroy_interval + """,
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
 smooth_option                       = 0
 zap_close_levels                    = 1,
 p_top_requested                     = 1000,
 eta_levels                          = 1.0000,0.9508334,0.8582535,0.7765451,0.7044966,0.6410096,
                                       0.5850902,0.5358422,0.4924589,0.4542161,0.4204658,
                                       0.3906297,0.3641936,0.3407014,0.3197505,0.3009862,
                                       0.2840981,0.2688150,0.2549014,0.2421538,0.2303973,
                                       0.2194822,0.2092815,0.1996879,0.1906118,0.1819786,
                                       0.1737269,0.1658067,0.1581776,0.1508076,0.1436715,
                                       0.1367499,0.1300280,0.1234950,0.1171429,0.1109663,
                                       0.1049615,0.0991261,0.0934586,0.0879584,0.0826250,
                                       0.0774583,0.0724583,0.0676250,0.0629583,0.0584584,
                                       0.0541250,0.0499583,0.0459583,0.0421250,0.0384583,
                                       0.0349583,0.0316250,0.0284583,0.0254583,0.0226250,
                                       0.0199583,0.0174583,0.0151250,0.0129583,0.0109583,
                                       0.0091250,0.0074583,0.0059583,0.0046250,0.0034583,
                                       0.0024583,0.0016250,0.0009583,0.0004583,0.0001250,0.00000
 /

 &physics
 mp_physics                          = 6,     3,     3,
 ra_lw_physics                       = 4,     1,     1,
 ra_sw_physics                       = 4,     1,     1,
 radt                                = 16,    30,    30,
 sf_sfclay_physics                   = 1,     1,     1,
 sf_surface_physics                  = 2,     2,     2,
 bl_pbl_physics                      = 1,     1,     1,
 bldt                                = 0,     0,     0,
 cu_physics                          = 1,     1,     0,
 cudt                                = 0,     5,     5,
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
    #=================== configuration-e ===================
    namelist.close()

def make_real_job():

    yyyy = tools.pick_value('namelist.input', 'start_year').zfill(4)
    mm = tools.pick_value('namelist.input', 'start_month').zfill(2)
    dd = tools.pick_value('namelist.input', 'start_day').zfill(2)
    hh = tools.pick_value('namelist.input', 'start_hour').zfill(2)

    datehour = yyyy + mm + dd + hh

    result_dir = os.path.join(env_vars.RESULTS_REAL, datehour)

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

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
RESULTS=""" + result_dir + """
EXECUTABLE=./real.exe

# Set up for MPI
export MPD_CON_EXT="sge_$JOB_ID.$SGE_TASK_ID"

# Load modules
module load bundle/basic-1
module load jobvars

WORK_DIR=/scratch4/fzhu/real/
# Do our work in our scheduler-assigned temporary directory
cd $WORK_DIR
# Copy your input to your $TMPDIR
rsync -a $INPUT/* $WORK_DIR
#mpiexec
mpiexec -machinefile $TMPDIR/machines -n $NSLOTS $EXECUTABLE
# Copy your results to a directory in /data/$USER
rsync -a ./wrfinput* $RESULTS
rsync -a ./wrfbdy* $RESULTS

#rm -rf ./*

exit 0""")
    #=================== configuration-e ===================
    job.close()

def make_wrf_job():

    yyyy = tools.pick_value('namelist.input', 'start_year').zfill(4)
    mm = tools.pick_value('namelist.input', 'start_month').zfill(2)
    dd = tools.pick_value('namelist.input', 'start_day').zfill(2)
    hh = tools.pick_value('namelist.input', 'start_hour').zfill(2)

    datehour = yyyy + mm + dd + hh

    result_dir = os.path.join(env_vars.RESULTS_WRF, datehour)

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

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
RESULTS=""" + result_dir + """
EXECUTABLE=./wrf.exe

# Set up for MPI
export MPD_CON_EXT="sge_$JOB_ID.$SGE_TASK_ID"

# Load modules
module load bundle/basic-1
module load jobvars

WORK_DIR=/scratch4/fzhu/wrf
# Do our work in our scheduler-assigned temporary directory
cd $WORK_DIR
# Copy your input to your $TMPDIR
rsync -a $INPUT/* $WORK_DIR
#mpiexec
mpiexec -machinefile $TMPDIR/machines -n $NSLOTS $EXECUTABLE
# Copy your results to a directory in /data/$USER
rsync -a ./wrfout* $RESULTS
rsync -a ./wrfvar* $RESULTS

#rm -rf ./*

exit 0""")
    #=================== configuration-e ===================
    job.close()

def run_real():

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

    subprocess.call('cp ' + os.path.join(env_vars.RESULTS_REAL, datehour, 'wrf* .'), shell=True)

def run_wrf():

    if env_vars.MPI_WRF == False:
        subprocess.call('./wrf.exe', shell=True)

    else:
        subprocess.call('qsub -sync y wrf.job', shell=True)

    yyyy = tools.pick_value('namelist.input', 'start_year')
    mm = tools.pick_value('namelist.input', 'start_month')
    dd = tools.pick_value('namelist.input', 'start_day')
    hh = tools.pick_value('namelist.input', 'start_hour')

    datehour = yyyy + mm + dd + hh

    subprocess.call('cp ' + os.path.join(env_vars.RESULTS_WRF, datehour, 'wrf* .'), shell=True)
