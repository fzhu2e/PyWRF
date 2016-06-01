clean:
	rm -rf __*

wps:
	./pywrf.py wps -t make_new_run -o run_OSSE
	./pywrf.py wps -t make_namelist -s 2012102618 -e 2012102900 -o run_OSSE
	./pywrf.py wps -t geogrid -o run_OSSE
	./pywrf.py wps -t ungrib -o run_OSSE
	./pywrf.py wps -t metgrid -o run_OSSE

wrf:
	./pywrf.py wrf -t make_new_run -o run_OSSE
	./pywrf.py wrf -t make_namelist -s 2012102618 -r 78 -o run_OSSE
	./pywrf.py wrf -t make_real_srun -o run_OSSE
	./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	./pywrf.py wrf -t real -o run_OSSE
	./pywrf.py wrf -t wrf -o run_OSSE

wrfda:
	./pywrf.py gsi -t make_new_run -o run_OSSE
	./pywrf.py gsi -t make_parame -o run_OSSE
	./pywrf.py gsi -t da_update_bc -a 2012102600 -o run_OSSE

gsi:
	./pywrf.py gsi -t make_new_run -o run_OSSE
	./pywrf.py gsi -t make_script -a 2012102600 -o run_OSSE
	./pywrf.py gsi -t gsi -o run_OSSE

tcr_2618:
	# wps 2012102618 -> 2012102918
	./pywrf.py wps -t make_new_run -o run_TCR
	./pywrf.py wps -t make_namelist -s 2012102618 -e 2012102918 -i 21600 -o run_TCR
	./pywrf.py wps -t geogrid -o run_TCR
	./pywrf.py wps -t ungrib -o run_TCR
	./pywrf.py wps -t metgrid -o run_TCR
	# real 2012102618 -> 2012102918
	./pywrf.py wrf -t make_new_run -o run_TCR
	./pywrf.py wrf -t make_namelist -s 2012102618 -e 2012102918 -i 21600 -o run_TCR \
				   --history_interval 180 --inputout_interval 360 --inputout_begin_h 6 --inputout_end_h 144
	./pywrf.py wrf -t make_real_srun -o run_TCR
	./pywrf.py wrf -t real -o run_TCR
	# wrf 2012102618 -> 2012102918
	./pywrf.py wrf -t make_wrf_srun -o run_TCR
	./pywrf.py wrf -t wrf -o run_TCR

tcr_2618_2700:
	# wrf 2012102700 -> 2012102700
	./pywrf.py wrf -t make_namelist -s 2012102700 -e 2012102918 -i 21600 -o run_TCR \
				   --history_interval 180 --inputout_interval 360 --inputout_begin_h 144
	./pywrf.py wrf -t make_wrf_srun -o run_TCR
	./pywrf.py wrf -t wrf -o run_TCR

tcr_2618_2700_da:
	# real 2012102700 -> 2012102918
	./pywrf.py wrf -t make_new_run -o run_TCR
	./pywrf.py wrf -t make_namelist -s 2012102700 -e 2012102918 -i 21600 -o run_TCR --inputout_interval 180
	./pywrf.py wrf -t make_real_srun -o run_TCR
	./pywrf.py wrf -t real -o run_TCR
	# gsi 2012102700
	./pywrf.py gsi -t make_new_run -o run_TCR
	./pywrf.py gsi -t make_script -a 2012102700 -o run_TCR
	./pywrf.py gsi -t gsi -o run_TCR
	# da_update_bc 2012102700
	./pywrf.py wrfda -t make_new_run -o run_TCR
	./pywrf.py wrfda -t make_parame -o run_TCR
	./pywrf.py wrfda -t da_update_bc -a 2012102700 -o run_TCR
	# wrf 2012102700 -> 2012102918
	./pywrf.py wrf -t make_namelist -s 2012102700 -e 2012102918 -i 21600 -o run_TCR \
				   --history_interval 180 --inputout_interval 360 --inputout_begin_h 144
	./pywrf.py wrf -t make_wrf_srun -o run_TCR
	./pywrf.py wrf -t wrf -o run_TCR

tcr_2618_2806:
	# wrf 2012102806 -> 2012102918
	./pywrf.py wrf -t make_namelist -s 2012102806 -e 2012102918 -i 21600 -o run_TCR \
				   --history_interval 180 --inputout_interval 360 --inputout_begin_h 144
	./pywrf.py wrf -t make_wrf_srun -o run_TCR
	./pywrf.py wrf -t wrf -o run_TCR

