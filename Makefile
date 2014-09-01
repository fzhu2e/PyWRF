clean:
	rm -rf __*

test:
	#./pywrf.py wps -t make_new_run -o OSSE
	#./pywrf.py wps -t make_new_run -s 2012102518
	#./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818 -o OSSE
	#./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818 -r 72 # test -e -r conflict
	#./pywrf.py wps -t geogrid -o OSSE
	#./pywrf.py wps -t ungrib -o OSSE
	#./pywrf.py wps -t metgrid -o OSSE

wps:
	./pywrf.py wps -t make_new_run -o run_OSSE
	./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818 -o run_OSSE
	./pywrf.py wps -t geogrid -o run_OSSE
	./pywrf.py wps -t ungrib -o run_OSSE
	./pywrf.py wps -t metgrid -o run_OSSE

wrf:
	#./pywrf.py wrf -t make_new_run -o run_OSSE
	#./pywrf.py wrf -t make_namelist -s 2012102518 -r 6 -o run_OSSE
	#./pywrf.py wrf -t make_jobs -s 2012102518 -r 6 -o run_OSSE
	#./pywrf.py wrf -t real -o run_OSSE
	./pywrf.py wrf -t wrf -o run_OSSE
