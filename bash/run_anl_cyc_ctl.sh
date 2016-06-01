#!/usr/bin/env bash
# WPS
./pywrf.py wps -t make_new_run -o run_OSSE
./pywrf.py wps -t make_namelist -s 2012102618 -e 2012102818 -i 21600 -o run_OSSE
./pywrf.py wps -t geogrid -o run_OSSE
./pywrf.py wps -t ungrib -o run_OSSE
./pywrf.py wps -t metgrid -o run_OSSE

# real
./pywrf.py wrf -t make_new_run -o run_OSSE

./pywrf.py wrf -t make_namelist -s 2012102618 -r 48 -i 21600 -o run_OSSE
./pywrf.py wrf -t make_real_srun -o run_OSSE
./pywrf.py wrf -t real -o run_OSSE

# wrf 2012102618 -> 2012102818
./pywrf.py wrf -t make_namelist -s 2012102618 -r 48 -i 21600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 99
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE


exit 0
