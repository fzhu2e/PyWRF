#!/usr/bin/env python3
import os
import subprocess
# import datetime
# import re
import time

import env_vars
import tools


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
        make_script()

    elif args.task == 'gsi':
        run_gsi()


def make_new_run():
    subprocess.call('cp -r ../run/* .', shell=True)


def make_script():
    yyyy = str(env_vars.ANA_TIME.year).zfill(4)
    mm = str(env_vars.ANA_TIME.month).zfill(2)
    dd = str(env_vars.ANA_TIME.day).zfill(2)
    hh = str(env_vars.ANA_TIME.hour).zfill(2)
    ww = str(env_vars.WINDOW.seconds/3600)

    ana_time = yyyy + mm + dd + hh
    window = ww

    date = yyyy + mm + dd

    datehour = ana_time
    result_dir = os.path.join(env_vars.RESULTS_GSI, datehour)

    ana_datetime = str(env_vars.ANA_TIME).replace(' ', '_')

    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

    print('COLD:', env_vars.COLD)
    if env_vars.COLD is True:
        bk_file = os.path.join(
            env_vars.WRF_ROOT,
            env_vars.RUN_NAME,
            'wrfinput_d01'
        )
    else:
        bk_file = os.path.join(
            env_vars.WRF_ROOT,
            env_vars.RUN_NAME,
            'wrfvar_input_d01_' + ana_datetime
        )

    if os.path.exists(bk_file):
        print(bk_file)
    else:
        raise NameError('BK_FILE not found!')

    user_name = os.environ['USER']

    run_script = open('run_gsi.sh', 'w')
    # =================== configuration-s ===================
    run_script.write("""#!/usr/bin/env bash
#====================================================================
#SBATCH --job-name=gsi_arw

#SBATCH --partition=s4
#SBATCH --export=ALL
#SBATCH --ntasks=""" + str(env_vars.GSI_PROC) + """
#SBATCH --mem-per-cpu=6000
#SBATCH --time=01:30:00
#SBATCH --output=/scratch/""" + user_name + """/tmp/gsi_arw-control.%j

source /etc/bashrc

module purge
module load license_intel intel/14.0-2
module load impi
module load hdf hdf5
module load netcdf4/4.1.3
#====================================================================

#####################################################
# case set up (users should change this part)
#####################################################
#
# ANAL_TIME= analysis time  (YYYYMMDDHH)
# WORK_ROOT= working directory, where GSI runs
# PREPBURF = path of PreBUFR conventional obs
# BK_FILE  = path and name of background file
# OBS_ROOT = path of observations files
# FIX_ROOT = path of fix files
# GSI_EXE  = path and name of the gsi executable
  BYTE_ORDER=Big_Endian
  #BYTE_ORDER=Little_Endian

  ANAL_TIME=""" + ana_time + """

  GSI_ROOT=""" + env_vars.GSI_ROOT + """

  WORK_ROOT=/scratch/""" + user_name + """/gsi/
  RESULTS=""" + result_dir + """

  OBS_ROOT=""" + env_vars.OBS_ROOT + """
  BK_FILE=""" + bk_file + """

  # WRF_NR
  #PREPBUFR=${OBS_ROOT}/prepbufr/prepbufr.gdas.""" + date + """.t""" + hh + """z.nr_block2
  #AMSUABUFR=${OBS_ROOT}/amsua/gdas.1bamua.t""" + hh + """z.""" + date + """.bufr_block
  #AIRSBUFR=${OBS_ROOT}/airs/gdas.airsev.t""" + hh + """z.""" + date + """.bufr_block
  #AIRSBUFR=${OBS_ROOT}/AIRS_LEO/""" + ana_time + """0000_geo_airs_bufr_clr
  #AIRSBUFR=${OBS_ROOT}/AIRS_GEO/""" + ana_time + """0000_geo_airs_bufr_clr
  #AIRSBUFR=${OBS_ROOT}/Hourly/WRFNR/GEO/""" + ana_time + """0000_geo_airs_bufr_clr

  # EC_NR
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/RAOB_prepbufr_doublenoise/""" + date + hh + """_prepbufr_doublenoise
  # AIRSBUFR=${OBS_ROOT}/Hourly/ECNR/GEO/""" + ana_time + """0000_geo_airs_bufr_clr
  # AIRSBUFR=${OBS_ROOT}/Hourly/ECNR/LEO/""" + ana_time + """0000_geo_airs_bufr_clr
  #AIRSBUFR=${OBS_ROOT}/Hourly/ECNR/LEO_Ocean/""" + ana_time + """0000_geo_airs_bufr_clr
  #AIRSBUFR=${OBS_ROOT}/Hourly/ECNR/GEO_Ocean/""" + ana_time + """0000_geo_airs_bufr_clr
  #AIRSBUFR=${OBS_ROOT}/Hourly/ECNR/GEO_New/""" + ana_time + """0000_geo_airs_bufr_clr

  # EC_NR with retrieval
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/3hourly/""" + date + hh + """_prepbufr_retrieval
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly/""" + date + hh + """_prepbufr_retrieval
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/3hourly_ocean/""" + date + hh + """_prepbufr_retrieval
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_ocean/""" + date + hh + """_prepbufr_retrieval
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/3hourly_obs/""" + date + hh + """_prepbufr_obs
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_obs/""" + date + hh + """_prepbufr_obs
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/3hourly_clr/""" + date + hh + """_prepbufr_retrieval_clr
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_clr/""" + date + hh + """_prepbufr_retrieval_clr
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/3hourly_err1/""" + date + hh + """_prepbufr_retrieval
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_err1/""" + date + hh + """_prepbufr_retrieval
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/3hourly_q95/""" + date + hh + """_prepbufr_rtvq95
  #PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_q95/""" + date + hh + """_prepbufr_rtvq95
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/hourly_44hr/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/hourly_44hr_err1/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_44hr/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_44hr_err1/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GOES/hourly_44hr/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GOES/hourly_44hr_err1/rtv_""" + date + hh + """.nr

  ### RAOB only
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/RAOB_prepbufr_doublenoise/""" + date + hh + """_prepbufr_doublenoise

  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/3hourly_44hr_obs_err0.1/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/3hourly_44hr_obs_err0.5/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/3hourly_44hr_obs_err1/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/3hourly_44hr_obs_err1.5/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_44hr_obs_err0.1/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_44hr_obs_err0.5/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_44hr_obs_err1/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/hourly_44hr_obs_err1.5/rtv_""" + date + hh + """.nr

  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err0.1/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err0.5/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err1/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err1.5/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err2/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err2.5/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err3/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err3.5/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err4/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err4.5/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/ALL/hourly_44hr_obs_err5/rtv_""" + date + hh + """.nr

  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/prepbufr_44hr_err0.1/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/prepbufr_44hr_err0.5/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/prepbufr_44hr_err1/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/prepbufr_44hr_err1.5/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/prepbufr_44hr_err2/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/prepbufr_44hr_err2.5/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/prepbufr_44hr_err3/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/prepbufr_44hr_err4/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO/prepbufr_44hr_err5/rtv_""" + date + hh + """.nr

  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/prepbufr_3hr_44hr_err0.1/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/prepbufr_3hr_44hr_err0.5/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/prepbufr_3hr_44hr_err1/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/prepbufr_3hr_44hr_err1.5/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/prepbufr_3hr_44hr_err2/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/prepbufr_3hr_44hr_err2.5/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/prepbufr_3hr_44hr_err3/""" + date + hh + """_prepbufr_retrieval
  PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/prepbufr_3hr_44hr_err4/""" + date + hh + """_prepbufr_retrieval
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/LEO/prepbufr_3hr_44hr_err5/""" + date + hh + """_prepbufr_retrieval

  ########## With UV
  ## GEO + RAOB + UV
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4/""" + date + hh + """_all
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4_raob_uv2/""" + date + hh + """_all
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4_raob_uv4/""" + date + hh + """_all

  ## RAOB + UV
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4_raob/rtv_""" + date + hh + """_uv.nr

  ## GEO + UV
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4_geo_tq_uv/""" + date + hh + """_geo_uv
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4_geo_tq_uv2/""" + date + hh + """_geo_uv
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4_geo_tq_uv4/""" + date + hh + """_geo_uv

  ## GEO only
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4_geo_only/rtv_""" + date + hh + """.nr

  ## UV only
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4_uv/rtv_""" + date + hh + """_uv.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4_uv2/rtv_""" + date + hh + """_uv.nr
  # PREPBUFR=${OBS_ROOT}/Hourly/ECNR/Retrieval/GEO_uv/hourly_44hr_err4_uv4/rtv_""" + date + hh + """_uv.nr

  ########## Vertical Thinning
  ## GEO + RAOB
  # PREPBUFR=${OBS_ROOT}/vertical_thinning_data/GEO/prepbufr_44hr_err4_6levels/rtv_""" + date + hh + """.nr

  ## LEO + RAOB
  # PREPBUFR=${OBS_ROOT}/vertical_thinning_data/LEO/prepbufr_3hr_44hr_err4_6levels/""" + date + hh + """_prebufr_retrieval

  ########## All NR data UVTQ
  # PREPBUFR=${OBS_ROOT}/NR_all_levels_obs/""" + date + hh + """_all_obs.nr
  # PREPBUFR=${OBS_ROOT}/NR_all_levels_obs_tq/rtv_""" + date + hh + """.nr
  # PREPBUFR=${OBS_ROOT}/NR_all_levels_obs_uv/rtv_""" + date + hh + """_uv.nr

# Static data
  CRTM_ROOT=""" + env_vars.CRTM_PATH + """
  FIX_ROOT=${GSI_ROOT}/fix
  GSI_EXE=${GSI_ROOT}/run/gsi.exe

#------------------------------------------------
# bk_core= which WRF core is used as background (NMM or ARW)
# bkcv_option= which background error covariance and parameter will be used
#              (GLOBAL or NAM)
# if_clean = clean  : delete temperal files in working directory (default)
#            no     : leave running directory as is (this is for debug only)
  bk_core=ARW
  bkcv_option=NAM
  #bkcv_option=GLOBAL
  if_clean=clean
#
#
##################################################################################

##################################################################################
# Check GSI needed environment variables are defined and exist
#

# Make sure ANAL_TIME is defined and in the correct format
if [ ! "${ANAL_TIME}" ]; then
  echo "ERROR: \$ANAL_TIME is not defined!"
  exit 1
fi

# Make sure WORK_ROOT is defined and exists
if [ ! "${WORK_ROOT}" ]; then
  echo "ERROR: \$WORK_ROOT is not defined!"
  exit 1
fi

# Make sure the background file exists
if [ ! -r "${BK_FILE}" ]; then
  echo "ERROR: ${BK_FILE} does not exist!"
  exit 1
fi

# Make sure OBS_ROOT is defined and exists
if [ ! "${OBS_ROOT}" ]; then
  echo "ERROR: \$OBS_ROOT is not defined!"
  exit 1
fi
if [ ! -d "${OBS_ROOT}" ]; then
  echo "ERROR: OBS_ROOT directory '${OBS_ROOT}' does not exist!"
  exit 1
fi

# Set the path to the GSI static files
if [ ! "${FIX_ROOT}" ]; then
  echo "ERROR: \$FIX_ROOT is not defined!"
  exit 1
fi
if [ ! -d "${FIX_ROOT}" ]; then
  echo "ERROR: fix directory '${FIX_ROOT}' does not exist!"
  exit 1
fi

# Set the path to the CRTM coefficients
if [ ! "${CRTM_ROOT}" ]; then
  echo "ERROR: \$CRTM_ROOT is not defined!"
  exit 1
fi
if [ ! -d "${CRTM_ROOT}" ]; then
  echo "ERROR: fix directory '${CRTM_ROOT}' does not exist!"
  exit 1
fi


# Make sure the GSI executable exists
if [ ! -x "${GSI_EXE}" ]; then
  echo "ERROR: ${GSI_EXE} does not exist!"
  exit 1
fi

#
##################################################################################
# Create the ram work directory and cd into it

workdir=${WORK_ROOT}
echo " Create working directory:" ${workdir}

if [ -d "${workdir}" ]; then
  rm -rf ${workdir}
fi
mkdir -p ${workdir}
cd ${workdir}

#
##################################################################################

echo " Copy GSI executable, background file, and link observation bufr to working directory"

# Save a copy of the GSI executable in the workdir
cp ${GSI_EXE} gsi.exe

# Bring over background field (it's modified by GSI so we can't link to it)
cp ${BK_FILE} ./wrf_inout


# Link to the prepbufr data
ln -s ${PREPBUFR} ./prepbufr

# Link to the radiance data
# ln -s ${OBS_ROOT}/gdas1.t12z.1bamua.tm00.bufr_d amsuabufr
# ln -s ${OBS_ROOT}/gdas1.t12z.1bamub.tm00.bufr_d amsubbufr
# ln -s ${OBS_ROOT}/gdas1.t12z.1bhrs3.tm00.bufr_d hirs3bufr
# ln -s ${OBS_ROOT}/gdas1.t12z.1bhrs4.tm00.bufr_d hirs4bufr
# ln -s ${OBS_ROOT}/gdas1.t12z.1bmhs.tm00.bufr_d mhsbufr
# ln -s ${OBS_ROOT}/gdas1.t12z.gpsro.tm00.bufr_d gpsrobufr
#
# Feng
# ln -s ${AIRSBUFR} ./airsbufr
##################################################################################

echo " Copy fixed files and link CRTM coefficient files to working directory"

# Set fixed files
#   berror   = forecast model background error statistics
#   specoef  = CRTM spectral coefficients
#   trncoef  = CRTM transmittance coefficients
#   emiscoef = CRTM coefficients for IR sea surface emissivity model
#   aerocoef = CRTM coefficients for aerosol effects
#   cldcoef  = CRTM coefficients for cloud effects
#   satinfo  = text file with information about assimilation of brightness temperatures
#   satangl  = angle dependent bias correction file (fixed in time)
#   pcpinfo  = text file with information about assimilation of prepcipitation rates
#   ozinfo   = text file with information about assimilation of ozone data
#   errtable = text file with obs error for conventional data (regional only)
#   convinfo = text file with information about assimilation of conventional data
#   bufrtable= text file ONLY needed for single obs test (oneobstest=.true.)
#   bftab_sst= bufr table for sst ONLY needed for sst retrieval (retrieval=.true.)

if [ ${bkcv_option} = GLOBAL ] ; then
  echo ' Use global background error covariance'
  BERROR=${FIX_ROOT}/${BYTE_ORDER}/nam_glb_berror.f77.gcv
  OBERROR=${FIX_ROOT}/prepobs_errtable.global
  if [ ${bk_core} = NMM ] ; then
     ANAVINFO=${FIX_ROOT}/anavinfo_ndas_netcdf_glbe
  else
    ANAVINFO=${FIX_ROOT}/anavinfo_arw_netcdf_glbe
  fi
else
  echo ' Use NAM background error covariance'
  # BERROR=${FIX_ROOT}/${BYTE_ORDER}/nam_nmmstat_na.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_1.5.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_1.4.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_1.3.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_1.2.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_1.1.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.9.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.8.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.7.gcv
  BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.6.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.5.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.4.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.3.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.2.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.1.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.07.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.05.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.03.gcv
  # BERROR=/home/fzhu/Scripts/BeReader/output/nam_nmmstat_na_0.01.gcv
  OBERROR=${FIX_ROOT}/nam_errtable.r3dv
  if [ ${bk_core} = NMM ] ; then
     ANAVINFO=${FIX_ROOT}/anavinfo_ndas_netcdf
  else
     ANAVINFO=${FIX_ROOT}/anavinfo_arw_netcdf
  fi
fi

# OBERROR=${FIX_ROOT}/feng_obserr_0.dat

SATANGL=${FIX_ROOT}/global_satangbias.txt
SATINFO=${FIX_ROOT}/global_satinfo.txt
# SATINFO=${FIX_ROOT}/global_satinfo_nobias.txt
# CONVINFO=${FIX_ROOT}/global_convinfo.txt
# CONVINFO=/home/fzhu/Scripts/vertical_thining/global_convinfo_vt50_Feng.txt
# CONVINFO=/home/fzhu/Scripts/vertical_thining/global_convinfo_vt75_Feng.txt
# CONVINFO=/home/fzhu/Scripts/vertical_thining/global_convinfo_vt100_Feng.txt
CONVINFO=/home/fzhu/Scripts/horizontal_thinning/global_convinfo_hz80_Feng.txt
# CONVINFO=/home/fzhu/Scripts/horizontal_thinning/global_convinfo_hz120_Feng.txt
# CONVINFO=/home/fzhu/Scripts/horizontal_thinning/global_convinfo_hz240_Feng.txt
OZINFO=${FIX_ROOT}/global_ozinfo.txt
PCPINFO=${FIX_ROOT}/global_pcpinfo.txt

#  copy Fixed fields to working directory
 cp $ANAVINFO anavinfo
 cp $BERROR   berror_stats
 cp $SATANGL  satbias_angle
 cp $SATINFO  satinfo
 cp $CONVINFO convinfo
 cp $OZINFO   ozinfo
 cp $PCPINFO  pcpinfo
 cp $OBERROR  errtable
#
#    # CRTM Spectral and Transmittance coefficients
CRTM_ROOT_ORDER=${CRTM_ROOT}/${BYTE_ORDER}
emiscoef_IRwater=${CRTM_ROOT_ORDER}/Nalli.IRwater.EmisCoeff.bin
emiscoef_IRice=${CRTM_ROOT_ORDER}/NPOESS.IRice.EmisCoeff.bin
emiscoef_IRland=${CRTM_ROOT_ORDER}/NPOESS.IRland.EmisCoeff.bin
emiscoef_IRsnow=${CRTM_ROOT_ORDER}/NPOESS.IRsnow.EmisCoeff.bin
emiscoef_VISice=${CRTM_ROOT_ORDER}/NPOESS.VISice.EmisCoeff.bin
emiscoef_VISland=${CRTM_ROOT_ORDER}/NPOESS.VISland.EmisCoeff.bin
emiscoef_VISsnow=${CRTM_ROOT_ORDER}/NPOESS.VISsnow.EmisCoeff.bin
emiscoef_VISwater=${CRTM_ROOT_ORDER}/NPOESS.VISwater.EmisCoeff.bin
emiscoef_MWwater=${CRTM_ROOT_ORDER}/FASTEM5.MWwater.EmisCoeff.bin
aercoef=${CRTM_ROOT_ORDER}/AerosolCoeff.bin
cldcoef=${CRTM_ROOT_ORDER}/CloudCoeff.bin

ln -s $emiscoef_IRwater ./Nalli.IRwater.EmisCoeff.bin
ln -s $emiscoef_IRice ./NPOESS.IRice.EmisCoeff.bin
ln -s $emiscoef_IRsnow ./NPOESS.IRsnow.EmisCoeff.bin
ln -s $emiscoef_IRland ./NPOESS.IRland.EmisCoeff.bin
ln -s $emiscoef_VISice ./NPOESS.VISice.EmisCoeff.bin
ln -s $emiscoef_VISland ./NPOESS.VISland.EmisCoeff.bin
ln -s $emiscoef_VISsnow ./NPOESS.VISsnow.EmisCoeff.bin
ln -s $emiscoef_VISwater ./NPOESS.VISwater.EmisCoeff.bin
ln -s $emiscoef_MWwater ./FASTEM5.MWwater.EmisCoeff.bin
ln -s $aercoef  ./AerosolCoeff.bin
ln -s $cldcoef  ./CloudCoeff.bin
# Copy CRTM coefficient files based on entries in satinfo file
for file in `awk '{if($1!~"!"){print $1}}' ./satinfo | sort | uniq` ;do
   ln -s ${CRTM_ROOT_ORDER}/${file}.SpcCoeff.bin ./
   ln -s ${CRTM_ROOT_ORDER}/${file}.TauCoeff.bin ./
done

# Only need this file for single obs test
 bufrtable=${FIX_ROOT}/prepobs_prep.bufrtable
 cp $bufrtable ./prepobs_prep.bufrtable

# for satellite bias correction
#cp ${FIX_ROOT}/sample.satbias ./satbias_in
cp ${FIX_ROOT}/satbias_cyc ./satbias_in
#cp ${FIX_ROOT}/ndas.t06z.satbias.tm03 ./satbias_in

#
##################################################################################
# Set some parameters for use by the GSI executable and to build the namelist
echo " Build the namelist "

if [ ${bkcv_option} = GLOBAL ] ; then
#   as_op='0.6,0.6,0.75,0.75,0.75,0.75,1.0,1.0'
   vs_op='0.7,'
   hzscl_op='1.7,0.8,0.5,'
else
#   as_op='1.0,1.0,0.5 ,0.7,0.7,0.5,1.0,1.0,'
   vs_op='1.0,'
   hzscl_op='0.373,0.746,1.50,'     # 00
   # hzscl_op='0.0025,0.005,0.01,'    # 01
   # hzscl_op='0.005,0.01,0.02,'     # 02
   # hzscl_op='0.01,0.02,0.04,'     # 03
   # hzscl_op='0.03,0.06,0.12,'     # 04
   # hzscl_op='0.05,0.1,0.2,'     # 05
   # hzscl_op='0.1,0.2,0.4,'     # 06
   # hzscl_op='0.15,0.3,0.6,'    # 07
   # hzscl_op='0.2,0.4,0.8,'     # 08
   # hzscl_op='0.3,0.6,1.2,'       # 09
   # hzscl_op='0.002,0.004,0.008,'    # 10
   # hzscl_op='0.001,0.002,0.004,'    # 11
   # hzscl_op='0.0005,0.001,0.002,'    # 12
fi

if [ ${bk_core} = NMM ] ; then
   bk_core_arw='.false.'
   bk_core_nmm='.true.'
else
   bk_core_arw='.true.'
   bk_core_nmm='.false.'
fi

# Build the GSI namelist on-the-fly
cat << EOF > gsiparm.anl
 &SETUP
   miter=2,niter(1)=100,niter(2)=100,
   write_diag(1)=.true.,write_diag(2)=.false.,write_diag(3)=.true.,
   gencode=78,qoption=2,
   factqmin=0.0,factqmax=0.0,
   ndat=87,iguess=-1,
   oneobtest=.false.,retrieval=.false.,
   nhr_assimilation=3,l_foto=.false.,
   use_pbl=.false.,
 /
 &GRIDOPTS
   JCAP=62,JCAP_B=62,NLAT=60,NLON=60,nsig=60,regional=.true.,
   wrf_nmm_regional=${bk_core_nmm},wrf_mass_regional=${bk_core_arw},
   diagnostic_reg=.false.,
   filled_grid=.false.,half_grid=.true.,netcdf=.true.,
 /
 &BKGERR
   vs=${vs_op}
   hzscl=${hzscl_op}
   bw=0.,fstat=.true.,
 /
 &ANBKGERR
 /
 &JCOPTS
 /
 &STRONGOPTS
 /
 &OBSQC
   dfact=0.75,dfact1=3.0,noiqc=.false.,c_varqc=0.02,vadfile='prepbufr',
   oberrflg=.true.,
 /
 &OBS_INPUT
   dmesh(1)=120.0,dmesh(2)=60.0,dmesh(3)=60.0,dmesh(4)=60.0,dmesh(5)=120,time_window_max=""" + window + """,
   dfile(01)='prepbufr',  dtype(01)='ps',        dplat(01)=' ',       dsis(01)='ps',                 dval(01)=1.0, dthin(01)=0, dsfcalc(01)=0,
   dfile(02)='prepbufr'   dtype(02)='t',         dplat(02)=' ',       dsis(02)='t',                  dval(02)=1.0, dthin(02)=0, dsfcalc(02)=0,
   dfile(03)='prepbufr',  dtype(03)='q',         dplat(03)=' ',       dsis(03)='q',                  dval(03)=1.0, dthin(03)=0, dsfcalc(03)=0,
   dfile(04)='prepbufr',  dtype(04)='pw',        dplat(04)=' ',       dsis(04)='pw',                 dval(04)=1.0, dthin(04)=0, dsfcalc(04)=0,
   dfile(05)='satwnd',    dtype(05)='uv',        dplat(05)=' ',       dsis(05)='uv',                 dval(05)=1.0, dthin(05)=0, dsfcalc(05)=0,
   dfile(06)='prepbufr',  dtype(06)='uv',        dplat(06)=' ',       dsis(06)='uv',                 dval(06)=1.0, dthin(06)=0, dsfcalc(06)=0,
   dfile(07)='prepbufr',  dtype(07)='spd',       dplat(07)=' ',       dsis(07)='spd',                dval(07)=1.0, dthin(07)=0, dsfcalc(07)=0,
   dfile(08)='prepbufr',  dtype(08)='dw',        dplat(08)=' ',       dsis(08)='dw',                 dval(08)=1.0, dthin(08)=0, dsfcalc(08)=0,
   dfile(09)='radarbufr', dtype(09)='rw',        dplat(09)=' ',       dsis(09)='rw',                 dval(09)=1.0, dthin(09)=0, dsfcalc(09)=0,
   dfile(10)='prepbufr',  dtype(10)='sst',       dplat(10)=' ',       dsis(10)='sst',                dval(10)=1.0, dthin(10)=0, dsfcalc(10)=0,
   dfile(11)='gpsrobufr', dtype(11)='gps_ref',   dplat(11)=' ',       dsis(11)='gps',                dval(11)=1.0, dthin(11)=0, dsfcalc(11)=0,
   dfile(12)='ssmirrbufr',dtype(12)='pcp_ssmi',  dplat(12)='dmsp',    dsis(12)='pcp_ssmi',           dval(12)=1.0, dthin(12)=-1,dsfcalc(12)=0,
   dfile(13)='tmirrbufr', dtype(13)='pcp_tmi',   dplat(13)='trmm',    dsis(13)='pcp_tmi',            dval(13)=1.0, dthin(13)=-1,dsfcalc(13)=0,
   dfile(14)='sbuvbufr',  dtype(14)='sbuv2',     dplat(14)='n16',     dsis(14)='sbuv8_n16',          dval(14)=1.0, dthin(14)=0, dsfcalc(14)=0,
   dfile(15)='sbuvbufr',  dtype(15)='sbuv2',     dplat(15)='n17',     dsis(15)='sbuv8_n17',          dval(15)=1.0, dthin(15)=0, dsfcalc(15)=0,
   dfile(16)='sbuvbufr',  dtype(16)='sbuv2',     dplat(16)='n18',     dsis(16)='sbuv8_n18',          dval(16)=1.0, dthin(16)=0, dsfcalc(16)=0,
   dfile(17)='hirs2bufr', dtype(17)='hirs2',     dplat(17)='n14',     dsis(17)='hirs2_n14',          dval(17)=6.0, dthin(17)=1, dsfcalc(17)=1,
   dfile(18)='hirs3bufr', dtype(18)='hirs3',     dplat(18)='n16',     dsis(18)='hirs3_n16',          dval(18)=0.0, dthin(18)=1, dsfcalc(18)=1,
   dfile(19)='hirs3bufr', dtype(19)='hirs3',     dplat(19)='n17',     dsis(19)='hirs3_n17',          dval(19)=6.0, dthin(19)=1, dsfcalc(19)=1,
   dfile(20)='hirs4bufr', dtype(20)='hirs4',     dplat(20)='n18',     dsis(20)='hirs4_n18',          dval(20)=0.0, dthin(20)=1, dsfcalc(20)=1,
   dfile(21)='hirs4bufr', dtype(21)='hirs4',     dplat(21)='metop-a', dsis(21)='hirs4_metop-a',      dval(21)=6.0, dthin(21)=1, dsfcalc(21)=1,
   dfile(22)='gsndrbufr', dtype(22)='sndr',      dplat(22)='g11',     dsis(22)='sndr_g11',           dval(22)=0.0, dthin(22)=1, dsfcalc(22)=0,
   dfile(23)='gsndrbufr', dtype(23)='sndr',      dplat(23)='g12',     dsis(23)='sndr_g12',           dval(23)=0.0, dthin(23)=1, dsfcalc(23)=0,
   dfile(24)='gimgrbufr', dtype(24)='goes_img',  dplat(24)='g11',     dsis(24)='imgr_g11',           dval(24)=0.0, dthin(24)=1, dsfcalc(24)=0,
   dfile(25)='gimgrbufr', dtype(25)='goes_img',  dplat(25)='g12',     dsis(25)='imgr_g12',           dval(25)=0.0, dthin(25)=1, dsfcalc(25)=0,
   dfile(26)='airsbufr',  dtype(26)='airs',      dplat(26)='aqua',    dsis(26)='airs281SUBSET_aqua', dval(26)=20.0,dthin(26)=2, dsfcalc(26)=2,
   dfile(27)='msubufr',   dtype(27)='msu',       dplat(27)='n14',     dsis(27)='msu_n14',            dval(27)=2.0, dthin(27)=2, dsfcalc(27)=1,
   dfile(28)='amsuabufr', dtype(28)='amsua',     dplat(28)='n15',     dsis(28)='amsua_n15',          dval(28)=10.0,dthin(28)=2, dsfcalc(28)=1,
   dfile(29)='amsuabufr', dtype(29)='amsua',     dplat(29)='n16',     dsis(29)='amsua_n16',          dval(29)=0.0, dthin(29)=2, dsfcalc(29)=1,
   dfile(30)='amsuabufr', dtype(30)='amsua',     dplat(30)='n17',     dsis(30)='amsua_n17',          dval(30)=0.0, dthin(30)=2, dsfcalc(30)=1,
   dfile(31)='amsuabufr', dtype(31)='amsua',     dplat(31)='n18',     dsis(31)='amsua_n18',          dval(31)=10.0,dthin(31)=2, dsfcalc(31)=1,
   dfile(32)='amsuabufr', dtype(32)='amsua',     dplat(32)='metop-a', dsis(32)='amsua_metop-a',      dval(32)=10.0,dthin(32)=2, dsfcalc(32)=1,
   dfile(33)='airsbufr',  dtype(33)='amsua',     dplat(33)='aqua',    dsis(33)='amsua_aqua',         dval(33)=5.0, dthin(33)=2, dsfcalc(33)=1,
   dfile(34)='amsubbufr', dtype(34)='amsub',     dplat(34)='n15',     dsis(34)='amsub_n15',          dval(34)=3.0, dthin(34)=3, dsfcalc(34)=1,
   dfile(35)='amsubbufr', dtype(35)='amsub',     dplat(35)='n16',     dsis(35)='amsub_n16',          dval(35)=3.0, dthin(35)=3, dsfcalc(35)=1,
   dfile(36)='amsubbufr', dtype(36)='amsub',     dplat(36)='n17',     dsis(36)='amsub_n17',          dval(36)=3.0, dthin(36)=3, dsfcalc(36)=1,
   dfile(37)='mhsbufr',   dtype(37)='mhs',       dplat(37)='n18',     dsis(37)='mhs_n18',            dval(37)=3.0, dthin(37)=3, dsfcalc(37)=1,
   dfile(38)='mhsbufr',   dtype(38)='mhs',       dplat(38)='metop-a', dsis(38)='mhs_metop-a',        dval(38)=3.0, dthin(38)=3, dsfcalc(38)=1,
   dfile(39)='ssmitbufr', dtype(39)='ssmi',      dplat(39)='f13',     dsis(39)='ssmi_f13',           dval(39)=0.0, dthin(39)=4, dsfcalc(39)=0,
   dfile(40)='ssmitbufr', dtype(40)='ssmi',      dplat(40)='f14',     dsis(40)='ssmi_f14',           dval(40)=0.0, dthin(40)=4, dsfcalc(40)=0,
   dfile(41)='ssmitbufr', dtype(41)='ssmi',      dplat(41)='f15',     dsis(41)='ssmi_f15',           dval(41)=0.0, dthin(41)=4, dsfcalc(41)=0,
   dfile(42)='amsrebufr', dtype(42)='amsre_low', dplat(42)='aqua',    dsis(42)='amsre_aqua',         dval(42)=0.0, dthin(42)=4, dsfcalc(42)=1,
   dfile(43)='amsrebufr', dtype(43)='amsre_mid', dplat(43)='aqua',    dsis(43)='amsre_aqua',         dval(43)=0.0, dthin(43)=4, dsfcalc(43)=1,
   dfile(44)='amsrebufr', dtype(44)='amsre_hig', dplat(44)='aqua',    dsis(44)='amsre_aqua',         dval(44)=0.0, dthin(44)=4, dsfcalc(44)=1,
   dfile(45)='ssmisbufr', dtype(45)='ssmis_las', dplat(45)='f16',     dsis(45)='ssmis_f16',          dval(45)=0.0, dthin(45)=1, dsfcalc(45)=0,
   dfile(46)='ssmisbufr', dtype(46)='ssmis_uas', dplat(46)='f16',     dsis(46)='ssmis_f16',          dval(46)=0.0, dthin(46)=1, dsfcalc(46)=0,
   dfile(47)='ssmisbufr', dtype(47)='ssmis_img', dplat(47)='f16',     dsis(47)='ssmis_f16',          dval(47)=0.0, dthin(47)=1, dsfcalc(47)=0,
   dfile(48)='ssmisbufr', dtype(48)='ssmis_env', dplat(48)='f16',     dsis(48)='ssmis_f16',          dval(48)=0.0, dthin(48)=1, dsfcalc(48)=0,
   dfile(49)='gsnd1bufr', dtype(49)='sndrd1',    dplat(49)='g12',     dsis(49)='sndrD1_g12',         dval(49)=1.5, dthin(49)=5, dsfcalc(49)=0,
   dfile(50)='gsnd1bufr', dtype(50)='sndrd2',    dplat(50)='g12',     dsis(50)='sndrD2_g12',         dval(50)=1.5, dthin(50)=5, dsfcalc(50)=0,
   dfile(51)='gsnd1bufr', dtype(51)='sndrd3',    dplat(51)='g12',     dsis(51)='sndrD3_g12',         dval(51)=1.5, dthin(51)=5, dsfcalc(51)=0,
   dfile(52)='gsnd1bufr', dtype(52)='sndrd4',    dplat(52)='g12',     dsis(52)='sndrD4_g12',         dval(52)=1.5, dthin(52)=5, dsfcalc(52)=0,
   dfile(53)='gsnd1bufr', dtype(53)='sndrd1',    dplat(53)='g11',     dsis(53)='sndrD1_g11',         dval(53)=1.5, dthin(53)=5, dsfcalc(53)=0,
   dfile(54)='gsnd1bufr', dtype(54)='sndrd2',    dplat(54)='g11',     dsis(54)='sndrD2_g11',         dval(54)=1.5, dthin(54)=5, dsfcalc(54)=0,
   dfile(55)='gsnd1bufr', dtype(55)='sndrd3',    dplat(55)='g11',     dsis(55)='sndrD3_g11',         dval(55)=1.5, dthin(55)=5, dsfcalc(55)=0,
   dfile(56)='gsnd1bufr', dtype(56)='sndrd4',    dplat(56)='g11',     dsis(56)='sndrD4_g11',         dval(56)=1.5, dthin(56)=5, dsfcalc(56)=0,
   dfile(57)='gsnd1bufr', dtype(57)='sndrd1',    dplat(57)='g13',     dsis(57)='sndrD1_g13',         dval(57)=1.5, dthin(57)=5, dsfcalc(57)=0,
   dfile(58)='gsnd1bufr', dtype(58)='sndrd2',    dplat(58)='g13',     dsis(58)='sndrD2_g13',         dval(58)=1.5, dthin(58)=5, dsfcalc(58)=0,
   dfile(59)='gsnd1bufr', dtype(59)='sndrd3',    dplat(59)='g13',     dsis(59)='sndrD3_g13',         dval(59)=1.5, dthin(59)=5, dsfcalc(59)=0,
   dfile(60)='gsnd1bufr', dtype(60)='sndrd4',    dplat(60)='g13',     dsis(60)='sndrD4_g13',         dval(60)=1.5, dthin(60)=5, dsfcalc(60)=0,
   dfile(61)='iasibufr',  dtype(61)='iasi',      dplat(61)='metop-a', dsis(61)='iasi616_metop-a',    dval(61)=20.0,dthin(61)=1, dsfcalc(61)=1,
   dfile(62)='gomebufr',  dtype(62)='gome',      dplat(62)='metop-a', dsis(62)='gome_metop-a',       dval(62)=1.0, dthin(62)=6, dsfcalc(62)=0,
   dfile(63)='omibufr',   dtype(63)='omi',       dplat(63)='aura',    dsis(63)='omi_aura',           dval(63)=1.0, dthin(63)=6, dsfcalc(63)=0,
   dfile(64)='sbuvbufr',  dtype(64)='sbuv2',     dplat(64)='n19',     dsis(64)='sbuv8_n19',          dval(64)=1.0, dthin(64)=0, dsfcalc(64)=0,
   dfile(65)='hirs4bufr', dtype(65)='hirs4',     dplat(65)='n19',     dsis(65)='hirs4_n19',          dval(65)=6.0, dthin(65)=1, dsfcalc(65)=1,
   dfile(66)='amsuabufr', dtype(66)='amsua',     dplat(66)='n19',     dsis(66)='amsua_n19',          dval(66)=10.0,dthin(66)=2, dsfcalc(66)=1,
   dfile(67)='mhsbufr',   dtype(67)='mhs',       dplat(67)='n19',     dsis(67)='mhs_n19',            dval(67)=3.0, dthin(67)=3, dsfcalc(67)=1,
   dfile(68)='tcvitl'     dtype(68)='tcp',       dplat(68)=' ',       dsis(68)='tcp',                dval(68)=1.0, dthin(68)=0, dsfcalc(68)=0,
   dfile(69)='mlsbufr',   dtype(69)='mls',       dplat(69)='aura',    dsis(69)='mls_aura',           dval(69)=1.0, dthin(69)=0, dsfcalc(69)=0,
   dfile(70)='seviribufr',dtype(70)='seviri',    dplat(70)='m08',     dsis(70)='seviri_m08',         dval(70)=0.0, dthin(70)=1, dsfcalc(70)=0,
   dfile(71)='seviribufr',dtype(71)='seviri',    dplat(71)='m09',     dsis(71)='seviri_m09',         dval(71)=0.0, dthin(71)=1, dsfcalc(71)=0,
   dfile(72)='seviribufr',dtype(72)='seviri',    dplat(72)='m10',     dsis(72)='seviri_m10',         dval(72)=0.0, dthin(72)=1, dsfcalc(72)=0,
   dfile(73)='hirs4bufr', dtype(73)='hirs4',     dplat(73)='metop-b', dsis(73)='hirs4_metop-b',      dval(73)=0.0, dthin(73)=1, dsfcalc(73)=0,
   dfile(74)='amsuabufr', dtype(74)='amsua',     dplat(74)='metop-b', dsis(74)='amsua_metop-b',      dval(74)=0.0, dthin(74)=1, dsfcalc(74)=0,
   dfile(75)='mhsbufr',   dtype(75)='mhs',       dplat(75)='metop-b', dsis(75)='mhs_metop-b',        dval(75)=0.0, dthin(75)=1, dsfcalc(75)=0,
   dfile(76)='iasibufr',  dtype(76)='iasi',      dplat(76)='metop-b', dsis(76)='iasi616_metop-b',    dval(76)=0.0, dthin(76)=1, dsfcalc(76)=0,
   dfile(77)='gomebufr',  dtype(77)='gome',      dplat(77)='metop-b', dsis(77)='gome_metop-b',       dval(77)=0.0, dthin(77)=2, dsfcalc(77)=0,
   dfile(78)='atmsbufr',  dtype(78)='atms',      dplat(78)='npp',     dsis(78)='atms_npp',           dval(78)=0.0, dthin(78)=1, dsfcalc(78)=0,
   dfile(79)='crisbufr',  dtype(79)='cris',      dplat(79)='npp',     dsis(79)='cris_npp',           dval(79)=0.0, dthin(79)=1, dsfcalc(79)=0,
   dfile(80)='gsnd1bufr', dtype(80)='sndrd1',    dplat(80)='g14',     dsis(80)='sndrD1_g14',         dval(80)=0.0, dthin(80)=1, dsfcalc(80)=0,
   dfile(81)='gsnd1bufr', dtype(81)='sndrd2',    dplat(81)='g14',     dsis(81)='sndrD2_g14',         dval(81)=0.0, dthin(81)=1, dsfcalc(81)=0,
   dfile(82)='gsnd1bufr', dtype(82)='sndrd3',    dplat(82)='g14',     dsis(82)='sndrD3_g14',         dval(82)=0.0, dthin(82)=1, dsfcalc(82)=0,
   dfile(83)='gsnd1bufr', dtype(83)='sndrd4',    dplat(83)='g14',     dsis(83)='sndrD4_g14',         dval(83)=0.0, dthin(83)=1, dsfcalc(83)=0,
   dfile(84)='gsnd1bufr', dtype(84)='sndrd1',    dplat(84)='g15',     dsis(84)='sndrD1_g15',         dval(84)=0.0, dthin(84)=1, dsfcalc(84)=0,
   dfile(85)='gsnd1bufr', dtype(85)='sndrd2',    dplat(85)='g15',     dsis(85)='sndrD2_g15',         dval(85)=0.0, dthin(85)=1, dsfcalc(85)=0,
   dfile(86)='gsnd1bufr', dtype(86)='sndrd3',    dplat(86)='g15',     dsis(86)='sndrD3_g15',         dval(86)=0.0, dthin(86)=1, dsfcalc(86)=0,
   dfile(87)='gsnd1bufr', dtype(87)='sndrd4',    dplat(87)='g15',     dsis(87)='sndrD4_g15',         dval(87)=0.0, dthin(87)=1, dsfcalc(87)=0,
 /
 &SUPEROB_RADAR
   del_azimuth=5.,del_elev=.25,del_range=5000.,del_time=.5,elev_angle_max=5.,minnum=50,range_max=100000.,
   l2superob_only=.false.,
 /
 &LAG_DATA
 /
 &HYBRID_ENSEMBLE
   l_hyb_ens=.false.,
 /
 &RAPIDREFRESH_CLDSURF
 /
 &CHEM
 /
 &SINGLEOB_TEST
   maginnov=1.0,magoberr=0.8,oneob_type='t',
   oblat=38.,oblon=279.,obpres=500.,obdattim=${ANAL_TIME},
   obhourset=0.,
 /

EOF

#
###################################################
#  run  GSI
###################################################
echo ' Run GSI with' ${bk_core} 'background'

srun --cpu_bind=core --distribution=block:block ./gsi.exe < gsiparm.anl >> stdout 2>&1
##################################################################
#  run time error check
##################################################################
error=$?

if [ ${error} -ne 0 ]; then
  echo "ERROR: ${GSI} crashed  Exit status=${error}"
  exit ${error}
fi
#
##################################################################
#
#   GSI updating satbias_in
# Bias correction by Feng
cp ./satbias_out ${FIX_ROOT}/satbias_cyc
#
# GSI updating satbias_in (only for cycling assimilation)

# Copy the output to more understandable names
ln -s stdout      stdout.anl.${ANAL_TIME}
ln -s wrf_inout   wrfanl.${ANAL_TIME}
ln -s fort.201    fit_p1.${ANAL_TIME}
ln -s fort.202    fit_w1.${ANAL_TIME}
ln -s fort.203    fit_t1.${ANAL_TIME}
ln -s fort.204    fit_q1.${ANAL_TIME}
ln -s fort.207    fit_rad1.${ANAL_TIME}

# Loop over first and last outer loops to generate innovation
# diagnostic files for indicated observation types (groups)
#
# NOTE:  Since we set miter=2 in GSI namelist SETUP, outer
#        loop 03 will contain innovations with respect to
#        the analysis.  Creation of o-a innovation files
#        is triggered by write_diag(3)=.true.  The setting
#        write_diag(1)=.true. turns on creation of o-g
#        innovation files.
#

loops="01 03"
for loop in $loops; do

case $loop in
  01) string=ges;;
  03) string=anl;;
   *) string=$loop;;
esac

#  Collect diagnostic files for obs types (groups) below
   listall="conv amsua_metop-a mhs_metop-a hirs4_metop-a hirs2_n14 msu_n14 \
          sndr_g08 sndr_g10 sndr_g12 sndr_g08_prep sndr_g10_prep sndr_g12_prep \
          sndrd1_g08 sndrd2_g08 sndrd3_g08 sndrd4_g08 sndrd1_g10 sndrd2_g10 \
          sndrd3_g10 sndrd4_g10 sndrd1_g12 sndrd2_g12 sndrd3_g12 sndrd4_g12 \
          hirs3_n15 hirs3_n16 hirs3_n17 amsua_n15 amsua_n16 amsua_n17 \
          amsub_n15 amsub_n16 amsub_n17 hsb_aqua airs_aqua amsua_aqua \
          goes_img_g08 goes_img_g10 goes_img_g11 goes_img_g12 \
          pcp_ssmi_dmsp pcp_tmi_trmm sbuv2_n16 sbuv2_n17 sbuv2_n18 \
          omi_aura ssmi_f13 ssmi_f14 ssmi_f15 hirs4_n18 amsua_n18 mhs_n18 \
          amsre_low_aqua amsre_mid_aqua amsre_hig_aqua ssmis_las_f16 \
          ssmis_uas_f16 ssmis_img_f16 ssmis_env_f16"
   for type in $listall; do
      #count=0
      #if [[ -f pe0000.${type}_${loop} ]]; then
         count=`ls pe*${type}_${loop}* | wc -l`
      #fi
      if [[ $count -gt 0 ]]; then
         cat pe*${type}_${loop}* > diag_${type}_${string}.${ANAL_TIME}
      fi
   done
done

#  Clean working directory to save only important files
ls -l * > list_run_directory
if [ ${if_clean} = clean ]; then
  echo ' Clean working directory after GSI run'
  rm -f *Coeff.bin     # all CRTM coefficient files
  rm -f pe0*           # diag files on each processor
  rm -f obs_input.*    # observation middle files
  rm -f siganl sigf03  # background middle files
  rm -f fsize_*        # delete temperal file for bufr size
fi

#==============================
# Feng Zhu
#==============================
#rsync -a $WORK_ROOT/* $RESULTS
cp $WORK_ROOT/* $RESULTS

#rm -rf $WORK_ROOT/*
#==============================

exit 0""")
    # =================== configuration-e ===================
    run_script.close()


