#!/usr/bin/env bash
SLEEP_TIME=30
# WPS
# ./pywrf.py wps -t make_new_run -o run_OSSE
# ./pywrf.py wps -t make_namelist -s 2012102618 -e 2012103006 -i 21600 -o run_OSSE
# ./pywrf.py wps -t geogrid -o run_OSSE
# ./pywrf.py wps -t ungrib -o run_OSSE
# ./pywrf.py wps -t metgrid -o run_OSSE

rm -rf $RESULTS/OSSE
### 2706 S
cp -r $RESULTS/OSSE_ec_multi_cyc_bak $RESULTS/OSSE
sleep $SLEEP_TIME
# real
./pywrf.py wrf -t make_namelist -s 2012102706 -r 48 -i 21600 -o run_OSSE
./pywrf.py wrf -t make_real_srun -o run_OSSE
./pywrf.py wrf -t real -o run_OSSE
./pywrf.py wrf -t make_namelist -s 2012102618 -r 12 -i 21600 -o run_OSSE
./pywrf.py wrf -t make_real_srun -o run_OSSE
./pywrf.py wrf -t real -o run_OSSE
# wrf 2012102618 -> 2012102706
./pywrf.py wrf -t make_namelist -s 2012102618 -r 12 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 12 --inputout_end_h 12
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102706 -o run_OSSE
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102706 -o run_OSSE
# wrf 2012102706 -> 2012102906
./pywrf.py wrf -t make_namelist -s 2012102706 -r 48 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE

mv $RESULTS/OSSE $RESULTS/OSSE_T01
### 2706 E

### 2712 S
cp -r $RESULTS/OSSE_ec_multi_cyc_bak $RESULTS/OSSE
sleep $SLEEP_TIME
# real
./pywrf.py wrf -t make_namelist -s 2012102712 -r 48 -i 21600 -o run_OSSE
./pywrf.py wrf -t make_real_srun -o run_OSSE
./pywrf.py wrf -t real -o run_OSSE
./pywrf.py wrf -t make_namelist -s 2012102700 -r 12 -i 21600 -o run_OSSE
./pywrf.py wrf -t make_real_srun -o run_OSSE
./pywrf.py wrf -t real -o run_OSSE
# wrf 2012102700 -> 2012102712
./pywrf.py wrf -t make_namelist -s 2012102700 -r 12 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 12 --inputout_end_h 12
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102712 -o run_OSSE
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102712 -o run_OSSE
# wrf 2012102712 -> 2012102912
./pywrf.py wrf -t make_namelist -s 2012102712 -r 48 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE

mv $RESULTS/OSSE $RESULTS/OSSE_T02
### 2712 E

### 2718 S
cp -r $RESULTS/OSSE_ec_multi_cyc_bak $RESULTS/OSSE
sleep $SLEEP_TIME
# real
./pywrf.py wrf -t make_namelist -s 2012102718 -r 48 -i 21600 -o run_OSSE
./pywrf.py wrf -t make_real_srun -o run_OSSE
./pywrf.py wrf -t real -o run_OSSE
./pywrf.py wrf -t make_namelist -s 2012102706 -r 12 -i 21600 -o run_OSSE
./pywrf.py wrf -t make_real_srun -o run_OSSE
./pywrf.py wrf -t real -o run_OSSE
# wrf 2012102706 -> 2012102718
./pywrf.py wrf -t make_namelist -s 2012102706 -r 12 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 12 --inputout_end_h 12
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102718 -o run_OSSE
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102718 -o run_OSSE
# wrf 2012102718 -> 2012102918
./pywrf.py wrf -t make_namelist -s 2012102718 -r 48 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE

mv $RESULTS/OSSE $RESULTS/OSSE_T03
### 2718 E


### 2800 S
cp -r $RESULTS/OSSE_ec_multi_cyc_bak $RESULTS/OSSE
sleep $SLEEP_TIME
# real
./pywrf.py wrf -t make_namelist -s 2012102800 -r 48 -i 21600 -o run_OSSE
./pywrf.py wrf -t make_real_srun -o run_OSSE
./pywrf.py wrf -t real -o run_OSSE
./pywrf.py wrf -t make_namelist -s 2012102712 -r 12 -i 21600 -o run_OSSE
./pywrf.py wrf -t make_real_srun -o run_OSSE
./pywrf.py wrf -t real -o run_OSSE
# wrf 2012102712 -> 2012102800
./pywrf.py wrf -t make_namelist -s 2012102712 -r 12 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 12 --inputout_end_h 12
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102800 -o run_OSSE
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102800 -o run_OSSE
# wrf 2012102800 -> 2012103000
./pywrf.py wrf -t make_namelist -s 2012102800 -r 48 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE

mv $RESULTS/OSSE $RESULTS/OSSE_T04
### 2800 E

exit 0