tcr_2618_2812:
	# wrf 2012102812 -> 2012102918
	./pywrf.py wrf -t make_namelist -s 2012102812 -e 2012102918 -i 21600 -o run_TCR \
				   --history_interval 180 --inputout_interval 360 --inputout_begin_h 144
	./pywrf.py wrf -t make_wrf_srun -o run_TCR
	./pywrf.py wrf -t wrf -o run_TCR

tcr_2618_2812_da:
	# real 2012102812 -> 2012102918
	# ./pywrf.py wrf -t make_new_run -o run_TCR
	# ./pywrf.py wrf -t make_namelist -s 2012102812 -e 2012102918 -i 21600 -o run_TCR --inputout_interval 180
	# ./pywrf.py wrf -t make_real_srun -o run_TCR
	# ./pywrf.py wrf -t real -o run_TCR
	# gsi 2012102812
	./pywrf.py gsi -t make_new_run -o run_TCR
	./pywrf.py gsi -t make_script -a 2012102812 -o run_TCR
	./pywrf.py gsi -t gsi -o run_TCR
	# da_update_bc 2012102812
	./pywrf.py wrfda -t make_new_run -o run_TCR
	./pywrf.py wrfda -t make_parame -o run_TCR
	./pywrf.py wrfda -t da_update_bc -a 2012102812 -o run_TCR
	# wrf 2012102812 -> 2012102918
	./pywrf.py wrf -t make_namelist -s 2012102812 -e 2012102918 -i 21600 -o run_TCR \
				   --history_interval 180 --inputout_interval 360 --inputout_begin_h 144
	./pywrf.py wrf -t make_wrf_srun -o run_TCR
	./pywrf.py wrf -t wrf -o run_TCR

tcr_2706:
	# wps 2012102706 -> 2012102918
	./pywrf.py wps -t make_new_run -o run_TCR
	./pywrf.py wps -t make_namelist -s 2012102706 -e 2012102918 -i 21600 -o run_TCR
	./pywrf.py wps -t geogrid -o run_TCR
	./pywrf.py wps -t ungrib -o run_TCR
	./pywrf.py wps -t metgrid -o run_TCR
	# real 2012102706 -> 2012102918
	./pywrf.py wrf -t make_new_run -o run_TCR
	./pywrf.py wrf -t make_namelist -s 2012102706 -e 2012102918 -i 21600 -o run_TCR \
				   --history_interval 180 --inputout_interval 360 --inputout_begin_h 6 --inputout_end_h 144
	./pywrf.py wrf -t make_real_srun -o run_TCR
	./pywrf.py wrf -t real -o run_TCR
	# wrf 2012102706 -> 2012102918
	./pywrf.py wrf -t make_wrf_srun -o run_TCR
	./pywrf.py wrf -t wrf -o run_TCR

tcr_da_cyc1:
	# wps 2012102618 -> 2012102918
	# ./pywrf.py wps -t make_new_run -o run_TCR
	# ./pywrf.py wps -t make_namelist -s 2012102618 -e 2012102918 -i 21600 -o run_TCR
	# ./pywrf.py wps -t geogrid -o run_TCR
	# ./pywrf.py wps -t ungrib -o run_TCR
	# ./pywrf.py wps -t metgrid -o run_TCR
	# real 2012102618 -> 2012102700, 2012102700 -> 2012102918
	# ./pywrf.py wrf -t make_new_run -o run_TCR
	# ./pywrf.py wrf -t make_namelist -s 2012102700 -r 66 -i 21600 -o run_TCR --inputout_interval 180
	# ./pywrf.py wrf -t make_real_srun -o run_TCR
	# ./pywrf.py wrf -t real -o run_TCR
	# ./pywrf.py wrf -t make_namelist -s 2012102618 -r 6 -i 21600 -o run_TCR
	# ./pywrf.py wrf -t make_real_srun -o run_TCR
	# ./pywrf.py wrf -t real -o run_TCR
	# wrf 2012102618 -> 2012102700
	# ./pywrf.py wrf -t make_namelist -s 2012102618 -r 6 -i 10800 -o run_TCR \
				   # --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	# ./pywrf.py wrf -t make_wrf_srun -o run_TCR
	# ./pywrf.py wrf -t wrf -o run_TCR
	# gsi 2012102700
	# ./pywrf.py gsi -t make_new_run -o run_TCR
	# ./pywrf.py gsi -t make_script -a 2012102700 -o run_TCR
	# ./pywrf.py gsi -t gsi -o run_TCR
	# # da_update_bc 2012102700
	# ./pywrf.py wrfda -t make_new_run -o run_TCR
	# ./pywrf.py wrfda -t make_parame -o run_TCR
	# ./pywrf.py wrfda -t da_update_bc -a 2012102700 -o run_TCR
	# wrf 2012102700 -> 2012102918
	./pywrf.py wrf -t make_namelist -s 2012102700 -r 66 -i 10800 -o run_TCR \
				   --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	./pywrf.py wrf -t make_wrf_srun -o run_TCR
	./pywrf.py wrf -t wrf -o run_TCR

