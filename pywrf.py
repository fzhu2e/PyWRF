#!/usr/bin/env python3

# ==============================================================================
#  Author: Feng Zhu
#  Date: 2014-08-30 15:58:11
# ------------------------------------------------------------------------------
#  Usage:
#
#  - WPS
#  ./pywrf.py wps -t make_namelist \
#                 -s <start_time> -e <end_time> -r <running_hours>
#  ./pywrf.py wps -t geogrid
#  ./pywrf.py wps -t ungrib
#  ./pywrf.py wps -t metgrid
#
#  - WRF
#  ./pywrf.py wrf -t make_namelist \
#                 -s <start_time> -e <end_time> -r <running_hours>
#  ./pywrf.py wrf -t real
#  ./pywrf.py wrf -t wrf
#
#  - WRFDA
#  ./pywrf.py wrfda -t make_parame
#  ./pywrf.py wrfda -t da_update_bc
#
#  - GSI
#  ./pywrf.py gsi -t make_script -a <ana_time> -w <da_windows>
#  ./pywrf.py gsi -t gsi
# ==============================================================================

import argparse

import settings
import env_vars
import wps
import wrf
import wrfda
import gsi


def main():
    parser = argparse.ArgumentParser(description='Run WRF in Python')

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s 0.01'
    )

    subparsers = parser.add_subparsers(help='running mode')
    subparsers.required = True
    subparsers.dest = 'mode'

    parser_wps = subparsers.add_parser('wps', help='run WPS')
    parser_wrf = subparsers.add_parser('wrf', help='run WRF')
    parser_wrfda = subparsers.add_parser('wrfda', help='run WRFDA')
    parser_gsi = subparsers.add_parser('gsi', help='run GSI')

    # ============================================
    #  WPS
    # ============================================
    parser_wps.add_argument(
        '-t',
        '--task',
        required=True,
        choices=[
            'make_new_run',
            'make_namelist',
            'geogrid',
            'ungrib',
            'metgrid'
        ],
        help='running task'
    )

    parser_wps.add_argument(
        '-o',
        '--workdir',
        help='work directory'
    )

    # below are just for make_namelist task
    parser_wps.add_argument(
        '-s',
        '--start',
        help='start time'
    )

    wps_run_length = parser_wps.add_mutually_exclusive_group()

    wps_run_length.add_argument(
        '-e',
        '--end',
        help='end time'
    )

    wps_run_length.add_argument(
        '-r',
        '--run',
        help='running hours'
    )

    # other parameters
    parser_wps.add_argument(
        '-i',
        '--interval_seconds',
        help='interval seconds'
    )

    parser_wps.add_argument(
        '--spec_bdy_width',
        help='boundary width'
    )

    parser_wps.add_argument(
        '--relax_zone',
        help='relax zone'
    )

    # ============================================
    #  WRF
    # ============================================
    parser_wrf.add_argument(
        '-t',
        '--task',
        required=True,
        choices=[
            'make_new_run',
            'make_namelist',
            'make_real_srun',
            'make_wrf_srun',
            'real',
            'wrf'
        ],
        help='running task'
    )

    parser_wrf.add_argument(
        '-o',
        '--workdir',
        help='work directory'
    )

    # below are just for make_namelist task
    parser_wrf.add_argument(
        '-s',
        '--start',
        help='start time'
    )

    wrf_run_length = parser_wrf.add_mutually_exclusive_group()

    wrf_run_length.add_argument(
        '-e',
        '--end',
        help='end time'
    )

    wrf_run_length.add_argument(
        '-r',
        '--run',
        help='running hours'
    )

    # other parameters
    parser_wrf.add_argument(
        '-i',
        '--interval_seconds',
        help='interval seconds'
    )

    parser_wrf.add_argument(
        '--history_interval',
        help='history interval'
    )

    parser_wrf.add_argument(
        '--inputout_interval',
        help='inputout interval'
    )

    parser_wrf.add_argument(
        '--inputout_begin_h',
        help='inputout begin hour'
    )

    parser_wrf.add_argument(
        '--inputout_end_h',
        help='inputout end hour'
    )

    parser_wrf.add_argument(
        '--spec_bdy_width',
        help='boundary width'
    )

    parser_wrf.add_argument(
        '--relax_zone',
        help='relax zone'
    )

    parser_wrf.add_argument(
        '--damp_opt',
        help='relax zone'
    )

    # ============================================
    #  WRFDA
    # ============================================
    parser_wrfda.add_argument(
        '-t', '--task',
        required=True,
        choices=[
            'make_new_run',
            'make_parame',
            'da_update_bc'
        ],
        help='running task'
    )

    parser_wrfda.add_argument(
        '-o',
        '--workdir',
        help='work directory'
    )

    parser_wrfda.add_argument(
        '-a',
        '--ana',
        help='analysis time'
    )

    parser_wrfda.add_argument(
        '-l',
        '--lower',
        action='store_true',
        help='update lower boundary condition'
    )

    # ============================================
    #  GSI
    # ============================================
    parser_gsi.add_argument(
        '-t',
        '--task',
        required=True,
        choices=[
            'make_new_run',
            'make_script',
            'gsi'
        ],
        help='running task'
    )

    parser_gsi.add_argument(
        '-o',
        '--workdir',
        help='work directory'
    )

    # below are just for make_script task
    parser_gsi.add_argument(
        '-a',
        '--ana',
        help='analysis time'
    )

    parser_gsi.add_argument(
        '-w',
        '--window',
        help='assimilation window'
    )

    parser_gsi.add_argument(
        '-c',
        '--cold',
        action='store_true',
        help='if cold start'
    )

    # parse the input command line
    args = parser.parse_args()
    # ============================================
    # initial
    settings.init(args)

    if args.mode == 'wps':
        wps.run(args)

    elif args.mode == 'wrf':
        wrf.run(args)

    elif args.mode == 'wrfda':
        wrfda.run(args)

    elif args.mode == 'gsi':
        gsi.run(args)

if __name__ == '__main__':
    main()
