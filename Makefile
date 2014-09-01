clean:
	rm -rf __*

wps:
	./pywrf.py wps -t make_new_run -o run_OSSE
	./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818 -o run_OSSE
	./pywrf.py wps -t geogrid -o run_OSSE
	./pywrf.py wps -t ungrib -o run_OSSE
	./pywrf.py wps -t metgrid -o run_OSSE

wrf:
	#./pywrf.py wrf -t make_new_run -o run_OSSE
	#./pywrf.py wrf -t make_namelist -s 2012102518 -r 6 -o run_OSSE
	#./pywrf.py wrf -t make_jobs -o run_OSSE
	#./pywrf.py wrf -t real -o run_OSSE
	./pywrf.py wrf -t wrf -o run_OSSE

wrfda:
	./pywrf.py gsi -t make_new_run -o run_OSSE
	./pywrf.py gsi -t make_parame -a 2012102600 -o run_OSSE
	./pywrf.py gsi -t da_update_bc -o run_OSSE

gsi:
	./pywrf.py gsi -t make_new_run -o run_OSSE
	./pywrf.py gsi -t make_script -a 2012102600 -o run_OSSE
	#./pywrf.py gsi -t gsi -o run_OSSE
