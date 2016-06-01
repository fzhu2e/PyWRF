#!/usr/bin/env bash
# WPS
# ./pywrf.py wps -t make_new_run -o run_OSSE
# ./pywrf.py wps -t make_namelist -s 2012102618 -e 2012102818 -i 10800 -o run_OSSE
# ./pywrf.py wps -t geogrid -o run_OSSE
# ./pywrf.py wps -t ungrib -o run_OSSE
# ./pywrf.py wps -t metgrid -o run_OSSE

# # real
# ./pywrf.py wrf -t make_new_run -o run_OSSE

# ./pywrf.py wrf -t make_namelist -s 2012102700 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102703 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102706 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102709 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102712 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102715 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102718 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102721 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102800 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102803 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102806 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102809 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102812 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102815 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102818 -r 3 -i 10800 -o run_OSSE --inputout_interval 360
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102618 -r 6 -i 21600 -o run_OSSE
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE

# # wrf 2012102618 -> 2012102700
# ./pywrf.py wrf -t make_namelist -s 2012102618 -r 6 -i 10800 -o run_OSSE \
               # --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
# ./pywrf.py wrf -t make_wrf_srun -o run_OSSE
# ./pywrf.py wrf -t wrf -o run_OSSE

##### if warm start the running, commment the lines above and uncomment the line below
./bash/renew_anl_cyc_3h.sh

# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102700 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102700 -o run_OSSE

# wrf 2012102700 -> 2012102703
./pywrf.py wrf -t make_namelist -s 2012102700 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102703 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102703 -o run_OSSE

# wrf 2012102703 -> 2012102706
./pywrf.py wrf -t make_namelist -s 2012102703 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102706 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102706 -o run_OSSE

# wrf 2012102706 -> 2012102709
./pywrf.py wrf -t make_namelist -s 2012102706 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102709 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102709 -o run_OSSE

# wrf 2012102709 -> 2012102712
./pywrf.py wrf -t make_namelist -s 2012102709 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102712 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102712 -o run_OSSE

# wrf 2012102712 -> 2012102715
./pywrf.py wrf -t make_namelist -s 2012102712 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102715 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102715 -o run_OSSE

# wrf 2012102715 -> 2012102718
./pywrf.py wrf -t make_namelist -s 2012102715 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102718 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102718 -o run_OSSE

# wrf 2012102718 -> 2012102721
./pywrf.py wrf -t make_namelist -s 2012102718 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102721 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102721 -o run_OSSE

# wrf 2012102721 -> 2012102800
./pywrf.py wrf -t make_namelist -s 2012102721 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102800 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102800 -o run_OSSE

# wrf 2012102800 -> 2012102803
./pywrf.py wrf -t make_namelist -s 2012102800 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102803 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102803 -o run_OSSE

# wrf 2012102803 -> 2012102806
./pywrf.py wrf -t make_namelist -s 2012102803 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102806 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102806 -o run_OSSE

# wrf 2012102806 -> 2012102809
./pywrf.py wrf -t make_namelist -s 2012102806 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102809 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102809 -o run_OSSE

# wrf 2012102809 -> 2012102812
./pywrf.py wrf -t make_namelist -s 2012102809 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102812 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102812 -o run_OSSE

# wrf 2012102812 -> 2012102815
./pywrf.py wrf -t make_namelist -s 2012102812 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102815 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102815 -o run_OSSE

# wrf 2012102815 -> 2012102818
./pywrf.py wrf -t make_namelist -s 2012102815 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102818 -o run_OSSE -w 1.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102818 -o run_OSSE

# wrf 2012102818 -> 2012102821
./pywrf.py wrf -t make_namelist -s 2012102818 -r 3 -i 10800 -o run_OSSE \
               --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE

exit 0
