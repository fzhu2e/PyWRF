#!/usr/bin/env bash
# WPS
# ./pywrf.py wps -t make_new_run -o run_OSSE
# ./pywrf.py wps -t make_namelist -s 2012102618 -e 2012102818 -i 3600 -o run_OSSE
# ./pywrf.py wps -t geogrid -o run_OSSE
# ./pywrf.py wps -t ungrib -o run_OSSE
# ./pywrf.py wps -t metgrid -o run_OSSE

# # real
# ./pywrf.py wrf -t make_new_run -o run_OSSE

# ./pywrf.py wrf -t make_namelist -s 2012102700 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102701 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102702 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102703 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102704 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102705 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102706 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102707 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102708 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102709 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102710 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102711 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102712 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102713 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102714 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102715 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102716 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102717 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102718 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102719 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102720 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102721 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102722 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102723 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102800 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102801 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102802 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102803 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102804 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102805 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102806 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102807 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102808 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102809 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102810 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102811 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102812 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102813 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102814 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102815 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102816 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102817 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
# ./pywrf.py wrf -t make_real_srun -o run_OSSE
# ./pywrf.py wrf -t real -o run_OSSE
# ./pywrf.py wrf -t make_namelist -s 2012102818 -r 1 -i 3600 -o run_OSSE --inputout_interval 60
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
./bash/renew_anl_cyc_1h.sh

# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102700 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102700 -o run_OSSE

# wrf 2012102700 -> 2012102701
./pywrf.py wrf -t make_namelist -s 2012102700 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102701 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102701 -o run_OSSE

# wrf 2012102701 -> 2012102702
./pywrf.py wrf -t make_namelist -s 2012102701 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102702 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102702 -o run_OSSE

# wrf 2012102702 -> 2012102703
./pywrf.py wrf -t make_namelist -s 2012102702 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102703 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102703 -o run_OSSE

# wrf 2012102703 -> 2012102704
./pywrf.py wrf -t make_namelist -s 2012102703 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102704 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102704 -o run_OSSE

# wrf 2012102704 -> 2012102705
./pywrf.py wrf -t make_namelist -s 2012102704 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102705 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102705 -o run_OSSE

# wrf 2012102705 -> 2012102706
./pywrf.py wrf -t make_namelist -s 2012102705 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102706 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102706 -o run_OSSE

# wrf 2012102706 -> 2012102707
./pywrf.py wrf -t make_namelist -s 2012102706 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102707 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102707 -o run_OSSE

# wrf 2012102707 -> 2012102708
./pywrf.py wrf -t make_namelist -s 2012102707 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102708 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102708 -o run_OSSE

# wrf 2012102708 -> 2012102709
./pywrf.py wrf -t make_namelist -s 2012102708 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102709 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102709 -o run_OSSE

# wrf 2012102709 -> 2012102710
./pywrf.py wrf -t make_namelist -s 2012102709 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102710 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102710 -o run_OSSE

# wrf 2012102710 -> 2012102711
./pywrf.py wrf -t make_namelist -s 2012102710 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102711 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102711 -o run_OSSE

# wrf 2012102711 -> 2012102712
./pywrf.py wrf -t make_namelist -s 2012102711 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102712 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102712 -o run_OSSE

# wrf 2012102712 -> 2012102713
./pywrf.py wrf -t make_namelist -s 2012102712 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102713 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102713 -o run_OSSE

# wrf 2012102713 -> 2012102714
./pywrf.py wrf -t make_namelist -s 2012102713 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102714 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102714 -o run_OSSE

# wrf 2012102714 -> 2012102715
./pywrf.py wrf -t make_namelist -s 2012102714 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102715 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102715 -o run_OSSE

# wrf 2012102715 -> 2012102716
./pywrf.py wrf -t make_namelist -s 2012102715 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102716 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102716 -o run_OSSE

# wrf 2012102716 -> 2012102717
./pywrf.py wrf -t make_namelist -s 2012102716 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102717 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102717 -o run_OSSE

# wrf 2012102717 -> 2012102718
./pywrf.py wrf -t make_namelist -s 2012102717 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102718 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102718 -o run_OSSE

# wrf 2012102718 -> 2012102719
./pywrf.py wrf -t make_namelist -s 2012102718 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102719 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102719 -o run_OSSE

