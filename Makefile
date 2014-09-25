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
	# WPS
	#./pywrf.py wps -t make_new_run -o run_OSSE
	#./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818 -i 10800 -o run_OSSE
	#./pywrf.py wps -t geogrid -o run_OSSE
	#./pywrf.py wps -t ungrib -o run_OSSE
	#./pywrf.py wps -t metgrid -o run_OSSE
	## real
	#./pywrf.py wrf -t make_new_run -o run_OSSE
	#./pywrf.py wrf -t make_namelist -s 2012102600 -r 3 -i 10800 -o run_OSSE --inputout_interval 180
	#./pywrf.py wrf -t make_real_srun -o run_OSSE
	#./pywrf.py wrf -t real -o run_OSSE
	#./pywrf.py wrf -t make_namelist -s 2012102603 -r 3 -i 10800 -o run_OSSE --inputout_interval 180
	#./pywrf.py wrf -t make_real_srun -o run_OSSE
	#./pywrf.py wrf -t real -o run_OSSE
	#./pywrf.py wrf -t make_namelist -s 2012102606 -r 3 -i 10800 -o run_OSSE --inputout_interval 180
	#./pywrf.py wrf -t make_real_srun -o run_OSSE
	#./pywrf.py wrf -t real -o run_OSSE
	#./pywrf.py wrf -t make_namelist -s 2012102609 -r 3 -i 10800 -o run_OSSE --inputout_interval 180
	#./pywrf.py wrf -t make_real_srun -o run_OSSE
	#./pywrf.py wrf -t real -o run_OSSE
	#./pywrf.py wrf -t make_namelist -s 2012102612 -r 54 -i 10800 -o run_OSSE --inputout_interval 180
	#./pywrf.py wrf -t make_real_srun -o run_OSSE
	#./pywrf.py wrf -t real -o run_OSSE
	#./pywrf.py wrf -t make_namelist -s 2012102518 -r 6 -i 21600 -o run_OSSE
	#./pywrf.py wrf -t make_real_srun -o run_OSSE
	#./pywrf.py wrf -t real -o run_OSSE
	## wrf 2012102518 -> 2012102600
	#./pywrf.py wrf -t make_namelist -s 2012102518 -r 6 -i 10800 -o run_OSSE \
				   #--history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	#./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	#./pywrf.py wrf -t wrf -o run_OSSE
	# gsi
	./pywrf.py gsi -t make_new_run -o run_OSSE
	./pywrf.py gsi -t make_script -a 2012102600 -o run_OSSE
	./pywrf.py gsi -t gsi -o run_OSSE
	# da_update_bc
	./pywrf.py wrfda -t make_new_run -o run_OSSE
	./pywrf.py wrfda -t make_parame -o run_OSSE
	./pywrf.py wrfda -t da_update_bc -a 2012102600 -o run_OSSE
	# wrf 2012102600 -> 2012102603
	./pywrf.py wrf -t make_namelist -s 2012102600 -r 3 -i 10800 -o run_OSSE \
				   --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	./pywrf.py wrf -t wrf -o run_OSSE
	# gsi
	./pywrf.py gsi -t make_new_run -o run_OSSE
	./pywrf.py gsi -t make_script -a 2012102603 -o run_OSSE
	./pywrf.py gsi -t gsi -o run_OSSE
	# da_update_bc
	./pywrf.py wrfda -t make_new_run -o run_OSSE
	./pywrf.py wrfda -t make_parame -o run_OSSE
	./pywrf.py wrfda -t da_update_bc -a 2012102603 -o run_OSSE
	# wrf 2012102603 -> 2012102606
	./pywrf.py wrf -t make_namelist -s 2012102603 -r 3 -i 10800 -o run_OSSE \
				   --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	./pywrf.py wrf -t wrf -o run_OSSE
	# gsi
	./pywrf.py gsi -t make_new_run -o run_OSSE
	./pywrf.py gsi -t make_script -a 2012102606 -o run_OSSE
	./pywrf.py gsi -t gsi -o run_OSSE
	# da_update_bc
	./pywrf.py wrfda -t make_new_run -o run_OSSE
	./pywrf.py wrfda -t make_parame -o run_OSSE
	./pywrf.py wrfda -t da_update_bc -a 2012102606 -o run_OSSE
	# wrf 2012102606 -> 2012102609
	./pywrf.py wrf -t make_namelist -s 2012102606 -r 3 -i 10800 -o run_OSSE \
				   --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	./pywrf.py wrf -t wrf -o run_OSSE
	# gsi
	./pywrf.py gsi -t make_new_run -o run_OSSE
	./pywrf.py gsi -t make_script -a 2012102609 -o run_OSSE
	./pywrf.py gsi -t gsi -o run_OSSE
	# da_update_bc
	./pywrf.py wrfda -t make_new_run -o run_OSSE
	./pywrf.py wrfda -t make_parame -o run_OSSE
	./pywrf.py wrfda -t da_update_bc -a 2012102609 -o run_OSSE
	# wrf 2012102609 -> 2012102612
	./pywrf.py wrf -t make_namelist -s 2012102609 -r 3 -i 10800 -o run_OSSE \
				   --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	./pywrf.py wrf -t wrf -o run_OSSE
	# gsi
	./pywrf.py gsi -t make_new_run -o run_OSSE
	./pywrf.py gsi -t make_script -a 2012102612 -o run_OSSE
	./pywrf.py gsi -t gsi -o run_OSSE
	# da_update_bc
	./pywrf.py wrfda -t make_new_run -o run_OSSE
	./pywrf.py wrfda -t make_parame -o run_OSSE
	./pywrf.py wrfda -t da_update_bc -a 2012102612 -o run_OSSE
	# wrf 2012102612 -> 2012102818
	./pywrf.py wrf -t make_namelist -s 2012102612 -r 54 -i 10800 -o run_OSSE \
				   --history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	./pywrf.py wrf -t wrf -o run_OSSE

