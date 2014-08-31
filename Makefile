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
	./pywrf.py wps -t make_new_run -o OSSE
	./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818 -o OSSE
	./pywrf.py wps -t geogrid -o OSSE
	./pywrf.py wps -t ungrib -o OSSE
	./pywrf.py wps -t metgrid -o OSSE

