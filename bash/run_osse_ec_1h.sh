#!/usr/bin/env bash
# WPS
#./pywrf.py wps -t make_new_run -o run_OSSE_hourly
#./pywrf.py wps -t make_namelist -s 2012102618 -e 2012102918 -i 3600 -o run_OSSE_hourly
#./pywrf.py wps -t geogrid -o run_OSSE_hourly
#./pywrf.py wps -t ungrib -o run_OSSE_hourly
#./pywrf.py wps -t metgrid -o run_OSSE_hourly
# real
#./pywrf.py wrf -t make_new_run -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102700 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102701 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102702 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102703 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102704 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102705 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102706 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102707 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102708 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102709 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102710 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102711 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102712 -r 54 -i 3600 -o run_OSSE_hourly --inputout_interval 180
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102618 -r 6 -i 21600 -o run_OSSE_hourly
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
# wrf 2012102618 -> 2012102700
#./pywrf.py wrf -t make_namelist -s 2012102618 -r 6 -i 10800 -o run_OSSE_hourly \
               #--history_interval 180 --inputout_interval 180 --inputout_begin_h 3
#./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
#./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102700 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102700 -o run_OSSE_hourly
# wrf 2012102700 -> 2012102701
./pywrf.py wrf -t make_namelist -s 2012102700 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102701 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102701 -o run_OSSE_hourly
# wrf 2012102701 -> 2012102702
./pywrf.py wrf -t make_namelist -s 2012102701 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102702 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102702 -o run_OSSE_hourly
# wrf 2012102702 -> 2012102703
./pywrf.py wrf -t make_namelist -s 2012102702 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102703 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102703 -o run_OSSE_hourly
# wrf 2012102703 -> 2012102704
./pywrf.py wrf -t make_namelist -s 2012102703 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102704 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102704 -o run_OSSE_hourly
# wrf 2012102704 -> 2012102705
./pywrf.py wrf -t make_namelist -s 2012102704 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102705 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102705 -o run_OSSE_hourly
# wrf 2012102705 -> 2012102706
./pywrf.py wrf -t make_namelist -s 2012102705 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102706 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102706 -o run_OSSE_hourly
# wrf 2012102706 -> 2012102707
./pywrf.py wrf -t make_namelist -s 2012102706 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102707 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102707 -o run_OSSE_hourly
# wrf 2012102707 -> 2012102708
./pywrf.py wrf -t make_namelist -s 2012102707 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102708 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102708 -o run_OSSE_hourly
# wrf 2012102708 -> 2012102709
./pywrf.py wrf -t make_namelist -s 2012102708 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102709 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102709 -o run_OSSE_hourly
# wrf 2012102709 -> 2012102710
./pywrf.py wrf -t make_namelist -s 2012102709 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102710 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102710 -o run_OSSE_hourly
# wrf 2012102710 -> 2012102711
./pywrf.py wrf -t make_namelist -s 2012102710 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102711 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102711 -o run_OSSE_hourly
# wrf 2012102711 -> 2012102712
./pywrf.py wrf -t make_namelist -s 2012102711 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102712 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102712 -o run_OSSE_hourly
# wrf 2012102712 -> 2012102918
./pywrf.py wrf -t make_namelist -s 2012102712 -r 54 -i 10800 -o run_OSSE_hourly \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly

exit 0