# wrf 2012102719 -> 2012102720
./pywrf.py wrf -t make_namelist -s 2012102719 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102720 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102720 -o run_OSSE

# wrf 2012102720 -> 2012102721
./pywrf.py wrf -t make_namelist -s 2012102720 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102721 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102721 -o run_OSSE

# wrf 2012102721 -> 2012102722
./pywrf.py wrf -t make_namelist -s 2012102721 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102722 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102722 -o run_OSSE

# wrf 2012102722 -> 2012102723
./pywrf.py wrf -t make_namelist -s 2012102722 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102723 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102723 -o run_OSSE

# wrf 2012102723 -> 2012102800
./pywrf.py wrf -t make_namelist -s 2012102723 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102800 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102800 -o run_OSSE

# wrf 2012102800 -> 2012102801
./pywrf.py wrf -t make_namelist -s 2012102800 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102801 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102801 -o run_OSSE

# wrf 2012102801 -> 2012102802
./pywrf.py wrf -t make_namelist -s 2012102801 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102802 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102802 -o run_OSSE

# wrf 2012102802 -> 2012102803
./pywrf.py wrf -t make_namelist -s 2012102802 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102803 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102803 -o run_OSSE

# wrf 2012102803 -> 2012102804
./pywrf.py wrf -t make_namelist -s 2012102803 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102804 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102804 -o run_OSSE

# wrf 2012102804 -> 2012102805
./pywrf.py wrf -t make_namelist -s 2012102804 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102805 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102805 -o run_OSSE

# wrf 2012102805 -> 2012102806
./pywrf.py wrf -t make_namelist -s 2012102805 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102806 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102806 -o run_OSSE

# wrf 2012102806 -> 2012102807
./pywrf.py wrf -t make_namelist -s 2012102806 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102807 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102807 -o run_OSSE

# wrf 2012102807 -> 2012102808
./pywrf.py wrf -t make_namelist -s 2012102807 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102808 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102808 -o run_OSSE

# wrf 2012102808 -> 2012102809
./pywrf.py wrf -t make_namelist -s 2012102808 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102809 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102809 -o run_OSSE

# wrf 2012102809 -> 2012102810
./pywrf.py wrf -t make_namelist -s 2012102809 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102810 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102810 -o run_OSSE

# wrf 2012102810 -> 2012102811
./pywrf.py wrf -t make_namelist -s 2012102810 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102811 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102811 -o run_OSSE

# wrf 2012102811 -> 2012102812
./pywrf.py wrf -t make_namelist -s 2012102811 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102812 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102812 -o run_OSSE

# wrf 2012102812 -> 2012102813
./pywrf.py wrf -t make_namelist -s 2012102812 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102813 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102813 -o run_OSSE

# wrf 2012102813 -> 2012102814
./pywrf.py wrf -t make_namelist -s 2012102813 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102814 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102814 -o run_OSSE

# wrf 2012102814 -> 2012102815
./pywrf.py wrf -t make_namelist -s 2012102814 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102815 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102815 -o run_OSSE

# wrf 2012102815 -> 2012102816
./pywrf.py wrf -t make_namelist -s 2012102815 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102816 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102816 -o run_OSSE

# wrf 2012102816 -> 2012102817
./pywrf.py wrf -t make_namelist -s 2012102816 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102817 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102817 -o run_OSSE

# wrf 2012102817 -> 2012102818
./pywrf.py wrf -t make_namelist -s 2012102817 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE
# gsi
./pywrf.py gsi -t make_new_run -o run_OSSE
./pywrf.py gsi -t make_script -a 2012102818 -o run_OSSE -w 0.5
./pywrf.py gsi -t gsi -o run_OSSE
# da_update_bc
./pywrf.py wrfda -t make_new_run -o run_OSSE
./pywrf.py wrfda -t make_parame -o run_OSSE
./pywrf.py wrfda -t da_update_bc -a 2012102818 -o run_OSSE

# wrf 2012102818 -> 2012102819
./pywrf.py wrf -t make_namelist -s 2012102818 -r 1 -i 3600 -o run_OSSE \
               --history_interval 60 --inputout_interval 60 --inputout_begin_h 1
./pywrf.py wrf -t make_wrf_srun -o run_OSSE
./pywrf.py wrf -t wrf -o run_OSSE

exit 0