tcr_da_cyc3:
	# wps 2012102618 -> 2012102918
	# ./pywrf.py wps -t make_new_run -o run_TCR
	# ./pywrf.py wps -t make_namelist -s 2012102618 -e 2012102918 -i 21600 -o run_TCR
	# ./pywrf.py wps -t geogrid -o run_TCR
	# ./pywrf.py wps -t ungrib -o run_TCR
	# ./pywrf.py wps -t metgrid -o run_TCR
	# real
	# ./pywrf.py wrf -t make_new_run -o run_TCR
	# ./pywrf.py wrf -t make_namelist -s 2012102700 -r 6 -i 21600 -o run_TCR --inputout_interval 180
	# ./pywrf.py wrf -t make_real_srun -o run_TCR
	# ./pywrf.py wrf -t real -o run_TCR
	# ./pywrf.py wrf -t make_namelist -s 2012102706 -r 6 -i 21600 -o run_TCR --inputout_interval 180
	# ./pywrf.py wrf -t make_real_srun -o run_TCR
	# ./pywrf.py wrf -t real -o run_TCR
	# ./pywrf.py wrf -t make_namelist -s 2012102712 -r 54 -i 21600 -o run_TCR --inputout_interval 180
	# ./pywrf.py wrf -t make_real_srun -o run_TCR
	# ./pywrf.py wrf -t real -o run_TCR
	# ./pywrf.py wrf -t make_namelist -s 2012102618 -r 6 -i 21600 -o run_TCR
	# ./pywrf.py wrf -t make_real_srun -o run_TCR
	# ./pywrf.py wrf -t real -o run_TCR
	# wrf 2012102618 -> 2012102700
	# ./pywrf.py wrf -t make_namelist -s 2012102618 -r 6 -i 10800 -o run_TCR \
				   # --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	# ./pywrf.py wrf -t make_wrf_srun -o run_TCR
	# ./pywrf.py wrf -t wrf -o run_TCR
	# gsi 2012102700
	# ./pywrf.py gsi -t make_new_run -o run_TCR
	# ./pywrf.py gsi -t make_script -a 2012102700 -o run_TCR
	# ./pywrf.py gsi -t gsi -o run_TCR
	# # da_update_bc
	# ./pywrf.py wrfda -t make_new_run -o run_TCR
	# ./pywrf.py wrfda -t make_parame -o run_TCR
	# ./pywrf.py wrfda -t da_update_bc -a 2012102700 -o run_TCR
	# # wrf 2012102700 -> 2012102706
	# ./pywrf.py wrf -t make_namelist -s 2012102700 -r 6 -i 10800 -o run_TCR \
				   # --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	# ./pywrf.py wrf -t make_wrf_srun -o run_TCR
	# ./pywrf.py wrf -t wrf -o run_TCR
	# gsi 2012102706
	# ./pywrf.py gsi -t make_new_run -o run_TCR
	# ./pywrf.py gsi -t make_script -a 2012102706 -o run_TCR
	# ./pywrf.py gsi -t gsi -o run_TCR
	# # da_update_bc
	# ./pywrf.py wrfda -t make_new_run -o run_TCR
	# ./pywrf.py wrfda -t make_parame -o run_TCR
	# ./pywrf.py wrfda -t da_update_bc -a 2012102706 -o run_TCR
	# # wrf 2012102706 -> 2012102712
	# ./pywrf.py wrf -t make_namelist -s 2012102706 -r 6 -i 10800 -o run_TCR \
				   # --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	# ./pywrf.py wrf -t make_wrf_srun -o run_TCR
	# ./pywrf.py wrf -t wrf -o run_TCR
	# gsi 2012102712
	./pywrf.py gsi -t make_new_run -o run_TCR
	./pywrf.py gsi -t make_script -a 2012102712 -o run_TCR
	./pywrf.py gsi -t gsi -o run_TCR
	# da_update_bc
	./pywrf.py wrfda -t make_new_run -o run_TCR
	./pywrf.py wrfda -t make_parame -o run_TCR
	./pywrf.py wrfda -t da_update_bc -a 2012102712 -o run_TCR
	# wrf 2012102712 -> 2012102918
	./pywrf.py wrf -t make_namelist -s 2012102712 -r 54 -i 10800 -o run_TCR \
				   --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	./pywrf.py wrf -t make_wrf_srun -o run_TCR
	./pywrf.py wrf -t wrf -o run_TCR