#osse-l:
	## WPS
	##./pywrf.py wps -t make_new_run -o run_OSSE
	##./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818 -i 10800 -o run_OSSE
	##./pywrf.py wps -t geogrid -o run_OSSE
	##./pywrf.py wps -t ungrib -o run_OSSE
	##./pywrf.py wps -t metgrid -o run_OSSE
	## real
	##./pywrf.py wrf -t make_new_run -o run_OSSE
	##./pywrf.py wrf -t make_namelist -s 2012102600 -r 3 -i 10800 -o run_OSSE --inputout_interval 180
	##./pywrf.py wrf -t make_real_srun -o run_OSSE
	##./pywrf.py wrf -t real -o run_OSSE
	##./pywrf.py wrf -t make_namelist -s 2012102603 -r 3 -i 10800 -o run_OSSE --inputout_interval 180
	##./pywrf.py wrf -t make_real_srun -o run_OSSE
	##./pywrf.py wrf -t real -o run_OSSE
	##./pywrf.py wrf -t make_namelist -s 2012102606 -r 3 -i 10800 -o run_OSSE --inputout_interval 180
	##./pywrf.py wrf -t make_real_srun -o run_OSSE
	##./pywrf.py wrf -t real -o run_OSSE
	##./pywrf.py wrf -t make_namelist -s 2012102609 -r 3 -i 10800 -o run_OSSE --inputout_interval 180
	##./pywrf.py wrf -t make_real_srun -o run_OSSE
	##./pywrf.py wrf -t real -o run_OSSE
	##./pywrf.py wrf -t make_namelist -s 2012102612 -r 54 -i 10800 -o run_OSSE --inputout_interval 180
	##./pywrf.py wrf -t make_real_srun -o run_OSSE
	##./pywrf.py wrf -t real -o run_OSSE
	##./pywrf.py wrf -t make_namelist -s 2012102518 -r 6 -i 21600 -o run_OSSE
	##./pywrf.py wrf -t make_real_srun -o run_OSSE
	##./pywrf.py wrf -t real -o run_OSSE
	## wrf 2012102518 -> 2012102600
	##./pywrf.py wrf -t make_namelist -s 2012102518 -r 6 -i 10800 -o run_OSSE \
				   ##--history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	##./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	##./pywrf.py wrf -t wrf -o run_OSSE
	## da_update_bc
	#./pywrf.py wrfda -t make_new_run -o run_OSSE
	#./pywrf.py wrfda -t make_parame -o run_OSSE -l
	#./pywrf.py wrfda -t da_update_bc -a 2012102600 -o run_OSSE -l
	## gsi
	#./pywrf.py gsi -t make_new_run -o run_OSSE
	#./pywrf.py gsi -t make_script -a 2012102600 -o run_OSSE
	#./pywrf.py gsi -t gsi -o run_OSSE
	## da_update_bc
	#./pywrf.py wrfda -t make_new_run -o run_OSSE
	#./pywrf.py wrfda -t make_parame -o run_OSSE
	#./pywrf.py wrfda -t da_update_bc -a 2012102600 -o run_OSSE
	## wrf 2012102600 -> 2012102603
	#./pywrf.py wrf -t make_namelist -s 2012102600 -r 3 -i 10800 -o run_OSSE \
				   #--history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	#./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	#./pywrf.py wrf -t wrf -o run_OSSE
	## da_update_bc
	#./pywrf.py wrfda -t make_new_run -o run_OSSE
	#./pywrf.py wrfda -t make_parame -o run_OSSE -l
	#./pywrf.py wrfda -t da_update_bc -a 2012102603 -o run_OSSE -l
	## gsi
	#./pywrf.py gsi -t make_new_run -o run_OSSE
	#./pywrf.py gsi -t make_script -a 2012102603 -o run_OSSE
	#./pywrf.py gsi -t gsi -o run_OSSE
	## da_update_bc
	#./pywrf.py wrfda -t make_new_run -o run_OSSE
	#./pywrf.py wrfda -t make_parame -o run_OSSE
	#./pywrf.py wrfda -t da_update_bc -a 2012102603 -o run_OSSE
	## wrf 2012102603 -> 2012102606
	#./pywrf.py wrf -t make_namelist -s 2012102603 -r 3 -i 10800 -o run_OSSE \
				   #--history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	#./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	#./pywrf.py wrf -t wrf -o run_OSSE
	## da_update_bc
	#./pywrf.py wrfda -t make_new_run -o run_OSSE
	#./pywrf.py wrfda -t make_parame -o run_OSSE -l
	#./pywrf.py wrfda -t da_update_bc -a 2012102606 -o run_OSSE -l
	## gsi
	#./pywrf.py gsi -t make_new_run -o run_OSSE
	#./pywrf.py gsi -t make_script -a 2012102606 -o run_OSSE
	#./pywrf.py gsi -t gsi -o run_OSSE
	## da_update_bc
	#./pywrf.py wrfda -t make_new_run -o run_OSSE
	#./pywrf.py wrfda -t make_parame -o run_OSSE
	#./pywrf.py wrfda -t da_update_bc -a 2012102606 -o run_OSSE
	## wrf 2012102606 -> 2012102609
	#./pywrf.py wrf -t make_namelist -s 2012102606 -r 3 -i 10800 -o run_OSSE \
				   #--history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	#./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	#./pywrf.py wrf -t wrf -o run_OSSE
	## da_update_bc
	#./pywrf.py wrfda -t make_new_run -o run_OSSE
	#./pywrf.py wrfda -t make_parame -o run_OSSE -l
	#./pywrf.py wrfda -t da_update_bc -a 2012102609 -o run_OSSE -l
	## gsi
	#./pywrf.py gsi -t make_new_run -o run_OSSE
	#./pywrf.py gsi -t make_script -a 2012102609 -o run_OSSE
	#./pywrf.py gsi -t gsi -o run_OSSE
	## da_update_bc
	#./pywrf.py wrfda -t make_new_run -o run_OSSE
	#./pywrf.py wrfda -t make_parame -o run_OSSE
	#./pywrf.py wrfda -t da_update_bc -a 2012102609 -o run_OSSE
	## wrf 2012102609 -> 2012102612
	#./pywrf.py wrf -t make_namelist -s 2012102609 -r 3 -i 10800 -o run_OSSE \
				   #--history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	#./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	#./pywrf.py wrf -t wrf -o run_OSSE
	## da_update_bc
	#./pywrf.py wrfda -t make_new_run -o run_OSSE
	#./pywrf.py wrfda -t make_parame -o run_OSSE -l
	#./pywrf.py wrfda -t da_update_bc -a 2012102612 -o run_OSSE -l
	## gsi
	#./pywrf.py gsi -t make_new_run -o run_OSSE
	#./pywrf.py gsi -t make_script -a 2012102612 -o run_OSSE
	#./pywrf.py gsi -t gsi -o run_OSSE
	## da_update_bc
	#./pywrf.py wrfda -t make_new_run -o run_OSSE
	#./pywrf.py wrfda -t make_parame -o run_OSSE
	#./pywrf.py wrfda -t da_update_bc -a 2012102612 -o run_OSSE
	## wrf 2012102612 -> 2012102818
	#./pywrf.py wrf -t make_namelist -s 2012102612 -r 54 -i 10800 -o run_OSSE \
				   #--history_interval 180 --inputout_interval 180 --inputout_begin_h 3
	#./pywrf.py wrf -t make_wrf_srun -o run_OSSE
	#./pywrf.py wrf -t wrf -o run_OSSE
