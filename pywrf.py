#!/usr/bin/env python3
#
#========================================================================================
# Author: Feng Zhu
# Date: 2014-08-30 15:58:11
#----------------------------------------------------------------------------------------
# Usage:
#
# - WPS
# ./pywrf.py wps -t make_namelist -s <start_time> -e <end_time> -r <running_hours>
# ./pywrf.py wps -t geogrid
# ./pywrf.py wps -t ungrib
# ./pywrf.py wps -t metgrid
#
# - WRF
# ./pywrf.py wrf -t make_namelist -s <start_time> -e <end_time> -r <running_hours>
# ./pywrf.py wrf -t real
# ./pywrf.py wrf -t wrf
#
# - WRFDA
# ./pywrf.py wrfda -t make_parame
# ./pywrf.py wrfda -t da_update_bc
#
# - GSI
# ./pywrf.py gsi -t make_script -a <ana_time> -w <da_windows>
# ./pywrf.py gsi -t gsi
#========================================================================================

import os, sys, time
import subprocess
import argparse

import settings
import wps, wrf, wrfda, gsi

#cmd1 = "ls"
#cmd2 = "ls -l"
#cmds = [cmd1, cmd2]

#for cmd in cmds:
    #subprocess.call(cmd, shell=True)

def main():
    parser = argparse.ArgumentParser(description='Run WRF in Python')

    parser.add_argument('-v', '--version',
            action='version',
            version='%(prog)s 0.01')

    subparsers = parser.add_subparsers(help='running mode')
    subparsers.required = True
    subparsers.dest = 'mode'

    parser_wps = subparsers.add_parser('wps', help='run WPS')
    parser_wrf = subparsers.add_parser('wrf', help='run WRF')
    parser_wrfda = subparsers.add_parser('wrfda', help='run WRFDA')
    parser_gsi = subparsers.add_parser('gsi', help='run GSI')

    #============================================
    # WPS
    #============================================
    parser_wps.add_argument('-t', '--task',
            required=True,
            choices=['make_namelist', 'geogrid', 'ungrib', 'metgrid'],
            help="running task")

    # below are just for make_namelist task
    parser_wps.add_argument('-s', '--start',
            help="start time")

    parser_wps.add_argument('-e', '--end',
            help="end time")

    parser_wps.add_argument('-r', '--run',
            help="running hours")

    #============================================
    # WRF
    #============================================
    parser_wrf.add_argument('-t', '--task',
            required=True,
            choices=['make_namelist', 'real', 'wrf'],
            help="running task")

    # below are just for make_namelist task
    parser_wrf.add_argument('-s', '--start',
            help="start time")

    parser_wrf.add_argument('-e', '--end',
            help="end time")

    parser_wrf.add_argument('-r', '--run',
            help="running hours")

    #============================================
    # WRFDA
    #============================================
    parser_wrfda.add_argument('-t', '--task',
            required=True,
            choices=['make_parame', 'da_update_bc'],
            help="running task")

    #============================================
    # GSI
    #============================================
    parser_gsi.add_argument('-t', '--task',
            required=True,
            choices=['make_script', 'gsi'],
            help="running task")

    # below are just for make_script task
    parser_gsi.add_argument('-a', '--ana',
            help="end time")

    parser_gsi.add_argument('-w', '--window',
            help="running hours")

    # parse the input command line
    args = parser.parse_args()

    print("==================================")
    print("Start running PyWRF...")
    print("----------------------------------")
    print("WPS_ROOT:", settings.WPS_ROOT)
    print("WRF_ROOT:", settings.WRF_ROOT)
    print("WRFDA_ROOT:", settings.WRFDA_ROOT)
    print("GSI_ROOT:", settings.GSI_ROOT)
    print("----------------------------------")
    print("Running mode:", args.mode)
    print("Running task:", args.task)
    print("==================================")

    if args.mode == 'wps':
        wps.run(args.task)

    elif args.mode == 'wrf':
        wrf.run(args.task)

    elif args.mode == 'wrfda':
        wrfda.run(args.task)

    elif args.mode == 'gsi':
        gsi.run(args.task)

if __name__ == "__main__":
    main()