def run_gsi():

    datehour = tools.pick_value('run_gsi.sh', 'ANAL_TIME')

    result_dir = os.path.join(env_vars.RESULTS_GSI, datehour)
    print(result_dir)

    if env_vars.MPI_GSI is False:
        # subprocess.call('qsub -sync y run_gsi_se.ksh', shell=True)
        print('NOT WORKING...')

    else:
        # subprocess.call('qsub -sync y run_gsi.ksh', shell=True)
        subprocess.call('sbatch run_gsi.sh', shell=True)

    while not tools.gsi_done(result_dir):
        print('gsi.exe is not done, sleep for a while...')
        time.sleep(30)

    user_name = os.environ['USER']
    work_dir = "/scratch/" + user_name + "/gsi/"
    subprocess.call('cp run_gsi.sh ' + work_dir, shell=True)

    subprocess.call('cp ' + os.path.join(result_dir, '* .'), shell=True)
    subprocess.call('cp run_gsi.sh ' + result_dir, shell=True)

    subprocess.call(
        'rm -f ' + os.path.join(
            env_vars.WRF_ROOT,
            env_vars.RUN_NAME,
            'wrfvar*'
        ),
        shell=True
    )
    subprocess.call(
        'rm -f ' + os.path.join(
            env_vars.WRF_ROOT,
            env_vars.RUN_NAME,
            'wrfinput_d01'
        ),
        shell=True
    )

    subprocess.call(
        'cp wrf_inout ' + os.path.join(
            env_vars.WRF_ROOT,
            env_vars.RUN_NAME,
            'wrfinput_d01'
        ),
        shell=True
    )