osse:
	./bash/run_osse.sh

osse-l:
	./bash/run_osse_update_lbc.sh

osse_hourly:
	./bash/run_osse_hourly.sh

# EC nature run
osse_ec_noncyc:
	./bash/run_osse_ec_noncyc.sh

osse_ec_3h:
	./bash/run_osse_ec_3h.sh

osse_ec_3h_debug:
	./bash/run_osse_ec_3h_debug.sh

osse_ec_3h_ctl:
	./bash/run_osse_ec_3h_ctl.sh

osse_ec_3h_raob:
	./bash/run_osse_ec_3h_raob.sh

osse_ec_1h:
	./bash/run_osse_ec_1h.sh

osse_ec_multi:
	./bash/run_osse_ec_multi.sh

osse_ec_multi_ctl:
	./bash/run_osse_ec_multi_ctl.sh

osse_ec_multi_cyc:
	./bash/run_osse_ec_multi_cyc.sh

osse_ec_multi_noncyc:
	./bash/run_osse_ec_multi_noncyc.sh

osse_ec_multi_cyc_1h:
	./bash/run_osse_ec_multi_cyc_1h.sh

osse_ec_multi_cyc_6h:
	./bash/run_osse_ec_multi_cyc_6h.sh

osse_ec_multi_cyc_12h_spinup:
	./bash/run_osse_ec_multi_cyc_12h_spinup.sh

osse_ec_multi_cyc_5steps:
	./bash/run_osse_ec_multi_cyc_5steps.sh

osse_ec_cyc_anl:
	./bash/run_osse_ec_cyc_anl.sh

osse_ec_cyc_anl_a1:
	./bash/run_osse_ec_cyc_anl_a1.sh

osse_ec_cyc_anl_a2:
	./bash/run_osse_ec_cyc_anl_a2.sh

osse_ec_cyc_anl_a3:
	./bash/run_osse_ec_cyc_anl_a3.sh

osse_ec_cyc_anl_a4:
	./bash/run_osse_ec_cyc_anl_a4.sh

osse_ec_cyc_anl_a5:
	./bash/run_osse_ec_cyc_anl_a5.sh

osse_ec_cyc_anl_ctl:
	./bash/run_osse_ec_cyc_anl_ctl.sh

# EC nature run, cyc anl
osse_anl_cyc_1h:
	./bash/run_anl_cyc_1h.sh

osse_anl_cyc_3h:
	./bash/run_anl_cyc_3h.sh

osse_anl_cyc_6h:
	./bash/run_anl_cyc_6h.sh

osse_anl_cyc_ctl:
	./bash/run_anl_cyc_ctl.sh

osse_anl_cyc_1h_ecmwf:
	./bash/run_anl_cyc_1h_ecmwf.sh

osse_anl_cyc_3h_ecmwf:
	./bash/run_anl_cyc_3h_ecmwf.sh

osse_anl_cyc_ctl_ecmwf:
	./bash/run_anl_cyc_ctl_ecmwf.sh


# To find out why GEO is worse than LEO
debug_01:
	./bash/run_debug_01.sh

debug_02:
	./bash/run_debug_02.sh

# Renews
renew:
	./bash/renew.sh

renew_hourly:
	./bash/renew_hourly.sh

renew_debug_01:
	./bash/renew_debug_01.sh

renew_debug_02:
	./bash/renew_debug_02.sh

renew_ec_noncyc:
	./bash/renew_satbias.sh
	./bash/renew_ec_noncyc.sh

renew_ec_3h:
	./bash/renew_satbias.sh
	./bash/renew_ec_3h.sh

renew_ec_3h_raob:
	./bash/renew_ec_3h_raob.sh

renew_ec_1h:
	./bash/renew_satbias.sh
	./bash/renew_ec_1h.sh

renew_ec_multi:
	./bash/renew_satbias.sh
	./bash/renew_ec_multi.sh

renew_ec_multi_cyc:
	./bash/renew_satbias.sh
	./bash/renew_ec_multi_cyc.sh

renew_ec_multi_cyc_12h_spinup:
	./bash/renew_ec_multi_cyc_12h_spinup.sh

renew_ec_cyc_anl:
	./bash/renew_ec_cyc_anl.sh
