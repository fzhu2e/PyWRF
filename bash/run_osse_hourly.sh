#!/usr/bin/env bash
# WPS
#./pywrf.py wps -t make_new_run -o run_OSSE_hourly
#./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818 -i 3600 -o run_OSSE_hourly
#./pywrf.py wps -t geogrid -o run_OSSE_hourly
#./pywrf.py wps -t ungrib -o run_OSSE_hourly
#./pywrf.py wps -t metgrid -o run_OSSE_hourly
## real
#./pywrf.py wrf -t make_new_run -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102600 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102601 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102602 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102603 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102604 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102605 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102606 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102607 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102608 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102609 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102610 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102611 -r 1 -i 3600 -o run_OSSE_hourly --inputout_interval 60
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102612 -r 54 -i 3600 -o run_OSSE_hourly --inputout_interval 180
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
#./pywrf.py wrf -t make_namelist -s 2012102518 -r 6 -i 21600 -o run_OSSE_hourly
#./pywrf.py wrf -t make_real_srun -o run_OSSE_hourly
#./pywrf.py wrf -t real -o run_OSSE_hourly
# wrf 2012102518 -> 2012102600
#./pywrf.py wrf -t make_namelist -s 2012102518 -r 6 -i 10800 -o run_OSSE_hourly \
               #--history_interval 180 --inputout_interval 180 --inputout_begin_h 3
#./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
#./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102600 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102600 -o run_OSSE_hourly
# wrf 2012102600 -> 2012102601
./pywrf.py wrf -t make_namelist -s 2012102600 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102601 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102601 -o run_OSSE_hourly
# wrf 2012102601 -> 2012102602
./pywrf.py wrf -t make_namelist -s 2012102601 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102602 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102602 -o run_OSSE_hourly
# wrf 2012102602 -> 2012102603
./pywrf.py wrf -t make_namelist -s 2012102602 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102603 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102603 -o run_OSSE_hourly
# wrf 2012102603 -> 2012102604
./pywrf.py wrf -t make_namelist -s 2012102603 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102604 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102604 -o run_OSSE_hourly
# wrf 2012102604 -> 2012102605
./pywrf.py wrf -t make_namelist -s 2012102604 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102605 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102605 -o run_OSSE_hourly
# wrf 2012102605 -> 2012102606
./pywrf.py wrf -t make_namelist -s 2012102605 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102606 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102606 -o run_OSSE_hourly
# wrf 2012102606 -> 2012102607
./pywrf.py wrf -t make_namelist -s 2012102606 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102607 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102607 -o run_OSSE_hourly
# wrf 2012102607 -> 2012102608
./pywrf.py wrf -t make_namelist -s 2012102607 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102608 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102608 -o run_OSSE_hourly
# wrf 2012102608 -> 2012102609
./pywrf.py wrf -t make_namelist -s 2012102608 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102609 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102609 -o run_OSSE_hourly
# wrf 2012102609 -> 2012102610
./pywrf.py wrf -t make_namelist -s 2012102609 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102610 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102610 -o run_OSSE_hourly
# wrf 2012102610 -> 2012102611
./pywrf.py wrf -t make_namelist -s 2012102610 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102611 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102611 -o run_OSSE_hourly
# wrf 2012102611 -> 2012102612
./pywrf.py wrf -t make_namelist -s 2012102611 -r 1 -i 3600 -o run_OSSE_hourly \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE_hourly
./pywrf.py gsi -t make_script -a 2012102612 -o run_OSSE_hourly -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE_hourly
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE_hourly
./pywrf.py wrfda -t make_parame -o run_OSSE_hourly
./pywrf.py wrfda -t da_update_bc -a 2012102612 -o run_OSSE_hourly
# wrf 2012102612 -> 2012102818
./pywrf.py wrf -t make_namelist -s 2012102612 -r 54 -i 10800 -o run_OSSE_hourly \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE_hourly
./pywrf.py wrf -t wrf -o run_OSSE_hourly

exit 0
