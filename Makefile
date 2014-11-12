clean:
	rm -rf __*

wps:
	./pywrf.py wps -t make_new_run -o run_OSSE
	./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818 -o run_OSSE
	./pywrf.py wps -t geogrid -o run_OSSE
	./pywrf.py wps -t ungrib -o run_OSSE
	./pywrf.py wps -t metgrid -o run_OSSE

wrf:
	./pywrf.py wrf -t make_new_run -o run_OSSE
	./pywrf.py wrf -t make_namelist -s 2012102518 -r 6 -o run_OSSE
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

osse:
	./bash/run_osse.sh

osse-l:
	./bash/run_osse_update_lbc.sh

osse_hourly:
	./bash/run_osse_hourly.sh

# EC nature run
osse_ec_3h:
	./bash/run_osse_ec_3h.sh

osse_ec_3h_ctl:
	./bash/run_osse_ec_3h_ctl.sh

osse_ec_3h_raob:
	./bash/run_osse_ec_3h_raob.sh

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

renew_ec_3h:
	./bash/renew_satbias.sh
	./bash/renew_ec_3h.sh

renew_ec_3h_raob:
	./bash/renew_ec_3h_raob.sh
