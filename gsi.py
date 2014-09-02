#!/usr/bin/env python3
import os
import subprocess
import datetime
import re

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

    run_script = open('run_gsi.ksh', 'w')
    #=================== configuration-s ===================
    run_script.write("""#!/bin/ksh
#====================================================================
# qsub options make you not require them on the command line.
# submit commad: qsub "this script"

# which shell to use
#$ -S /bin/bash

# Set job name
#$ -N gsi_arw

# Merge stdout stderr
#$ -j y

# Set the number of processors
#$ -pe mpi2_mpd 48

# Set output directory
#$ -o $HOME/output

#====================================================================

# Source /etc/csh.cshrc for basic environment and modules
source /etc/ksh.kshrc

# Set up for MPI
export MPD_CON_EXT="sge_$JOB_ID.$SGE_TASK_ID"

# load modules
module load bundle/basic-1
module load udunits/1.12.11
module load szip/2.1

#####################################################
# machine set up (users should change this part)
#####################################################
#
#
# GSIPROC = processor number used for GSI analysis
#------------------------------------------------
  #GSIPROC=1
  #ARCH='LINUX_PGI'
  #ARCH='LINUX_Intel'
# Supported configurations:
            # IBM_LSF,,IBM_LoadLevel
            # LINUX_Intel, LINUX_Intel_LSF, LINUX_Intel_PBS,
            # LINUX_PGI, LINUX_PGI_LSF, LINUX_PGI_PBS,
            # DARWIN_PGI
#
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
  BYTE_ORDER=Little_Endian

  ANAL_TIME=""" + ana_time + """

  GSI_ROOT=""" + env_vars.GSI_ROOT + """
  WRF_ROOT=""" + env_vars.WRF_ROOT + """

  WORK_ROOT=/scratch4/fzhu/gsi/
  RESULTS=""" + result_dir + """

  OBS_ROOT=/data/fzhu/Data/ForOSSE/OSSE/
  BK_FILE=${WRF_ROOT}/""" + env_vars.RUN_NAME + """/wrfvar_input_d01_""" + ana_datetime + """
  PREPBUFR=${OBS_ROOT}/prepbufr/prepbufr.gdas.""" + date + """.t""" + hh + """z.nr_block2
  AMSUABUFR=${OBS_ROOT}/amsua/gdas.1bamua.t""" + hh + """z.""" + date + """.bufr_block
  #AIRSBUFR=${OBS_ROOT}/airs/gdas.airsev.t""" + hh + """z.""" + date + """.bufr_block
  AIRSBUFR=${OBS_ROOT}/AIRS_LEO/""" + ana_time + """0000_geo_airs_bufr_clr

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
  #bk_core=NMM
  bkcv_option=NAM
  if_clean=clean
#
#
#####################################################
# Users should NOT change script after this point
#####################################################
#
#case $ARCH in
   #'IBM_LSF')
      ####### IBM LSF (Load Sharing Facility)
      #BYTE_ORDER=Big_Endian
      #RUN_COMMAND="mpirun.lsf " ;;

   #'IBM_LoadLevel')
      ####### IBM LoadLeve
      #BYTE_ORDER=Big_Endian
      #RUN_COMMAND="poe " ;;

   #'LINUX_Intel')
      #BYTE_ORDER=Little_Endian
      #if [ $GSIPROC = 1 ]; then
         ##### Linux workstation - single processor
         #RUN_COMMAND=""
      #else
         ####### Linux workstation -  mpi run
        #RUN_COMMAND="mpirun -np ${GSIPROC} -machinefile ~/mach "
      #fi ;;

   #'LINUX_Intel_LSF')
      ####### LINUX LSF (Load Sharing Facility)
      #BYTE_ORDER=Little_Endian
      #RUN_COMMAND="mpirun.lsf " ;;

   #'LINUX_Intel_PBS')
      #BYTE_ORDER=Little_Endian
      ##### Linux cluster PBS (Portable Batch System)
      #RUN_COMMAND="mpirun -np ${GSIPROC} " ;;

   #'LINUX_PGI')
      #BYTE_ORDER=Little_Endian
      #if [ $GSIPROC = 1 ]; then
         ##### Linux workstation - single processor
         #RUN_COMMAND=""
      #else
         ####### Linux workstation -  mpi run
         #RUN_COMMAND="mpirun -np ${GSIPROC} -machinefile ~/mach "
      #fi ;;

   #'LINUX_PGI_LSF')
      ####### LINUX LSF (Load Sharing Facility)
      #BYTE_ORDER=Little_Endian
      #RUN_COMMAND="mpirun.lsf " ;;

   #'LINUX_PGI_PBS')
      #BYTE_ORDER=Little_Endian
      ####### Linux cluster PBS (Portable Batch System)
      #RUN_COMMAND="mpirun -np ${GSIPROC} " ;;

   #'DARWIN_PGI')
      #### Mac - mpi run
      #BYTE_ORDER=Little_Endian
      #if [ $GSIPROC = 1 ]; then
         ##### Mac workstation - single processor
         #RUN_COMMAND=""
      #else
         ####### Mac workstation -  mpi run
         #RUN_COMMAND="mpirun -np ${GSIPROC} -machinefile ~/mach "
      #fi ;;

   #* )
     #print "error: $ARCH is not a supported platform configuration."
     #exit 1 ;;
#esac


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

# Check to make sure the number of processors for running GSI was specified
#if [ -z "${GSIPROC}" ]; then
  #echo "ERROR: The variable $GSIPROC must be set to contain the number of processors to run GSI"
  #exit 1
#fi

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
# ln -s ${OBS_ROOT}/ndas.t12z.1bamua.tm12.bufr_d_le amsuabufr
# ln -s ${OBS_ROOT}/ndas.t12z.1bhrs4.tm12.bufr_d_le hirs4bufr
# ln -s ${OBS_ROOT}/ndas.t12z.1bmhs.tm12.bufr_d_le mhsbufr

# Feng Zhu
ln -s ${AMSUABUFR} ./amsuabufr
ln -s ${AIRSBUFR} ./airsbufr
#
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
  if [ ${BYTE_ORDER} = Little_Endian ] ; then
    BERROR=${FIX_ROOT}/nam_glb_berror.f77.gcv_Little_Endian
  else
    BERROR=${FIX_ROOT}/nam_glb_berror.f77.gcv
  fi
  OBERROR=${FIX_ROOT}/nam_errtable.r3dv
  ANAVINFO=${FIX_ROOT}/anavinfo_wrf_globalbe
else
  echo ' Use NAM background error covariance'
  if [ ${BYTE_ORDER} = Little_Endian ] ; then
    BERROR=${FIX_ROOT}/nam_nmmstat_na.gcv_Little_Endian
  else
    BERROR=${FIX_ROOT}/nam_nmmstat_na.gcv
  fi
  OBERROR=${FIX_ROOT}/nam_errtable.r3dv
  ANAVINFO=${FIX_ROOT}/anavinfo_wrf_nambe
fi

SATANGL=${FIX_ROOT}/global_satangbias.txt
SATINFO=${FIX_ROOT}/global_satinfo.txt
CONVINFO=${FIX_ROOT}/global_convinfo.txt
OZINFO=${FIX_ROOT}/global_ozinfo.txt
PCPINFO=${FIX_ROOT}/global_pcpinfo.txt

RTMFIX=${CRTM_ROOT}
RTMEMIS=${RTMFIX}/EmisCoeff/${BYTE_ORDER}/EmisCoeff.bin
RTMAERO=${RTMFIX}/AerosolCoeff/${BYTE_ORDER}/AerosolCoeff.bin
RTMCLDS=${RTMFIX}/CloudCoeff/${BYTE_ORDER}/CloudCoeff.bin

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
## CRTM Spectral and Transmittance coefficients
 ln -s $RTMEMIS  EmisCoeff.bin
 ln -s $RTMAERO  AerosolCoeff.bin
 ln -s $RTMCLDS  CloudCoeff.bin
 nsatsen=`cat satinfo | wc -l`
 isatsen=1
 while [[ $isatsen -le $nsatsen ]]; do
    flag=`head -n $isatsen satinfo | tail -1 | cut -c1-1`
    if [[ "$flag" != "!" ]]; then
       satsen=`head -n $isatsen satinfo | tail -1 | cut -f 2 -d" "`
       spccoeff=${satsen}.SpcCoeff.bin
       if  [[ ! -s $spccoeff ]]; then
          ln -s $RTMFIX/SpcCoeff/${BYTE_ORDER}/$spccoeff $spccoeff
          ln -s $RTMFIX/TauCoeff/${BYTE_ORDER}/${satsen}.TauCoeff.bin ${satsen}.TauCoeff.bin
       fi
    fi
    isatsen=` expr $isatsen + 1 `
 done

# Only need this file for single obs test
 bufrtable=${FIX_ROOT}/prepobs_prep.bufrtable
 cp $bufrtable ./prepobs_prep.bufrtable

# for satellite bias correction
cp ${FIX_ROOT}/ndas.t06z.satbias.tm03 ./satbias_in

#
##################################################################################
# Set some parameters for use by the GSI executable and to build the namelist
echo " Build the namelist "

export JCAP=62
export LEVS=60
export JCAP_B=62
export DELTIM=${DELTIM:-$((3600/($JCAP/20)))}

if [ ${bkcv_option} = GLOBAL ] ; then
   vs_op='0.7,'
   hzscl_op='1.7,0.8,0.5,'
else
   vs_op='1.0,'
   hzscl_op='0.373,0.746,1.50,'
fi

if [ ${bk_core} = NMM ] ; then
   bk_core_arw='.false.'
   bk_core_nmm='.true.'
else
   bk_core_arw='.true.'
   bk_core_nmm='.false.'
fi

# Build the GSI namelist on-the-fly
# Feng Zhu: pay attention to the value of "niter", the default is 10
cat << EOF > gsiparm.anl
 &SETUP
   miter=2,niter(1)=100,niter(2)=100,
   write_diag(1)=.true.,write_diag(2)=.false.,write_diag(3)=.true.,
   gencode=78,qoption=2,
   factqmin=0.0,factqmax=0.0,deltim=$DELTIM,
   ndat=67,iguess=-1,
   oneobtest=.false.,retrieval=.false.,
   nhr_assimilation=3,l_foto=.false.,
   use_pbl=.false.,use_compress=.false.,nsig_ext=13,gpstop=30.,
 /
 &GRIDOPTS
   JCAP=$JCAP,JCAP_B=$JCAP_B,NLAT=$NLAT,NLON=$LONA,nsig=$LEVS,hybrid=.true.,
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
   anisotropic=.false.,an_vs=1.0,ngauss=1,
   an_flen_u=-5.,an_flen_t=3.,an_flen_z=-200.,
   ifilt_ord=2,npass=3,normal=-200,grid_ratio=4.,nord_f2a=4,
 /
 &JCOPTS
 /
 &STRONGOPTS
   jcstrong=.false.,jcstrong_option=3,nstrong=0,nvmodes_keep=20,period_max=3.,
   baldiag_full=.true.,baldiag_inc=.true.,
 /
 &OBSQC
   dfact=0.75,dfact1=3.0,noiqc=.false.,c_varqc=0.02,vadfile='prepbufr',
 /
 &OBS_INPUT
   dmesh(1)=120.0,dmesh(2)=60.0,dmesh(3)=60.0,dmesh(4)=60.0,dmesh(5)=120,time_window_max=1.5,
   dfile(01)='prepbufr',  dtype(01)='ps',        dplat(01)=' ',         dsis(01)='ps',                  dval(01)=1.0,  dthin(01)=0,
   dfile(02)='prepbufr'   dtype(02)='t',         dplat(02)=' ',         dsis(02)='t',                   dval(02)=1.0,  dthin(02)=0,
   dfile(03)='prepbufr',  dtype(03)='q',         dplat(03)=' ',         dsis(03)='q',                   dval(03)=1.0,  dthin(03)=0,
   dfile(04)='prepbufr',  dtype(04)='uv',        dplat(04)=' ',         dsis(04)='uv',                  dval(04)=1.0,  dthin(04)=0,
   dfile(05)='prepbufr',  dtype(05)='spd',       dplat(05)=' ',         dsis(05)='spd',                 dval(05)=1.0,  dthin(05)=0,
   dfile(06)='radarbufr', dtype(06)='rw',        dplat(06)=' ',         dsis(06)='rw',                  dval(06)=1.0,  dthin(06)=0,
   dfile(07)='prepbufr',  dtype(07)='dw',        dplat(07)=' ',         dsis(07)='dw',                  dval(07)=1.0,  dthin(07)=0,
   dfile(08)='prepbufr',  dtype(08)='sst',       dplat(08)=' ',         dsis(08)='sst',                 dval(08)=1.0,  dthin(08)=0,
   dfile(09)='prepbufr',  dtype(09)='pw',        dplat(09)=' ',         dsis(09)='pw',                  dval(09)=1.0,  dthin(09)=0,
   dfile(10)='gpsrobufr', dtype(10)='gps_ref',   dplat(10)=' ',         dsis(10)='gps',                 dval(10)=1.0,  dthin(10)=0,
   dfile(11)='ssmirrbufr',dtype(11)='pcp_ssmi',  dplat(11)='dmsp',      dsis(11)='pcp_ssmi',            dval(11)=1.0,  dthin(11)=-1,
   dfile(12)='tmirrbufr', dtype(12)='pcp_tmi',   dplat(12)='trmm',      dsis(12)='pcp_tmi',             dval(12)=1.0,  dthin(12)=-1,
   dfile(13)='sbuvbufr',  dtype(13)='sbuv2',     dplat(13)='n16',       dsis(13)='sbuv8_n16',           dval(13)=1.0,  dthin(13)=0,
   dfile(14)='sbuvbufr',  dtype(14)='sbuv2',     dplat(14)='n17',       dsis(14)='sbuv8_n17',           dval(14)=1.0,  dthin(14)=0,
   dfile(15)='sbuvbufr',  dtype(15)='sbuv2',     dplat(15)='n18',       dsis(15)='sbuv8_n18',           dval(15)=1.0,  dthin(15)=0,
   dfile(16)='omibufr',   dtype(16)='omi',       dplat(16)='aura',      dsis(16)='omi_aura',            dval(16)=1.0,  dthin(16)=6,
   dfile(17)='hirs2bufr', dtype(17)='hirs2',     dplat(17)='n14',       dsis(17)='hirs2_n14',           dval(17)=6.0,  dthin(17)=1,
   dfile(18)='hirs3bufr', dtype(18)='hirs3',     dplat(18)='n16',       dsis(18)='hirs3_n16',           dval(18)=0.0,  dthin(18)=1,
   dfile(19)='hirs3bufr', dtype(19)='hirs3',     dplat(19)='n17',       dsis(19)='hirs3_n17',           dval(19)=6.0,  dthin(19)=1,
   dfile(20)='hirs4bufr', dtype(20)='hirs4',     dplat(20)='n18',       dsis(20)='hirs4_n18',           dval(20)=0.0,  dthin(20)=1,
   dfile(21)='hirs4bufr', dtype(21)='hirs4',     dplat(21)='metop-a',   dsis(21)='hirs4_metop-a',       dval(21)=6.0,  dthin(21)=1,
   dfile(22)='gsndrbufr', dtype(22)='sndr',      dplat(22)='g11',       dsis(22)='sndr_g11',            dval(22)=0.0,  dthin(22)=1,
   dfile(23)='gsndrbufr', dtype(23)='sndr',      dplat(23)='g12',       dsis(23)='sndr_g12',            dval(23)=0.0,  dthin(23)=1,
   dfile(24)='gimgrbufr', dtype(24)='goes_img',  dplat(24)='g11',       dsis(24)='imgr_g11',            dval(24)=0.0,  dthin(24)=1,
   dfile(25)='gimgrbufr', dtype(25)='goes_img',  dplat(25)='g12',       dsis(25)='imgr_g12',            dval(25)=0.0,  dthin(25)=1,
   dfile(26)='airsbufr',  dtype(26)='airs',      dplat(26)='aqua',      dsis(26)='airs281SUBSET_aqua',  dval(26)=20.0, dthin(26)=1,
   dfile(27)='msubufr',   dtype(27)='msu',       dplat(27)='n14',       dsis(27)='msu_n14',             dval(27)=2.0,  dthin(27)=2,
   dfile(28)='amsuabufr', dtype(28)='amsua',     dplat(28)='n15',       dsis(28)='amsua_n15',           dval(28)=10.0, dthin(28)=2,
   dfile(29)='amsuabufr', dtype(29)='amsua',     dplat(29)='n16',       dsis(29)='amsua_n16',           dval(29)=0.0,  dthin(29)=2,
   dfile(30)='amsuabufr', dtype(30)='amsua',     dplat(30)='n17',       dsis(30)='amsua_n17',           dval(30)=0.0,  dthin(30)=2,
   dfile(31)='amsuabufr', dtype(31)='amsua',     dplat(31)='n18',       dsis(31)='amsua_n18',           dval(31)=10.0, dthin(31)=2,
   dfile(32)='amsuabufr', dtype(32)='amsua',     dplat(32)='metop-a',   dsis(32)='amsua_metop-a',       dval(32)=10.0, dthin(32)=2,
   dfile(33)='airsbufr',  dtype(33)='amsua',     dplat(33)='aqua',      dsis(33)='amsua_aqua',          dval(33)=5.0,  dthin(33)=2,
   dfile(34)='amsubbufr', dtype(34)='amsub',     dplat(34)='n15',       dsis(34)='amsub_n15',           dval(34)=3.0,  dthin(34)=3,
   dfile(35)='amsubbufr', dtype(35)='amsub',     dplat(35)='n16',       dsis(35)='amsub_n16',           dval(35)=3.0,  dthin(35)=3,
   dfile(36)='amsubbufr', dtype(36)='amsub',     dplat(36)='n17',       dsis(36)='amsub_n17',           dval(36)=3.0,  dthin(36)=3,
   dfile(37)='mhsbufr',   dtype(37)='mhs',       dplat(37)='n18',       dsis(37)='mhs_n18',             dval(37)=3.0,  dthin(37)=3,
   dfile(38)='mhsbufr',   dtype(38)='mhs',       dplat(38)='metop-a',   dsis(38)='mhs_metop-a',         dval(38)=3.0,  dthin(38)=3,
   dfile(39)='ssmitbufr', dtype(39)='ssmi',      dplat(39)='f13',       dsis(39)='ssmi_f13',            dval(39)=0.0,  dthin(39)=4,
   dfile(40)='ssmitbufr', dtype(40)='ssmi',      dplat(40)='f14',       dsis(40)='ssmi_f14',            dval(40)=0.0,  dthin(40)=4,
   dfile(41)='ssmitbufr', dtype(41)='ssmi',      dplat(41)='f15',       dsis(41)='ssmi_f15',            dval(41)=0.0,  dthin(41)=4,
   dfile(42)='amsrebufr', dtype(42)='amsre_low', dplat(42)='aqua',      dsis(42)='amsre_aqua',          dval(42)=0.0,  dthin(42)=4,
   dfile(43)='amsrebufr', dtype(43)='amsre_mid', dplat(43)='aqua',      dsis(43)='amsre_aqua',          dval(43)=0.0,  dthin(43)=4,
   dfile(44)='amsrebufr', dtype(44)='amsre_hig', dplat(44)='aqua',      dsis(44)='amsre_aqua',          dval(44)=0.0,  dthin(44)=4,
   dfile(45)='ssmisbufr', dtype(45)='ssmis',     dplat(45)='f16',       dsis(45)='ssmis_f16',           dval(45)=0.0,  dthin(45)=4,
   dfile(46)='gsnd1bufr', dtype(46)='sndrd1',    dplat(46)='g12',       dsis(46)='sndrD1_g12',          dval(46)=1.5,  dthin(46)=5,
   dfile(47)='gsnd1bufr', dtype(47)='sndrd2',    dplat(47)='g12',       dsis(47)='sndrD2_g12',          dval(47)=1.5,  dthin(47)=5,
   dfile(48)='gsnd1bufr', dtype(48)='sndrd3',    dplat(48)='g12',       dsis(48)='sndrD3_g12',          dval(48)=1.5,  dthin(48)=5,
   dfile(49)='gsnd1bufr', dtype(49)='sndrd4',    dplat(49)='g12',       dsis(49)='sndrD4_g12',          dval(49)=1.5,  dthin(49)=5,
   dfile(50)='gsnd1bufr', dtype(50)='sndrd1',    dplat(50)='g11',       dsis(50)='sndrD1_g11',          dval(50)=1.5,  dthin(50)=5,
   dfile(51)='gsnd1bufr', dtype(51)='sndrd2',    dplat(51)='g11',       dsis(51)='sndrD2_g11',          dval(51)=1.5,  dthin(51)=5,
   dfile(52)='gsnd1bufr', dtype(52)='sndrd3',    dplat(52)='g11',       dsis(52)='sndrD3_g11',          dval(52)=1.5,  dthin(52)=5,
   dfile(53)='gsnd1bufr', dtype(53)='sndrd4',    dplat(53)='g11',       dsis(53)='sndrD4_g11',          dval(53)=1.5,  dthin(53)=5,
   dfile(54)='gsnd1bufr', dtype(54)='sndrd1',    dplat(54)='g13',       dsis(54)='sndrD1_g13',          dval(54)=1.5,  dthin(54)=5,
   dfile(55)='gsnd1bufr', dtype(55)='sndrd2',    dplat(55)='g13',       dsis(55)='sndrD2_g13',          dval(55)=1.5,  dthin(55)=5,
   dfile(56)='gsnd1bufr', dtype(56)='sndrd3',    dplat(56)='g13',       dsis(56)='sndrD3_g13',          dval(56)=1.5,  dthin(56)=5,
   dfile(57)='gsnd1bufr', dtype(57)='sndrd4',    dplat(57)='g13',       dsis(57)='sndrD4_g13',          dval(57)=1.5,  dthin(57)=5,
   dfile(58)='iasibufr',  dtype(58)='iasi',      dplat(58)='metop-a',   dsis(58)='iasi586_metop-a',     dval(58)=20.0, dthin(58)=1,
   dfile(59)='gomebufr',  dtype(59)='gome',      dplat(59)='metop-a',   dsis(59)='gome_metop-a',        dval(59)=1.0,  dthin(59)=6,
   dfile(60)='sbuvbufr',  dtype(60)='sbuv2',     dplat(60)='n19',       dsis(60)='sbuv8_n19',           dval(60)=1.0,  dthin(60)=0,
   dfile(61)='hirs4bufr', dtype(61)='hirs4',     dplat(61)='n19',       dsis(61)='hirs4_n19',           dval(61)=6.0,  dthin(61)=1,
   dfile(62)='amsuabufr', dtype(62)='amsua',     dplat(62)='n19',       dsis(62)='amsua_n19',           dval(62)=10.0, dthin(62)=2,
   dfile(63)='mhsbufr',   dtype(63)='mhs',       dplat(63)='n19',       dsis(63)='mhs_n19',             dval(63)=3.0,  dthin(63)=3,
   dfile(64)='tcvitl'     dtype(64)='tcp',       dplat(64)=' ',         dsis(64)='tcp',                 dval(64)=1.0,  dthin(64)=0,
   dfile(65)='modisbufr', dtype(65)='modis',     dplat(65)='aqua',      dsis(65)='modis_aqua',          dval(65)=1.0,  dthin(65)=6,
   dfile(66)='modisbufr', dtype(66)='modis',     dplat(66)='terra',     dsis(66)='modis_terra',         dval(66)=1.0,  dthin(66)=6,
   dfile(67)='mlsbufr',   dtype(67)='mls',       dplat(67)='aura',      dsis(67)='mls_aura',            dval(67)=1.0,  dthin(67)=0,
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
   l_cloud_analysis=.false.,
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

#case $ARCH in
   #'IBM_LSF'|'IBM_LoadLevel')
      #${RUN_COMMAND} ./gsi.exe < gsiparm.anl > stdout 2>&1  ;;

   #* )
      #${RUN_COMMAND} ./gsi.exe > stdout 2>&1  ;;
#esac

/opt/intel/impi/current/bin64/mpiexec -machinefile $TMPDIR/machines -n $NSLOTS ./gsi.exe < gsiparm.anl >> stdout 2>&1

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
#
# cp ./satbias_out ${FIX_ROOT}/ndas.t06z.satbias.tm03

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

ls -l pe0*.* > listpe
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
      count=`grep ${type}_${loop} listpe | wc -l`
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
  rm -f listpe         # list of diag files on each processor
  rm -f obs_input.*    # observation middle files
  rm -f siganl sigf03  # background middle files
  rm -f xhatsave.*     # some information on each processor
  rm -f fsize_*        # delete temperal file for bufr size
fi

#==============================
# Feng Zhu
#==============================
rsync -a $WORK_ROOT/* $RESULTS

rm -rf $WORK_ROOT/*
#==============================

exit 0""")
    #=================== configuration-e ===================
    run_script.close()

def run_gsi():

    if env_vars.MPI_GSI == False:
        subprocess.call('qsub -sync y run_gsi_se.ksh', shell=True)

    else:
        subprocess.call('qsub -sync y run_gsi.ksh', shell=True)

    datehour = tools.pick_value('run_gsi.ksh', 'ANAL_TIME')

    subprocess.call('ln -sf ' + os.path.join(env_vars.RESULTS_GSI, datehour, '*') + ' .', shell=True)
